# Team 22 | Sauti: Kiswahili limited semantic parsing

**Track:** C · **Team:** 22 (Kiswahili 3) · **Language:** Kiswahili

## Idea

Sauti turns a typed Kiswahili request into one of the ten Track C action labels
and extracts exact text spans for any explicit date, time, location, item, or
topic. The demo explains the predicted frame in Kiswahili. It does not execute
calendar or alarm actions, retrieve weather or news, or answer factual
questions.

## Data and review

The contribution dataset contains 250 unique team-authored requests: 25 for
each action, split into 150 training, 50 validation, and 50 test examples.
An independent Kiswahili reviewer approved all 250 records, including 50
documented label corrections. The data has 475 slot annotations across five
types, including two slot-free test examples. The structural audit found no
invalid slot JSON, unsupported types, span-boundary errors, or overlaps.

The final model run used CSV hash
`0756d1b54581bd23eab36a0455e987e3ca6d45d51f61ab5f544d146058509193`. The
submitted CSV uses an opaque private permission-record ID and concise,
judge-facing adjudication notes; its hash is
`0e10c800925e101af08aee1213f55543dcc508a024da918d6c87d3a96703835f`. These
metadata-only edits preserve requests, labels, slots, review statuses, and
splits used by the model.

Dataset use is authorized for this Datathon submission and assessment; no
open-data licence is claimed. See the dataset card and row-level source log
for data details. Permission records containing supporting evidence are kept
outside the submission package.

## Approach

1. Annotate each request with one Track C action and exact Unicode character
   spans using the handbook's five slot types.
2. Train an AfriBERTa joint intent and slot model with a constrained
   linear-chain CRF and training-only slot-value augmentation.
3. Select the configuration on validation data, then evaluate once on the
   frozen test set.
4. Compare the model with train-only majority-intent and character TF-IDF
   baselines, including a training-value slot matcher.
5. Present the parse in Sauti's browser interface with a short Kiswahili
   explanation and inspectable JSON frame.

## Results

The final run used `castorini/afriberta_large`, seed 42, and selected epoch 8.
It was evaluated on 50 examples from the frozen test set.

| System | Intent accuracy | Intent macro-F1 | Exact slot F1 | Full-frame exact match | JSON validity | Unseen-value exact recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AfriBERTa joint model | 100.00% | 100.00% | 79.01% | 58.00% | 100.00% | 58.33% |
| Character TF-IDF + train-only surface matcher | 86.00% | 85.65% | 56.52% | 24.00% | 100.00% | 0.00% |
| Character TF-IDF, empty slots | 86.00% | 85.65% | 0.00% | 4.00% | 100.00% | 0.00% |

Exact slot scoring requires the correct slot type and Unicode character
boundaries. Full-frame exact match requires the intent and complete slot set
to be correct. Detailed metric definitions, final test error examples, and the
baseline comparison are in
[`docs/model/MODEL_EVALUATION_PROTOCOL.md`](docs/model/MODEL_EVALUATION_PROTOCOL.md).
Machine-readable baseline outputs are in `results/track_c_baselines/`.

## Limitations

The test set has only five examples per action, so its 100% intent score does
not establish broad Kiswahili performance. The model reached 58.00%
full-frame exact match and 58.33% unseen-value exact recall; most remaining
errors involve missed, partial, or extra slots. The former test set had been
used during development, so the current test was reselected from former
training examples. It is a fresh split, not a newly collected prospective
test. The interface displays predictions and does not carry out the requested
actions.

## Run and reproduce

Use Python 3.11 or newer and a PyTorch build compatible with the machine.
Install dependencies from the repository root:

```powershell
python -m pip install -r requirements-model.txt
python audit_track_c.py Team_22_Dataset_Track_C.csv
python evaluate_track_c_baselines.py --data Team_22_Dataset_Track_C.csv --output-dir results/track_c_baselines
```

The complete Colab sequence for validation selection, final training,
evaluation, artifact backup, and Sauti is in
[`docs/model/COLAB_TRACK_C_RUN.md`](docs/model/COLAB_TRACK_C_RUN.md).
The final checkpoint is 500 MB and is not included in Git; its matching
`metrics_and_errors.json` must stay beside it. Sauti rejects checkpoints
whose labels or evaluation metadata do not match Track C.

## Contributions

| Member | Contribution |
| --- | --- |
| Gift Githaka Gicheru | Sauti frontend and interaction design. |
| Brian Terer | Track C model training and evaluation in Google Colab. |
| Nyawita Elsie Damar | Dataset preparation, annotation, and provenance records. |

Codex-assisted work, including slot annotation assistance and code/document
changes, is disclosed in
[`docs/team/contribution_and_ai_use.md`](docs/team/contribution_and_ai_use.md).

## Project evidence

- [Sauti live demo](https://sauti.jollyground-e681768c.centralindia.azurecontainerapps.io/)
- [Authoritative dataset](Team_22_Dataset_Track_C.csv)
- [Dataset card](docs/data/dataset_card.md)
- [Annotation guide](docs/data/annotation_guide.md)
- [Quality report](docs/data/quality_report.md)
- [Source and correction logs](provenance/)
- [Track C evaluation protocol and results](docs/model/MODEL_EVALUATION_PROTOCOL.md)
- [Runnable Sauti demo](sauti/README.md)
- [Original team repository](https://github.com/xtensionlabs/xtenders-nlp-datathon)
