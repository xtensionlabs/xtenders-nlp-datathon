# Track C slot-filling improvement experiment

> **Historical results only:** Every percentage and error below comes from the
> earlier dataset and split. The current 250-row Track C CSV uses the final
> action schema and a newly frozen test split. Do not report these historical
> scores as final Track C performance.

## Baseline

The T4 baseline used `castorini/afriberta_large`, an intent head, and an
independent token softmax slot head. It trained on the supplied 150 rows,
selected a checkpoint using the 50-row validation split, and produced the
baseline metrics below on the 50-row test split.

| Version | Intent accuracy | Slot F1 (seqeval) |
| --- | ---: | ---: |
| AfriBERTa baseline | 94.00% | 41.46% |
| CRF + controlled augmentation | 100.00% | 72.08% |
| CRF + augmentation vs. baseline | +6.00 pp | +30.62 pp |
| CRF + augmentation + LLRD | 90.00% | 57.99% |
| LLRD change vs. current champion | -10.00 pp | -14.09 pp |

The hybrid T4 run selected epoch 8. Its validation metrics were 96.00% intent
accuracy and 76.29% slot F1. On the 50-row test split it scored 100.00% intent
accuracy (50/50), 72.08% slot F1, and 0.8604 joint score. It generated 138
augmented training rows and reported two FP16 optimizer steps skipped in epoch
1; later epochs reported none.

The LLRD ablation also selected epoch 8, but validation intent accuracy was
96.00%, slot F1 was 57.47%, and joint score was 0.7674. This is below the
current hybrid's validation slot F1 of 76.29% and joint score of 0.8614. Its
test joint score was 0.7399, also below the current hybrid's 0.8604. The
measured result rejects these LLRD rates for this task; the uniform-LR hybrid
remains the chosen model.

## Rejected LLRD ablation

The AfriBERTa checkpoint was trained with a masked-language-model head, so its
unused MLM weights are reported as unexpected when loading the encoder. The
previously missing XLM-R pooler is also unused: intent prediction reads the
first token from `last_hidden_state`. The script now disables that pooler at
load time ([Transformers XLM-R model docs](https://huggingface.co/docs/transformers/main/model_doc/xlm-roberta)).

The tested `0.85` decay and `5e-5` head rate reduced validation and test
scores here. Published
fine-tuning studies report that layer-wise decay can help in some settings,
with results depending on architecture and task ([systematic study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10140607/)); this run shows it is not a universal gain.
LLRD support has been removed from the maintained training script; its default
optimizer is the uniform-LR V2 configuration.

The regex fallback is not included. The remaining time error is a multiword
boundary error, while the numeric time in `rec_024` is already tagged
correctly; the missed span is a date phrase. A fixed 0.85 confidence cutoff
would need validation calibration and could introduce false positives.

## Why this experiment

The training annotations contain 594 `O` word labels and 561 entity word
labels, so the main issue is not a large `O`-class imbalance. They contain 277
slot spans; 147 spans cover more than one word. The T4 error examples include
partial multiword entities and one illegal `I-time` transition after `O`.

The improved run adds two targeted changes:

1. A linear-chain CRF with BIO transition constraints decodes each whole word
   sequence, preventing invalid transitions such as `O -> I-time`. CRFs model
   label-sequence dependencies rather than making each tag decision
   independently ([Lafferty, McCallum & Pereira](https://www.cs.columbia.edu/~jebara/6772/papers/crf.pdf)).
2. One optional synthetic example is created for each eligible training row by
   replacing one slot value with a value from the training split that has the
   same intent, slot type, and word count. Original examples remain in the
   training data; validation and test rows are never used for augmentation.
   On the current split and seed 42, this creates 133 additional rows. Data
   augmentation has helped small NER datasets in published experiments, but
   its value must be measured on this Kiswahili task ([Dai & Adel, COLING 2020](https://aclanthology.org/2020.coling-main.343/)).
   The script writes a CSV preview with source IDs and replaced values for
   manual review; these are synthetic training examples, not new collected
   annotations.

The FP16 training loop also advances its learning-rate schedule only when the
gradient scaler did not skip an optimizer update.

## Evaluation protocol

The script keeps the existing 150/50/50 split boundaries. It chooses the
checkpoint using the validation average of intent accuracy and slot F1, then
reports test metrics and up to five test errors. The baseline test errors were
inspected to guide this experiment, so the test comparison is exploratory,
not a fully blinded estimate. The test split has only 50 examples; treat the
100% intent result cautiously and validate on a fresh holdout or with grouped
cross-validation before presenting it as a generalization claim.

The CRF + augmentation model fixed intent classification on all test examples, but its
remaining slot errors show room to improve boundaries: `rec_021` split one
time span into two, `rec_024` truncated a date and added a spurious item,
`rec_048` merged a location into a date, `rec_074` overextended an item span,
and `rec_097` split a two-word location into two location entities.

Those 50 former test records are now in training. A new 50-row test set was
selected from five former training records per action; see
`MODEL_EVALUATION_PROTOCOL.md` and
`../../provenance/track_c_split_reassignment.json`. The model
must be retrained from the pretrained AfriBERTa weights. Do not resume the old
joint checkpoint.

Follow [`COLAB_TRACK_C_RUN.md`](COLAB_TRACK_C_RUN.md) for the paste-ready
Google Colab cells. It runs the baselines, compares three validation-only
configurations, then trains and evaluates the selected configuration once.
Do not run the retired typo fine-tuning snippets or resume the historical
checkpoint.

The training output includes the checkpoint, exact Track C metrics, all test
predictions, up to five actual errors, tokenizer, label mappings, augmentation
preview, and a run manifest with data/code/checkpoint hashes and package
versions. The baseline output contains the separate intent and slot baseline
metrics and predictions. Do not make further model changes after inspecting
the new test results and continue to call them final; any such follow-up result
is exploratory unless a new held-out set is created.

The rejected ablation used a `0.85` layer decay and `5e-5` head learning rate.
