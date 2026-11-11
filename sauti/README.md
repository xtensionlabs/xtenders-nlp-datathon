# Sauti — Kiswahili semantic parsing demo

Sauti accepts a Kiswahili request and shows what it understood in plain Kiswahili.
Expand **Maelezo ya modeli** to inspect the predicted JSON frame and exact text slots. It simulates the
next action. It does not set alarms, change calendars, fetch weather, or answer
factual questions. Slot offsets are zero-based Unicode character positions
with an exclusive `end`.

## Model status

The checkpoint currently in `models/` is historical and uses the earlier
action labels. The app rejects a checkpoint whose labels do not match all ten
Track C actions, so it cannot silently present that model as final. The final
run must use `Team_22_Dataset_Track_C.csv`, with its matching
`metrics_and_errors.json` beside the checkpoint. See
[`../docs/model/MODEL_EVALUATION_PROTOCOL.md`](../docs/model/MODEL_EVALUATION_PROTOCOL.md) for the
split and metric definitions. A valid JSON frame still does not guarantee a
correct parse.

## Run in Google Colab

Open the team's [Sauti Colab demo](https://colab.research.google.com/drive/1_Zz6qY-MJbF5CKRsMzEESwLqzGEHT9Xo#scrollTo=gng68AWYvVr0) and run **Open the Sauti app** after final training artifacts are available. For use after a runtime reset or by another teammate, mount the team-shared Drive folder and set `TRACK_C_MODEL_DIR` to its `track_c_final` directory; the checkpoint and matching metrics persist there. The helper can also download a published checkpoint when `TRACK_C_CHECKPOINT_ID` is set, while requiring the matching metrics locally. It validates the metadata and rejects legacy labels or incomplete Track C evaluation. Colab needs internet access for dependencies and the AfriBERTa tokenizer/configuration.

## Run locally on Windows

From the repository root, use Python 3.11 or newer with the model dependencies
and the PyTorch build that matches your hardware:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-model.txt
```

Copy the final Colab output folder, including `best_model.pt` and its matching
`metrics_and_errors.json`, to `models/track_c_final/`. Keep that metadata with
the checkpoint; the label order is part of the model weights.

Start the server from the repository root:

```powershell
.\.venv\Scripts\python.exe sauti/sauti.py --repo . --checkpoint models/track_c_final/best_model.pt
```

Open <http://127.0.0.1:8000/>. The first start downloads the model's
configuration and tokenizer from Hugging Face. `models/` and model weight files
are ignored by Git; arrange judge access to the checkpoint and matching
metadata, or include a reproducible download location and hashes in the final
manifest.

## Deploy on Azure

From the repository root in Azure Cloud Shell (Bash), place the final run's
`metrics_and_errors.json` in `models/track_c_final/`. Set
`TRACK_C_CHECKPOINT_ID` to the Drive file ID for the matching final
`best_model.pt`. The Azure build needs download access to that file.

```bash
export TRACK_C_CHECKPOINT_ID='your-final-checkpoint-drive-id'
bash sauti/deploy-azure.sh sauti-rg westeurope youruniqueregistryname
```

Use a region allowed by your subscription and a globally unique registry name.
The script builds the image, verifies that Sauti can load the final checkpoint,
and prints a public HTTPS URL. Azure resources can incur charges.

## Demo evidence checklist

- Show a request with an intent and several extracted slots.
- Show a request that has no slot, once one exists in the accepted dataset.
- Show an unseen slot value and explain that this model can miss new names or
  expressions.
- Explain that the displayed frame is a model prediction and may be wrong.
- Record a 2–3 minute backup video after the final model and data are frozen.

The current repository does not include that backup recording yet.
