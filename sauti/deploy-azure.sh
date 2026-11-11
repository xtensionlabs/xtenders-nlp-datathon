#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "Usage: bash deploy-azure.sh RESOURCE_GROUP AZURE_REGION UNIQUE_REGISTRY_NAME" >&2
  exit 2
fi

group=$1
region=$2
registry=$3
app=sauti
environment=sauti-env
identity=sauti-registry-pull
tag=$(date -u +%Y%m%d%H%M%S)

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
: "${TRACK_C_CHECKPOINT_ID:?Set TRACK_C_CHECKPOINT_ID to the Drive ID of final best_model.pt.}"
if [[ ! -f models/track_c_final/metrics_and_errors.json ]]; then
  echo "Copy the matching final metrics to models/track_c_final/metrics_and_errors.json." >&2
  exit 2
fi
az account show --query '{subscription:name, id:id}' -o table
az extension add --name containerapp --upgrade --only-show-errors
for provider in Microsoft.App Microsoft.ContainerRegistry Microsoft.ManagedIdentity; do
  az provider register --namespace "$provider" --wait
done
az group create --name "$group" --location "$region" --output none

if ! az acr show --resource-group "$group" --name "$registry" --output none 2>/dev/null; then
  az acr create --resource-group "$group" --name "$registry" --sku Basic --location "$region" --output none
fi
server=$(az acr show --resource-group "$group" --name "$registry" --query loginServer -o tsv)
image="$server/$app:$tag"
az acr build --registry "$registry" --image "$app:$tag" --file sauti/Dockerfile \
  --build-arg "TRACK_C_CHECKPOINT_ID=$TRACK_C_CHECKPOINT_ID" .

if az containerapp show --resource-group "$group" --name "$app" --output none 2>/dev/null; then
  az containerapp update --resource-group "$group" --name "$app" --image "$image" --output none
else
  az containerapp env create --resource-group "$group" --name "$environment" \
    --location "$region" --logs-destination none --output none
  az identity create --resource-group "$group" --name "$identity" --location "$region" --output none
  identity_id=$(az identity show --resource-group "$group" --name "$identity" --query id -o tsv)
  principal_id=$(az identity show --resource-group "$group" --name "$identity" --query principalId -o tsv)
  registry_id=$(az acr show --resource-group "$group" --name "$registry" --query id -o tsv)
  az acr config authentication-as-arm update --registry "$registry" --status enabled --output none
  az role assignment create --assignee-object-id "$principal_id" --assignee-principal-type ServicePrincipal \
    --role AcrPull --scope "$registry_id" --output none
  az containerapp create --resource-group "$group" --name "$app" --environment "$environment" \
    --image "$image" --registry-server "$server" --registry-identity "$identity_id" \
    --user-assigned "$identity_id" --ingress external --target-port 8000 \
    --cpu 2 --memory 4Gi --min-replicas 0 --max-replicas 1 --output none
fi

hostname=$(az containerapp show --resource-group "$group" --name "$app" \
  --query properties.configuration.ingress.fqdn -o tsv)
printf 'Sauti URL: https://%s\n' "$hostname"
