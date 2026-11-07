# 📑 Team 22: Track C Annotation & Semantic Parsing Guide

## 1. Task Specification
This guide defines the slot-filling annotation schema for a localized East African voice/text assistant using pure Kiswahili Sanifu (Standard Swahili). The target model performs joint Intent Classification and Named Entity Recognition (NER) across 10 MASSIVE-aligned action envelopes.

## 2. Slot Type Taxonomy & Bounding Rules
We explicitly restrict extractable tokens to 5 key semantic slot variables. Functional grammatical particles, prepositions (e.g., *wa*, *ya*, *kwa*), and verbs remain strictly outside bracket bounds.

*   `location`: Proper nouns denoting geographic cities, towns, institutional structures, or nations.
    *   *Sanifu Example:* "...safari kutoka [location: Nakuru]..."
*   `date`: Relative or absolute calendar temporal properties, including days of the juma (week) or structural periods.
    *   *Sanifu Example:* "...utabiri wa hali ya hewa kesho kutwa..."
*   `time`: Specific digital/analog time stamps or relative indicators of diurnal phases (e.g., *asubuhi*, *jioni*, *mchana*).
    *   *Sanifu Example:* "...mikutano mingapi na [time: saa ngapi]?"
*   `item`: Specific titles of singular digital media, structural assets, list values, or physical household devices.
    *   *Sanifu Example:* "Naomba uniwekee wimbo wa [item: Kodongklan]."
*   `term`: Broad conversational anchors, names of specific public figures, musical artists, organizations, or target conceptual vocabulary terms undergoing semantic mapping.
    *   *Sanifu Example:* "Nisikilizishe wimbo ya [term: Bien] mpya..."

## 3. General Parsing Constraints
1. **The Lowercase Token Rule:** All bounding metadata keywords within raw inline notations (`[slot_name: value]`) must remain exclusively lowercase to prevent tokenizer crashes.
2. **Whitespace Uniformity:** A singular blank character must follow the parsing colon token before tracking internal text spans.
3. **Bracketing Priority:** Disconnected multi-word entities belonging to a unified target construct are captured under a singular parent bracket span to ensure correct sequence labeling.
