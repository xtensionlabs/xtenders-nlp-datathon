# Track C Colab training cells

Use these cells for the final Track C model run. They replace the older typo
fine-tuning cells. Do not download the old `joint_model.pt`, use
`Team_22_Dataset_Clean.csv`, or delete Colab's `/content/.config`; those steps
belong to the retired experiment.

## Cell 1 — Clone or update the project

```python
from pathlib import Path
import os
import subprocess

REPO_URL = "https://github.com/xtensionlabs/xtenders-nlp-datathon.git"
REPO = Path("/content/xtenders-nlp-datathon")

def run_git(*args):
    subprocess.run(["git", "-C", str(REPO), *args], check=True)

if (REPO / ".git").is_dir():
    run_git("fetch", "origin")
    run_git("switch", "main")
    run_git("pull", "--ff-only", "origin", "main")
elif REPO.exists():
    raise RuntimeError(f"{REPO} exists but is not a Git checkout; move it aside manually.")
else:
    subprocess.run(
        ["git", "clone", "--branch", "main", "--single-branch", REPO_URL, str(REPO)],
        check=True,
    )

os.chdir(REPO)
required = [
    "Team_22_Dataset_Track_C.csv",
    "train_joint_intent_slot.py",
    "track_c_evaluation.py",
    "evaluate_track_c_baselines.py",
    "compare_track_c_validation.py",
    "compare_track_c_results.py",
]
missing = [name for name in required if not (REPO / name).is_file()]
if missing:
    raise RuntimeError(
        "GitHub main is missing the current Track C files: " + ", ".join(missing)
        + ". Publish the reviewed local Track C changes to GitHub, then rerun this cell."
    )

print("Repository:", REPO)
subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], check=True)
```

The guard matters for this checkout: at the time these cells were prepared,
GitHub `main` and `sauti-app` had no new commits, and the Track C changes in
this workspace had not been published. The cell stops if a clone would use the
old data or scripts.

## Cell 2 — Install model dependencies and confirm GPU

Colab already supplies a CUDA-matched PyTorch build. Keep it; install the other
packages used by this project:

```python
%pip install -q "transformers==5.3.0" "sentencepiece>=0.2,<0.3" "pandas>=2.2,<4" "scikit-learn>=1.5,<2"
```

If Colab asks for a runtime restart, restart once and continue at Cell 3.

```python
import torch
print("PyTorch:", torch.__version__)
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "none")
if not torch.cuda.is_available():
    raise RuntimeError("In Colab, select Runtime > Change runtime type > T4 GPU, then rerun this cell.")
```

## Cell 3 — Audit the dataset and run train-only baselines

```bash
%%bash
set -e
python audit_track_c.py Team_22_Dataset_Track_C.csv
python evaluate_track_c_baselines.py \
  --data Team_22_Dataset_Track_C.csv \
  --output-dir /content/track_c_baselines
```

## Cell 4 — Train three validation-only configurations

All three candidates use the same data, seed, training budget, and validation
selection rule. These runs do **not** evaluate the test split.

```bash
%%bash
set -e
python -u train_joint_intent_slot.py \
  --data Team_22_Dataset_Track_C.csv \
  --output-dir /content/track_c_crf_aug_validation \
  --epochs 8 --batch-size 8 --gradient-accumulation-steps 2 \
  --seed 42 --precision fp16 --use-crf --augment-slot-values --validation-only

python -u train_joint_intent_slot.py \
  --data Team_22_Dataset_Track_C.csv \
  --output-dir /content/track_c_softmax_validation \
  --epochs 8 --batch-size 8 --gradient-accumulation-steps 2 \
  --seed 42 --precision fp16 --no-crf --no-slot-value-augmentation --validation-only

python -u train_joint_intent_slot.py \
  --data Team_22_Dataset_Track_C.csv \
  --output-dir /content/track_c_crf_validation \
  --epochs 8 --batch-size 8 --gradient-accumulation-steps 2 \
  --seed 42 --precision fp16 --use-crf --no-slot-value-augmentation --validation-only

python compare_track_c_validation.py \
  --candidate /content/track_c_crf_aug_validation \
  --candidate /content/track_c_softmax_validation \
  --candidate /content/track_c_crf_validation \
  --output /content/validation_model_selection.md

cat /content/validation_model_selection.md
```

Use the selected candidate named in the report for the final run. The report
also prints the exact final-run flags. The priority is validation full-frame
exact match, then intent macro-F1, then exact-span slot F1.

## Cell 5 — Train the selected configuration and evaluate the test set once

Set `WINNER` to the candidate directory named in
`validation_model_selection.md`. This cell maps that choice to the matching
flags, trains a fresh run from pretrained AfriBERTa, and evaluates the frozen
test split once. It does not resume the old checkpoint.

```python
from pathlib import Path
import subprocess
import sys

WINNER = "track_c_crf_aug_validation"  # replace with the report's selected candidate
FINAL_FLAGS = {
    "track_c_crf_aug_validation": ["--use-crf", "--augment-slot-values"],
    "track_c_softmax_validation": ["--no-crf", "--no-slot-value-augmentation"],
    "track_c_crf_validation": ["--use-crf", "--no-slot-value-augmentation"],
}
if WINNER not in FINAL_FLAGS:
    raise ValueError("WINNER must match one candidate name in the validation report.")
if Path("/content/track_c_final").exists():
    raise RuntimeError("/content/track_c_final already exists. Preserve it and choose a new output path for a rerun.")

command = [
    sys.executable, "-u", "train_joint_intent_slot.py",
    "--data", "Team_22_Dataset_Track_C.csv",
    "--output-dir", "/content/track_c_final",
    "--epochs", "8", "--batch-size", "8", "--gradient-accumulation-steps", "2",
    "--seed", "42", "--precision", "fp16", *FINAL_FLAGS[WINNER],
]
print("Final configuration:", WINNER, FINAL_FLAGS[WINNER])
subprocess.run(command, check=True)
```

## Cell 6 — Compare the final model with the baselines

```bash
%%bash
set -e
python compare_track_c_results.py \
  --model-dir /content/track_c_final \
  --baseline-metrics /content/track_c_baselines/baseline_metrics.json \
  --output /content/track_c_comparison.md
cat /content/track_c_comparison.md
```

## Cell 7 — Keep the run artifacts in Google Drive

This preserves the final checkpoint and the evidence needed to reproduce and
review the result. The validation folders contain checkpoints and can take
substantial Drive space.

```python
from google.colab import drive
from pathlib import Path
import shutil

drive.mount("/content/drive")
source = Path("/content")
destination = Path("/content/drive/MyDrive/Team_22_Track_C_Run")
destination.mkdir(parents=True, exist_ok=True)

folders = [
    "track_c_final", "track_c_baselines",
    "track_c_crf_aug_validation", "track_c_softmax_validation", "track_c_crf_validation",
]
files = ["validation_model_selection.md", "track_c_comparison.md"]
for name in folders:
    shutil.copytree(source / name, destination / name, dirs_exist_ok=True)
for name in files:
    shutil.copy2(source / name, destination / name)
print("Saved run artifacts to", destination)
```

Keep `best_model.pt` beside its matching `metrics_and_errors.json`. Do not use
the old Drive checkpoint ID or replace final metrics with a historical run.

## Cell 8 — Open the Sauti demo (optional)

Run this after the final training cell has completed successfully:

```python
import os
os.environ["TRACK_C_MODEL_DIR"] = "/content/track_c_final"
%run /content/xtenders-nlp-datathon/sauti/colab_demo.py
```
