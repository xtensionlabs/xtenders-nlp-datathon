"""Load the datathon checkpoint and turn its predictions into Kiswahili replies."""

from importlib.util import module_from_spec, spec_from_file_location
import json
import sys


INTENTS = {
    "alarm_set": "kuweka kengele",
    "calendar_query": "kuangalia ratiba yako",
    "calendar_set": "kuongeza tukio kwenye ratiba yako",
    "datetime_query": "kujua tarehe au saa",
    "general_qa": "kupata jibu la swali lako",
    "iot_wemo": "kudhibiti kifaa chako",
    "news_query": "kupata habari",
    "play_music": "kusikiliza muziki",
    "take_note": "kuandika dokezo",
    "weather_query": "kujua hali ya hewa",
}
SLOTS = {"date": "Tarehe", "time": "Muda", "location": "Mahali", "item": "Kipengee", "term": "Mada"}


def format_reply(intent, entities):
    action = INTENTS.get(intent)
    if action is None:
        return "Sijaelewa ombi hilo. Jaribu kuliandika kwa maneno mengine."
    details = [f"{SLOTS[entity['type']]}: {entity['value']}" for entity in entities if entity["type"] in SLOTS]
    return "\n".join([f"Nimeelewa kuwa unataka {action}.", *details])


def load_responder(repository, checkpoint):
    import torch
    from transformers import AutoConfig, AutoModel, AutoTokenizer

    architecture = spec_from_file_location("_sauti_architecture", repository / "train_joint_intent_slot.py")
    training = module_from_spec(architecture)
    sys.modules[architecture.name] = training
    try:
        architecture.loader.exec_module(training)
    finally:
        del sys.modules[architecture.name]

    metadata = json.loads((repository / "metrics_and_errors.json").read_text(encoding="utf-8"))
    intent_labels = metadata["intent_labels"]
    slot_labels = metadata["slot_labels"]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained(metadata["model_name"], use_fast=True)
    class CheckpointModel(training.JointTransformerModel):
        """Reuse the training model's forward pass with weights supplied by our checkpoint."""

        def __init__(self):
            torch.nn.Module.__init__(self)
            config = AutoConfig.from_pretrained(metadata["model_name"])
            self.encoder = AutoModel.from_config(config, add_pooling_layer=False)
            self.dropout = torch.nn.Dropout(0.1)
            self.intent_classifier = torch.nn.Linear(config.hidden_size, len(intent_labels))
            self.slot_classifier = torch.nn.Linear(config.hidden_size, len(slot_labels))
            use_crf = metadata["slot_decoder"] == "constrained_linear_chain_crf"
            self.crf = training.LinearChainCRF(slot_labels) if use_crf else None

    model = CheckpointModel()
    weights = torch.load(checkpoint, map_location="cpu", weights_only=True)
    weights.pop("encoder.pooler.dense.weight", None)
    weights.pop("encoder.pooler.dense.bias", None)
    model.load_state_dict(weights, strict=True)
    model.to(device).eval()

    @torch.inference_mode()
    def respond(text):
        words, _ = training.whitespace_words(text)
        encoded = tokenizer(
            words, is_split_into_words=True, truncation=True, max_length=128,
            return_tensors="pt",
        )
        word_ids = encoded.word_ids()
        first = [
            word_id is not None and (index == 0 or word_id != word_ids[index - 1])
            for index, word_id in enumerate(word_ids)
        ]
        if not any(first):
            return "Jaribu kuandika ombi lako kwa maneno machache ya Kiswahili."
        mask = torch.tensor([first], dtype=torch.bool, device=device)
        result = model(
            encoded["input_ids"].to(device), encoded["attention_mask"].to(device),
            first_subtoken_mask=mask, decode_slots=True,
        )
        intent = intent_labels[result["intent_logits"][0].argmax().item()]
        predictions = result["slot_predictions"]
        ids = (predictions[0] if predictions is not None
               else result["slot_logits"][mask].argmax(dim=-1).tolist())
        tags = [slot_labels[index] for index in ids]
        tokenized_words = [words[word_id] for word_id, include in zip(word_ids, first) if include]
        return format_reply(intent, training.decode_entities(tags, tokenized_words))

    return respond
