# Team 22 data plan

## Declaration

- **Team:** 22, Kiswahili 3
- **Track:** C, limited semantic parsing
- **Language:** Kiswahili, reviewed by the team's independent Kiswahili
  reviewer.
- **Output:** one exact handbook action label plus zero or more text spans of
  type `location`, `date`, `time`, `item`, or `term`.

## Dataset

`Team_22_Dataset_Track_C.csv` is the only dataset CSV. It has 250 rows, exactly
25 per Track C action, with 15/5/5 train/validation/test splits. It contains
224 inherited team-authored examples, including 50 reviewer-approved label
corrections, and 26 additional team-authored requests. Twenty-six
programmatic-padding records from older drafts are excluded.

The team confirms that the independent reviewer approved all 250 records,
including language, labels, slots, and grouping. Every row is marked
`independently_reviewed`. The new requests use contributor code `T22-AUTH-01`
and reviewer code `T22-R1`; inherited rows retain source reviewer code
`member_A`.

## Annotation and split plan

The ten labels are the exact Track C actions in the handbook. The 25 additional
`lists_query` examples are split 15/5/5. One additional `calendar_set` request
fills that action's split to 15/5/5. The dataset has 475 slot annotations,
239 slot-bearing records, and 338 distinct exact slot type/value pairs. All
five slot types occur, with both slot-bearing and slot-free test requests.

Slot offsets are zero-based Python Unicode character positions with exclusive
`end`; each slot must satisfy `text[start:end] == value`. The structural audit
finds no invalid JSON, unsupported slot types, invalid offsets, or overlapping
spans. The audit reports per-action slot-value diversity and 51 exact test
slot values absent from training. The former test split was used during model
development, so five records per action were selected from the former training
rows for the new test; the old test rows moved to training. This preserves
15/5/5 and is recorded in `../../provenance/track_c_split_reassignment.json`.

## Sources, rights, and release

`../../provenance/Team_22_Source_Log.csv` records source IDs, versions, URLs, methods, permission
references, contributor/reviewer codes, review statuses, splits, and label
corrections for all 250 rows. `../../provenance/track_c_label_correction_log.csv` preserves
original and accepted labels for the 50 corrected records.

`../team/permission_and_release_record.md` documents Team 22's permission for
submission, judging, evaluation, and demonstration. This secures the declared
Datathon use. It does not grant open redistribution, commercial use, or reuse
outside this project. Keep identity mappings private and do not claim CC0 or
another open license.

The existing model artifacts predate this final dataset; the next model run
should use `Team_22_Dataset_Track_C.csv`. See `../model/TRACK_C_READINESS.md`,
`quality_report.md`, `../../provenance/Team_22_Source_Log.csv`, and
`../team/permission_and_release_record.md` for the rubric audit and provenance scope.
