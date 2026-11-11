# Track C model evaluation protocol

## Frozen data split

The original 50-row test split was used to compare model experiments. To keep a
final report from reusing those test outcomes, `reassign_track_c_splits.py`
created a new 50-row test split from five former training records per intent.
The former test rows moved to training; validation stayed fixed. The operation
changed no sentence, label, slot, or review field. It kept the authoritative
dataset at exactly 250 rows with 15 train, 5 validation, and 5 test records per
intent. The row-level split changes are recorded in
`../../provenance/track_c_split_reassignment.json`, and
`../../provenance/Team_22_Source_Log.csv` was updated to
match.

The new test records were not evaluated in the previous experiment. The old
checkpoint had included them in its training set, so the final run must start
from the pretrained AfriBERTa model and train only on the new `train` split; do
not resume the old joint checkpoint. This is a fresh holdout for the final
training run, with a small-data limitation: these are not newly collected
utterances. A completely prospective test would require additional reviewed
records.

From this point forward, use `validation` to select the model configuration and
checkpoint. `--validation-only` saves validation metrics and predictions
without evaluating test. Run the final `test` evaluation once after code, data,
and settings are frozen.
If test errors lead to another model change, label the resulting test score
exploratory and reserve a new holdout for a final estimate.

## Required measurements

`track_c_evaluation.py` reports:

- Intent accuracy, macro-F1, per-label precision/recall/F1, and a confusion
  matrix.
- Micro slot precision/recall/F1 using an exact `(slot type, start, end)` match
  over Unicode character offsets.
- Full-frame exact match, requiring the correct intent and the complete exact
  slot set.
- JSON validity after serialization, with schema, allowed slot types, offsets,
  and `text[start:end] == value` checked.
- Unseen slot-value counts and exact recovery/error details. A test value is
  considered seen only if the same normalized `(type, value)` occurs in the
  training annotations.
- All per-record predictions and up to five actual errors (all errors when
  fewer than five occur).

The model checkpoint is selected using validation full-frame exact match,
breaking ties by intent macro-F1 and then exact-span slot F1. Test results do
not participate in checkpoint selection.

## Baselines

Run `evaluate_track_c_baselines.py` on the same preset split. It fits only on
the train rows and records:

- A majority-intent comparator.
- Character TF-IDF (2–5 grams) with logistic regression for intent.
- The same intent model with an empty slot set.
- The same intent model plus a longest-match surface-value slot matcher built
  only from training annotations.

Each system is scored with the same intent, exact-slot, frame, JSON, and unseen
value metrics. The output includes overall metrics, per-label F1, confusion
matrices, predictions, and up to five errors.

The baselines have been run on the revised test set. Character TF-IDF plus
logistic regression scored 0.8565 intent macro-F1. Adding the train-only
surface matcher scored 0.7647 slot precision, 0.4483 recall, 0.5652 F1, and
0.2400 full-frame exact match. The TF-IDF empty-slot comparator scored 0.0400
full-frame exact match. The majority-intent macro-F1 is 0.0182. Full results
are in `results/track_c_baselines/`.

The fixed test contains five examples per action. Treat these as prototype
estimates, report the per-action counts and errors, and avoid presenting them
as broad claims about Kiswahili performance.

## Colab run

Use the cell-by-cell instructions in [`COLAB_TRACK_C_RUN.md`](COLAB_TRACK_C_RUN.md).
They clone or fast-forward `main`, stop if the current Track C files are missing,
run train-only baselines and three validation-only ablations, select one
configuration without test metrics, then run the final test comparison once.

Keep the complete `/content/track_c_final` folder with the checkpoint,
`metrics_and_errors.json`, `test_predictions.json`, `label_mappings.json`,
`validation_metrics.json`, `validation_predictions.json`, `run_manifest.json`,
and tokenizer. The manifest records data/code/checkpoint
hashes, package versions, split sizes, and run settings. Keep the baseline
output folder, all three validation-only candidate folders, and
`validation_model_selection.md` too. Do not replace the old historical metrics with new values
until the run has completed successfully.

Choose among the three variants using validation full-frame exact match,
breaking ties by intent macro-F1 and exact-span slot F1. If softmax/no
augmentation wins, use `--no-crf --no-slot-value-augmentation` for the final
run. If CRF/no augmentation wins, use `--use-crf --no-slot-value-augmentation`.
If CRF plus augmentation wins, keep the command as written.
