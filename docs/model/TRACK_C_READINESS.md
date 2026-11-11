# Team 22 Track C judging readiness

**Audit date:** 11 November 2026  
**Track:** C, limited semantic parsing  
**Authoritative dataset:** `Team_22_Dataset_Track_C.csv`

This maps repository evidence to the handbook's six criteria. It is not an
official mark: judges assign a level from 0 to 4 and apply the stated weight.

## Rubric status

| Criterion | Weight | Evidence now present | Remaining gap |
| --- | ---: | --- | --- |
| Data quality and annotation | 30 | All 250 records are marked independently reviewed. The accepted labels include 50 documented corrections; all ten actions have 25 examples and 15/5/5 splits. There are 475 structurally valid slots, 2 slot-free test examples, an annotation guide, and row-level review notes. | **Secured on the team's review confirmation and structural audit.** |
| Provenance, ethics, and rights | 20 | All 250 rows link to a permission record. Source IDs, versions, methods, contributor/reviewer codes, label transformations, and AI use are documented; the dataset has no third-party source text. | **Secured for the declared Datathon submission, judging, evaluation, and demo scope.** The permission record does not grant open redistribution, commercial use, or reuse outside this project. |
| Contribution coverage and balance | 15 | Exactly 250 reviewed rows, 25 per action, and 15/5/5 splits. There are 239 slot-bearing rows, 338 distinct exact slot type/value pairs, all five slot types, and 51 exact test values absent from training. | **Secured on the handbook's coverage requirements and audit.** The 26 programmatic-padding rows from older drafts are excluded. |
| Baseline and evaluation | 15 | Exact-span evaluation and train-only baselines now run on the revised split. Character TF-IDF intent macro-F1 is 85.65%; its surface matcher slot F1 is 56.52%; empty-slot full-frame exact match is 4.00%. | **Partly evidenced.** Final AfriBERTa test metrics and its comparison to the baselines are pending the Colab run. Historical neural scores are exploratory only. |
| Reproducibility and documentation | 10 | The loader accepts canonical `label`; evaluation and baseline commands are documented; the model run writes data/code/checkpoint hashes, package versions, predictions, and label mappings. Split changes are reproducible and logged. | **Partly secured.** Complete the Colab run, retain its full output, then freeze a commit/tag, manifest and snapshot with judge-accessible checkpoint/metadata. |
| Demonstration, explanation, and teamwork | 10 | Responsive browser UI, updated Colab helper, shared exact-offset decoder, and guards that reject stale labels/metrics. | **Partly secured.** Load the final checkpoint, verify the demo on new input, record the backup video, and add named contribution evidence. |

## Dataset and corrections

`Team_22_Dataset_Track_C.csv` is the only dataset CSV. It has 250 rows and
exactly 25 examples for each Track C action. Twenty-six programmatic-padding
records from older drafts were excluded.

Per the team's confirmation, an independent Kiswahili reviewer approved all
250 records, including language, labels, slot annotations, and grouping. Every
row records `independently_reviewed`. The 50 accepted label corrections map
`take_note` to `lists_createoradd` and `general_qa` to `qa_definition`.
Corrected rows use `source_method=corrected_with_evidence`. The original labels,
reasons, and reviewer codes are retained in
`../../provenance/track_c_label_correction_log.csv`. Row-level source details
are in `../../provenance/Team_22_Source_Log.csv`. The 26 additional
requests use contributor code `T22-AUTH-01` and reviewer code `T22-R1`.

## Structural audit

Run the audit against the authoritative file:

```powershell
.\.venv\Scripts\python.exe audit_track_c.py Team_22_Dataset_Track_C.csv
```

It reports 250 unique IDs/texts, all ten labels at 25 each, 150/50/50 splits,
475 slots, zero JSON/type/offset/overlap issues, 2 slot-free test records,
250 independently reviewed rows, and no group crossing splits.

The original test split had already been used during model development. The
former test records now belong to training; five records per action selected
deterministically from the former training set form the new test. The operation
preserves 250 rows and 15/5/5 per action, updates the source log, and records
every changed row in `../../provenance/track_c_split_reassignment.json`.

The baseline command writes metrics, per-label results, predictions, and errors
under `results/track_c_baselines/`. On this new test set, character TF-IDF plus
logistic regression scored 86.00% intent accuracy and 85.65% macro-F1. Adding
the train-only surface matcher scored 76.47% exact slot precision, 44.83% recall,
56.52% F1, and 24.00% full-frame exact match. The TF-IDF empty-slot baseline
scored 4.00% full-frame exact match. These are baseline results, not neural
model results.

## Current disposition

Data quality, contribution coverage, and provenance for the declared Datathon
use are documented. The dataset is not licensed for open redistribution. The
existing checkpoint and metrics predate the final labels and revised test
split; Sauti now rejects them. Evaluation code and baselines are ready, but the
model criterion cannot be called secured until a fresh Colab run is completed
and compared with those baselines.

Supporting documents: `../data/quality_report.md`, `../data/dataset_card.md`,
`../data/data_plan.md`, `../data/annotation_guide.md`,
`../team/contribution_and_ai_use.md`, and
`../../provenance/Team_22_Source_Log.csv`. Permission scope:
`../team/permission_and_release_record.md`.
