# Dataset quality report: Team 22, Track C

**Audit date:** 11 November 2026  
**Audited file:** `Team_22_Dataset_Track_C.csv`  
**Method:** structural checks via `audit_track_c.py`, row-level label
inspection, and the team's confirmation that an independent Kiswahili reviewer
approved all 250 records, including the accepted label corrections. Every row
records `independently_reviewed`.

## Results

- **Size and balance:** 250 rows, 250 unique IDs and exact texts; 25 per action;
  150 train, 50 validation, 50 test; each action has the required 15/5/5 split.
- **Action schema:** all ten exact Track C labels are present. The 50
  `take_note` and `general_qa` rows have reviewer-approved corrections to
  `lists_createoradd` and `qa_definition`. Original labels, accepted labels,
  reasons, and reviewer codes are in `../../provenance/track_c_label_correction_log.csv`.
- **Human contribution and review:** 224 inherited team-authored rows plus 26
  additional team-authored requests are included. All 250 are marked
  independently reviewed per the team's confirmation. Twenty-six
  programmatic-padding records from older drafts are excluded.
- **Slot coverage:** 475 annotations; 239/250 rows are slot-bearing. Test has
  48 slot-bearing and 2 slot-free rows; train has 144 and 6; validation has
  47 and 3. This exceeds the 100-row minimum and includes both kinds in test.
- **Slot-value breadth:** the dataset contains 338 distinct exact
  `(slot type, value)` pairs: 119 date, 114 item, 104 term, 81 time, and
  57 location annotations. All five allowed slot types occur.
- **Per-action diversity:** the table gives distinct exact `(slot type, value)`
  pairs. `lists_query` has 14 slot-bearing examples; every other action has 25.

  | Action | Rows | Slot-bearing | Distinct type/value pairs | Slot types |
  | --- | ---: | ---: | ---: | --- |
  | `alarm_set` | 25 | 25 | 48 | date, item, time |
  | `calendar_query` | 25 | 25 | 44 | date, item, location, time |
  | `calendar_set` | 25 | 25 | 84 | date, item, location, time |
  | `datetime_query` | 25 | 25 | 30 | date, location, time |
  | `lists_createoradd` | 25 | 25 | 53 | date, item, location, time |
  | `lists_query` | 25 | 14 | 11 | date, item, location, time |
  | `news_query` | 25 | 25 | 51 | date, location, term, time |
  | `play_music` | 25 | 25 | 35 | date, item, location, term, time |
  | `qa_definition` | 25 | 25 | 28 | term |
  | `weather_query` | 25 | 25 | 33 | date, location, term, time |

- **Span structure:** zero invalid JSON records, unsupported slot types, invalid
  Python character offsets, or overlapping spans. The audit checks exact
  offsets; reviewer approval covers annotation meaning and completeness.
- **Grouping:** all rows are marked reviewer-approved; no group crosses splits.
- **Held-out values:** 51 distinct exact `(slot type, value)` pairs in test do
  not occur in train. The model evaluator normalizes case/whitespace when it
  calculates unseen-value results.
- **Evaluation split:** the former test set was used during model development.
  Five records per action were selected from the former training rows for the
  new test; former test rows moved to training. This preserves 15/5/5 and is
  recorded in `../../provenance/track_c_split_reassignment.json`.
- **Provenance:** `../../provenance/Team_22_Source_Log.csv` links every row to
  `../team/permission_and_release_record.md`. Team 22 permission is documented for
  submission, judging, evaluation, and demonstration. The scope excludes open
  redistribution and reuse outside this project; no open license is claimed.

## Disposition

The data-quality, contribution-coverage, and provenance requirements for the
declared Datathon use are documented. The dataset is not licensed for open
redistribution. The current neural checkpoint predates the final action labels
and revised test split; it must not be reported as a final result.

Run the structural audit with:

```powershell
.\.venv\Scripts\python.exe audit_track_c.py Team_22_Dataset_Track_C.csv
```

See `../model/TRACK_C_READINESS.md` for the rubric mapping and next steps.
