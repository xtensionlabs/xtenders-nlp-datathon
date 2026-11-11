# Provenance records

These files document the dataset's sources, accepted annotation changes,
review evidence, and reproducible split reassignment. They are supporting
records; `../Team_22_Dataset_Track_C.csv` is the repository's only dataset.

- `Team_22_Source_Log.csv`: one provenance and review record per dataset row.
- `track_c_label_correction_log.csv`: original and accepted labels for the 50
  corrected examples.
- `track_c_split_reassignment.json`: deterministic row movement for the
  refreshed 15/5/5 split.
- `source_log_template.csv`: blank template for recording future additions.

The permission evidence referenced by each row is in
[`../docs/team/permission_and_release_record.md`](../docs/team/permission_and_release_record.md).
Keep private identity mappings and consent records outside the repository.
