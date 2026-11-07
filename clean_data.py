import pandas as pd
import re
import json


def finalize_stratified_250_dataset(file_path, output_path):
    # Load your unified raw 276-row data asset
    df = pd.read_csv(file_path)

    # Secure row isolation to only keep active data items
    df = df[df['record_ID'].str.startswith('rec_', na=False)].copy()

    # 1. Drop any absolute textual duplicates to optimize clean variety
    df = df.drop_duplicates(subset=['inline_annotated'])

    # 2. Extract exactly 25 rows per unique intent to reach the perfect 250 cap
    stratified_chunks = []
    for label, group in df.groupby('label(intent)'):
        stratified_chunks.append(group.head(25))

    df_final = pd.concat(stratified_chunks).copy()

    # 3. Cleanly sort and reset the index counters sequentially 1 to 250
    df_final = df_final.sort_values(by='label(intent)').reset_index(drop=True)
    for idx in range(len(df_final)):
        df_final.at[idx, 'record_ID'] = f"rec_{idx + 1:03d}"

    pattern = r'\[([a-z_]+):\s*([^\]]+)\]'
    intent_counters = {}

    # 4. Programmatically re-derive character counts and split arrays
    for idx, row in df_final.iterrows():
        intent = row['label(intent)']
        if intent not in intent_counters:
            intent_counters[intent] = 0
        current_count = intent_counters[intent]

        # Enforce exact 15 train, 5 validation, 5 test segmentation per intent
        if current_count < 15:
            df_final.at[idx, 'split'] = 'train'
        elif current_count < 20:
            df_final.at[idx, 'split'] = 'validation'
        else:
            df_final.at[idx, 'split'] = 'test'

        intent_counters[intent] += 1
        df_final.at[idx, 'group_id'] = f"{intent}_group"

        # Auto-compute text character indices from inline bracket strings
        inline_str = str(row['inline_annotated'])
        slots = []
        clean_text = inline_str
        while True:
            match = re.search(pattern, clean_text)
            if not match:
                break
            slot_type = match.group(1)
            slot_value = match.group(2)
            start_idx = match.start()
            end_idx = start_idx + len(slot_value)

            slots.append({"type": slot_type, "value": slot_value, "start": start_idx, "end": end_idx})
            clean_text = clean_text[:match.start()] + slot_value + clean_text[match.end():]

        df_final.at[idx, 'text'] = clean_text
        df_final.at[idx, 'slots_json'] = json.dumps(slots, ensure_ascii=False)

    print("👑 Verification Matrix (Targeting a perfect 15 / 5 / 5 grid across all 10 intents):")
    summary = df_final.groupby(['label(intent)', 'split']).size().unstack(fill_value=0)
    print(summary)

    # Save the polished output file
    df_final.to_csv(output_path, index=False)
    print(f"\n🚀 Master Dataset finalized at: {output_path}")


# Run compilation execution
finalize_stratified_250_dataset('Team_22_Dataset_Raw.csv', 'Team_22_Dataset_Clean.csv')
