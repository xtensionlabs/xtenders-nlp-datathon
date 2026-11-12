# Sauti live demo narration

**Hosted app:** [Sauti live demo](https://sauti.jollyground-e681768c.centralindia.azurecontainerapps.io/)

This 2–3 minute script is written for the live Sauti interface. The three
example requests were checked against the contribution CSV and are not exact
duplicates. Treat them as live demonstrations, separate from the frozen-test
metrics.

## Before recording

Open the hosted app and wait for the input screen. Start a fresh conversation.
Keep the browser zoom at a readable size so the response and JSON frame fit on
screen. Enter the prompts below in the **Ombi lako** field and select **Tuma**.

## Narration and on-screen cues

### 0:00–0:20 | Introduce the project

“Hello, we’re Team 22. This is Sauti, our Kiswahili Track C parser. It predicts
one of ten actions and extracts details such as dates, times, places, items,
and topics. I’ll enter a few requests in Kiswahili and show the structured
frames Sauti returns.”

### 0:20–0:55 | Weather request

Enter:

> Hali ya hewa itakuwaje Nairobi kesho?

Say: “Sauti identifies this as a weather request. It extracts Nairobi as the
location and kesho, ‘tomorrow’, as the date. The JSON shows where those values
appear in the original sentence. This demo parses the request; it does not
fetch a forecast.”

Keep the response and JSON visible while speaking. If the JSON section is
collapsed in the deployed build, select **Maelezo ya modeli** to expand it.

### 0:55–1:35 | Calendar query

Start a fresh conversation, then enter:

> Nina mkutano wa wanahabari lini wiki ijayo?

Say: “Here the action is a calendar query. Sauti extracts the event, mkutano wa
wanahabari, and the time window, wiki ijayo. It is showing how it understood
the question; it is not looking up a real calendar.”

Point to the `calendar_query` intent and the `item` and `date` slots.

### 1:35–1:55 | Request without explicit details

Start a fresh conversation, then enter:

> Nisomee orodha zangu zote zilizohifadhiwa.

Say: “This asks about saved lists but names no particular item or date, so the
frame contains the `lists_query` action and an empty slot list.”

### 1:55–2:30 | Results and limits

“On our frozen test set of 50 requests, intent accuracy and macro-F1 were both
100%. Exact slot F1 was 79.01%, full-frame exact match was 58%, JSON validity was
100%, and unseen-value exact recall was 58.33%. There were only five test
examples per action, so these results describe a small evaluation set. Slot
extraction still makes errors, and Sauti displays parses rather than carrying
out the requested actions.”

### 2:30–2:50 | Contributions

“Gift Githaka Gicheru built the interface, Brian Terer trained and evaluated
the model, and Nyawita Elsie Damar prepared the dataset and provenance. Thank
you.”

## Recording checklist

- Show the live page and type the requests during the recording.
- Pause until each response appears, then point out its intent and slots.
- Keep the spoken metric values consistent with the evaluation report.
- Confirm the final 2–3 minute video opens for viewers who do not own it.

The hosted app link is optional in the submission README; the accessible demo
video link is still required.
