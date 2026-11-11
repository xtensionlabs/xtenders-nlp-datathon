# Team 22 NLP Datathon — Track C

Team 22 is building a Kiswahili limited semantic parser. For each request, the
demo predicts one handbook action and extracts exact `location`, `date`,
`time`, `item`, and `term` spans. It simulates the response; it does not
execute actions or fetch facts.

## Project layout

```text
Team_22_Dataset_Track_C.csv   # sole authoritative dataset
train_joint_intent_slot.py   # model training
track_c_evaluation.py        # shared Track C scorer and span decoder
audit_track_c.py             # dataset and provenance structure audit
evaluate_track_c_baselines.py
compare_track_c_*.py         # validation selection and final comparison
sauti/                       # browser demo
docs/
  handbook/                  # supplied task guide
  data/                      # data plan, card, annotation and quality docs
  model/                     # evaluation, Colab run and readiness docs
  team/                      # contribution and permission statements
provenance/                  # source log, correction log and split record
models/, results/            # local outputs; ignored by Git
```

The source log, correction log, split record, and source-log template are
provenance artifacts, not additional dataset files. Older dataset drafts and
preparation outputs have been removed.

## Dataset and audit

The authoritative CSV has 250 reviewer-approved records, ten handbook labels,
and balanced 15/5/5 train/validation/test splits. Audit it from the repository
root:

```powershell
.\.venv\Scripts\python.exe audit_track_c.py Team_22_Dataset_Track_C.csv
```

The audit checks label and split balance, slot JSON and character spans,
review-status fields, source methods, permission-reference paths, slot-free
coverage, split leakage, and unseen test slot values. It cannot independently
judge Kiswahili fluency or the legal scope of permission.

## Model and Colab run

Install model dependencies from `requirements-model.txt` with a PyTorch build
that matches the local hardware. The paste-ready Colab sequence, including
baselines, validation-only comparisons, one final test run, and artifact
backup, is in [`docs/model/COLAB_TRACK_C_RUN.md`](docs/model/COLAB_TRACK_C_RUN.md).
The final model must be retrained on the authoritative CSV; existing checkpoint
metrics are historical and must not be presented as final results.

Run train-only baselines locally with:

```powershell
python evaluate_track_c_baselines.py --data Team_22_Dataset_Track_C.csv --output-dir results/track_c_baselines
```

## Sauti demo

The responsive browser demo displays a short Kiswahili explanation and the
model's predicted JSON frame. Follow [`sauti/README.md`](sauti/README.md) for
local or Colab use. Final checkpoint metadata must remain beside its matching
weights.

## Documentation and evidence

- **Handbook:** [`docs/handbook/Strathmore NLP Hub Datathon 2026 _ Student Handbook and Task Guide.md`](<docs/handbook/Strathmore NLP Hub Datathon 2026 _ Student Handbook and Task Guide.md>)
- **Data:** [`docs/data/`](docs/data/), including the annotation guide, data
  plan, dataset card, and quality report.
- **Model:** [`docs/model/`](docs/model/), including the evaluation protocol,
  historical improvement notes, Colab cells, and judging-readiness status.
- **Team:** [`docs/team/`](docs/team/), including the contribution/AI-use
  statement and permission record.
- **Provenance:** [`provenance/`](provenance/), including the row-level source
  log, accepted label corrections, split reassignment record, and blank log
  template.

Before submission, complete the named-work and evidence table in
[`docs/team/contribution_and_ai_use.md`](docs/team/contribution_and_ai_use.md).
Keep code-to-person mappings and personal consent records private.
