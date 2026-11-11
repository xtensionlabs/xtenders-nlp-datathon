# Build Language Data. Show What It Can Do.

## Strathmore NLP Hub Datathon 2026 \| Student handbook \| Final instructions, 2 November 2026

## Motivation Example

Imagine that you are building a small assistant for people who prefer to write in Kiswahili (or another language of your choice). A user asks about tomorrow's weather. Your assistant must first recognise what the person is asking before it can route the request.

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** Weather enquiry (weather\_query)

Display a message such as “You are asking about the weather.” For this datathon, simulate the next action. You do not need to fetch a real forecast.

## How will you solve the problem?

1. Collect natural examples in your team's language.  
2. Give each example the correct label and ask a competent reviewer to check the language and meaning.  
3. Use the starter code to train a small model. Test it on examples that were kept out of training.  
4. Build a Streamlit or mobile interface that accepts new text and displays the model's result.  
5. Show what works, explain mistakes and submit your data, code and documentation.

Your main contribution is useful, reviewed language data supported by a working demonstration. Do not count unchanged downloads or practice examples as your own new data.

# 1\. Choose one task

* Track A: recognise what a user wants to do. Choose intent classification if you want to build a request-routing assistant.  
* Track B: recognise a positive, negative or neutral opinion. Choose sentiment analysis if you want to build a feedback analyser.  
* Track C: recognise an action and extract its details. Choose limited semantic parsing if your team is ready to annotate fields such as place, date and time.

Read “06 Choose your task” before deciding. Keep your assigned team and language, and confirm any unresolved language choice with the organisers. Record your track, source and reviewer in the data plan before large-scale annotation. Request a separate written scope if you want to work on NER or news topics.

# 2\. Begin with these actions

* Find your team in “03 Teams and dataset routes”. Report any correction through the event communication channel.  
* Read the handbook and download the starter kit when the materials are shared by email on Monday, 2 November. Attend the official Google Meet walkthrough and questions session on Tuesday, 3 November, from 6:00 to 7:00 p.m. EAT. Join the walkthrough: https\://meet.google.com/fej-afrs-qmq  
* Agree who will lead language review, data/documentation and code/demo work. Share duties where useful and keep evidence of every member's contribution.  
* Create your own team GitHub repository. Download starter kit v2 from “04 Build and demonstrate” and run the practice example for your chosen track.  
* Prepare 30 sample records and a short data plan. Review the sample before producing the full dataset.

# 3\. Submit these deliverables

* Your accepted contribution dataset: Track A, at least 250 records; Track B, at least 300; Track C, at least 250 including 100 or more slot-bearing records. Follow the split and review rules in tab 06\.  
* An annotation guide, source log, dataset card, quality report and contribution/AI-use statement.  
* Runnable baseline code, actual evaluation results and an analysis of up to five actual mistakes; if there are fewer, report all of them.  
* A working Streamlit or mobile demo, run instructions and a 2–3 minute backup recording.  
* Your GitHub repository URL, frozen commit SHA and submission package. Follow the final NLP Hub repository instructions when announced.

**Go above and beyond.** Treat these deliverables as the minimum requirements. Feel free to extend your solution with thoughtful, useful improvements, such as richer reviewed language data, stronger error analysis, a carefully tested model improvement or a more accessible demo. Initiative and creativity are admirable and will be considered in judging. Explain what you added and show evidence of its value. Complete the required deliverables first and keep your extensions within the datathon's text-based scope, data-use rules and deadline.

# 4\. Follow the dates

* Materials release: Monday, 2 November, by email. Datathon work begins: Tuesday, 3 November. Official walkthrough and questions: Tuesday, 3 November, 6:00–7:00 p.m. EAT, Google Meet.  
* Midpoint progress follow-up and Q\&A: Friday, 6 November, 6:00–7:00 p.m. EAT. Show your sample, source log, review decisions and running baseline. Use the Google Meet link in your calendar invitation.

**Final submission: Wednesday, 11 November 2026, 11:59 p.m. EAT.**

* Judging: 12–13 November. Finalists announced by Friday, 13 November, 5:00 p.m. EAT.  
* Finalist preparation: 14–16 November. Presentations and awards: Tuesday, 17 November, during the Dean's Roundtable. Follow the event announcement for the exact presentation time.

# 5\. Understand the marking

Use the rubric in tab 05 to check your work: data quality 30 marks; provenance/ethics 20; coverage 15; baseline/evaluation 15; reproducibility 10; demo/teamwork 10\. Meet the same evidence standard whichever track you choose. Do not compare raw model scores across different tasks or languages.

# 6\. Use this guide

* Read tab 02 for contribution rules, data fields and intent examples.  
* Use tab 03 to find your team and dataset routes.  
* Follow tab 04 to install the kit, train, test and build your demo.  
* Check tab 05 before your final submission.  
* Read tab 06 for your chosen task's target, examples and evaluation.  
* Follow tab 07 after the practice run. Use its completed examples to write your own documents.

Use written text only. Ask for help through the official event channel if you lack a competent language reviewer, encounter a dataset-access problem or cannot run the code. Include your team number, language, the problem and a small example without private information.

Use your own GitHub repository now. The organisers will provide the final NLP Hub submission repository and process separately. Keep your work versioned while you wait.

Keep private data and unverified permission records out of public GitHub. Declare AI assistance, check its output and explain your own work. Show uncertainty and failures honestly; a high model probability does not guarantee a correct prediction.

# **The Task and Worked Examples**

## Track A intent guidance \| Track C reuses these action labels \| See tab 06 for Track B

# **1\. Understand the prediction**

Read the request in your team's language and predict its action label. Display a clear simulated response. Do not translate the input into English as a hidden prediction step.

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** weather\_query

**Show in your demo:** “You are asking about the weather.”

You may use the English examples below to understand the meanings. Write natural language-specific examples rather than translating every word mechanically. Record genuinely natural code-switching and the language variety when relevant.

# **2\. Track A and C: use these 10 action labels**

Use the exact MASSIVE-aligned action labels shown below. Put the label in the label column of the v2 template. Keep label identifiers consistent across languages. Follow these working definitions and examples when you annotate.

## **weather\_query**

Use this label to: Ask for weather or a forecast.

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** weather\_query

**Check:** Use this label for a forecast request. Use news\_query for a request to read news about a storm.

## **datetime\_query**

Use this label to: Ask for the current time, date or day.

**For Example:**

**Input:** Ni saa ngapi sasa?

**Output:** datetime\_query

**Check:** Do not use this label when the user asks you to set an alarm.

## **alarm\_set**

Use this label to: Set an alarm that will ring at a requested time.

**For Example:**

**Input:** Wake me at seven tomorrow.

**Output:** alarm\_set

**Check:** Use calendar\_set when the user asks you to schedule an event.

## **calendar\_set**

Use this label to: Add an event or scheduled reminder to a calendar.

**For Example:**

**Input:** Add my project meeting for Friday.

**Output:** calendar\_set

**Check:** Use calendar\_query when the user asks about an existing event.

## **calendar\_query**

Use this label to: Read events already on a calendar.

**For Example:**

**Input:** What meetings do I have today?

**Output:** calendar\_query

**Check:** Do not use this label to create an event.

## **lists\_createoradd**

Use this label to: Create a list or add an item.

**For Example:**

**Input:** Ongeza mkate kwenye orodha yangu ya manunuzi.

**Output:** lists\_createoradd

**Check:** Use lists\_query when the user wants to read an existing list.

## **lists\_query**

Use this label to: Read an existing list.

**For Example:**

**Input:** What is on my shopping list?

**Output:** lists\_query

**Check:** Do not use this label when the user asks to add an item.

## **play\_music**

Use this label to: Start music playback.

**For Example:**

**Input:** Cheza muziki.

**Output:** play\_music

**Check:** Exclude a general question about who wrote a song; it does not request playback.

## **news\_query**

Use this label to: Read news or headlines.

**For Example:**

**Input:** Nipe habari za hivi karibuni.

**Output:** news\_query

**Check:** Use weather\_query for a forecast request.

## **qa\_definition**

Use this label to: Explain the meaning of a word or concept.

**For Example:**

**Input:** Neno bayoanuwai lina maana gani?

**Output:** qa\_definition

**Check:** Exclude general factual questions that do not ask for a definition.

**Each accepted record must have one clear intent. Exclude unclear, multi-intent or unsupported examples and explain the exclusion. Do not invent labels to make the data fit.**

[Official MASSIVE label definitions in the dataset loader](https://huggingface.co/datasets/AmazonScience/massive/blob/main/massive.py)

# **3\. Create a balanced contribution**

Tracks A and C: minimum 25 accepted examples per action, giving 250 total: 15 train, 5 dev and 5 test per action. Track C also needs at least 100 examples with slots. Optional intent stretch: 700 \= (50 train \+ 10 dev \+ 10 test) × 10; it is not a compulsory increase. Track B uses 300 total: 60 train, 20 dev and 20 test for each of positive, negative and neutral. Add useful diversity, not padding.

Training examples teach the model. Development examples help you choose settings. Test examples are held back until your choices are frozen. Every test example must be checked by a competent reviewer who did not author that example. Review a sample of other records too and record disagreements.

The starter validator enforces this minimum split and checks whether your reviewer code differs from the contributor code for independently reviewed records. Automated checks cannot verify genuine independent judgement or fluency.

# **4\. What counts as a contribution**

* New, natural examples authored by people with suitable language knowledge, with permission for the intended use.  
* Human localisation of permitted source examples, with the source ID, changes and language review documented.  
* New human intent annotations on suitable permitted text, including Common Voice sentences that genuinely fit a selected intent.  
* Corrections to existing labels or text, with the original value, reason and review evidence recorded separately.  
* Technical, review and documentation work also counts as a member contribution, recorded in the contribution statement and commits.

# **5\. What does not count**

* Downloading 250 rows and claiming them as newly created data, or counting the same sentence more than once.  
* Changing punctuation, replacing one name or making trivial near-duplicates solely to increase the count.  
* Copying a notebook, README or interface without attribution and describing it as original work.  
* Bulk AI-generated or automatically translated sentences counted as verified human examples. AI may assist coding, debugging or explanation if declared; humans must check the work.  
* Fine-tuning on test records, reporting development results as test results, inventing scores or choosing only successful demo examples.

Unchanged external training material may be useful, but keep it separate from the track-specific contribution file. It does not count toward the 250/300 target. The supplied baseline trains only on your contribution training split; report external-data experiments separately.

# **6\. A worked record**

`record_id: T23-001`

`language: sw-KE`

`text: Je, kutakuwa na mvua kesho?`

`intent: weather_query`

`source_method: original_human`

`source_dataset: team_authored`

`source_version: v1`

`source_record_id: T23-001`

`source_url: not_applicable`

`licence_or_permission: documented_contributor_permission`

`contributor_code: T23-A`

`reviewer_code: T23-B`

`review_status: independently_reviewed`

`group_id: T23-weather-rain-01`

`split: test`

This is an illustration, not permission evidence. Replace it with your own work and link permission evidence in your private source log. If you create paraphrases or translations of the same underlying source, give them the same group\_id and keep the entire group in one split.

Keep original scripts and diacritics. Document any normalisation. Use pseudonymous contributor/reviewer codes, not admission numbers or phone numbers. Exclude personal details from request text.

# **7\. Keep a complete record**

Starter kit v2 uses label for the intent/action or sentiment class. Required columns: record\_id, language, text, label, source\_dataset, source\_version, source\_record\_id, source\_url, source\_method, licence\_or\_permission, contributor\_code, reviewer\_code, review\_status, group\_id and split. Track C adds slots\_json. Legacy intent headers remain accepted for A/C. Use the matching template; add variant or adjudication\_note when useful.

Allowed source\_method values: original\_human, human\_localised, newly\_annotated and corrected\_with\_evidence. Accepted records use self\_reviewed or independently\_reviewed; all test records use independently\_reviewed. Explain justified not\_applicable values in the dataset card.

# **Teams, Languages and Dataset Routes**

24 teams \| Member names, email addresses and submitted phone numbers

Keep the team and primary language shown below, confirming any unresolved choice at launch. Choose A intent, B sentiment, or C limited semantic parsing with your data plan. A dataset suitable for one task is not automatically suitable for the others.

Contact your teammates using the details below. Each member is listed as Name \| Email \| Phone. “Phone: not provided” means no individual phone number was submitted. Use these details only for datathon coordination and keep them within the participant group; do not publish or forward this contact list.

**No team should scale up data collection before a competent language reviewer and a permitted data route are confirmed.**

# **1\. Dataset routes used below**

Route A: MASSIVE provides existing intent-labelled reference data for Kiswahili, Arabic and French. Use the matching locale and selected labels, preserve source IDs and splits, and make a documented new contribution. Arabic/French remains a language-choice decision for Team 19\.

[Route A: MASSIVE official dataset card, language list and files](https://huggingface.co/datasets/AmazonScience/massive)

Route B: human-authored or human-localised examples in a confirmed language, reviewed by a competent speaker. There is no verified direct intent dataset for several assigned languages in the resources checked. Use MASSIVE for the common label schema; do not claim it supplies data in an unsupported language.

Optional Route C: inspect Common Voice text for the exact language/release, select only suitable sentences, then add intent labels and review. Text availability and task fit are not confirmed by the assignment list. Do not download or process audio for this task.

[Route C: Common Voice releases and download guidance](https://github.com/common-voice/cv-dataset)

[Common Voice sentence-text fields and archive structure](https://github.com/common-voice/cv-dataset/blob/main/datasets/scripted-speech/README.md)

# **2\. Your team**

## **Team 1 \| Data warriors**

**Members:**

**1\. Ian Kitheka** \| [ian.kitheka@strathmore.edu](mailto:ian.kitheka@strathmore.edu) \| Phone: 0716548444

**2\. Austin Mwendo** \| [austin.muia@strathmore.edu](mailto:austin.muia@strathmore.edu) \| Phone: not provided

**3\. Esther Muema** \| [esther.muema@strathmore.edu](mailto:esther.muema@strathmore.edu) \| Phone: 0710182030

**Working language:** Kamba

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 2 \| Jaribu**

**Members:**

**1\. Guyo Kana Godana** \| [guyo.kana@strathmore.edu](mailto:guyo.kana@strathmore.edu) \| Phone: 0741574715

**2\. Elsa Umutoni** \| [umutoni.bucagu@strathmore.edu](mailto:umutoni.bucagu@strathmore.edu) \| Phone: not provided

**3\. Danick Ndatinya** \| [danick.ndatinya@strathmore.edu](mailto:danick.ndatinya@strathmore.edu) \| Phone: not provided

**Working language:** Kinyarwanda (proposed)

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 3 \| Ubuntu**

**Members:**

**1\. Alvin Murithi** \| [alvin.muriuki@strathmore.edu](mailto:alvin.muriuki@strathmore.edu) \| Phone: 0797814639

**2\. Mukundi Witness Chingwena** \| [mukundi.chingwena@strathmore.edu](mailto:mukundi.chingwena@strathmore.edu) \| Phone: not provided

**3\. Natalie Chelagat** \| [natalie.chelagat@strathmore.edu](mailto:natalie.chelagat@strathmore.edu) \| Phone: not provided

**Working language:** To confirm: Shona / Kimeru

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 4 \| SautiByte**

**Members:**

**1\. Omwoyo Leo Kinara** \| [kinara.leo@strathmore.edu](mailto:kinara.leo@strathmore.edu) \| Phone: 0733332587

**2\. Daniel Brian Kikuvi** \| [brian.daniel@strathmore.edu](mailto:brian.daniel@strathmore.edu) \| Phone: not provided

**3\. Zakariya Mohamed** \| [zakariya.mohamed@strathmore.edu](mailto:zakariya.mohamed@strathmore.edu) \| Phone: not provided

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 5 \| Zeus**

**Members:**

**1\. Patriciah Mbua** \| [patriciah.mbua@strathmore.edu](mailto:patriciah.mbua@strathmore.edu) \| Phone: 0797174462

**2\. Robi Memusi** \| [memusi.robi@strathmore.edu](mailto:memusi.robi@strathmore.edu) \| Phone: not provided

**3\. Mariam Abdi** \| [mariam.abdi@strathmore.edu](mailto:mariam.abdi@strathmore.edu) \| Phone: not provided

**Working language:** To confirm: Kikuyu / Somali

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 6 \| Data buddies**

**Members:**

**1\. Sydney Aisha** \| [aisha.sydney@strathmore.edu](mailto:aisha.sydney@strathmore.edu) \| Phone: 0725740426

**2\. Tiffany Wanjiru** \| [tiffany.wanjiru@strathmore.edu](mailto:tiffany.wanjiru@strathmore.edu) \| Phone: not provided

**3\. Poni Yokwe** \| [poni.yokwe@strathmore.edu](mailto:poni.yokwe@strathmore.edu) \| Phone: not provided

**Working language:** Luganda (proposed)

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 7 \| Datalynk**

**Members:**

**1\. Musimwa Caroline-berly Mirindi** \| [caroline-berly.musimwa@strathmore.edu](mailto:caroline-berly.musimwa@strathmore.edu) \| Phone: \+254 720278069

**2\. Mwangi Emmah Wambui** \| [emmah.mwangi@strathmore.edu](mailto:emmah.mwangi@strathmore.edu) \| Phone: not provided

**3\. Gathingu Tatyana Wamuyu** \| [tatyana.gathingu@strathmore.edu](mailto:tatyana.gathingu@strathmore.edu) \| Phone: not provided

**Working language:** Lingala

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 8 \| Verity**

**Members:**

**1\. Wayne Kimutai** \| [kimutai.wayne@strathmore.edu](mailto:kimutai.wayne@strathmore.edu) \| Phone: 0703385412

**2\. Grace Wangari** \| [grace.wangari@strathmore.edu](mailto:grace.wangari@strathmore.edu) \| Phone: not provided

**3\. Joy Tele** \| [joy.tele@strathmore.edu](mailto:joy.tele@strathmore.edu) \| Phone: not provided

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 9 \| Cheche**

**Members:**

**1\. Cindy Wanini Gichuhi** \| [cindy.gichuhi@strathmore.edu](mailto:cindy.gichuhi@strathmore.edu) \| Phone: 0798199985

**2\. Ivy Tanui** \| [ivy.tanui@strathmore.edu](mailto:ivy.tanui@strathmore.edu) \| Phone: not provided

**3\. Irene Kariuki** \| [irene.kariuki@strathmore.edu](mailto:irene.kariuki@strathmore.edu) \| Phone: not provided

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 10 \| MANENO MASHINANI**

**Members:**

**1\. Lydiah Wangui Wangaru** \| [lydiah.wangaru@strathmore.edu](mailto:lydiah.wangaru@strathmore.edu) \| Phone: 0110022277

**2\. Keisha Wambui Wairimu** \| [keisha.wairimu@strathmore.edu](mailto:keisha.wairimu@strathmore.edu) \| Phone: not provided

**3\. Hellen Njeri Karanja** \| [hellen.karanja@strathmore.edu](mailto:hellen.karanja@strathmore.edu) \| Phone: not provided

**Working language:** Kikuyu (proposed)

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 11 \| Dholuo**

**Members:**

**1\. Mboya Celestine Adhiambo** \| [celestine.mboya@strathmore.edu](mailto:celestine.mboya@strathmore.edu) \| Phone: 0700282402

**2\. Emma Ogwayo** \| [emma.ogwayo@strathmore.edu](mailto:emma.ogwayo@strathmore.edu) \| Phone: \+254794583325

**3\. Nicholas Njue Wambui** \| [njue.wambui@strathmore.edu](mailto:njue.wambui@strathmore.edu) \| Phone: 0769160473

**Working language:** Dholuo

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 12 \| Kikuyu 1**

**Members:**

**1\. Moses Mwangi** \| [moses.gmwangi@strathmore.edu](mailto:moses.gmwangi@strathmore.edu) \| Phone: not provided

**2\. Maina Michael** \| [gathungu.maina@strathmore.edu](mailto:gathungu.maina@strathmore.edu) \| Phone: \+254792548476

**3\. John Mwaura** \| [john.mwaura@strathmore.edu](mailto:john.mwaura@strathmore.edu) \| Phone: 0108381840

**Working language:** Kikuyu

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 13 \| Kikuyu 2**

**Members:**

**1\. Nadine Njora** \| [nadine.njora@strathmore.edu](mailto:nadine.njora@strathmore.edu) \| Phone: 0701656180

**2\. Wanyingi Shirleen Muthoni** \| [shirleen.wanyingi@strathmore.edu](mailto:shirleen.wanyingi@strathmore.edu) \| Phone: 0768435333

**3\. Celestine Nyingi** \| [celestine.nyingi@strathmore.edu](mailto:celestine.nyingi@strathmore.edu) \| Phone: 0702109487

**Working language:** Kikuyu

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 14 \| Maa**

**Members:**

**1\. Philip Tait** \| [philip.tait@strathmore.edu](mailto:philip.tait@strathmore.edu) \| Phone: 0716914156

**2\. Mapelu Neema Naserian** \| [neema.mapelu@strathmore.edu](mailto:neema.mapelu@strathmore.edu) \| Phone: 0790819897

**3\. Mayabi Muigai Ivan** \| [muigai.mayabi@strathmore.edu](mailto:muigai.mayabi@strathmore.edu) \| Phone: not provided

**Working language:** Maa

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

**Reviewer support needed: the language anchor reported basic proficiency. Arrange a competent reviewer before accepting annotations.**

## **Team 15 \| Kisii**

**Members:**

**1\. Jerome Nyasimi** \| [jerome.nyasimi@strathmore.edu](mailto:jerome.nyasimi@strathmore.edu) \| Phone: 0797229826

**2\. Natalia Odhiambo** \| [natalyafaith.odhiambo@strathmore.edu](mailto:natalyafaith.odhiambo@strathmore.edu) \| Phone: not provided

**3\. Gianna Mutheu** \| [gianna.mwangangi@strathmore.edu](mailto:gianna.mwangangi@strathmore.edu) \| Phone: 0796956841(WhatsApp)

**Working language:** Kisii

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

**Reviewer support needed: the language anchor reported basic proficiency. Arrange a competent reviewer before accepting annotations.**

## **Team 16 \| Kinyarwanda**

**Members:**

**1\. Atta Wasike** \| [atta.wasike@strathmore.edu](mailto:atta.wasike@strathmore.edu) \| Phone: 0792079566

**2\. Emmanuel Abelle** \| [emmanuel.abelle@strathmore.edu](mailto:emmanuel.abelle@strathmore.edu) \| Phone: not provided

**3\. Amana Achieng Okello** \| [amana.okello@strathmore.edu](mailto:amana.okello@strathmore.edu) \| Phone: 0794367798

**Working language:** Kinyarwanda

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 17 \| Lingala**

**Members:**

**1\. Aganze Shukuru Chris Gift** \| [aganze.shukuru@strathmore.edu](mailto:aganze.shukuru@strathmore.edu) \| Phone: 0792936212

**2\. Lenny Mwaura Mwangi** \| [mwaura.mwangi@strathmore.edu](mailto:mwaura.mwangi@strathmore.edu) \| Phone: 0790263292

**3\. Chelcie Laura Barasa** \| [chelcie.barasa@strathmore.edu](mailto:chelcie.barasa@strathmore.edu) \| Phone: 0793942948

**Working language:** Lingala

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 18 \| Luganda**

**Members:**

**1\. Ssennoga Tendo Lynette** \| [tendo.ssennoga@strathmore.edu](mailto:tendo.ssennoga@strathmore.edu) \| Phone: \+256783790792

**2\. Vincent Murage Mureithi** \| [vincent.mureithi@strathmore.edu](mailto:vincent.mureithi@strathmore.edu) \| Phone: 0792956128

**3\. Ravine Riang'a** \| [ravine.rianga@strathmore.edu](mailto:ravine.rianga@strathmore.edu) \| Phone: 0758585870

**Working language:** Luganda

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 19 \| Arabic / French**

**Members:**

**1\. Ezra mutugii ntwiga** \| [ezra.ntwiga@strathmore.edu](mailto:ezra.ntwiga@strathmore.edu) \| Phone: 0743523819

**2\. Harry Kipngetich Sigei** \| [harry.sigei@strathmore.edu](mailto:harry.sigei@strathmore.edu) \| Phone: 0741043687

**3\. Michael Mwenda Majau** \| [michael.majau@strathmore.edu](mailto:michael.majau@strathmore.edu) \| Phone: 0727573017

**Working language:** To confirm: Arabic / French

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 20 \| Kiswahili 1**

**Members:**

**1\. Hafswa Sufi** \| [hafswa.sufi@strathmore.edu](mailto:hafswa.sufi@strathmore.edu) \| Phone: \+254 76964 7419

**2\. Gitau Irene Nyambura** \| [irene.gitau@strathmore.edu](mailto:irene.gitau@strathmore.edu) \| Phone: 0717035023

**3\. Kathy Auma Ochieng** \| [kathy.ochieng@strathmore.edu](mailto:kathy.ochieng@strathmore.edu) \| Phone: 0782550220

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 21 \| Kiswahili 2**

**Members:**

**1\. Sharon Njogorio** \| [sharon.njogorio@strathmore.edu](mailto:sharon.njogorio@strathmore.edu) \| Phone: 0708590769

**2\. Nyabuto Daniel Obuya** \| [daniel.nyabuto@strathmore.edu](mailto:daniel.nyabuto@strathmore.edu) \| Phone: 0740378920

**3\. Joan Gichana** \| [joan.gichana@strathmore.edu](mailto:joan.gichana@strathmore.edu) \| Phone: 0114978709

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 22 \| Kiswahili 3**

**Members:**

**1\. Gift Githaka Gicheru** \| [gift.githaka@strathmore.edu](mailto:gift.githaka@strathmore.edu) \| Phone: 0705761819

**2\. Brian Terer** \| [brian.kterer@strathmore.edu](mailto:brian.kterer@strathmore.edu) \| Phone: 0719123126

**3\. Nyawita Elsie Damar** \| [elsie.nyawita@strathmore.edu](mailto:elsie.nyawita@strathmore.edu) \| Phone: 0116801809

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 23 \| Kiswahili 4**

**Members:**

**1\. Fiddel Omondi Owuor** \| [fiddel.owuor@strathmore.edu](mailto:fiddel.owuor@strathmore.edu) \| Phone: 0115013290

**2\. Claudia Ng'endo** \| [claudia.ngoru@strathmore.edu](mailto:claudia.ngoru@strathmore.edu) \| Phone: 0723 047 088

**3\. Amani Chebet Ng’eno** \| [amani.ngeno@strathmore.edu](mailto:amani.ngeno@strathmore.edu) \| Phone: not provided

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

## **Team 24 \| Kiswahili 5**

**Members:**

**1\. Moses Kibet** \| [moses.kipkemboi@strathmore.edu](mailto:moses.kipkemboi@strathmore.edu) \| Phone: 0769188962

**2\. Krysia Njoroge** \| [krysia.njoroge@strathmore.edu](mailto:krysia.njoroge@strathmore.edu) \| Phone: 0111490655

**3\. Nathan Mwangi Njuguna** \| [nathan.njuguna@strathmore.edu](mailto:nathan.njuguna@strathmore.edu) \| Phone: 0734693118

**Working language:** Kiswahili

**Task:** Choose A, B or C in this language.

**Dataset:** Use the matching source route in section 1\. Use permitted human examples if the chosen dataset does not cover your language.

**Action:** Confirm your source and reviewer in the data plan.

# **3\. How to use Common Voice as text**

1. Choose an available release and locale through the official source. Read its datasheet and terms. Prefer validated\_sentences.tsv when supplied.  
2. Extract sentence text, sentence\_id and necessary source/variety information. Clip metadata can contain repeated text; deduplicate. Do not include speaker IDs or demographics in your text dataset.  
3. Check a small sample with a fluent reviewer. Many sentences are statements rather than requests. Keep only examples that genuinely fit the selected intents; do not force labels.  
4. Add your own intent annotations, review, provenance and split groups. Speech validation votes do not verify your new intent labels.

A whole archive may be required to access text metadata, depending on the release. Extract only what is needed and do not load audio. If there is insufficient relevant text, use Route B after checking permission and reviewer support.

# **4\. Other useful resources**

These are references or possible organiser-approved alternatives, not extra requirements and not automatic permission to change tasks. Different tasks need different labels, evaluation and marking arrangements.

[KINNEWS: Kinyarwanda news classification](https://github.com/Andrews2017/KINNEWS-and-KIRNEWS-Corpus)

[MasakhaNER 2.0: entity extraction, including Kiswahili, Luo, Luganda, Kinyarwanda and Shona](https://github.com/masakhane-io/masakhane-ner/blob/main/MasakhaNER2.0/README.md)

[FLORES: translation evaluation; keep benchmark evaluation data out of training](https://github.com/facebookresearch/flores/blob/main/flores200/README.md)

[AfriQA: question answering; inspect pivot-language material and task setup](https://github.com/masakhane-io/afriqa)

[African NLP dataset catalogue: follow through to each original source](https://github.com/OmondiKevin/africanlp-public-datasets/blob/main/README.md)

Sentiment is now a supported choice. The original AfriSenti publisher states CC BY 4.0; pin the upstream source/version and cite it. Some mirror metadata conflicts with the publisher, so record the exact version and its terms. For unsupported languages, use permitted human-authored or newly annotated material with a fluent reviewer. Source and code licences remain distinct.

# **Build and Demonstrate**

## A supported beginner path with room for more experienced teams

# **1\. Download the materials**

Starter kit v2.0 contains three supported tracks, 100 intent and 100 semantic practice records, 120 sentiment practice records, Kiswahili taxonomy illustrations, NEXT\_STEPS.md, NATURAL\_DATA.md, empty and completed documentation examples, readable evaluation reports and a Streamlit app. Credit the kit and upstream sources.

[Download starter kit v2.0](https://drive.google.com/file/d/1OTDqXGAWxq9Kf7mTFLmu4rjzcYMzKlqQ/view?usp=drivesdk)

**All practice records are constructed English teaching examples and count as ZERO contribution records. No 80% F1 target is promised. Their repeated patterns and small test sets do not establish real-world language performance.**

# **2\. Understand the workflow**

*![][image1]*

*Training, development and test data have separate roles. The test set informs the final report, not model tuning.*

# **3\. Create your own GitHub repository**

1. One team member creates a repository, for example nlp-datathon-2026-team-23, and invites the other two members as collaborators. Use your own account or team organisation.  
2. Add the starter code and a README with the team number, language and member roles. Commit small, meaningful changes as you work.  
3. Keep source logs and cleared contribution data organised. Keep personal or uncleared records private; give organisers the access needed for assessment.

Suggested folders: data/ for permitted contribution data, templates/ for completed documentation, artifacts/ for model and metric outputs, and app.py for the UI. Ignore .venv/, \_\_pycache\_\_/, secrets, tokens and large raw dataset archives. Store heavy model files through an organiser-approved route if GitHub size limits apply.

# **4\. Run the practice example**

Use Python 3.10 or later. Open a terminal in the extracted starter-kit folder. A virtual environment keeps the project dependencies together. On Windows you may need py or python instead of python3.

python \-m venv .venv

\# macOS/Linux:

source .venv/bin/activate

\# Windows PowerShell instead:

.venv\\Scripts\\Activate.ps1

python \-m pip install \-r requirements.txt

python validate.py \--track intent \--data data/practice\_intent.csv \--practice

python train.py \--track intent \--data data/practice\_intent.csv \--practice

python evaluate.py \--track intent \--data data/practice\_intent.csv \--practice

python \-m streamlit run app.py

Run the activation command for your operating system only. Follow the local address printed by Streamlit. A localhost address works on your computer; it is not a public demo link. The notebook/Colab route is optional if your team already knows it; do not assume compute credits or paid tools are provided.

# **5\. Build your real dataset**

1. Copy data/template.csv to data/contribution.csv. Read the intent examples. Agree language-specific spelling and boundaries with your reviewer.  
2. Prepare 30 examples covering your chosen track's labels before scaling up. Review them together, discuss naturalness and edge cases, and record decisions. For semantic parsing, verify the slot values and character spans.  
3. Complete the target for your chosen track. Identify related examples with group\_id before splitting; keep source translations, close paraphrases and duplicates together. All test records need independent review.  
4. Independently review every test example. Record corrections and disagreements in the quality report. Verify source rights and permission.  
5. Run the validator, inspect its messages, correct problems and rerun. A passing validator does not prove that language, labels or rights are correct.

# **6\. Train, develop and evaluate**

python validate.py \--data data/contribution.csv

python train.py \--data data/contribution.csv

\# Inspect dev\_metrics.json and make decisions using development data only.

\# Freeze the model/data/code choices, then run the final evaluation:

python evaluate.py \--data data/contribution.csv

python \-m streamlit run app.py

The classification baseline is character TF-IDF with logistic regression and a majority comparator. Track C adds a training-only surface-value slot matcher. Artifacts are stored separately in artifacts/\<track\>/. Evaluation prints accuracy, macro-F1 and per-label F1 bars, and saves metrics, predictions and per\_label\_report.csv. Track C also reports slot F1 and full-frame exact match. The validator is a structural aid, not proof of language quality.

Accuracy is the fraction of correct predictions. Use macro-F1 to give each class equal importance. The report and confusion matrix show which labels are confused. Report your test size, per-label counts and up to five actual mistakes; report all if there are fewer, and explain their likely causes.

**Choose settings on development data. Evaluate the frozen approach on test data once. A lower-than-expected result is acceptable when reported honestly; invented improvement is not.**

# **7\. Demonstration requirements**

* Show the team number, working language and prototype status.  
* Accept a new written request, predict an intent and show a labelled simulated response or action.  
* Show at least three successful examples and at least two real failures or unsupported requests, with explanations.  
* Display or link to the evaluation results and the dataset contribution summary.  
* Provide run instructions and a 2–3 minute backup video or recording that judges can access.

Streamlit route: adapt app.py and run it locally. Mobile route: build an equivalent input/prediction/output screen and document how the exact saved classifier is called. A set of hard-coded responses or an interface mock-up alone does not meet the model-demo requirement. A mobile UI earns no automatic bonus over Streamlit.

The app shows friendly labels and an explicitly uncalibrated model probability. It still forces a known class for unsupported text. Track C's memorised slot matcher can miss unseen values. Show these failures; no real actions, text-to-SQL execution or factual answers are required.

# **8\. Troubleshooting**

If installation fails, copy the error and your Python version to your team issue log. If the model fails because classes are missing, check every split has all labels. If a dataset link fails or the language lacks support, ask the organisers and continue documentation or reviewer work while the issue is resolved.

The starter README contains the same run instructions, file explanations and limitations. Only load model files you created and trust. Use plain dependency files and record any changes so judges can reproduce your result.

# **Marking and Final Submission**

## Transparent assessment of data quality, evidence and a working prototype

**The rubric totals 100 marks across all supported tracks. Data quality and responsible sourcing carry 50 marks. High model scores or a polished interface cannot compensate for unsupported data claims.**

# **1\. Marking rubric**

## **Data quality and annotation: 30 marks**

Show natural, accurate language; correct and consistent labels; a clear annotation guide; independent review; and evidence of corrections. Keep review decisions traceable and explain the language variety.

## **Provenance, ethics and rights: 20 marks**

Show source IDs, versions, URLs, permission or licence, transformations, contributor credit and AI-use disclosure. Keep personal details out of released data. Do not present downloaded or generated rows as original human work. The same standard applies to every team.

## **Contribution coverage and balance: 15 marks**

Meet your track's contribution target with useful class/intent coverage and, for C, varied slot-bearing examples. Distinguish contributions from unchanged downloads. Judges reward meaningful diversity and balance rather than padding or trivial variants.

## **Baseline and evaluation: 15 marks**

Use suitable held-out splits and report actual results. A/B: accuracy, macro-F1, per-label F1 and majority baseline. C: intent macro-F1, exact type-and-span slot F1, full-frame exact match, JSON validity and unseen-slot-value errors. Judges assess experimental quality and baseline comparison within the declared track; raw scores across tasks/languages are not directly ranked.

## **Reproducibility and documentation: 10 marks**

A judge should be able to find and run your code, load the cleared data, inspect the frozen commit, understand dependencies, reproduce results and see each member's contribution.

## **Demonstration, explanation and teamwork: 10 marks**

Show a working Streamlit or mobile interface connected to the declared model. Explain examples and limitations clearly, include a backup recording and give credible evidence of shared work. Visual polish alone receives little credit.

**Go above and beyond.** Judges will recognise initiative, creativity and useful improvements beyond the minimum deliverables within the relevant criteria above. For example, demonstrate richer reviewed language coverage, compare an improved model fairly with the baseline, test challenging inputs or make your demo easier to use. Explain the added value and provide reproducible evidence. Extra features or a larger dataset do not automatically earn higher marks; quality, relevance and evidence matter. The rubric remains out of 100, and extensions do not replace required deliverables.

# **2\. How the marks are calculated**

Check your evidence against the 0–4 rating scale: 0 \= absent or unusable; 1 \= major gaps; 2 \= partly complete; 3 \= complete with minor gaps; 4 \= strong and well evidenced.

Calculate criterion marks as (level ÷ 4\) × weight.

**For Example:**

**Input:** Data-quality level \= 3; criterion weight \= 30 marks.

**Output:** (3 ÷ 4\) × 30 \= 22.5 marks.

Add the six criterion marks to obtain a score out of 100\. Where multiple judges assess your team, the moderated mean total applies. A final tie is resolved using provenance/ethics first, then data quality. Follow the published rubric for your submission.

# **3\. Submission and finalist-readiness checks**

* All required data, documents, code, evaluation outputs and demo evidence are present and accessible to judges.  
* The language choice and reviewer are confirmed. The accepted contribution file meets the target and required review/split standards.  
* No unresolved material privacy, permission, fabricated-result or undisclosed-generation issue remains. Flag and quarantine disputed records; do not conceal them.

Judges can provide feedback on incomplete work, but finalist consideration requires a complete, reviewable package and resolution of material integrity/rights problems. Ask early about genuine access or language-support barriers; do not silently reduce requirements or invent evidence.

# **4\. Prepare your final package**

1. Finish and run the validator, baseline, final evaluation and demo. Complete the annotation guide, dataset card, quality report and contribution/AI-use statement.  
2. Freeze your work with a Git commit and tag, for example submission-v1. Record the full commit SHA. Create a ZIP snapshot of the same state.  
3. Prepare a submission manifest: team number/name, primary language, GitHub URL, commit SHA, data counts, source licences, metric-file location, demo run instructions, demo/recording location and known unresolved issues.  
4. Use the final NLP Hub GitHub repository and submission process when announced. Follow its instructions for a pull request or upload; do not guess the URL or assume a personal repository link is the final hand-in.

**Own team GitHub repository now. Final NLP Hub GitHub repository later. Deadline: 11 November 2026, 11:59 p.m. EAT.**

If the final repository is not available near the deadline, contact Kevin and Titus for the official fallback. Keep the frozen commit and ZIP ready. A timestamped commit alone does not prove that the required submission channel received your work.

# **5\. Suggested README checklist**

* Team, members/roles, language/variety and the problem addressed.  
* What you contributed, what you reused, data counts and source/permission summary.  
* Install, validate, train, evaluate and demo commands; Python version and dependencies.  
* Frozen experiment details, test results, majority baseline, mistakes and limitations.  
* Contribution/AI-use statement, code licence, source dataset terms and any pending data-release decision.

# **6\. Showcase and stewardship**

Finalists should prepare a five-minute presentation: problem and language; data contribution; review evidence; short demo; results and limitations. Organisers will confirm the final running order and presentation arrangements.

The NLP Hub will review accepted submissions for a possible combined corpus. Contributors will be credited appropriately. Awards, contributions and paper authorship are separate matters; participation does not guarantee a publication or author position.

Keep uncleared data restricted until rights and quality review are complete. Public GitHub code can link to permitted data, while private permission evidence stays outside the public repository. Publishing the handbook as a webpage does not make every dataset or student response public.

# **7\. Complete your final check**

Before handing in, check your data, review evidence, runnable code, results, documentation, demo recording and frozen Git commit. Follow the event announcement for launch/support links and the final NLP Hub submission process. Do not include private records in your public repository.

# **Choose Your Task**

## Three supported choices \| Declare one track in your team data plan

**You do not have to choose intent classification. Choose A intent, B sentiment, or C limited semantic parsing, with a confirmed language reviewer and source plan.**

Keep your current team and primary language. Track choice does not mean changing language to whichever has the biggest dataset. Confirm any unresolved language assignment with the organisers. Do not begin one task and silently submit another.

# **Track A. Intent classification**

## **Motivation Example**

Imagine a user asking a local-language assistant about tomorrow's weather. Build a classifier that recognises the request and displays the correct route.

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** Weather enquiry (weather\_query).

**How to solve it:** Collect labelled requests, train the supplied classifier and connect it to a simulated action panel. Use the 10 labels in tab 02\.

Prepare at least 250 accepted contributions, 25 per intent; per intent use at least 15 train, 5 development and 5 test examples. Treat this as a small prototype. Optional stretch: 700 records \= 50 train \+ 10 dev \+ 10 test per intent. Extra rows help only if they add reviewed diversity.

Use **MASSIVE** where it covers your locale, or permitted new human examples/localisation and annotations. Unchanged MASSIVE rows are reference/training material, not new contributions. Report accuracy, macro-F1, per-intent F1, a confusion matrix and a majority-class comparator.

# **Track B. Sentiment analysis**

## **Motivation Example**

Imagine a campus service team reading feedback in your language. Build a system that groups feedback by the opinion expressed. Choose one domain and one clear target for annotation.

**For Example:**

**Input:** Huduma ilikuwa nzuri sana.

**Output:** positive

**For Example:**

**Input:** Nimesikitishwa na huduma hii.

**Output:** negative

**For Example:**

**Input:** Ofisi inafunguliwa asubuhi.

**Output:** neutral

**How to solve it:** Collect permitted feedback, label it consistently, train the sentiment baseline and display its predictions in a feedback interface.

Prepare at least 300 accepted contributions, 100 per label. For each label use at least 60 train, 20 development and 20 test examples. Do not apply the 10-intent validator or action labels to sentiment.

Use upstream AfriSenti for supported languages such as Kiswahili or Kinyarwanda, or permitted new human-authored/newly annotated text in another confirmed language. Record exact release, attribution and rights. The original publisher states CC BY 4.0. A mirrored page with inconsistent metadata should not be your only rights reference.

[AfriSenti original publisher, datasets and starter resources](https://github.com/afrisenti-semeval/afrisent-semeval-2023)

[AfriSenti Hugging Face dataset viewer](https://huggingface.co/datasets/masakhane/afrisenti)

Label approval as positive, disapproval as negative and a statement without clear opinion as neutral. Read the full sentence and its target.

**For Example:**

**Input:** Huduma haikuwa nzuri.

**Output:** negative

**Reason:** The negation changes the meaning of nzuri.

Exclude or adjudicate mixed opinion, sarcasm and unclear targets. Keep an exclusion log.

Demo: type feedback and show its sentiment label and a small summary. This is not emotion detection or a measure of a person's mental state. Metrics: accuracy, macro-F1, per-class counts/F1, confusion matrix and majority baseline. Explain up to five actual errors; report all if there are fewer.

# **Track C. Limited semantic parsing**

## **Motivation Example**

Imagine that recognising a weather request is not enough: your assistant must also identify the place and date mentioned. Extract these details into fields called slots. Choose this advanced track only if your team can check the slot annotations carefully.

**For Example:**

**Input:** Hali ya hewa Nairobi kesho?

**Output:**

{"intent":"weather\_query","slots":\[

  {"type":"location","value":"Nairobi","start":13,"end":20},

  {"type":"date","value":"kesho","start":21,"end":26}

\]}

**How to solve it:** Annotate the action and the exact place/date spans, train the action model, and run the training-only slot matcher. Display the extracted JSON and explain errors. Preserve kesho as written; do not infer an exact calendar date, translate the request or fetch weather. Keep local clock expressions unchanged unless you explicitly implement and evaluate their conversion.

Use the same 10 action labels and only five slot types: location, date, time, item and term. Permit zero or more non-overlapping slots in one request; \[\] means no slot. Exclude multiple actions, nested logic, text-to-SQL and executable commands from this starter scope.

Prepare at least 250 accepted records, with the same 15/5/5 minimum per action and at least 100 records containing one or more slots. Test data should contain slot-bearing and slot-free examples. Include an explicitly identified subset with slot values unseen during training, and report its results separately.

Add slots\_json to the standard CSV. Each slot has type, value, start and end. Indices are Python Unicode character positions, starting at zero; end is exclusive. text\[start:end\] must equal value exactly. Check the entire span, not just the translated meaning.

Use MASSIVE's intent and slot annotations for supported locales. Human-localise/annotate examples for unsupported languages only with reviewer support and source permission. Common Voice sentences have no ready-made semantic frames.

[MASSIVE raw and slot-annotated fields](https://huggingface.co/datasets/AmazonScience/massive/blob/main/README.md)

Start with the action classifier and the supplied matcher, which learns known slot surface values from training annotations only. It is deliberately limited and may miss unseen names or expressions. It is not a general learned semantic parser; extending it is optional and must be documented.

Report intent macro-F1; slot micro-precision/recall/F1 using exact type and character span; full-frame exact match requiring the correct action and entire slot set; and JSON validity. Check the meaning as well as JSON validity; correctly formatted JSON alone is not a correct parse. Compare slot results with an empty-slot baseline and inspect unseen-value failures.

**Semantic parsing is more than printing a JSON wrapper around an intent label. Slot values must be extracted from new input and assessed against independently checked annotations.**

# **Other tasks: possible with a separate written scope**

NER via MasakhaNER 2.0 and news-topic classification via KINNEWS remain possible when a mentor and organisers confirm the dataset language, annotation schema, contribution target, evaluator and demo. The v2 kit implements only A/B/C. Do not feed token-level NER tags into its classification validator or promise unsupported tracks to your team.

[MasakhaNER 2.0 for a separately agreed entity track](https://github.com/masakhane-io/masakhane-ner/blob/main/MasakhaNER2.0/README.md)

[KINNEWS for a separately agreed Kinyarwanda topic task](https://github.com/Andrews2017/KINNEWS-and-KIRNEWS-Corpus)

Audio, unrestricted translation/QA and open-ended semantic parsing are outside the supported starter scope. A request for an alternative should include a 30-example sample, reviewer, source terms, target, evaluation plan and runnable baseline. Keep the existing deadlines.

# **Fair marking across choices**

Use the same rubric in tab 05: 30 data quality, 20 provenance/ethics, 15 coverage, 15 evaluation, 10 reproducibility and 10 demo/teamwork. Report your task-specific results honestly. Do not treat a sentiment accuracy and a semantic-frame score as directly comparable. Explain the evidence and limitations; choosing a harder track does not earn an automatic bonus.

# **Next Steps and Completed Examples**

## Read this after the practice run \| Kit v2.0 includes the editable examples

# **1\. Move from practice to your own work**

1. Choose A, B or C. In the kit commands, these are intent, sentiment and semantic. Open TRACKS.md and agree your source, primary language and reviewer.  
2. Copy the matching empty template to data/contribution.csv. Use label for the class/action; semantic adds slots\_json. Keep practice rows out of this file.  
3. Complete DATA\_PLAN.md and prepare 30 suitable examples covering the selected labels. Discuss them with a reviewer before scaling up.  
4. Read NATURAL\_DATA.md and the annotation examples. Check boundary cases, negation, code-switching and language variety.  
5. Build your track's contribution target. Keep related source examples and translations in the same group and split. Independently review every test record.  
6. Validate, train and inspect development results. Freeze choices before final test evaluation. Use the right \--track option every time.  
7. Complete the real documents, analyse mistakes, run the demo and freeze your GitHub commit. The final NLP Hub submission channel will be provided.

# **2\. Commands for each choice**

\# A: English intent practice

python train.py \--track intent \--data data/practice\_intent.csv \--practice

python evaluate.py \--track intent \--data data/practice\_intent.csv \--practice

\# B: English sentiment practice

python train.py \--track sentiment \--data data/practice\_sentiment.csv \--practice

python evaluate.py \--track sentiment \--data data/practice\_sentiment.csv \--practice

\# C: English semantic practice

python train.py \--track semantic \--data data/practice\_semantic.csv \--practice

python evaluate.py \--track semantic \--data data/practice\_semantic.csv \--practice

\# Launch the UI and choose a trained track

python \-m streamlit run app.py

The installation instructions in tab 04 still apply. For real data, run validate.py, train.py and evaluate.py with \--track YOUR\_TRACK \--data data/contribution.csv, without \--practice. Replace YOUR\_TRACK with one of the three actual names.

Each track stores artifacts in its own folder. Evaluation prints readable scores and per-label F1 bars, and saves per\_label\_report.csv, test\_predictions.csv and test\_metrics.json. Review weak classes instead of looking only at the headline score. A bar with support n=2 is based on only two examples.

# **3\. Completed example: data plan**

Use this fictional example to understand the data-plan format. Replace every detail with your real team's plan.

**Team:** DEMO

**Track:** B, sentence-level sentiment

**Language:** English

**Labels:** positive, negative, neutral

**Source:** organiser-authored practice\_sentiment.csv, kit v2.0

**Plan:** Run the practice workflow, then prepare permitted, independently reviewed examples in the team's real language.

**Important:** Do not claim the practice fixture as a student contribution or real feedback.

A real team's plan must name the task, primary language, variety, exact source/version, contribution method, reviewer capacity, split strategy and members' work. Reviewer codes P1/P2 in a fixture are placeholders, not proof that anyone independently checked it.

# **4\. Completed example: annotation guide**

Annotate one sentence about one declared target. State the boundaries in your guide.

**For Example:**

**Input:** Huduma ilikuwa nzuri sana.

**Output:** positive

**For Example:**

**Input:** Huduma haikuwa nzuri.

**Output:** negative

**Reason:** Read the negation; do not label a sentence from one favourable word alone.

**For Example:**

**Input:** Walimu ni wazuri lakini huduma ni mbaya.

**Output:** Exclude or adjudicate as mixed opinion.

Record the exclusion or review decision rather than forcing a confident label.

Decide from the requested action, not one shared word.

**For Example:**

**Input:** Nipe habari kuhusu mvua iliyonyesha jana.

**Output:** news\_query

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** weather\_query

Ask a fluent reviewer to check the wording and label boundary in your team's language.

# **5\. Completed example: dataset card**

Write your dataset card using clear fields. Use this completed teaching example only as a model.

**Title:** Starter sentiment practice corpus v2.0

**Language:** English

**Task:** Positive/negative/neutral sentiment classification

**Source:** 120 constructed teaching records

**Splits:** 72 train; 24 development; 24 test

**Source method:** practice\_fixture

**Reuse terms:** CC0, as recorded in the starter kit

**Intended use:** Learn the software workflow.

Limitations: artificial patterns, small vocabulary, balanced classes and no claim of independent field validation. It is not evidence about realistic campus feedback or another language. For a real card, replace every field with actual counts, source rights, annotation/review details, variety, contributors and limitations.

# **6\. Completed example: quality and contributions**

Write a quality note. Record the checks you ran, the examples reviewed, disagreements, exclusions, split grouping and actual metrics. Describe up to five observed mistakes; report all if there are fewer.

**For Example:**

**Input:** Huduma haikuwa nzuri.

**Output predicted by a hypothetical model:** positive

**Expected output:** negative

**Reason to investigate:** The model may have missed negation.

**Important:** This is a teaching scenario, not a reported test result. Use actual predictions from your own run.

Write a contribution statement that matches the work actually completed.

**For Example:**

**Member A:** Authored candidate data and drafted annotation rules.

**Member B:** Independently reviewed reserved examples and logged disagreements.

**Member C:** Adapted the model/demo and recorded reproducible runs.

**Evidence:** Record ranges, review logs and commit SHAs.

Declare AI tools, their purpose, affected work and the human checks you applied. Do not copy these example claims as facts about your team.

**Completed example documents are teaching material. Do not copy their fictional permissions, reviewer claims or results into your real submission.**

# **7\. Write language people would naturally use**

* Begin with real situations in the language, not a word-for-word translation list. Ask how someone would actually express the request or opinion.  
* Vary wording, sentence order, length and context. Do not create a large dataset by swapping one name or time into the same template.  
* Preserve spelling conventions and diacritics. Record genuine code-switching and dialect choices instead of treating them automatically as errors.  
* Use non-sensitive examples. Keep source text and changed text distinguishable and explain corrections.  
* Ask another competent speaker to check naturalness and label meaning. Record disagreement and exclusion decisions; they are part of the contribution.

The intent taxonomy CSV now includes Kiswahili illustrations for all 10 labels. They help explain the task; they are not substitutes for evidence of review in each chosen language.

# **8\. Read the model output critically**

Practice sets now contain 100 intent examples, 100 semantic examples and 120 sentiment examples. We do not promise 80% F1. Constructed patterns can make a practice model look stronger than it is; a lower result on varied real text may be more informative.

Display friendly labels and explain the model score.

**For Example:**

**Input:** A new request entered into your trained model.

**Output:** Weather enquiry; model probability (uncalibrated): 80%.

**Important:** This illustrative score is not an observed result or an 80% guarantee of correctness. Replace it with your real output. Show unsupported-input failures and discuss improvements without tuning on the test set.

# **Datathon Launch: From Language Data to a Working Prototype**

## **Strathmore NLP Hub Datathon 2026 \| Task overview and expectations**

Use this overview to understand the problem, choose your task and prepare your team's solution. Refer to the other handbook tabs for team contacts, full task rules, installation instructions and marking details.

# **1\. Motivation Example: why does this work matter?**

An application can only respond usefully if it understands what people mean in their own language. Build reviewed examples that help a model recognise that meaning, then demonstrate the result in a working prototype.

**For Example:**

**Input:** Hali ya hewa Nairobi kesho?

**Output:** A weather enquiry about Nairobi and kesho (tomorrow).

An intent model recognises the request. A semantic parser also extracts its details. A sentiment model instead recognises the opinion in feedback. Better language data lets us test these abilities and expose failures before using them in an application.

![][image2]

Future use: an application or AI agent could use a prediction to propose a tool or next step. MCP (Model Context Protocol) connects AI applications to tools and data. It is not an intent classifier, and a label is not permission to act. Check required fields and permissions, and seek user confirmation where appropriate. For this datathon, a simulated next step is enough; MCP integration is optional.

[Background: official MCP tool documentation](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx)

# **2\. Choose one task and understand its output**

Read the examples below and choose one track with your team. Keep your confirmed language and refer to tab 06 for the full requirements.

## **Track A: intent classification**

Build a request-routing assistant. Use the 10 fixed intent labels in tab 02\.

**For Example:**

**Input:** Je, kutakuwa na mvua kesho?

**Output:** {"prediction":"weather\_query","label":"Weather enquiry","confidence":0.87}

Demo response: “You are asking about the weather.” A forecast service is not required.

## **Track B: sentiment analysis**

Build a feedback analyser. Choose one domain and target; use positive, negative and neutral labels.

**For Example:**

**Input:** Huduma haikuwa nzuri.

**Output:** {"prediction":"negative","confidence":0.86}

Demo response: show the opinion label and a summary. Negative feedback may be flagged for human review; it should not automatically trigger a penalty or message.

**Important: these confidence numbers are illustrative, not measured results. Show your real model output and label its probability as uncalibrated. A high score does not guarantee correctness.**

## **Track C: limited semantic parsing**

Build an action-and-details extractor. Use the same 10 actions plus location, date, time, item and term slots. Choose this track only if your team can review the spans carefully.

**For Example:**

**Input:** Hali ya hewa Nairobi kesho?

**Output:** {"intent":"weather\_query","slots":\[

  {"type":"location","value":"Nairobi","start":13,"end":20},

  {"type":"date","value":"kesho","start":21,"end":26}

\]}

Keep kesho as written. Offsets start at zero and exclude the end position. Display the extracted fields; normalising dates, live tool calls and text-to-SQL are not required. Valid JSON alone is not a correct parse.

* # **3\. Choose sources and make a real contribution**

* MASSIVE: use reference intent/slot annotations only where the locale is supported. Retain source IDs, terms and splits. It does not cover every assigned language.

[Inspect MASSIVE](https://huggingface.co/datasets/AmazonScience/massive)

* AfriSenti: inspect the original publisher for supported sentiment languages, exact release and rights.

[Inspect the original AfriSenti resources](https://github.com/afrisenti-semeval/afrisent-semeval-2023)

* Common Voice: use sentence text only where suitable; preserve sentence IDs and deduplicate repeated text. Add your own task labels and competent review. Speech validation does not validate your intent or sentiment labels. Do not process audio.

[Inspect Common Voice text guidance](https://github.com/common-voice/cv-dataset/blob/main/datasets/scripted-speech/README.md)

* If no suitable source covers your language/task, use permitted human-authored or human-localised examples and document the source method and review.

**Your contribution must add value: new reviewed examples, new annotations, useful localisation or documented corrections. Unchanged downloads, practice rows, renamed files, a code wrapper or duplicated templates do not count as new contribution records.**

Write natural language people would actually use. Declare AI assistance and check its output. Do not call bulk synthetic data human-authored data. Count an example only after it passes your quality and review checks.

# **4\. Build, test and demonstrate your solution**

[Open Starter Kit v2](https://drive.google.com/file/d/1OTDqXGAWxq9Kf7mTFLmu4rjzcYMzKlqQ/view)

1. Start with the kit's README, practice CSV and label guide. Follow the validation, training and evaluation steps, then open the app. The intent commands below illustrate the process; use the matching track and practice file for your chosen task. Follow tab 04 for installation instructions.  
2. Read README.md and NEXT\_STEPS.md, and inspect the matching practice CSV. Use the practice records to learn the workflow. They count as ZERO student contributions.  
3. Run validation, train on the training split, choose settings using development data, then freeze the model and evaluate the test split.

python validate.py \--track intent \--data data/practice\_intent.csv \--practice

python train.py \--track intent \--data data/practice\_intent.csv \--practice

python evaluate.py \--track intent \--data data/practice\_intent.csv \--practice

python \-m streamlit run app.py

4. Inspect per-label F1, the majority baseline, test predictions and errors. No minimum model score is guaranteed. For sentiment, use its track and CSV; semantic parsing also reports slot and full-frame results.  
5. Enter a new example into the app, then an unfamiliar or ambiguous example. Show what the model predicts and discuss where it fails. Select only a track that you have trained.

**Your final demo must use your trained model on new input. Do not hard-code the displayed example or present a generic chatbot/API wrapper as your evaluated solution. A mobile interface is an alternative to Streamlit.**

For your own work, use contribution.csv and remove \--practice. Keep related examples together in one split. Follow tab 04 and the kit's README for installation and exact commands.

* # **5\. Meet your data and review targets**

* A: at least 250 accepted records, 25 per intent. Per intent: at least 15 training \+ 5 development \+ 5 test examples.  
* B: at least 300 accepted records, 100 per sentiment label. Per label: at least 60 training \+ 20 development \+ 20 test examples.  
* C: at least 250 accepted records with the same 15/5/5 minimum per action; at least 100 records must contain slots. Include slot-free examples and report an explicit test subset with values unseen during training.

**Confirm a competent language reviewer before scaling up. Every test example needs independent competent review. Keep review decisions, disagreement resolutions, source records and split-group IDs traceable. A validator checks structure; it cannot establish naturalness or consent.**

Begin with 30 reviewed sample records covering your labels. Use them to settle label boundaries and source/reviewer arrangements before producing the full dataset. Raise language-support or access problems early; do not silently lower requirements.

Report accuracy, macro-F1, per-label results, a confusion matrix and the majority baseline for A/B. For C, also report exact type-and-span slot F1, full-frame exact match, JSON validity and unseen-value results. Use tab 06 for the complete metric definitions. Keep test data out of training and tuning.

1. # **6\. Submit evidence and understand judging**

2. Data: accepted contribution CSV/JSON fields, reproducible splits and traceable source/review records.  
3. Documentation: annotation guide, source log, dataset card, quality report and each member's contribution/AI-use statement. Adapt the completed examples to your real work; never copy their fictional permissions or results.  
4. Code and evaluation: runnable training/evaluation code, dependencies, actual metric files, baseline comparison and analysis of up to five real errors. Report all if there are fewer.  
5. Demonstration: working Streamlit or mobile UI, clear run instructions and a 2–3 minute backup recording.  
6. Submission package: your team GitHub URL, frozen full commit SHA and ZIP of the same state, with a manifest showing where each deliverable is located. Follow the final NLP Hub repository process when announced.

**Marking, out of 100: data quality 30 \| provenance/ethics/rights 20 \| coverage/balance 15 \| baseline/evaluation 15 \| reproducibility/documentation 10 \| demo/explanation/teamwork 10\.**

Judges assess quality and evidence within your track. Raw model scores across tasks or languages are not directly ranked. Choosing a harder track does not earn an automatic bonus. Go above and beyond with useful, tested improvements; explain their value within the same rubric. Complete the required deliverables first.

1. # **7\. Begin with your team and follow the dates**

2. Find your members and contacts in tab 03\. Keep team coordination in a smaller team group; use the main WhatsApp group for general questions, announcements and housekeeping.  
3. Confirm your language, one task, source route and reviewer. Agree language-review, data/documentation and code/demo duties, and keep evidence of every member's work.  
4. Create your own GitHub repository, run the practice example, prepare the 30-example reviewed sample and complete DATA\_PLAN.md. Keep private data and permission evidence out of public GitHub.

**Midpoint progress follow-up and Q\&A: Friday, 6 November, 6:00–7:00 p.m. EAT. Show your sample, source log, review decisions, selected task and running baseline.**

**Final submission: Wednesday, 11 November 2026, 11:59 p.m. EAT.**

Judging: 12–13 November. Finalists announced by 5:00 p.m. EAT on 13 November. Prepare on 14–16 November. Presentations and awards: Tuesday, 17 November; the date is fixed and the exact event time will be announced.

Before beginning, confirm your team's language and task, who will review your data, what you must submit and when it is due. If anything is unclear, ask for help and include your team number and a brief description of the issue.

**Your goal: contribute reviewed language data, show what a trained model can do with new text, report evidence honestly, and submit a reproducible team package on time.**

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmUAAAG+CAIAAABd/OQBAACAAElEQVR4XuydBXjcxtaGdXu5fzGFuNxbbtowFMLMxjAzx2FmxiYNNcxMDqPtgGMndowxMzOtcc3e/4yOVla0dhyQk/Xu+Z7v8TOaGY1G0mhezWgtcRoSiUQikUiViZNHkEgkEolE0hHxkkQikUikykW8JJFIJBKpchEvSSQSiUSqXMRLEolEIpEqF/GSRCKRSKTKRbwkkUgkEqlyES9JJBKJRKpcxEsSiUQikSoX8ZJEIpFIpMpFvCSRSCQSqXIRL0kkEolEqlzESxKJRCKRKhfxkkQikUikykW8JJFIJBKpchEvSSQSiUSqXMRLEolEIpEqF/GSRCKRSKTKRbwkkUgkEqlyVQkv7zo+0LU8U7WSSRMrcF5+vjyh6rVg+Z+w6Q8aW8oTytPnLftDZq62qTyBpKN3G5izY/VJV3mCRtOhxxhI+tVslDxBab3T0AI21LrXBHmC0YjjfocjMHjqcnkCiaR/qhJeIl2krtnESp6pWskgeVmjoQW4uLhEnvAUUqvVuLo8ofqIePn0KikpfZHWgsrOydVtM8RLUjVSFfKS+6lbRGS0aHkm0tOp6niJp+n5ekC1Og9XlydUHz2Bly9N1YiXL9JaUNk56ureZkhGrqrk5bedZfGFRcXiBfNWfdZbBYeGQzg2PumNemaY9N+6ZkdtromrcD90hcg7jg85rg1mWL75gDq/AAqH8PuNLAJDIsTMUnFvt4UM7zQwd3D2+LCRpXiVRsXEY0fJavhOmzRVJsa/xUfCLbBYAubJyy+QhIXxJewIVgD8n7qmtneE2ebjZy6zYj/tgIvcd11gsfOI+RAuLRV6HAhg6j+a9q/Jx7BVuLYYiWpoNUkb33zhikp4yXGthMxN+sh42W3wtA8bs33XltYM+iyI9w4IEyOFpK8ZNuBm/x3twcH8xSVCbaUKDAmXr16rOyZt2nuibKf+0zo+MeXxVQW5PgrkfmRnFg3n0cXdR56JF1erG2R4r+VAXHyvkWXNxsKpXLdlHySJ45Wi4mLuq05YIOz1px1GYjyIe5edCO63vs5u3izAHx8ZL7nv2An9ucNgjc748m91WOP83XQE9xPDG1uLa4lJKPEUmA+bxf2vI8tQs700g6giaDkm7TDz9gOndXnJ/V1IZW49uCz+/1j7577v8nWH4Zg6fcmfEF+r6yhc/LptWWbWPrlmYjlwWsvK+ZAdCjhoB09e+oC/LuAIq/OEhp2Vk8vVYBeOsOKnHbKyc85evF5WJd6Ww2ZA5tdbD2F5Pu564859CLxWhx1VjqsFZ7OshJpCw05VZcoK4b7pwueXjy8/7zBCbLRwNMT4E5fsca3YuMR/1zU14ZtNQHCYmIFEqmpVIS+hL5i1YDV62twVGgkvTX7pAb1ezcaWwMvQ8GjsYbmfu3P/E/q7vuMXYVHIy//UN/9bHdN3GgjX4T/qmUHH8Y+6rBeD/l26aVHIS9hETb73xE7W0zdQuA5/6AolmPBJBUXFkDRk4iIW/5nA+D1Hz7HFnwTw4FrIy5LS0n/zdH+9vjn3aXtMOmFzVcwJ8dK1uI9Z15mYnMqX3xGTuK+FPeU+avcB3zvU7jQck9Zs3iskfdcF+rIafKdWES/rdxF6T+7LjlCrj37pwcJaXg4YN59V8ouO3OcdMNu/6ppB/KOA0H/yRw/8n3pmEOZqsopx35nBWYPMUBrWivu+nOEXdFL/rSdgFdZlq/+PHbdaHYYKlfmiI5wvE34ePi4xVb6+RuPiFQBHnp3xj9q9zt85gQsLC+X5NJrGPditA/bFGu0hdXTxgDDXkN9Z/vCCXuO3yOr/iXBSuO+7YRLy8qvmfWryR5Krzegu5SX3U3eWodUAzF8uL6HCcKzEE7d+2wGh8C9ZTE12cju8Ud9caMwV8BI3xOrwUbv3+DNrIuEl9wFjLbRVABWWM335NiGJ56UJf77EOtTvMuLdhha44yaScZt4duBQCPURDwXPS6EOH2tT3xewhBzi6phyNdv9my8EeHnmwrV/aW9n/823FtPBUzVaXn72e28s7TX+qMLReLOBOdw0cN8IN5TcT6zJpaZnirX6Fza5j9ghkvGS+0q71sft8WbiH3yL1Wh5aYKHWtue36rg8ieRqkJVyEupuR/Z5SrykvusbMKwBn9VzFop9AtjZq7EPLiIvOQ+FXptTFq8Ya90MSQ8ChelQl6C0zOyxEi8b3X18hPy/F9rvnBhOGjC94lCEj+syS8sEpNMtLzk/tESwm36TsakvccuPFZhftj0yD8EB5RWo+ZhmRzXCBYPHD0L4ai4ROkqoDd4ZkTEJJRqt+XmHSAU+DXr4MrlZVp6BmYWx6z/4ilY7nxsmvYGX4zBxSfMsGGG8MgYeUJ587GxieyGAKzmR+SgN/mdggMi5qlIvUfPZTm/lk9IaNh9Rpq4oQ1b2YASCMF9xHLW5M/mFXsnDTu8TVgJn3TCtcKjYqXVQ16CU9IzhHJFXjbqiUlT5q8Tk8rlJdAdFwdPXMgWv2LDo4eePtINabTtuVxe7jtyRpYZF5GXt+65mPB7J6bi3R6GkZdiM+C+5K+Ln4QqQd1g8fYDTwjfe+hlwkMXkzTaKv257wzLqeUlJmVm5+AitiDEp7iiqHLnY5GX4OzcPEneMpVo51Rw/JqdkyvdNErGS8wQGBopXeS+Z1AUeZlfwO6rYhNTdEsjkapUVcjLJ8zH5qrLLjCMiYpNwMWHnn7SywB5aXPVXpoZxmrSxaAQNqkrkzi+lEYKFeO+47hvwe/x/Yi4Lewszly8npAkvxRxEXn5LnaI/2qNhXDcr9LMP5qNh/CURRvdfYKAlJHRrOOG+Nd4kmF3Y3vLQVsTLOFbXDx26nxOrvCMp5Af9YKmzl9jUgEvnVxZzyhuGvTfX3qxYrW8hM1B9YD9EMNpB5RiZlyU9oBstpD7ifuJz19bGLWE8HPmMunych8/IpfGYFcojZGq26iFMDrHDb2PE4PljWVBOJEAAe6DDnDj9U6THu/xUMHCsfeEOkN4xYZd4lqYmpnNJtiF+dj/tBFTNVpeor/uOlaaVC4v63YcgotLNjJscx8yIu49cla2jziuKpeXdbqNlmXGtoS8HDNrFabKWoWjC6OgMB9bSxgm/txlBJ+zMS7CrQYsHr9gx8K/DmRJnwszGSymBhtw/x8/7YG8/KCR0Jzy8gtxKyU8MLkP2GwwDHxZG+B+Fq/KJ/CS41qIMSBVRhbHNYCbJHZmtQNfGKRqnoKXTm4+Jvwsq5j6t9rsPgB7EmE+9oeyRqJbGolUpXo1vBRhoNFmjoyJx0Vnd3bNiJcB8vKWg7M0c1JKmnTxCbyUztaWzQbrGDP8u/kgCHMm7bnPWOfLfSKMOzWP87JGw7IngrqFJPKsZQ+Bfu2FXQkwOzo+SZrn4lU73dXBm7YfLOOldmg7fuZykwp4CQNlabEgYYpSy8u/4xRlA3MYfsm4rimPlzj+/kcdUxgNc1xDzPCUvDxw4rFxtuaJvHzvV8Z1VlXud9gQ9zM/DVgBL79rwwBwyf4+9KRNLcZMX77VhO/f2Sra3hPnAxatEWYpNGWnjA12xeeXYqpGy8vPfhdqcvPOfTGpXF7+1n0ELq7YeoiVxvPywhVbXF1cF4jOUsvjZRMLdi8lzYxtCXk5aNISTJXZ7i57Oi4+v8QV63Vn6OW4+rgo8PIiu638Zxs2Rc99KQy1WWoNRsG3G/LzHNrnl5gEdxu4FeQlaPLiTThaRU9dslnzZF5+/NhZw2wfAnHhtPJzKiZPzUsXT38Txsuypv5PvgFzX7N9EZ9fiqm6pZFIVapXz0v8+QP3H+F3AdzH7BGOeBkoyEsQjmOcH/9piaePMPOp0U7xoYMjYsV4jBHmY/krvPNA9ghHVEJS2VM6sQRnt0ewyNUTysRRkYZNjWZhjLgKSJzGfJ1/VsQ16I2LOJlWLi+BqVjO/hOXMAYXkZdJyYzc72s36vTQU7ZRXNy096QsRrZYPi/zBF7iAA6FMacu3JQuch+XddyihKTG/XCR+/FJvPSS/DrJzTtIw6+OkwEr/9iBeWqZMhS920DY2dGz2KDcRGxFFfOS+6TrFXsnzPzQQ2gYT89LjfYmY/zsVRAOCo3Eosrl5d37bpiKzwjytKxCXt53e2Ty+HwsKClVhYGn5yW0Uiz2kX8wLEbGJuBiUmo6y1kZL0W16TWBbeI7YYuYzS+o7Pc1FfFSnAqO006ZIi/VeULFouOSxPzlzseu3rRHurh4/U4N8ZKkB3r1vIyMTYQLjOWvbcp9KzxcmbGM3dVqlObl4BmrcZWGnYb0GzXr65b9XoOxlKQb/WdDlmqi021hJPIyOVUl/EqivmWfETOadh8OHb30v8pwks2ETTuz/LOXbsRF6Y8q8aeJbzYw7zV0isUA6381Kps63nnwlJCfn0f9L/8UsFxegroMmCxk/r7rm/XNse9GXqoys4V9+aVnnxHTZZPPoLe1E5KwO6v/+Euj3c3vWvXvMWQKPn00qYCXGi0ncPVBUxktuKaDhcp80wV/hAI7lav97aVUf9NO9sIB5Gqbvcf/orIiXmq0FTPRVv4/2rnl+CShJYBwVAS3RPjElxX4mjAB+2ReQnjt9qOstk2sfAJCNM/Iy9r8DDy6JvuBN8/+8ngJwp9Vs1/0fN1FPIBlv/fhf8jD1THt1m+Cab8JXF3zt7V3AE/PS9A/+TqwDOKh4FoLOZ/IS3b0fjazGjSp55DJQiMXN/GO8IMjiLe5dkdTMS9ZZF2Lbn0n4O2piZaXrBB+GgAL+a3rUBYj+70P11wo4esuQqvQTiEQL0mvXFXCS9bRg98WLlFRhUVFHNcUDAFpfFaOmqvZjv2KFa6Hd9s6OruLSRxXB/LfvMV+08EvstXF55e4GBAUKuYXxXFf8qm/yOI37jyClxkaBnPDpq8UU2FMiZUfMWutZCVhQ+LP7gNDI8XOzoT/lRD3cxnPOK4Z5sfFQvYQkS3e53/ViYKiuI+E3/gJHQTXSkz9a+9xwBt06HW7j546bzW/+m9iqkyDJy3+sJEl7Mi8Vdu4dzvxmRti0tApy8TyVZnCLzvEFTOycn7rMRF6KFhl0YqNENO6p9D1A+duOwmDoYp4mZCcVt9sLO5at1ELMdLuzn3kFpuRq21VoJ1VlsntkT/eJIHrdh4+bcFadgQq5iXH/cBvqJ6w+GYXfrHs3ySE+Lfb420BcGXt5n1l8Xwr4rjHGMbPUUNkXVxctWkv7ou7t/93LfqycONe2pyN2GID4dDNW7+Hz/kVLoLuObtzXIuabYbEJ6UK87FfVbwvtSxYg/mhKww32dNlrunHrQeVpWp/Vorm3tb+oJr7lN/oz8Ji/d78onD9clwtWDx49gYuglr0ssbJTGgYn7ZlZNLmxEMhXBfAS9zrEv4fh/BH42Vbr9lB/CkZ6PO2QzHzyUsMzNzHZtIDiOK+F1ANrVdsciIvoT10GjQDC4G7AZafqWn3kfPEElZu3IN3yXAqe4yeK8YfsrkhPQIati4rR1wkkapaVcJLEsl4NGPVDl9+VKphT9+9kRDbD5x6PBeJRKr2Il6SSC+khRvYz2UfG5ZxzeSZSCRS9RfxkkR6IWVm5y5cuYn7vDP3drsv2wx+6FX28zESiWRIIl6SSCQSiVS5iJckEolEIlUu4iWJRCKRSJWLeEkikUgkUuUiXpJIJBKJVLmIlyQSiUQiVa4q4eVJmysnbC7ffeAmTyhPs1dtKymp8JNSyiorO6fdgCni97xE/bH7WEJSakZWzvBZq2VJMtk7PMgrEF70evzsZd23bj6r6pgKL11TSsFhkQ78Fy2qhY6dvQyt5czFG4nJZW+2MwBNWrJJHvUs4n5/7NV9JBJJH1QlvLzPv2fc0yfQxdNXnvZK9U3nYfIoXlsPnE5MTs3MzrFexF4L9wSt3bY/O1cNgZa9x8vTnksdB06RR/EKjyp72/szKSQ8ysmVHf9XqKY9x8mjKlCHQcJr6y/evNOit/Aa1arQAGvhjX1P0Mcdhsijnlez17D38T636pqOlEfpKDTi1Z9oEsmoVCW8vKd9UeqC1VswYDpiVsu+1o4PvSBcWzuicnB29/EPnrP6LxxfHrW50qLPxHmrt0K4WDvi/KKTQLjvugzHAGrvsXMt+0wcNZO9+jUwNALC7QdOCQ5jH46+88D9vpt3s94TYLwIbGvee0KvcfMhfv/Rs2bDZ9TnX6L9lbbYdjyuZLx0cBbGZ7W6Ca/YFsV4qc6bsWxTAf/ZRdDSP3Y0thxjvUD42nBSSlrTXuP7a3vnbzsP23PkTOt+k8Kj4jAGpVbndR4yrcfYuZ0GCby0HDXn1x7jouMSIczVs2rWazxWdc7Kzb9YjbWSvEgT9U2nocOmL+Oask98WI6e06qvtR3/VnqRlzFxiV2HTh80eQnmX/Hnbiin67AZkjI03v7BbftP7jZsBr4a9+Cpi1D5RWuFvv6vg6eHTF0KJeNiYEg4HEwgXCj/BWnbuw9CI2Ob8ZDbtOtII4sxQ6cuhXBASDge50MnzsHiMZurkDSfP626EnkJ2rz35B1HFwg88g+GQzFy5gqMN2k3aNnGXXC4iotLYC/gRBcVC+/r7z1+frNeE3L4O5iA0MjElDRoQoMmL8bURev+gk0Pn87e5d192HSo0v86DnX18rvl5NZ73PzU9Myte4626T+pv/UifEsqVvsLnppX7e7BaZ22ZAMWhUpTZcIWId7tkTBFcf+hZ98JC9oOED4eDmrZd+KI6cvnrRM+nCJq9srNUNVrtxwh/JO2XUVGx928y74jZjZi1m89xm0/cALjkZffam/v4KRo+E/F9Rgzt8PAKf7B7I2+zXuNb913IjaSzOxci1GzoTkVVfz1bxKJ9IKqEl7uPHTaycVtwCSh2xLHDcfOs/dBH7W5qsrIhECrvhPh7+INu4CXh05eEOc2B09aBH//3HUY/m7YcSgoLDotI/PIGeGTVRr2auzdyWns40SiYhOSAkIixs9j0Lrn4nn41EWMX/oH+xIQqCOPpTra2/bm2ipZjZ6j0eFlqz5CKgJeKuBlp4GTYXO4eN+1LIODi2d+QeHuI2dwERAOf7sMFnjQ0GJMQaGAWBD0/hjooO1qc9V5AH7oi3FROr4Mi4oNDInYuOuoGAOCamCgofloDGzYdUyj5WV6RtbhM5cxHmvy5052PGVq+fiQTvxuzIpNu+Fvx8FCJdvwZwoUHZ8Ix9lqDIP3rXsuB08Kx1nDhjsxQWGRv1mxDy+L48sNOw/j95xBs5aXM0Up5SVo0JRlCYnJ7t7+uPgLfzTa9ReALd5b/NaT8aNtPyEekA9/g8KikKM4AQC3XAdPXsAMGsn40s07YNPuI2J8fFJqYGhkCx5I4vjy+IWb8UkpGB4xQ8A2qrCoCE7TMu2HqaGpY2DLHnZ2xCqJ5xH1ew/he9RwKxAeFePwwC2Mv+dozZ8aDf9tSCjWyzcQF5GX4tnpNnQ6BvLyC+D4I57F8WV+QcGMFcKN6e/8kSGRSFWhKuGl40M2Plv8h9CnwK39IOsFzJNYnwVY/LHriJS0jLVb97NsPC9hfDZk8iLMNnwaG6bA7TP0ZdAJTlm4bvt+4b4bJY7eUJt2HcaJ3/lrt2t4Xro9Yh2uX1CY1ajZwqatF2iempdnr9gnJKXc4sc6MgEv1fkF7bWQ23nwtFj+nmPnHF08e42Zg4sDJrItttSid+XWg9FxwtfqQVMWrccAzscCLDfsPlpUVPRFR+FTEiIvAaj4mfsJC4RVUNjFayR9dK5aXVhYhLy0d3DpPXauUJMJbHh98MwVuGkQa46CAZP5iJlt+0+CsE9g6OBJC3EV64VsWzC+xGy4Fys373P3YR36wCnLNDwvI/mKadgdxkT8yBp28SIv4VQOmSSc1rFz2De/ZJLysqCwaN7a7cfPXx8wcT6u0p+vOVIT9CsPYzHwc3fhbM7jJz+D+NkFqf46dKZF74krt+zXPM5L8fku3Encvs8+hoM7KPJy1Ixl4qGA4SNGgnYftVm0fgdAa/dh4cg4aB/SL9/I7jBaa28sZq4s+3I1yJRdAljgQvycDu7U3JXsu3UpaaqtB07BuVOr8/CusVxewo6s3MI+utJp2Ey4sxF5mZau6jFaaOd4r0kikapCVcJLcT526FQ2GSh26KK6DJk2banwpBB5eeDE+Zj4sq/IgppYjZ29/E8INLYYI+vlV2/em6j9BKZGAj+cORR5CZow97Hf74i8bKW9r283gKFC9/nlLz3GiaNMqcTnl+15zjnxdwaioCddqv2CMaqrdnzZgI0vyz5u1Ukbj+PL3ceEkVAb7bHC8YeGDWGFTUzgGSZK5GUD7fhy3U42bEJeAgjX8H2rTBAvj+IHZJt3sXWlX70GtdfCDMeXIgWRClJeduZ3p7S0tAN/PH/X5lz318HImHgMlyspL3uMnhMTnxiXkHT47FVJlgp52a5sfMk2qstL1NQl7JwO1IKE8dJZaJ8WI2dhAEeuX2nnP4/YXPP2Zx+mlqn3OOGzUz3HCgEZLysaX7bQedrdY8wcuEnC8NFz1zAA1JTyUlwLb6rEQSrQHXgZFhGN8x/Q6sz52z4SiVSlqhJe3rkvdCIjZ60K5L+e2G/iQuhBZmpn5PILCn/RfiN3zmrh97FX7BzaDZwCPZEL/5n7sIiot9sMhMAlW4e2g4SJQVGHT19q0WfixPnsK5U56rxfe4ybvWLzdL78Ow/cxd8ZFRQWth0wuU3/Sdv3HYdFfNoHys8vgJ56855jbQewnmjD7uP4+9gRs9Zghq17j12zvweB2tpBDAq6ReSlhu8TMzKzN+85+nvP8aYjhJ43Iyu7VT9r2JEDx200/BDh0KmLrftNkmFDrc7vPGR6n/HzRdpBfXqMmcvV74mL/a0XYacJo+tfrcbtPWYzbEbZdzpBX3Ys+3EKHLSWfa3xB8nBYZH3+PFTSroK4qHYgyfPw+LQactgW+JzVtT81dvg0E3SkvjijdtQTu/x8/2DwjRsOHVuxIwVLbXPL9Mzsn6xGjt/9Vaz0YwWtncfhEcLO3XqwvWmPcffc3b/H18rVWY2HHZ8fnnVnj0I7DlunocPexF5Pe1HmFF1LcZCzG89xq3avEeMDI2MadZrQpeh04/bMHC+1Zo1A1ANvj2A3ms7CAN9Jy7kn18y8ASERmIkCk7EoMlL4F7qCD8vnZyqgmbwWYchD738bmvb58Ubd+DcXbVz+JIf1ucXFHQcNPWT9oM1/BwJ7KzFqDkPtPcrqK7DZsAh3XnwJC7ecRImIRasEQaU0CzHzF41bbkwQSpq9Za9jSzGTF70h3jbhE8lUe0GsJZfVFSEvOSasYYK9YG7xrXbDmBOdR5rM3NXbWncyxq/IDt4ylJsJHkFhf0nLYL7xa372Jy8iHMSiaSgqoSXBiDZ72KeW7IHhNVLOw6dkUeRSCSSsYp4WY7qmI68fpv9avHF9RE/WKmm2rT3scfGJBKJZMwiXpJIJBKJVLmIlyQSiUQiVS7iJYlEIpFIlYt4SSKRSCRS5SJekkgkEolUuYiXJBKJRCJVLuIliUQikUiVi3hJIpFIJFLlIl6SSCQSiVS5iJckEolEIlUu4iWJRCKRSJWLeEkikUgkUuUiXpJIJBKJVLmIlyQSiUQiVS7iJYlEIpFIlYt4SSKRSCRS5SJekkgkEolUuYiXJBKJRCJVLuKlsShLXWDnGWVPJpOVM1xTcGXJLzaSgYp4aRTKzMm394xOUOVnqEtUucVkMvnFDVcTXFNwZcH1Jb/kSIYo4qXhq1Sjgbtg3audTCYrYri+SuWXHckARbw0fDn5xQXHZehe5GQyWRHD9QVXmfzCIxmciJeGr1te0WnZhboXOZlMVsRwfcFVJr/wSAYn4qXhiz1foceWZHKVGa4vuMrkFx7J4ES8NHwRL8nkKjXx0khEvDR8ES/J5Co18dJIRLw0fBEvyeQqNfHSSES8NHwRL8nkKjXx0khEvDR8VcRLrv/evw3YS28wIJNf0MRLIxHx0vBVES+/GX4AHBqfpZtEJpOf3sRLIxHx0vClV7y889Cf4xrybvJjt3Fp2UW6eSpydoHmw8aWF2+56iZVqf9Z14yr1VU6EM8p1NRsbMVx9XQzg3MhtYlVfGq2bpLM3IdtTJpYZeWX6iYpa9gKV8dMN14PnZWvgdq6+Zf/RqropIwhM9YeuXBbN+kVmnhpJCJeGr70ipf33AOhN2xoac21GAJQ4b7qJHIIAsAh6aIsDI5MSE9UqaX5oXstN79upBgD3M2VbEjMBkVBgdJIrM+TeYkrQoGZeQL2RF5CjLRAFQ8DaYwuL2UVlu4IrAg1180pXQXDsN3cx7cr8lK3tuJauAnZFsUkMVK6ihiGAnMKHjukUFWsrSyndBMyZ+WVQt2kvGT5Hz9ZUQkqSF234zjGZGjP5ku453iCiZdGIuKl4UsPeRkYkQhh00FTaja2xI6P+6or69M/bgd/63UbxWJ+6PpeQwsV3xl90Mhi9fbj0vHlIRtblv/T9hDzXbshEOPkFQIxKnWJV3AMv4kEyA8BRzd/aQW47zpzX3XkPmzLVv/JFGI8AyIh/HnLAULkt10gMiWrEMJv1Dfjvu8Cm3gCL/8ONP2hC/dZe7bu151VWl7+2HG4UGCNtiq+Z3+3gTnsL/dRO0j1CophldHhpasfq8yBs7YQ7jt5JVe7O6xo7+zDyvmy47sNLOAOA/NDTM0OoyHQafh8CKuLGZwg8NnvvbgvOnDcr2KZGI+85Lg2sC/cu61ZTK2uSHRWFCyasIMPOwvZIB5isLaf/NYTAnAw7Z08IMMV+weQ4RfT0RCGQHi86v2GFtw7rWs0tOD3hVVjxvJtrPyP2sFJhMC63afZputYscgvOrC/Daxk1OR+ZKtzH7TlanU30fKS1eqT9nhsOw6cDrV6u745hKE9/LuOKVQJymc7yzebX8zGSAt8mSZeGomIl4YvPeQlxzXhuAYQsLnuqNJOwXUbMQ/C9cwnYEd87NJdCEAX6RUUCwEcryAvYSDyej2zH7qx/rFQw9bNzGOpEIhNzlqx+UDdzsM7jZj/KCj6g0aWshEeZMNBDPetKWIAednYbCyk1mjWH8LQlZuNnPdOA3McDDE0VszL3CKhwHmrtuO6yMvhczZCamxqDkR6h8afuuYEAagt20pDc65WN1V5vMxQF/+rjikAGMJ/r2Pab+pqKBAyc2+0zeBJDPmHTl2pqpiX3E/d+XIeO+MsnudlWW03HIRI3/AE5CX3M1tr7c6TeKgd3AIgkJzFXqP4Wp3uT+BlBj+chQLzSzUfNrJ8+CgYwnBnYDl6AaQmZuSb8LyEbGwrDXvBXizdchTCYXHpYvWE4/lFBwi7B0SbaHmJVQX/vXb31+ubQyFRCemsQO34UtydzQcvmPCtRbrXL83ESyMR8dLwpYe8rN19LPcWG3s5ewWr+F6PdaZfduTeas391A27bOgQgY63XHzrdxoK4wmV5Pml0L1+24Xlf4sNlTYfvKjiqfBT1zHcG218Q2K4/3UcOfsPGKzIKvC/VgPe40dCaCgKeXno9FVIbddvignPPI5rzn3Cum/wv+s9aT621+h5b9Y3EwsUeSk+v4TI3cevTJ2/ju2jtsIwGssGZuvwEnz47A2ITMsugr+p2YWw11DhpZsPi6U17DwUA8jLjo/zsm0PBn6Z2aZ5Xg6fuvz/6pXV9vIdd4GXddhQ+9pdVxP+4A+YvvYDYCQ/WOQ+7/wEXvqHJ8KhFgu8YOuENb9sx7Jl83dCwEu8mwGWsyPwORtiTli0WaxeYFQKxHzUbrjq8eeX3Ndd4Y4HS36noQXcJ0XGM16u3X4cV5wwd937krOZLZmvfpkmXhqJiJeGLz3kJc7H9h+/EMLqIk1mHht8DJuxBp9gBUUlY+YNO47V5PvBbfvPqCS8ZDyrbWo6fC7khyEFjFSysGd/pzXmh8X3G7FudP6GA9KtQ2aIXL/jBAS4bzqZPMbLa5ChvZaXc1fvgG2l5xTnYEdfAS+TMwsg9bM2Q6EmLS0ZQkReftNpJGzl6l13iExIVwMAIJCoyoOdhR25/eARq3B5vGR792M3qD+O+Vi2H7txNdtCtnSefMu3HlUhArlf2I5819lEwsuOvcdLS0OzzDwv+bV+ZWvxs6MyXl7X8jIuNRsCp6448Htqibx0eOgLkYvW74HD+4+6piY8L7nX20AqFBgUlWTC8xJ2kPu+C/cTG50fPmdnIhlf1us2mh8OlkYlZUmPJxQOXHytdncoZ/eJqyY8L/EuKj4tF44tbELgJT++nLNiG6yCdXvgGQRrWQ6biTXX3feXYOKlkYh4afjSW15iT93Mgk2rcr/1h77vX3XN3qxvDsbMmAG4lcPPqYq8hHBobBqEYeT3tzqm7zSwgL4VIpf8uZ91/Z+1ZwV+ySii+zOQN/kHYFzt7k3MxphUzEvo1qE+7zeyhJwMXRXwkrHta8ZdyGY1bimui7y0Gr8UIlkS1xrX4n7oyh7IYYFccxZTHi/BG/adg/hxM9m8Kzg5M5/tbF0z9iS1RlusCfIeSmvTb5rJU/NSu5bp8m3HTCrmJcv5LTuAr9cz+0fDHshLGCy+VpthEkBeu8MQE56X2/afhgCchR87DIP9Al5CpE9YPH/0LOp0HQWp6/aw251m/WYAFKHA/9Yzg+E13uKIbtSLHXnYnbd/7WPC8xInGNgz1NrduZ+6IS9V6pLX6vB1qNWNHfzP+KehtbtPW7lLrPnLN/HSSES8NHzpFS/xByYieyCMLMSwq294REKGtCeVZsBF8RkVy+8X4REQJebHwjF/Dj/+EFcUDV2q86NQVS77oSZmyJT8zla6FpTm4h2G4xjdospWzyuFagAjsyW/fc3h9zElq/ChT7i4CsREJ2c98ArJYD8ZfawQmfNLGcPyeASKBcLB8QmNF2Ngu25+ETD8whqK2cplhrgh2LR7QBQe5BztwZTui7QoVlq+5p91TDl+5Kfi51edvUNxXTEnjJ4DIpNwFYa03OKY5GzMAEN/2JHgaGHCAGLc/CMDo5JxplfmuLTcqMRMzIYtFjYKh0t2CqRnGXYHM2CVdMt8OSZeGomIl4YvveIluVJz77FB5+7jV3STXqZhSIczsVxtcym5n8aHzt2CoWRN/gfGZ6456GYwMBMvjUTES8MX8bJ6GX/wqRv/kp2p/W9I3aSnMa6Lw02DN/HSSES8NHwRL8nkKjXx0khEvDR8ES/J5Co18dJIRLw0fBEvyeQqNfHSSES8NHwRL8nkKjXx0khEvDR86RsvM/NK1cX4Em150st3uf998QRn5ZVaz1+rG/98hvNSbmkrNu3TjRQ9Y/nm5/4ZDjo+Lafc/+j4Y9fx5Ix83XipM9Ql527cg0C5NZf5WQ9vNTXx0khEvDR86RUv07ILuwye+tAn9Nx1hxv33HUzvGRPXbpJN/IJBlA1Le+Fc89nuHVo1rOc0kbPEt5UUK47D5vxghyKTckut4Spy7cmZeTpxksNvDx49joETly4qZsqc79Ji3UjDc/ESyMR8dLwpVe8vHnPzdEjUBqz8I89rftO7DtxYQb/5u5TV+9CpF94/NEL9hDYvPdkh4GTx85d5xMS267/JMiZmlUA8cNnrGjVZ8KEBeshHBCR2KafNSw6PV6yiu/c63Ufbj5yVpu+EyMTVBBjMXJ2q74T2/a3hm1BUd2HTmvZZ8Le09cu3HTCtyics72fmVfywCto/+lrsLmcQk3HQVOgcKtRs1USXjYyHzVu3lrYbkwyO4CJKjXUs1Wfien8dm84esAqUGEIewVFY/W8guTfdBR52Xf8fNhW236sViqel30nLIBVEtNzMVuHAZMhw5aDZ1VaXgZGJsJeQB7PwLJinTwCYKOwOY+ASFicvfovV98wWHHFFuG9gF2GTIXF2y6+Ul7CTnUePBXqP2v1duDloTPXMPXIedu41BxbJ08XnzCoW8+x8/g3LQi8rNNtGK7bfeh0qMaW/eyldx0HsmNlPmIGJNU3HWE6bHrzXuMy2XvsVLDd9gMmZ0rGtZC/29DpEG9z3UFdzF6ecNHeGTZ0yc5p3rqdEN/fehG2ikv2zir+ONjcZO8PgoPffgDbzfB4dk6tF22EjXYaNEV8D8ZLNvHSSES8NHzpFS8z1MV/7jvdus+EkbNWQe/m4OZ36goDZHxaTo8x86BDxH9v9w9POHbpNgSmLGFf+QBP1QbAa/46nF+qyS3SRCdl2txw7D1+AaxYbl8JkW37TsRevlnPcSq+zwWAOboHAEtYsdrx5UW7+1jCBbsHwEvnR8HiJyQBmfe9gm67+CSmq0VeQreOxQK0VDy/oT7gJhajYBOt+owXgWQ5ek5mXvkffRR5Cam+oXFQqwbm7FtmY/iDAwHAGOQBEmDh521ZJZGXv1qNTc8p0i02OTMfymnZazysOH/dTnxT4KRF7OjdvOeOE7l+oXFSXjbrMRZbSPPeE4CXR2xuYOqxC/bxqTl2970On2NDyYj49HHz1mVoefm71RgIA6ikdYA9ve8Z5OIdiiXg+BLCc1Zvx11o2qPsq1ujZ6/Gg7xh1zHk5anLt1Q8gy/yr2uHcfC4uWsh/vItF77w0vO2LL7DAHYjAu44cDJE9hw79xW+3EdFvDQaES8NX3rFS9HQLwN4Ltx0DORfpQZdKowYRF7C+BJ5uXE3+xIFxP91+Jy47sApS+8+9AWAgR8FxUDqsYv2Q6Yuw9fSSg1dOeINAs15XrbtNzEwKgk67tFz1qjK4+V5fnwJvMT/tYfC120/nJpdqFKXxKVmi7xs0Ut4TSsMg+DvsOnLsT63nX2gnOx8zdptB1v1Hg9IgxJgoDZg0uLwuDRZ9URewr77hMZBrRqYjlBJ5mN7j5sHRcHgUijchRWOvIR1T165M2jKEsCYWOCyP/eeu+nEyjFjb3sHXubw3Jq3dmd6TvGJi3aYDe4zRF5Cga21zJuwcIOUl0fP2yEv3f3ZaBUigU8yXsK64tZhi3/uPQmBIg37fLRKy0uoDxxnrP8tZ28xv9XoOfjuXJtrd5GXt/jX0MOGgqNTVPzrCWHkzXh5+zFewu0IlgB3EnygZPPek/ydSjnt/CWYeGkkIl4avvSKl5EJKrFT+81qTEK6evKiDRB2dPPbc5J9UWvNtoPwd9exi1JegrsPmy6OY67cdra976Xi+3owds0q9kOYrSq+d8ZFzCDlJfztM3GRih8yIi9xlAl29gpESLQfOEXKy5jkLBEeT+Blu37WmA3/4jDOPyx+66FzGAObXrxxr+rx6om8NBvOJjBhrUba8SWuBXSHv33GL8AC8TwiL8W9nrKYHUB0yz4TodqA2G5Dp+ny0i8sXsWXcPS8rchLVv7ERZn8AL3jgEnAyxsOrngT03HgFOTlRH7e+9Z9Lxh8S3mpYqPnufi2PKhhJpviZp/M3H74XA7/RTZIVfH73p6fmlY9/gugVVsP4IZgCC7lJeSft2Y7BOycPE9cvgOBrftPqdgkRC7ysstgNvUK+WGUr+IPI/w9du4GvnT+5Zt4aSQiXhq+9IqX0LW5+0dAj+wdHC3G2N5zw6eA4KjEjJsOrrEp2V78YznAmJjtrou3naM7UhP+3rj78KE3e3c5rAsl3LrvifE4jkTD4tVbrIcFYyA+LQdWjE7KsufzQ7E37rp6+EdA2N7J475HoG9oLKwVFpuKGwI7uPpi5uSMfLHAsmJvs0drYDe/cCg5ScV+LxMYmQhh39A4Fb9HrHoPBMCXWz0Yv0L+8Lj0K/b3sSZwYwEVE+vw0CcUMjwKjoHw9TsPodpsrx3dsVjREA+HKDQ2FcqBdR1cfZAlsAtiOZABNofxol28Q1x9Q++4eCPwINsDryCvwMiUzHzgpW9YPCSFaweyHv7sJfLiEfAOjrl5zy2Ff65896HP7QePcvjhLyyGxKRcv+OSwd/W2Dl5wH6xkbpku7AuHJxj52/CbQTkCYoUZwhKID5O+w3RiHgVtArI4BMSC4ste493eRRs7+SJx8fdLwIOTlxajrTkl2nipZGIeGn40iteVrUZVh/66MbriVOzCgBCuvH6bOClNw9+xQ3j4ESVOiWzoF1/9jBYN0NFblneN8teoYmXRiLipeHLqHhJVtww1Ibhvm68Inb3C3Ny85MNdiu1w8Oyh6D6YOKlkYh4afgiXpLJVWripZGIeGn4ejIvQ4iXZPKLmXhpJCJeGr4q4iXXf8+nQ5703jUymfw0Jl4aiYiXhq+KeEkmkxUx8dJIRLw0fBEvyeQqNfHSSES8NHwRL8nkKjXx0khEvDR8ES/J5Co18dJIRLw0fBEvyeQqNfHSSES8NHzd8orGl5yRyeSqMFxfcJXJLzySwYl4afiKSsx0D0nWvcjJZLIihusrKilTfuGRDE7ES6OQvWd0hs5FTiaTX9xwZdFkrJGIeGkUyi8stveKTlSxz2voXvBkMvk5DFcTXFNwZcH1Jb/kSIYo4qURKTM33zcy9a53zB2yfvv6wzA6TXpuOEFwNcE1Jb/MSIYr4iWJpHcaumB7SUmpPJZEIr1SES9JJL0T8ZJE0kMRL0kkvRPxkkTSQxEvSSS9E/GSRNJDES9JJL0T8ZJE0kMRL0kkvRPxkkTSQxEvSSS9E/GSRNJDES9JJL0T8ZJE0kMRL0kkvRPxkkTSQxEvSSS9E/GSRNJDES9JJL0T8ZJE0kMRL0kkvRPwUh5FIpFetYiXJJIeafSSXVLLk0kk0qsT8ZJE0iMNXbBDhCWE5ckkEunViXhJIumRIuNTRF5GxafIk0kk0qsT8ZJE0i8NnrcNYDlo3jZ5AolEeqUiXpJI+qWCwiLgZa6aPkRMIumXiJckkt7JNyhcHkUikV61iJfGopA4lZ1nlL1n1O1H0WQy+cUNVxNcU3BlyS82koGKeGkUuusdk6DKU+UWk8lkZR2fngfXl/ySIxmiiJeGr+KSUnvPaN3rnEwmK2IYaBbT+5iMQMRLw9cd75jwxGzdi5xMJitiuL7u0BDTCES8NHzB4DJTXaJ7kZPJZEUM1xdcZfILj2RwIl4avoiXZHKVmnhpJCJeGr6Il2RylZp4aSQiXhq+iJdkcpWaeGkkIl4avoiXZHKVmnhpJCJeGr6Il2RylZp4aSQiXhq+KuLlF0P3fzP8QFpOkW4SmUx+ehMvjUTES8NXRbwEWIJD47N0k6qdM9QlGfw+ioEXMV+IPPL5/OKVeUG/8grIrMgJ0jcTL41ExEvDV/XlZUK6muOac9934Wq27TtphW4GdE6hxqSJ1Tuth0KYq232YWNLCMSl5Q6cuiozr5wdf7KhN4fSLEfN100CZ+VrBk5Z5eoTqpuka1tHDygqO1+jm/RybHPDCSrg7huqm/Rkw3GDo3fY5qZu0rPaJyQWirK5fg8XOa4O92NX3WzV2sRLIxHx0vBVTXmZmVdas7HlwTM3sws0uYWaYTPWYnxsclZ8ag54xfYTadmFqsd5GZeSDU7PKfIPT4DI+NRsyC8d0CSm50IMZPjr2FV7F1+ISUjLXbf7zL6ztghXKS8hycbWefb6fb6hcVAfXB14bO/oBoWk8ltPVKk3H7p4y9lXZDPk3HPqRnhcqq2jZ7m8hGLX7jpzwMYez0tSRp5YydjkTAhDAHbwyIXb8zceCo9Lw6TUrEJIgsJ3n7pxzvYBnyd77h8HsGKQB1JTMgtCY1L2nbHFSCkvYcQcm5I1a+2+yASVOHqOSsyYtmrXmetO8Wm50hpCybDihr8OiRVLzsxfvPnIwXP2adnCBD7Er9pxyvlRCF/tLDwXEBkWmzp73b74tBzMds/VF4raffgsFoW8hMyrd56OTSl77RSkLt1yLCIuHTcHGXBnz9u5LP/rhLRuemjipZGIeGn4qqa8TM8thn62z+g5MSk5InIQZg27DOe+6sgY2cAcKKI7voxKzHyrvhlEvlHPDAy4FYvduuc4xNf4rTdXo83a3Wd8QuJgkfuu8//VM+O+6wIdtJSXXF1L7tvO3Ocd+DxdIQlKg/C7Dcwh4B0UtWnfGZb0c3f2t1bXnAINlMB93Zktvt/my1YDTXR46RkQxVK/7fRmfTPuh26Qn90ZNLFq1H2UKpdtesXmg2zTsN3/dcTd5L7qDDGPAiMh/HaTHtwn7SGwYO1OrNi7v/SEVNgKhL9uM4h7rw1b5evOwG8pL7kfTLFW8Ld+5+EQs+SPPSzm3dbcD124Wt2kleS+YbvwfiML2E24Xzl+6Q7L+Vn79xtZ1mxshTDmvuX3ukabN5v0hIB/RCK/YhcWyddh4KSlEAPniBXV0OL1uqZQFPASboP+VceU+6kbxCdnFkCeOp2GYvns78edICYwgt3ufNS0D/dBW+73AdK66aGJl0Yi4qXhq5ryEty4+yjoNPmO23LAlJUqLS+5TztA4IoDm+18u/1IXV5CICopCyKz8ktlTyKRl8NmrsPSoGfn6ltCAAs5f9NRykuIzMpnHj9/A0TCYYQe/4NGlg/c/bBYVpmfurNBVVwahGcu24wd/cipyyAV15Lykm3xo3ZcAytYPbeIbfH6XVeIX7/7FCvqx67ch+0xJ2wIN819b1aT3yPkpatfBODqP3VNua+6QGl7T1yu0dACsiEvF/2xB3IOsV4EYRhoiry87xkEgaHTVkHq3JXbIAzrftJ6MJAeAll5pTmSWwowxECebXtPQD3ZXUJ9czyquJVVWw5i5U9fvw+R1xzcTXheZvJr/XXoHET+2Gkkv5VSd79wCBw+dRmPGPASSuP3jmXeuvckHnDTQVMhdefRixB28gjCw3jl9kN20HQahr6ZeGkkIl4avqovL1X83GZCem59s/HQe3oFRmHfOnIWm5tV8102xzWpgJeZEIkjIamRl4GRbDAEqW/XNwcYc7VNBTcdKPKSsern7h80tuS4H7jv2bAJ8iMv77v7YWkQCUPDstXf7zjvjwMMDxduQ+rNewwkUl5CCTDeek+6xeaDMf4//Mg1JilTxRPirQbmAELYNIzMIF6l5SXsLIPuD10HWi+ByOu3nT9oVMbL284+ELn/jC2El287LvLS5tpdCACoxO3CjrByGvWDgSwMGaFA6VFC8gEvIQyDZjik3BcdWMXUJTAQ7zVqbkBkMqtMAdu1aP5Qi7z8Wx3trtU2feAV7OYbxg7IqctYsvj8EjNv2nkEagKBd2FntWvtPGSDvJRRXG9NvDQSES8NX9WUl9CfHjx9DTAAATd+jOIfnogw477uBJ3sup0nIDxmwaZyeZmaUwSRKVmF2XyfLlrKS5b/s06fNuuXzc+jJmXkw5hM5GVoTCoERs9YCTT6R2M25Yi8fL+Rxe5jlxlvcosZ0uqYQQUgKTNf4+wVFMOPa1tajoGYBt1Hm+jMx3JfdP6i5QDcYoIqLzI+nUXWYVCcvWoHYAMndU3YxOwhCOPUqEqHlwOsF6t0eNlhwDRY9zdTNraLTckSeQkwg8DYWashFTIHR6fAuncf+mE11m4/ZsKPOMVKYgWmL/4Tjx5Xm029wogwUZUHgf2nbyDkTIfPgRr+YmVtIuHlhj2n2YHK17j7R0LAw59Ve9G6nUJROrzEA96l/2QcT4cnqOBEEC9JeijipeGr+vLyX3XN2LCjDv/gra5FhnY+1mLkvL9j5A/siWO5vIR4fEIG4zMpCWS8hA4amPdOAwso8L2GFg+9Q8vGl1DCj13ZVmp3Hzd3vYl2tMr9yOABo8zo5Kz7nkH/Vx/Gixb/rmcGMftOXIZKcrXYSPG1OqZdh8010eElbPE9tkVz2CJs2js4Gp/UHj13EzbNRnK1zSHwX364ydXq+ov5OJOn5mW34fNeEw4XOwjS55ft+k2BwmHw92Z9czAUYjFyLoythfxfdpRWku1mLXb0YKdgryMTVHAuYATMRqI/d8cMfx06X5N/hDxzzV4TxsskiHy/aX+IhMxwSCFnNk4p8ycCDiY7KTq8hPCUxZugbm/wFYMC49NyiZckPRTx0vBVTXmJzuSfron1R5hNmL+BJenMtT63M/kf3ejGY5JupG4eWbZK19JdRddZlWWQGnkJQ0bVE7eexf+gSVzMUMtjnmC+zmU5567drS7S5BVr3v6tz7v8M1RpzqcsU2pW/rOvpQ8mXhqJiJeGr2rNS5mlvCRLLeXly/FPZhNqNmY/l4XhY3i8SjeD8Zh4aSQiXhq+DImXKn4+8wnjJ2M2HJnnGNW9iPGJI50O4qWRiHhp+DIwXpLJ+mbipZGIeGn4Il6SyVVq4qWRiHhp+CJekslVauKlkYh4afgiXpLJVWripZGIeGn4qha8zC3SiNZNfT6PmM5eSveUHj6Vvez0OSyrM4TFNyRA4Am7U+nPZDLUJXtOXtWNl1paPhQoqwxWQPwREITFjT6hYtsPsxfaPb2l/yUJYekRUPEbEjNgDcWk5/t1Er5USK9MvDQSES8NX9WClx0GTPIMiPQA+0fopj6fW/QapxtZkZv2GKMbWanb9p9k/8Drvkcg/vfhuHnrXH3CrBesD4lOgZgxc1Y7uPpG86+4m7xI/j8wt50fPfkrm4CTe27+uvHSDM16lu3jgElLHN0Drtx2PnvdQcXDac6qbc5ewa16j4fFfaeuXbvr2qL3eFgrK780JIa94qdcr97O3iHwlL7vGRTBv6JIxdfn2Lmb7n4RQ6YuxQNy5tpdB1e/3ccvHra5Aam/W4156BNq6+QJSZfsnWW8lJK1IsNONbEYpRv/ak28NBIRLw1f1YKXbfpOxH/hxz60w0D2djQX79CUrEKImb70z+sO7j3HzMX/Xhg9Z/XWA2cGWC909Qk9cOa66fAZOKAZM3ft4XO2yzbtwy9tIS9v3HOfu/qvwzY3+/EvxBE9efHG/aevrd9xNCoxQ6Xl5R+7jp255rDsz70nLtrDYqfBU61Gz2abGDEbFqFw7OvR0Ln7hce36GM9d+1OXBw/n73GHY52uwGTYBi059iFtOzCoMjEs1fvJmfkSbcOpNx59ILdfa9rDm4AVMh/5Y4rrLJyy/4b9zzGzGYvroMd37jvDGTuPHjqxt0noLYNzUdLC4lPU9/3DJTGoJtYsGwrtx7E1wvc9wqC42O9aGNKZn5j81FQ8u89xuqu1arPhAt2D8bOWYO87DBwCuzvvlNXHwVFw2Kz3hNU/K5BNulazXsxAMuKgs0FRSXB1ltrMwOzYbtwewGZ1+06HhSZ5MUXK7W9s/dtF5+bjuwIdxs6/cqdhx0GTIa1YpKzYMgLx2fWym23XHza9p1o6+QlW/fVmnhpJCJeGr6qBS9Nh03/puNgsOXoObCYnlNsPmJmU223Dpi85+4PQ5m/Dp6FDtRsxCwVz6eVm/dD4K6rr6tvOAT+2HkU84+ezT7EAbyE3hlAiLOUM1ZuS5dscebKbRjoM2GBSjK+DI1Jvevq15wftwEvcQKzac+xUBQjuuRIJqryxs5dC5HhcWn+4QmwidXbDmFS237WKvbprohdxy/lFmrWbT9y6vKt1v2spROV4vgSeJmu/agkZHbyDIJhpU9IjMjLToOmYGon/iMeokfPYu+2lcaAYd3IBPb2gAnz1mBMbEoOvkXv6Hm72JSsYxfsILJW12GzVwlHQMUPDe+7s7EsBICXsJu3nX3wuP1iyehrMYrdMcAdDFRbutaEBX+Ii2Kk2YiZKn4sCMcNIxHhUYmqzfvPQHyb/pOCopK/7zw0ih98o8XxZWSiqkjDNh2RoLK54Xj3oY8qtwSpTONL0isU8dLwVS14CeNL6TAFwp0GTt536oqKh6XVqNmAOuhD128/zI8v2fdJoD/dffQ8BB54BQPhIHDm6h1c3YqHLvASMrfrb+3g5u/g6gcGDIub2M8XzjbNsw152XHQVOdHIepiDY5NO2r59JvVGN1RFFTA0T1Axdd252Eb6OunLPkTF7FMtPnIWbALMD4DWM5YukmMl/ISY2DFifPXJany8ko0Hv7hIi9htI0Zug9nHELDOW1oNlJcRMOhmLRoI4YXrt+JdXbzjxA5nZ5TtGrbIXe/MEi6YOsofhkUFv3D4jDMeJlXevzSLTxod/ivajt5BEIhXYdOkxLaKzDKT7uWWM4vlmPwY9FQiDi+bNGLzQmjZ6/eDkXhIeqovRVQSXjp4h0Cm8Ot+4ay8s9cvTtsxop5a3cQL0mvUMRLw1e14GXbvhNVfG8OhkDL3uOz8kuvO7hBxwp9aI8xcyGy27AZT+Zl1yHTYPWAiETobVXa+diVWw5csHsA8faMT2XHAUa0Kjbiybhk/0DF8zKDn2yEv7tOXG7fH3vzx3h55LydnWQ+Ftyu/yT4a3P9Hr5UvQU/abll/2mcVASnZhfiC1qb9RwbFJV04Mx1cV2gAuwLVEzkJSzOXbcbYoZPX1EpL70CIqMTH3sLneWo2QAw8RjmFGgOnb0BgfZ8JdEDJ7NJaX6ytHT8/PXSd8HDjQXclFy58xDnY9v2m4hFrdt9EjPMXLF16rIt0i0250fw4mIGf5cDf7ECKjbiPwaLngFRSzbuxRjYbkpmvoodKzZDO24em8FGw4kOi0uDexpYpde4+VBIokoN4Su3nLFAODvQklvyj2P1ysRLIxHx0vBVLXh5y8nj1n1mO0d36EaDtN8PgUX4G5GguufqC+x09Q6GDtSBTdCxcaenP5uGDY9PD41NhcC56w7OXkGObsI7VG3vuWEAxkC3H3hF8s8pRR85d/OhdwgWJWaGMm8/8EzLKcJFeye2dTHVOzg6OIp9hUM09ONQ8qOgKFyEusGif3iCmMHOUahDBvvxjvzlrpD5poNrkuTRpldg5B2XR1CNqEQVrOLmG8YXIlTD3slDzGk5em7m47+wtZccQ4yBwRlsQswABYqAhPgIftpWdFp24e37nvFpuQ+9g1U82Jzc/SGbuBUoXwQhegL/vFY0lI8VAIfHpWHkXRdvl0esQPSt+8KdBJvylRSOhrOMxxzIfcf5Ef74K1NdCmE4Uzi0jUnOEgvRExMvjUTES8NXteClIrbhfxf6lAZe6kZWI5+94aQb+TKdwX86RjfeCE28NBIRLw1fxsNL6dxgpZaNbMjk5zbx0khEvDR8PZmX8emP/Z8DmUx+VhMvjUTES8NXRbxcf9aj3fzzGTrxZDL5mUy8NBIRLw1fFfGSTCYrYuKlkYh4afgiXpLJVWripZGIeGn4Il6SyVVq4qWRiHhp+CJekslVauKlkYh4afgiXpLJVWripZGIeGn4uuUVnaBibyAjk8lVYbi+4CqTX3gkgxPx0vBVWFQCF7PuRU4mkxUxXF9wlckvPJLBiXhpFLL1iHzyp4nJZPJzWl1s6xElv+RIhijipbHIziMKHByXEZumJpPJL264mvCykl9sJAMV8ZJE0jv1nbm5tLRUHksikV6piJckkt5p6ILtJSXESxJJv0S8JJH0TsRLEkkPRbwkkfROxEsSSQ9FvCSR9E7ESxJJD0W8JJH0TsRLEkkPRbwkkfROxEsSSQ9FvCSR9E7ESxJJD0W8JJH0TsRLEkkPRbwkkfROxEsSSQ9FvCSR9E7ESxJJD0W8JJH0TsRLEkkPRbwkkfROxEsSSQ9FvCSR9E7ESxJJD0W8JJH0TsRLEkkPRbxUUmHR8cERsWTyizgkIm74wh2BYfJ4MvlZHRQeI++kSC8g4qWSGr1kF5lMJuuPo+NT5P0U6XlFvFRS0DoLCovlsSTSM4rmY0mKCHqkGOKlciJeKiniJUkRES9Jioh4qayIl0qKeElSRMRLkiIiXior4qWSIl6SFBHxkqSIiJfKinippIiXJEVEvCQpIuKlsiJeKiniJUkRES9Jioh4qayIl0qKeElSRMRLkiIiXior4qWSIl6SFBHxkqSIiJfKinippIiXJEVEvCQpIuKlsiJeKiniJUkRES9Jioh4qayIl0qKeElSRMRLkiIiXior4qUyKiouLiougdaZm1cAYXkyifR0gsZTXFwCvCwoLKKGRHpuQeMpKWE9UmRsEjUkpUS8VEajJS84HrV4lzyZRHo6SRsSWJ5MIj2doBeihqS4iJfKaMSisqY5bvleeTKJ9HQavnCH2JCGL9ohTyaRnk7QC4kNaQTdwSsk4qUyys3LF1snPXciPbcSUjPEhpSYmiFPJpGeTqWSuQroneTJpOcS8VIxDVuwHZrmqCW75Qkk0rNo4qoD0JCsVx+QJ5BIzyLoi6AhDV2wXZ5Ael4RLxVTZFwytM60jBx5Aon0LCrmf6aRV1AoTyCRnkXqgkJoSD7BUfIE0vOKeKmkgsKj5VEk0rMrOj5RHkUiPbtCIuLkUaQXUJXw0s4zys4jyjMsJSwhKzwxm2yohvPrEZoMp/uWV5XcKDgHxNt7RnmFp4RSQzJow/mFswznGs64vBEooTjP1bEeq9JCj+Ym2KoT7MiGaji/6aHHY91XxnqskDcCJaQ8Lz1CkkLjM1W5xWTjsXdEanBsurwpvJjsPaOdAxJ0t0U2YD8ISABqypvCiykjxl4VcVqTG6DJ9ScbiXPib6aEnJQ3hReWwrwsLWXdnO5lQDZ42ys6xFTnF8GYVXcrZIM3nHc4+/IG8QKK81yj25+SDd5xHms0pSXy1vBiUpiX7iFJYQlZutcA2eDtEZocmZgpbxDPKye/uHSdTZCNwXDe7/sp9tQtK8ElLeSobmdKNnjnxtumwKlXVArz8qZ7ZHx6nu41QDZ4hydmu4co9isVW4+oDHWJ7lbIBm8473D25Q3ieZUSfEqdaKfbmZIN3oXpLrFui+UN4sWkPC8TVfm61wDZ4B2VnOsaRLwkv6iV5WVy4NH8lLu6nSnZ4F2kco11WyJvEC8m4iVZGRMvyYqYeElWxMRLsv6aeElWxMRLsiImXpL118RLsiImXpIVcTXmZaa6RF2k0Y0nG4xfDi8zcoupIRm2XxIv1QGaojB5JNmAXI15+fqgfd8MPzBrzz3dJLJh+OXwsumcc9CQbN0idZPIhuGXw0vbde9dXf6hw18/6iaRDcPVmJdv8bzsNuOkbhLZMPxyeMmZ74CGdPiKp24S2TD8cnh5aSEHvLwwh9NNqmaGgbLMupFi5rxAweoK1pVmruYmXr4aRyWoTJpYyewZFCOGazQwb9xtpJhfXaTB+JDoFIzxj0iCRY5rBGGLQZMh3HPUHEyqyeJ/1d1otTPx8vncvMcEbC0fNLLkvutyzz0Q499raCE2sPcbWWTmldRsbPVOAwtxxTfqmdVoaJFdYGiz08TLZ7K0U0IXZ/ly33aTxrCceYHcD6Zv1rfg/t2B+9l02py5mrwA3XVHzVqsu4lqauLlqzFcwOpiTYFGA11Yu8GzIQxGXnJfdoPwx7/1gnBmXinm79Cb9YAfNrbiTLpgjC4vwYkq9mIH4mW5MjZe5pVonH3CuR9NIWz/wEfF8/L1embY2MAQ81WnUZCalc/CcHD4FtVMt8DqbuLlc7h573FwL6XJD2SL6gDgJdxdSTOkxrpAg9EUBeNiYaavmMR9ZcaS8gxnZIkmXr5Kw408dGGtBszARYGXn3eF8DDrhVJe/rOuKfdNp0WbDtdsbJmVzyJ1efla7e6cSUcV8bICGRsvYfgIYWhCrJ181B72XZeX4XHpkHrb2RvCzt5hEI5OMsAPGxAvn8PNe8l5Cc1j5cql4BUrl0Bkerwra1p1LFetXh4f5SxdV+ClAc3EoomXr9Ll8hINXPQIiMJ4GDVCzI177tj3LVi9XVUeL1OyCmCtwza2xMtyZZy8BNdoaPFOA3NoPDgfy3G/866Lqd+3HcT90CVTXcJ91oH7rrtuaQZg4uVzuFxe2l8/xnztGOZJiXPl3u/6bgO+XX3VTQQk8fLpRbx8WpfLS+5/3cPi0z9oZAlDAYw3H7uExZu042q0ZYGfukHfp8tLCIyesfLfdU2Jl+XKOHkpjC8/KRtfyjJ7BsVChvRcNhl73s5ZtzQDMPHyOazLS9l8bJnVAQuWL2eAxMzEy2cR8fJpXT4v+fnYWSu3m/APluBSf6O+2VuNevzUbQz446Z9IT4sLrVcXkKBJvzwlHipK2PjpbpY4xMaz/1gDuFrd91U2ueXuUUaNGbGx5bvNmDZxPl/AzPx8jmsy0toIWdO7EJr8gLS4h7+r+1A30f2UWH3azbry9UyFR9YEi+fXsTLpzXgjeNa/Gg6ARc9AqK5N1pz3C8q/p/oOa4hxzXZe+IKRCZnCkcgt1DD52ngF57IB16DyNYWoyCMGXyCY/j4Grqbq3YmXj6fv2k3lLWBGm252hbDpy4Xf+8KjY3Fay3m57jGfJupp1uUYZh4+Rw+dHjnnl0bBQSq/Xft2LB315+iWbw6wNbOZoT1jG4Dx6/fsFpKxx07NrI8xMunEPGSrIyJl2RFTLwkK2LiJVl/TbwkK2LiJVkREy/J+mviJVkREy/Jiph4SdZfEy/Jiph4SVbExEuy/pp4SVbExEuyIiZekvXXxEuyIiZekhUx8ZKsvyZekhUx8ZKsiImXVeiUzPxElZo5Xc392hPfai1zek4RBnIKNfi2dGXdfaTw0RKppy/bVC2+QWG0vMzMK01S5SVn5GXyFR4yZYlunipySlYBBtKyCzP4QFhc2rbD53VzViMbMC/z0h/lq3inPzp58oBuBrnzAgJ9bskjn87z1mx8pn+p7DFhoW7k87lmp7G6kS/fxMsq9BGb64Al6PvA+aWMT4DMvJKyV6uAvUPiIAligJfQRWJATIVFGdgwFUuAXkBaVG7hYyVDTli33yShq4VNi6nz1mzPIV5qrW+8PHT2xpJN++F8ZeWXHjl3E2LGzV2TLTl9Kr4BSNsJhMUTCmtJU6XnXTSWJt7AiS0HGmqvsfOgQWbllR48c7VIw+IhElNZi8ovKxmbn7R8Wa30xwbMy3ZDZhRl+bK3B4DxUyEQyA9kYe3b6TQFQZqiEOH7lHmBwX63HytESOVBCAGMhHXBar5M7RdIlm3YzGLYpy75zOyzl3wAS8AVS8NyUh8JiyWhQiSUUCgUImxLW2aZ1Xw28ZMmsPXCsrWa9ZnEAoVBZYXIVn8pJl5WoYGXuTy0oE/5qesw+HvX1e+BV7CTRyBmgMv49LV7zo+CwdDRjJ+/7q6r78T56yAe3Nhy9D03/1krtgRFJYtlTlq0wXLUHEf3ANMRs4ZNXw4Frty8H+IDIhL2n7pyyf5Bh4FTYPGCrdO8tTsO29wYOm0ZLIbGpE5csN7+waNfLcdAycRLqfWNl50GTpbVs8/4+UfP3bS5cc8nNBYW/9x76vIt578Onp24cAMsdhw8fd/Jy4vW7zp+0Z5lHjfPwdUfckAhQZGJ1gv/sHvg1aznOLFMaJDQxhw9Auas2gaLDq6+NtcdLt92adZ7fHxartXoOdBE41KzV209+NAnzMkzMDw+fefxS7DWqFmrgN8zl29+FBwDKzbvNe7aXbfN+06NnLkSFhtbsOZ6+sodPWxahs3Lkhw/Rqy8AJuzhyAmLNhx7Jxlnu62FiNnsfhc/wsXj3m62f7aYyJbRcbLvMCN27Z4uN40Gz4DFptAHp6yI6cthHWHT1vs/ODateunvT3tNFpeBnrbZSV7wKK/t310qGN2iufFS8c93G627DcFUv28bzk5XX0E+dUBQ2cshWz7D++3tz+3//Ae6/krWYUHTJm5eOXlKyd/7ztVUo2Atv2nOD+42qrf5GKG/8BlG/68e+fi7n078TNhjJfqgHYD+VXytIGXbuJlFRp4uf3Ihb8Onz9+6TbyMjWrUPaKTnf/SLzNB14GRzMuQscElI1IUN128VYXa/JLNH0nLBTzAy/xFr55r/FYFHRb0B206C28VG/Rxn0Q37rPBOwff7UaA3/bDZiUx3/CyeEh+3IT8VJqfeNly97jZTFDpizFQIs+1rAL7fpb42L3YTNgwNdzzFwVj4Q2fSdCAAAJLQT3tGnPcXkl7Lw7uvklpOXiWsmZBVsOnMF5C8gG7Qc/77V1/2mIgdKy+Ha198QlHDhKeaniG+rUJRshcPD0FSwQeQlNTtyuvtmwebn74L59h/d7ediJvHS4cwECHm62YJYtP8jR8cqc5WvYcO1xXo6ZtURTHMKsiQBApie4OjlcBGT+2hPhGhAWdO/u3UsdBzE+lctLlq0wGMqfvnRtvsob1k1PcMfCGS/VAYBAXOw+fCb8bQ2L/CCyRV8hHuzufDWKL0qV4L5w3Uao5NGTh7ECHq43NNrx5di5K9Tpj/we2dvanxfXfZkmXlahgZciHSvipZuEl/j8MoefHHPzC7/h4IZzudJVgJfY0/1mxUaKEGjB87Jpj7GYAfAM+dv0FXjZku9DW/aZAFsRiyJeSq1vvOzQfxI+thQ9bu4aDNTpPhzOYIcBk3Gxx5i50BgGWC/CxTb9JmbwMxMpWQWLN+yBnNA2siXnXTSUH5+W076/NQSAc9Jm9gRezln9lwqHpwvWw1bOXLmNpSEvwdC8V27Z7xUULd2WPtiweVmQ4YNhkZfuPGP8fW4/uH915Z+bMxIZwNZs3KjLy37j57ABJZtZxfeq+zfrPen02SM5KZ6waAqE49nWgR/PibzM5nnp5HgFeLn7wG4cAk5evDon1UvOy7yANv2n4GKf8XPhb3N+pAiBNgPKxoj37pxHBsNodTwMQ/MC7zleYUl5AUBrjTgfmxfQuId1s17Wz/QYVUETL6vQurwEPwqMTkgX7vRV/JUcm5INMTJeQnzrvhPiUnNikjIX/bFbzF8RL2EAERiREJeajZ3p9sPnTly+HRqT0mMM+73PHRefCQv+gC7S1SdURbx83PrGy8CIRBhixiRnRidl1O0+XPU4L1U8n2KSs9x8QzsNngqLLXpP8AmJsbl+b9KijZl5JeFxaXCil/y5D3b27kOfcfPWxafmPPQOTcsuxEJuOnlFJaqgacFNFSzuPn4xKCoJFm/cc4fF4dOXQWuEzFduP7zl7A2j0nJ5CYF2/axjU7LuewYiL89evwfbXb/jqG9ovHR39MHGzMuLV05fuHg8N9XLavQsXV4C3o6dPJyb5pUe74povHTpeKu+WqT1m5yT6hnke7vT4GkaLS8Bab/0mgxA7T9hLvDS9saZq9fOACkHTJzHeJkXcOLMURgFAnpxPnbawpXAwhD/Ox35QsrlJdQKsAqrN7SamJPiVSEvc/2nLFhx6gw/9HwVJl5WoUOik8UO2s0nBMPewdEefmHSbF4BkZ4BEUDWtGz2W1nxTh/+egVE+ATHSH9Y6x0kdPruvqEYIwag03wUGImDA7BvaCzwEkrGxcR0tad/OHSmLCkkRjaC0U8bJy9V/I904ET7hsTi2YTTivHQijAAMX6hsbg78BdOfRBcJXySf1g8nOioxAxcBPix8x6fLhYO7QraBkSKN3N+oXGe/hHAYLZpvtVhmG+r4ckZ+QBU2Ao0G9wc1A0DUAjknL5sEyxGJqhgEf6KG9IfGzAvQ/xus+eXfDg52hn+5qY9ykwSxmoqfmQJVIsIcogLd2JEVAcAAqUlqBLcQ/1vx0U8EGLyAqJC7ompkJSR5B7ix35SK8y+5vqnx7vhk8s84CLEh7DyY8Oc2KPHXP+oEEdYCzYUFigcpfDAu2xd/gdHwb7Cr3OxzDLnBYYF3MGhKqyrwkGq2j89wU26VliQY9nvmF66iZdk/bXR8rJa+I0WfRZu2NOq70T9n6swYF4alVdv2tzIin+w+opMvCTrr4mX+mw4mDBCLfeQ6puJlwZifnwsj3yJJl6S9dfES7IiJl6SFTHxkqy/Jl6SFTHxkqyIiZdk/TXxkqyIiZdkRUy8JOuviZdkRUy8JCtiA+DlCd0ksmH4JfHSjHhp4H5JvFzAeHmeeGm4rsa8bDDl5NfDDniGsX8oJBukXw4vbRyCvhq2PzK57CUSZAPzy+Gl59nxV5d/EP1wu24S2TBcjXlJNni/HF6SDd4vh5dkgzfxkqy/Jl6SFTHxkqyIiZdk/TXxkqyIiZdkRUy8JOuviZdkRUy8JCvi6sHLBOKlUToyOcctmHhJflErzMug43lJd3Q7U7LBu0j1UN95ec83NjIpW/caIBu8vSNSg6LT5A3ieXXnUQzx0jgN5x3OvrxBPK9U0faqiDO6nSnZ4K1OupPgs0XeIF5MCvOyuJjdG+peA2SDt52nYmMCUJIq9643+yIV2dgM5x3OvrxBvIBiPVbpdqZkg3es+4rS4gJ5a3gxKcxL0C2v6Ayda4Bs2E7PLb7tFS1vCi8me8/o+HT2UW6y8RjOOJx3eVN4McV5rdHkCl+dJBuL1QFxnmvkTeGFpTwvNXxP5x6SnJZTlMFmV8iG69xiOMvOgQmK93EoKNY/Oj09h32aW75psgEZzi+cZTjXVdSQ4jxWJwfsKs3x0eTyH5kiG6pzA+AspwUfhDMubwRKqEp4CSopKU3JyPUITXIPMRbDzp6w83IPTtRNMlR7hianZalLS0vlp185FRaXJKTleIUl627dgH3c1tM9xIgaEpxfOMtwruWnX0GVluRnRqeGnkoJPmosDjnqZPtHjM9BebzhOjX0RF5GWGlJkfzsK6Sq4qVxavSSXQWFxfJYEukZNXTBdrjjlMeSSM8o6JFi4lPksaTnFfFSSREvSYqIeElSRMRLZUW8VFLES5IiIl6SFBHxUlkRL5UU8ZKkiIiXJEVEvFRWxEslRbwkKSLiJUkRES+VFfFSSREvSYqIeElSRMRLZUW8VFLES5IiIl6SFBHxUlkRL5UU8ZKkiIiXJEVEvFRWxEslRbwkKSLiJUkRES+VFfFSSREvSYqIeElSRMRLZUW8VFLES5IiIl6SFBHxUlkRL5UU8ZKkiIiXJEVEvFRWxEslRbwkKSLiJUkRES+VFfFSSREvSYqIeElSRMRLZUW8VFLES5IiIl6SFBHxUlkRL5UU8ZKkiIiXJEVEvFRWxEslRbwkKSLiJUkRES+VFfFSSREvSYqIeElSRMRLZUW8VFLES5IiIl6SFBHxUlkRL5UU8ZKkiIiXJEVEvFRWxEslRbwkKSLiJUkRES+VFfFSSUHrjIpPiU9KIz/R6Tox5DInJKcPW7iDeEl6cREvlRXxUkmNWrwTGiiZ/OKWty0S6dk1mnipqIiXpP9v7zzAorjWPj5f7r3Jzc1Nrkk0cnO/76ZXO2rUmBgLKopUGyL2higg2CsiYlfEroglKqgUFZWi9K703pHehrL0YuF7z5zdcdwlrlFYXX3/z599zpw5bZad+c05O3uOQnUrKGrOxqPSsSgUqhOEvOxYIS9RChXyEoVSmJCXHSvkJUqhQl6iUAoT8rJjhbxEKVTISxRKYUJedqyQlyiFCnmJQilMyMuOFfISpVAhL1EohQl52bFCXqIUKuQlCqUwIS87VshLlEKFvEShFCbkZccKeYlSqJCXKJTChLzsWCEvUQoV8hKFUpiQlx0r5CVKoUJeolAKE/KyY4W8RClUyEsUSmFCXnaskJcohQp5iUIpTMjLjhXyEqUgeQZFT1xhN2vDETiHIWB37oZ0ChQK1UHSMreFswzOtWlrDuku3y+9G/VcQl6iFCTb328uEqxXtXa/o3QKFArVQZJaW1B6N+q5hLxEKU782Qsns/Q+FArVcUpIz+VPN4/AKOndqOcS8hKlOBltsacnsOPNYOl9KBSqQ4Wdyw4X8hKlUOEJjEIpRqbbTsO5NnP9EekdqOcV8hKlUJ254jt7Az4fi0IpQgs3H2eraqRjUc+rzuLlo0cP7+Ym+qXf9UWjBYaPRGBmlGw8+nW1f0ZkbH6q9AXiJenOvTfrovSmnWvwzwXuAH2k//EdpE7h5fXEIK+U0MTirMKasqKacjQa/cY6t6oktiD9ZlJwYlGm9JVCgfJJv3MD2lCcWSDCi9JrayAOcAfoAwyS/gR0hDqel9cTAysaRWxDNRqNRvOOyk/xSAmRvl4oREDK/OpS2SahX1cDg4BE0p+DF1YH87L1QSvcSMq2Ho1Gv+GuaBDBxUH6kqEQeSaHyLYH/XobbpKAR9IfhRdTB/MyODsmrSxXtuloNBodmBlV1VgrfdXoZLU8aE0rx4vSG2cgUXB2rPSn4cXUwby8lhhYIMJxDzQa3Y6jC1KTirOkrxqdrOqG2gqZlqBfewOJrnX0kGwH89Kd8LJMtuloNBodU5Cm+Kd+XlleMsyvYv80zdX7tmyCF/Sq7QcmL9lQWPWGXpCBRO7ISzQaraRGXgqt8tPEj/vrzl69/R99dSB8yvU6ja9orC6vfyJlZVNNZaOosklUXl8lfJqSxsBeSUYRH4YS9BevhmILqsr4SKEhI/tEUTUQI6wXShNWB3XRcvg0NIuwTEkh0KSX/8gn8hKNRiuxkZdCA8yY7zUg4OztC2Ebu2MQDkuI7w7xX6j/s6/2JwP1gEBALNjbQ20G87k6RWyRiK1qqmH+O5aU0FUNXt9S1YO8Z67cgPCH/XWZd0cOm2oC2WETymE+HiWs970h+l0H6DFvjWB6aAYnJECM9UEHUtS345nuo2MyUqHG9wdOIs14ZyTE6y/ZAGlmL7eC8P8NnQqF301N8Q4NJVn+dyy0h/lmAmQpqakgMZ+rMx+qde2vK3u8CjbyEo1GK7GRl0IDXQhgmEGEgkP0KRqZL8d9xMFG1FoHgZsBAZSXzJeErD6RURB+e/icc25XIXDWzR0ideaYQxiSUV7mlBfT8qcarYLN/IonHighVXyuvuPYmarmWtJtbaqpaq6BipgehLgs149MzMmAjLGZ6bB52uUKhIGFlJdON7xoIX/rrTXWwIRLXwPx/nfvZpcWftxf7155MZQMFlb6UqzEvCyuq1h5dldlYzvDAmg0+g3xK8VLuOivOLPzJf5YHDDTbYDeNxMWExx+TbpowCqIIZv/pw6GgMa8NZSXc1dYQ5aa+/VkLzNskvF6CESnp0HkCWd3CANfKS/50dd2eQm+4hsAgOw+cCLTUyu9uEDUSsoMiY/lE5y9cp0U2FIH4cTcHAjnlBZSXmaVFrISRv69rw7fzo37jhESfzu+20A96Lz2GjNLqlLFW4l5+fUm/X5WM3T3msnuQqPRb4hfKV4yK8bARemMr6vsLsWYkI8bjw2Ji4Nwr7GzIcx0IyOcwCpgEtAxOTdb3L/8TqO6pW6P/TkIL7Hcdz0gEALTTTdC7/Db4QYqgv4lz8u5yzbAJnT7qjny8b7mF0A7l8yXWl1+mgQZ/wHk6z4aiAulZZUUZBTlQ0bHG56QZvFam08G6kEaykvaeSVo/HTMML2F1S21VU01GcUkS7GIhRIgS+2DBkgZm5Upe8iKtBLz8hvkJRr9xvvV4uVKdbgonfZxkd2lGPO8JPj5ajxlHrANwh8P0PtAVRdAFZ6YQHmpt2jNX3trcVkm0NHOb4YbdP9p4r9Uoaeot2TjLlby/SXPy9SCvA9VdUmW/lOF9TLMLx/21/2A23X2mifE3Csvhn4t9Au7qOrGpKdCzHLrvbD3/X7kQSQXbx9W8v0lP9hbVFPRdYDuR1w5H/TTScjJyqsogQZDFiiK+VaDb8bLMvISjUYrsZGXz2juYVTxQDHl5fzVW2m8TMrnwRI39ku+LhVGCivl08jmfUoWLqZGtpEvxchLNBqtxH5xXra2tjY1NUtF5uTmS8UIpYy8FFrIS/SzG3mJRqOV2E/n5c6Dp+7EJNLwSAPTJ3eKJaqpLS2vkIo85OAoFSOUsvOSFXfa5HT10FJGXqLRaCW2XF720VkEgU27j6lygb7ai27cCpy8eD2ELfced7zied7lBuXlDHNrRzcP2+Pn2153XuZXlh46/XtWCXkwlbfdyTOHTp0FiCbdy4K9QdGRshmlTLKcOc9yHdbqljqpwVgpCxMcdCB1yaZ5xY28RKPRSmy5vMzIyX3w8OFKazvKy+YWsr7E7YBQeB0zawW8BoZHAy8Dw6LKytnScnaM4bK2152XOWWFKj9NTMzNFkYyX2h2G6BX3VIbGh/LfDr23JVrshmlzDDDma90IJCcd++TgXoZRfmyaajzKkshQVBsrCTjr8wHarLJXnEjL9FotBJbLi/hdY7FFrZSRHlJFRYZB6+mm23hNa+wBHh50unq/fsPWu/fB7cpFS+hR7jKevco/aUas8yTcnNopNWeA1a77XLKi3+bbGzrcI5GAguN11ibW+7IY0uewsv4rPQtew/eDguFkrfsObBxxz6bA8dH6i9Nyc+NTE9TNzRbvXUPzbJpl53VvsPQa4QGQIFrbfZARtg8dO6y4dJ1o6aZbN57iE41sHGnLSRYutYaEqQV5m3etR9aSAvJKSueMNtCe+7yG0HiJdLWb9tjve9QaELCWEOzM1dv0EiPkDDdeStGTF2686jD0zuynWfkJRqNVmI/Cy+pKC/7aC10cvMwNLOE8PaDp+zPu1719KPjsb/qm1686vnhqFltSsVLUWudR3BIelH+zaBgYNKtiDsQ+T730w4H5ysL12yDwEa7k1XNNd1/mvhRf13AFfPZhKfwMjyB/HbT8doNyNK1PykHuo9MPzLpwXHHyy63yEx7UWkpJMvXmn//2QDode6aB8lyw+t6QCBsLl677U5KckRK8jt9tD/op1PZJHLx9oEEwFFIkF9Zynyv8c9+pGPaU4tMrQD9Tq/QMAjsPvE7KZYZBmH3gEBnLpd3eASUAIEbgUEpBbnHL1x8Wd+8Ii/RaLQS++m87CS9UrwEbz9x/rPfDD7k2Paj7lKW4+VHqgRILPejTL3ZZtDXhADzby2IySwmswc8Iy+ZL8bB3rU7D0IkxFS31HUfONH/TgTJwvGS5cZjYS8/HltaV6mxYG2X/rpduamFWO4bU8pFcV0SXv5PL/IDUHHkB2rM96R5wMu3+pEJ/KA62Pu721X6QC/TQ6uPxoKi6nK+zQo28hKNRiuxkZdW+48DSw797uQZ6A8BlTELWI6Xf+1F2MNKeJlWSBjJ9CHzDGQVF/wJXn4yBvZa7juiwk1cAAm6D9R7Ci+LRSypqK+OZ4B/16FkniD2j3n5F27CBHHkWyOZbyaQAPQvB09meV66XoVwQk7W8q37mf+SnvEVv0C+2Yo08lLpPd2czJEB5u4E1Y9ccJZN09needKR+U7jin+w7K52fdnbF9LLxrdr5l01hhE/GuDsdUtFMuL0jKZ3puQE/ljtZX3t8acMTf3ylycmT+Fd3VwLe7v9NEl21xtr5OU8i03wqbA97fTxLwROf8RL+PD/T09NCDu4XHu/r7ZKh/KSThjLfDS2h9biwqoyEu6tY7bVjp56LCFf7ScD9ZjPx/fSNoYSeF7uP3sJEsxbu0Nt1koI+EZGkWJleAmNZ/46Bo5xC7fsyeaDp4QtV5iRl0pvysvf3a45A4Q+HQPh23fED4KLWuo8QsOjMzJ4TtQ+aKx90FDWUO3k6UOHVhw9fUrrHi84V9FUc+66N//UAM0Cn++6Bw03gsMF5TQ4etyOSEmpuV8Pm3bnXaFez/C7kJjuhQDsuujlSzch4OITWHO/gVTRKLoWGALpa7hk4qa21v/u7iU1KSWtnflOk/lCi7ac56VvZIx3RCTfnsom0fWgsJuh4dBUqRIa21rIpSE7o/5RE6SnNcZkZrj4BLDcExA3Q8J9o2Lg3eBr5E2PDnIVVJU7+wTUcu1nuSmqYS9cO64Fht5NI/NTS5nbK8oqLcouI3N9QfpL3n58FVDgrYjIy7f84V3ls2SVFMINRxVHRJ6XotY698DQ1II8eqTIS1kjL8k6XMxvzFvDI9NSGEaV6UI4xDC9GeY7lluTEiIHqs+EcFldJcMMZZifM4oLIDI+J0tYDsN8zzB94YwIiY2BvWec3eATyzB9GOYj2GthvRciKS8Zpt/t0FAuy3dQNc2us8SSYfpDegiv232E+d8xxpv3McwYyEUT3E1JZpgBXBV1DPMlw/Si8X6RkUw3NebDURttj0taAhrMcryE7PZOzoSXX+kwXdWY/4wx2ih+2kjxRl4qvSkvr/r40U2mpybzoya9vKpIZmtkekygsxhD+NNBk5gvx0Hg7d5a7/fV/heXgM4euf3IKZL4C7KX+YIMjFRyWXqOm0/nomR6kVPR5tBJEv5W4y+9tKCbCHnpAghwK/o/vbQgC9NH5/2+OmRBn6/GQ71kNbvP1N/tQ25p75UXZxTmdh1Avmj5UFWni6pORWP11yMMSYGfk3pH6JMFfXjDaaPC3aJCSmaoIeVlz3Fzma9Je1SG6kOawupy2AuH8/c+2t25r1j47AAt2KXCrfDHDJ5WVF0O4fcGT4V3oJfGAt+7kbRkaD/cMueUFQPYunCt6s6t8zdzxVZyOPTYfyADQefcb0Kxc1dsgfA7vbWYHuSGPSXv8e0FK7nX/s+IWfSdPHb+4jvcsTPfjmfpJeDLcfAOwC22imQ5iHRuNmrmxwn/5G78KS9Pu1xT4f5NZNf/jSWXKuSljJGXaIUZean0luLl0Gnm3KBKHbnl/GY8XJ0p8wZqzqe8ZH7QhGTfTVikwmGSrsjqFRZBl/WBbhDLEQjCnkHBNO/B0+R5dKYHgRy5u+wzGXBy1T+woLKUPqi25zQZVIHOFm0D8JKygRrgnVNaAGa+naCqtwRiXG6TL1ro3oDIuxB2uOxa2VzzuytZGE/q4TfmW03mc9JmVjIe6+ROHjFnPhlLVjmAQJdRcMhwpHA4zNcav023EGaHtwKyJGQRLFFexmWLb6uB6MAnlrstgCNivie3CCw3dgTJug+dBiz/ZtwCFbLkUDE0b5DOQtpsykvuvRUxPbXU560W1kh56R5IRqe7DtD7Rx9Sxbhp5DlACExcQMad6HyYDDPqfVVdcu/8jQbDDKfZVSS8hADzr1FQb0ltJYT1F61CXsoaeYlWmJGXSm/p/uV7I//aW5v0iriV03kz32mJedmH9BFHzCRXbbhS02vxjeBQumJOVmkRy41SqnBYory85HkbIt8erK/C8bKktoLpMwU6Q6Q0ldFQSDu8ZAbRcGxmOkHRv8cwzBBI0+U3Mi4k5OXuk+eF7QSX1z9xgLK8pN9fMl9rdudWBaI9P94M84swuywv6SgrmHyh8pk6yxEdqPY3DmzAJEAg02Us7aMD0qSaB/GUlxDgatf8zXC5sEbKS+hGsxyS4R8BgQnTl6hwh9xr3FyaF8LjF274eICeCG5uemh+PIIsvcQ+yUuhvxhuiLyUNfISrTAjL5XelJfu/gFF1eyCNdshPMt8M0su9GPf6qUFeKvkljuPTkt5Oi9pp8pozVaIDI0nX/hHpqa0y8uUvGzStWoULdm8T4XDD11d1sGNPCBAqhbwcummXTQXFPVBPx3Ky+vc95dQEaRPzMmE8Oa9h6HLBS3Mk1mKlumpw/xdjdYoy0sS6Ef6u9zye1BgbXbJE5OMtMPLVjEv3+pNBj8hQTntzPXWIfcZ3dWAo3TdPtjccsBehXuujyu8JqMoj5X0L5+Pl1b7DqtwfWhSl8po+tzTu/0nAjKruG+UVSS87A5N+mocfeugorisdOSlrJGXaIUZean0nmpqSfpD4B81mf+MveJHHmMBk4HKd0a930/nX6q60AOzOXKGPBcAyb4iF+ihBhYQ5nhZAQE6s0ZpbSWE4RL/dh/tuynJLDdQCTEXPW6xhIKTIEzGY4cYMr21Idk7fbSZT7VJXYCNv40ghXclD7JCFQzTmzaDlPCdBrThl0nGzEejmcHTxem/1SDpue5dVFoqtBAKfLevDvMpeRhP6KS8HGAJJD5x0fWypzcEvMO5Z/M+Vod4cWndJ3ygqvMhwKmnlm8E2cubDE331IrPJCvwFVWXQZjnJWnbX0d+oKr7z34A+FFAxIiUFPGbyXm6BVmA3tT6ANOLvC3AVzpqOtN8M333SNX/GTt46jJhjcBL2Et5CcfFvDsSAmOnGkEkTWC0cQ/8Xz6E/8t3GrSjCZiHwrtADDMSkn00UPKE/cdq0DzyH/xO4/wNb3Hftxd5z9HUyEu0woy8fM3Nfav35+bCqOY6arLxQsNV/lmS8X6WNtCOlGz8M5p+fykbL9cko7x66fFStnWIZVvL9bbbaf9z/AffKCuAl9W19Qut7BsEa34hL99MIy/RaLQSWwG8TEjPXWR1Ajx7wxEag7x8M428RKPRSmzg5aUgv+NOHp3nHSdcKS+pZ60/Uttcj7x8A428RKPRSmzg5TGP6zPWHe48z9l4VMhLw7WH61sakJdvoJGXaDRaiU3GY4sVNB4L7Lz/4GEbjse+qUZeotFoJbYCvr989OiRd3C0MAZ5+WYaeYlGo5XYCuClrF5xXlY2ie6VFeWWF73IA+cv7oWrrEWtZEbosnrxDNV77MnyllKmv8tiud93XfN/OQuPPKORl6+J4XMJph+76vZ+lvAcjkiMr26pAwdGR7HcbwRl07y4b4WFF1Q+nqMATnW6efzCJdnEvPl51blfoXBHLTNXu5RT8nLoj0qf0SccL8tGyv1pBxxOThmZI0mu4Z9FL2fweuz8RdkE6Gcx8lLKNa31I/VNEnMy47MyRs94Ym5IBTs6NQnOzcpGUVymeE2Cw+faOalFrfUi7ifRcCJ4BIvnCHs1jbxUesOHbPR0Mwq2m4FBEDPGcBl8/oCalHAULeQXhC2Pf0EIu3jkiCn7GDziZO5+/rXcAhpQGsQYLrMSlsCXyd/DkjKf/JEirYUm4MvnM9LwMSdXAIywZJpshL6ppBDpnypCgQfPigGz/7QTmYeoUbT96BlhGt60VeIAx9Qq8s6Qucsl4cfoFQZGGy5jJU3lb0G2HnKgU/+wXDOebDZp5zEnt9T8ezSGzy5sP//OZ5cWnnZ1p+H6R038Xv7HoPQd41tFYzrprkV5jbyU8vjZy4X3jtDOsTMs4MqwcLVNRGICy822ceWWz7yV1ld9/T2DQ6YsXkd7gUbrtnuHhp287JZVUsByC3iFxsebW+3NKMqHj7HGbItTzlcgZufxM2ddr7nd8lm6aRdfS35lac39elFL3cRFayoaqx3db1S11K7cug9KvpOcdM0vICwhAQox2bTrRkCgi9etTMnK0mBIEJmaHJYQD2eQ2ea9t8MjDp11ohcN9dkrA6KiHC67HTzbDmgVb+Sl0hsuoGoGpkLYTJi9/OTla+eueayysV28fse2o2fhczxsytLDF1zUDMwgpdttv9U7D+91cISrP2SB6/uc5VvgQg/c/Xmi8aHzzpCMlfCy5n6D03WPrJLCKYvX21++Ss8lakgGZY7QN4EyoQo4A/edcgznzklwQVXZ+j1HDp67DMUamGw64ugyykCMQLXpZjaHT4+dYQ6nFvDSwtrW7uxFiKzkZom7V1bISngZGh83Qt9s6aY9a3cc4Ot9Ci8vXPcUdgG3HT41Z4U1HGxSTiZ0Lj1DwiByxVZbk8379JdujE5PtbSzH6lvSrDUXDvVeB3LvZ/9NBeyEl52Gz5r3ymnBWu351aUQMmL1u44efmqV2gYtIG+V79NJQuqFFaXj5pmutzGbs/JC0Je/nv4THhP5qy0KRaxsGm6ea/2/NUQA+8YtHzFtgPwtkONv0wyZsk0e9ZzV9oMn2pCe6iwOWaGxcZ9x8OTklhy1TM/fMF53iobvnA0i7x80vC5Gj19mfCeFbx21yGWO2tGTiPn1Kjp5iy3yt6uY+SUCYyJ8eNWnbR1OE/TwylD018PCLrqG7B6ux0USBcOgsiZ5lb07nyA9iL+3g7OIGev27fC72QWF0AajTkrIQvlpbB/uXm/eMWuQ2ccaYB9sn95wd2D5W6R/aKiIO/a7Xa0LjgoPv1LNPLydbBPRMSvk5eMn72CLiwFny3aRQNewnWcJbeKRxvamuFjl5CdGRQTAzEltRWxmemABPhYw/Wd3s15BpH1FyGw3OYAxAt5CZEGZmRaWt6FVWWldZUs9ymPTk8DXs7k5q3lDbzUmL0SAvfKiopEpBkOLu5w8hiab6E8OOXiDjgEXsZlpsNmTEaaT3i4FC/HzVoOpw20/JdJS/iu1VN4GZGUIJx1SGf+Kn72dp6Xy61tWe6ctD1FLhDl9VUAsz/iJbwPGUV5sRlp81dthc0tB07Si5Hxpj20YXUPGyHLkIlLyrhlRA1MN0n1L9MLSXaAK2wuWP2YdulFeSedr9IagZdQ1GwLK9owQCPLHTtNaWCyEV6Bx9i5lDXyUsrjZlkIxyTA9hddaWAkd2tLT2ToDjpcIvHhSYleoeEQuHrbhybTmr8aTiL1meZldZX1DxtNLXdDrkG6i1luhAN4GZ2WSi0EM3x6jdfvgI9oRnE+/bTL8pIfj91nf5bPKDseSwIhYeUN1cs276EVRaWl8OlfopGXr5V1F6yBD7SQlyJuZAZuGOGyTsYVudHRaSYbYZO7ZyQdU7i+0xPMNyICOnwsN+ooy8vpT/IyPjuTfsrh+u7s7QsVQXXCBMDLFdsOkkBlKe3zQTKoXVXbiCaIzki9HR4GvMziZkgvqi4/e+W6kJcQht4YbbbwEgBn4NaD9jS8Yc/RpHvZTxmPhUZa2R47efkKz0t6rkLhbj7+LIcr4GWVgJeqWotYCS/VZ1hQSukv3cAKeKmqZSRs2M96i2myLQcchLzUnr+KHjv071lujIvfJcVLuLKsstnPEsRW036A4TJLmnLyYtIwcLGoYtEamxxuDRk0NfJSyrX3G0ZOM8kqKcgszh8zcznpcRouyyrO37DnyI0A8jTNH/FSf8l6yBUSGxOZkgxnh5qBGdzX6ixYI+Qlyw3begQFZ5cU7DpBlvnjPWSi8SgDcsqMn2URHBPNSngJeS97eOWWF8MHu11ewhnkHxkJCaR4yZKBqGVwFNB4863k1HjpRl4qveFyfD0gCHAFn8txMy3gVX2GOXAOrsI8L6PTU1dvP0Cu7I0i6E5BHwiSwQmjPW/Fs/NyuL5p9ZNf163Yuh9i7C+5Qd/o2XmZkJ0BjalprYfzCrgOvNSYswJKUJ9pAVmk+pcjp1vEpKfC3tD4eOHN7LiZ5lUttVApHCxk4Xl5k1uzk092xdcf0sABmlrZPp2X5LIyfRkcjt0Zp/7aAl7ONAfiZpcWTltKOnkOzlfJLXNTDZzG/lFRkB4OBGr3DA45dO4SvKVjDc2EvJwwZwWkzyzJH84N20IfEbqh9Osl+Edstj1Ov2am47F0XN33zt3FG8g3Q1K8jEqD96HW2etWSHwcXz4aeSlr+Hwm5mQm3cuk5wK8JuVkwmeY7k3MzuAiRZncYjsFlWXAKpYMLwWl5OUk3xOvDltSWwG5IC+NieNWLKAGgCXmZJTUkuEl3hmFubSc+Mw0OtaSnJtFz9nU/JyErHQI00UIwOkFj88RcNK9rPisNEhwr5zcC3IBUhRcjqANYLbh8bn/Eo28fB2cVpDrcNntkoc37eLAq/1Fl9PObuRbd8kIXmlt5bHzFz2DQ+EjCOcApL/seevI707w0YQTifIsOlX8+Kirtw8kC4uPo0OO/nfvQiRwC0qg5xg13GMev3ApkssFFdFlnHkDhBw50BaJyul5GxQTQ8+ftMK8kxddKKQ9Q0KhZ3na+UphFRmz5Z+PPXTmAi0nMCYGDgeOUVg4VHfB/SbE0wOsIF/K+kLA2u6EEKvphflwEw0QZcnZm30nmXwR6O5L1gqFZCFxsVyNNSU1FbRMeycXuD3f70Ceej98lnzFAm07duFSXGb6CSdnmvi44+VrvgS04YkJcPjukifg4eigDXA4/IWJZBexkCYhO/PgaTL2C9kv3vSCY6eNvOYXALVA5AFub1VTzbmr13241crAJ7nbf1bypC5UB+9/RFIiXziaRV52nIGXspFooZGX6NfKQlii3wQ/By8fPiRz9Dxdra2t0lECvZa8xHNHrpGXaDRaif0cvIxPyWwULM7VrnppLpCOEui15CVarpGXaDRaif0UXn6ntehuXPLwaSYQ/s3AjI/3D43KyS++/+CBoanlNjuHlVv2F5ey0Ol8wM0NO8rA9OHDRz/pGbFVIj6LlJCXb6aRl2g0Won9FF4u37wXXkvLKxPTsoS8jE5Iramth4DB0o00pp+ukZCXbcrfvyyvr5q8ZJNsPO9JRmvpd//0l8HP6Kkm4mfQ/pTHzSbPFcrGy3VlU012SQHkpY/gvXQjL9FotBL7KbwEJMBrfHJac3PLRKP1EG5uId9KxializheGppuoilX2RyC1wcPHsCr2nRC1p6a88WltKeXy0vumWoytxTLPaTGTz5FZ4PiyVT3sFGcXjAtVDX3izJ4pXurW+ryKkrhVTjLh/AJc1YyRxUtduZyMpWBVJmSzcfzUtG28dZbtFZ2pqo/2qxofDzFGLQkp5RMkEInwKIPlgsz0mPhNzvbyEs0Gq3Efgov45LTdRes1llIqJlfVGqwdMPtoIg27nkfrbkr03Pyp5tsGjLVZMgkY5r+lylLIJ7ycs7KbYYm4t6nrF4iLwEnZla2JpZ7Ji1eFxQbu+Wgg8acFZVkYizRYD3jQ+ech081AYJC/3KG+RaW+1WlufV+PaN1+RUlLPcDpxkWWyz328O9AgDvpPO1IxecT1y6wjaI6MweotY64Rxeopa6kdNMj1xwUdUhv7+kvFywyvqYk9vIaWah8XEAtlEGZnsdLkAnEppx3S9gx7GzVgcdHG9684UAL6FVRx1dJxmRX0aV1FTYHDkNbfCJiIDN447Ou+3Pr997zD8yEqAL1R085zxC3wTClJcV3C/FIeWvk5eoz7RYse3AnOVkZo/4rPRfJi85fMHFzHIPX1enGnmJRqOV2E/hpVzx47F/Vi+Xl5OMydQZQBF3/wCW62/FZpAJdAKjo5dZ7TXfss/t1m3KS4Dohj1HacbhU8mMGeNniyeNoryEQnIkP3/Snr+axJuREdegmJigmNhKMrMdoSBfO+Ul1Lh6u53Z5j30F8Ojp5vdDAymc+MdOX/5ym0/2f4l7X0CGrlKq7cdOgmQg4wsN/vYdf9AOoetntH6E06X7Z2cj1+45HTDU5aXtDFqBmYQGD/LAlKCJy5ayz7XeO+fNfISjUYrsV+El8+tl8vLOau2cQGRTziZlwd6k9HpqYVVZTuOnuHGTutcvbx5XlranqAZKS/5SRZleTnTYgvEjJlhwXKz/9TcJ2stjOd6jXztwEvIAp1FrkdbQyeVhSZVNNWMm2VRys1gIGqtt3U4v3r7AT4X4SVXiP1FV6ji6PmLZH4VMieJCZ0gBYrafsThtOtVjbmr6PBvNTduLMXLXyYZC3kJ2WlKhQ3JIi/RaLQSG3nJ89Lc2hZ6adrzVvK8ZCWrFUGATr4oy8v0glz6DWhqQe7iddvpZM68r/r47Tx2BoBE5/qgvBw5jUz1ddHj1ljDZdBxLKgqh83Zy63z2JIzbmTJHYhZtObxVMnAyxMXXavJVJ1mkP34hctk4rAHDeozlsHhuHH90XvlxdYHT0JjjNZuB5rCgSTnZj+dl3NX2tA5tqLSUiuxf0mFvESj0X/kN42XrOSxF1bwYE6F5OkY2tOCzlxZXdVcyVI23BIf/PM+4rzCAB0L5UY4xTQVupJbfYhWIcxVwX3ZyXLPHNF5YlmuJSJBdXxiYV4aprnEWcgaecLHfx5v0mJpSvpKAoJ3AMLCJRY61chLNBqtxH4DefksXrJxd1hCnGz8HxnAM2+VjdSsk2gpIy/RaLQSG3nZrp/jK73nyPKmGXmJRqOV2MhLtMKMvESj0Ups5CVaYVZiXn7F8dLgIPnNEBqNfjP9avFyrRZclC4GP7GwHfq1sRLzsrJRVMv9QgiNRr+xfqV4CcaL0mtsJeYlGo1Gv2q8RL/GRl6i0WglNvISrTAjL9FotBIbeYlWmJGXaDRaiY28RCvMSsDLawkBuVXFsk1Ho9HoiHsJmeV50leNTlZtU31ZfZVsY9Cvt4FEwCPpT8OLqYN5mVdVEpIdK9t0NBqNvpkUIn3JUIh80u7INgb9ehtIBDyS/ii8mDqYl6CbySGyTUej0W+4S+sqbiQFSV8vFKKbScF0KnD0m2MgkfTn4IXV8bxMKckJzo6taMBPJxqNFruyUXQzObVZbqkAABFxSURBVLiuuUH6eqEQJRdnw9WTLuuIfu0N9AEGAYmkPwcvrI7nJaiptdkrJRTu6dBoNPpGUnBwVoz0ZULhupObKNs29OtnoA8wSPrf3xHqFF6iUCgUCvWaCXmJQqFQKJR8IS9RKBQKhZIv5CUKhUKhUPKFvEShUCgUSr6QlygUCoVCyRfyEoVCoVAo+UJeolAoFAolX8hLFAqFQqHkC3mJQqFQKJR8IS9RKBQKhZIv5CUKhUKhUPKFvEShUCgUSr6QlygUCoVCyRfyEoVCoVAo+epgXj58+KixuRWNRqPR6JduaUS9mDqYlygUCoVCvZZCXqJQKBQKJV/ISxQKhUKh5At5iUKhUCiUfCEvUSgUCoWSL+QlCoVCoVDyhbxEoVAoFEq+kJcoFAqFQskX8hKFQqFQKPlCXqJQKBQKJV+dwkvmm/ENjU0k8Mlo5jN16d1/UrX1DcO05t6JS5He0Z5EtXWQODAiVnqHRH/trZWVWygdywkyPnz4SDr2z2vdjiNQlHRse/p7X+23+miHRUTxMUM1Zk9dYvk4xR+LYYaduHBVOpYT00f3xDlX6dgOFfPjBIYZKIz5auiUXmozhDFPl5WtA9NTUzoWhUKhXlV1Ci9VfprY2NRstfvoO320W1pfdAa/puYWKDAyIV16R3uqb2yGxEF346V3SPQUXkJG6ajnksUWu2cp6nZIlGyyf/TTGT1rtVTkKyhZXjLvjGC+niCMQaFQqNdJncXL9/pqAyz5GOaHCcwPmnNMN3X/aaKorh5iug/UY/pP0pm94p99SbKTv1+GXMx/x340eAoEikpZPu88s00Qozd35fxllrD5z346wyYa/6A2q9tAPVJyN00oE3Yx/SZm3CuYyyXWnmWxaPkWvgToNXYboPeLrhHTVw/2Ul4yqpMgTY+xcyi0jJZvgQC8zjXdWFRSNnLK0kXLrd7rp80wv/DlgFZZ2UIy3TkrPoH2fzmOlPPteOa9ESTQZTwtqu/Y2RBYvMLaOyCczxgVlwKRs002vt1X561emvUNTRMMl9Fk9/KLaZqgsCgo9othBkYrSOP/1lsLNmcs2bD/8CmrvSdmLd1gaLy+6wDdHC49003N3tGdBHpqMj0mzDWz7D5w4u2gCIj516DJ9ufdyK73Rv6rn848M0so5+BJRxLzje67/XRmmWyE+waG+U3cOE4bbOygedMXr4NWsZWiNu7/+E5vLSgZAofOkgLJUffUhCaRf9aTvHyvn06X/nq05czX45guIyFgtGzjJ9y/aboxyaIzZwXTS+tt7oNhvf9U1wFkV5cxC2DXmGmmb/fVhkOAmN9dPFTI/3Qz8804+vFAoVCol67O4iX4bVVdYcyazbu3bLf7qL/u2OnmNGbrzgMQA4Hf3bwpL6FXCrsgTT/dJXze2roG2BUWnQzhazdvQ3jLDjubXQfhQlxZXcsw6kBQnxDxkGZ1TR0k8AuN5rODLrqR6y8NA28oLzdsP8T8ZyzTbTS/CwJ0PBb+Rk1ZAnu7qOrye6ng8j1gwnwI3PDyhV3QnZXlpZklYaowF9mrogaIomG618M/XDYZ9C9HzlhJw8BLoAsNk4p66QAj4ah37Ldve5KX63dzMUwv5gudtid5uffwaQjMNNuiNs20jau6pfU+2TVslhQv2eoapoc2FAtpTpwmcIXA5t3H2rg3DTBPYyoqq0n23trt9C+/0hCH2+NlN46O/sER9KileAmBpPRcGmD+O27b/pMQCI1MQF6iUKhXRJ3Fy7zicuj2zVtuw8estd6/ZosteK3NARqzxppsgu0dr1FeUlwB/5jBBnxpQl6edbpCMnK5wIUl5RDp4RdqwHVfzjheaZeX+49foB0X0Pv9dICXbEU1JCurEPei6C6+AUCCj/vrVorq5q7Zze+lgnjd2cvbSF/wLuwqrxRBH4j5iLCBYQbQxO3z8kt1ICsN073PwsvPfp5Cw8wX6tvtHCDQY9z8dVvtSIyAl6FRiSTAfM18TKoQ8tLzdiAETDfsGT55aZvgYHWNN0vxkvlu/L5j5yAAYNt7kNQFiZ1v+kOgi6oOz8tqUS1J3ENTmpdvP8nLbmoQ0J9POuJtHC//wt0uBIZF0jbI8rK4rIIGmO6jXa56QiAlMxd5iUKhXhF1Fi9pTxEoBZxoIz0G9Q9UdeHyzXyvce4ieUqFgc4TXHPfGwFdqPv3H4jHY3tpMT9O6DZQT1RLxmx5kcFb2MUMIRm/Gke7L5CSK1kbWMJ0J72i045X2uiYYS+t74bpC0t4Dxj8+Vjmm/HQJOAl1Eiq6zqK+UGTRwiJ+d8xDPNzH50lJPzRqD7qc6WQdvysM9mlQnql7w8iMBsyxYwm/vegSTRxcGQCiemull8oHmgFlVVUwnExH46C3jPzNaFau7wE+pKDfZt0WIGX/+V52UeXvGOfjv5q2LQX4eWvU5cB8qG134+YLs3LbyaQN/k/Y+At+iNeMr00Sfs/HtVdZjx2kI4ROep/kJZ/P34RCX+i1m3gxOfgpX94LMn+wcjPhk6lvGxqbqWJUSgU6mWpU3gZHZtw/8EDCBSVlEM4KoY8fZOWlRsTm5BXVMoni09Oj4lLrKlraJN8fwkBiGmSWeSTrRTFSMoBxSakxMQnlZRX0s3ktCzIlVtYQjcrqkjiuPgkuskL0sBrdEx8bT2pka0SxSWmkpjYBJogNfMehCO5WhKS0+OT0pLSsvi9vIDlUFROXhEfA+VA+rvR8XziZC5jQ0Mjn6aNG+aFjFAm3SwuY2ULb+PS0HhoaowgAX2v4MDTMrJhMyo67l4+aQMkY7kx0juRMZHRpPGQ/V4eGXOOjI4rLi2DQEpaZlwC6aDTcqDxTL+pDNNXUrZYsKu+sQmyZ2Xfa+PKKSgm2aNj4dDEb35MXFJuQQlUejdK+iHk2Phk/oigmUWlbHJKGo1JTE6L5t7YMraSxmRk5YoPMy6JBuAeS5gd3tLgO7G0U/7g4cN23ysUCoVSmDqFl88hnpeoTtUtv1CGGQb9VHi3W++TLzJfTTGfjGLe+g16uje8A6T3oVAo1MvQq8JLFAqFQqFeZSEvUSgUCoWSL+QlCoVCoVDyhbxEoVAoFEq+kJcoFAqFQskX8hKFQqFQKPlCXqJQKBQKJV+dxcvBk5dGx//hClyrt+yTjuo4NXJLiT1dfJpL7reyBTMPPLsG6i6SjuogPWpra25pkY59NtU1NLp7+UnHdo7MLPdKR7WnpmYy01Mbty7bA24WCxQKhVJGdRYv1aabjZu9QjpWonU2+6WjOk6/6ZOJ356u4dNMpKP+pIZNeTwjfMeqsan5yJlL0rHPJuDldW9/6djO0fItttJR7clqH5kLHoVCoZRdncLLRWt3Qq/C3Er6enrVy9/tps+5y+4zTDfB5qNHbUMnG4fejdNZsKaN63+s2nogMDwaNuOS0wPDo2aZby5lyaR3OgvXuF6/tXT9Li//UNgcMc0ESgiNjBs0iUCruKzC5bp38J0Y43U707Pzxs5YFh5F5k475OA0d6VNyB0ybZvNfntIb7ZpT3EZW1Rarj7DPCI6saJKdPn67RxuVjkoM+Ru7PjZFlWiGtgcbWhmZ3/+xDnngw5OfPtJ/AzzG7cCzrtcH85R+eHDhxab9wZFxIwyIKt/gAbpGYXcjVtlvZ9OVjfdZCNsbrMjq23wGjxxMZTsG3xnOLdmCAAS6g0Ii6SF+IdFbdx1JCzq8RKeotq6VTYHIEHmvYIT51y8/EJu3g6cbLwBds1Ytnn4NDO/kLtqXF6elwdPXgi9G3va6Wo915MuKCrZd/x3OMClG3bD5uTF6696+EAbzjlf52sBDZq42Ns/dNVWOzpp31UPXxo/Ye4qeF259QC8h8fOXnK84tEm4aVXQHhyOpmfr6Gx+Qw3M/AhB0c45FOObs0tZF7DZZb7wqMTohNS+f7l4MlL/UMj1207eMGNlDNC32SK8QYvv9Dfpsq/0UGhUKiXpU7hJb3u00lNhRrB4QFkyPHSzGp/633xAF1RSRlcT0fNsIBw6/3700wsabyd/YWGxibDZeLFLNWmkxL4ctS5pUKuefnTTSq+fwm8pLSgcr8VdMUzoK+OUZugf0l5GXQnJi6JzCULGjOTlMlfu6X6kRbWZK7zNklLth0g85KD8rl5cX1D7vIrd46ZYZ5fXOp0hayzIaUhk4xpQH0OWYpk4ZrtdDM1M6etvf4l8FJVT5zlp4nigPV+UjXwkm6GRcZ6BUQI+5degeGuN/32ckuO/CpAUVNzi+tNHxoGcvPxoIzsPBoYOpkcNb0nAMVwE+2CPP3DoMxhXGl/xEsuMgKS2R4nVfP9S56XhiYbaQz9P46Q/C8mLSK3TSgUCvVqqlN4uWnn4ciY+MiYhCXrdgjjRxsuo4E11uRS+73GPC+fIG9f4qpqEVxP1+w4AvH379+35pY/bOOAVC2qOe9KOiIgeqXmYUb7WCDoKv2kZ3TKiVyvhbykAdDo6WZ0Cvg+WgvbZHhptd8BgE1jKFposjZS4xO89PANpoHfuHgDU0u6+fDhI+hOnbrgeuOWPz0iTx+yMAh08maab1m/47A4P6dBEkrNMLeG1yEcnECV1aRr2y4v1+462kbemQea81bR8sFtAl4WlpTDe8XzUnfhGjqt/JptB9vIHczj8efC4rID9ueFhfA67+wubvxtMmur1d7j8OrI9QLbuFuHBu7+g3JUhpdNlJdTl2yoqycTzW/YRf6bUryE+4lN3JqaIM155HbhV8kdib7xehpAoVCoV1Adz8tTTmQlKaqBekYPHj7kN4dOEZNs3EyyZHQ5W7lc0l178ODhH/ESXsdwoK1vaJwwjwwMSvGytLyCbtKeCmVqm4CXzS0t6rNIr/GAw8W+2gSEIyXDp5SXTc3Nw6aZweZNv9DL7t5tf8xL2q3kAiR9dHwKRcjqbYdo/BTJRb+guLSiiqyvCdJesJoGqKR46RsUfuICWYlskgT/O54cvyW83El4CVKT3HPQeoGXZy5dg8CUJaTTxvNy15GzbWQRsSrKy+0HT9O+XT23ZArfpWMrqmiAapQh+b+0Cd7SBSu38r3M4fokV05eIf13UF7CP+7wKfI+W1jupbw8cJKsNV1UUk55efTMZZqd71+O4t46OCj6PkjxEm5rKqqkRyZQKBTqpavjefnOcEM+fC+v0PbEBcHOtiFTTOwcnEwk/c7CkrIfNRcuXLsTwjV19UYb9rRx47GrJPhZu50EgA1aC9ZuthVThBkyjQYGTiZX8NJy9uepJupzVlZzXz3m5hf11iEPr+48dJomA/mF3Bkx3Ry6bsz3ZB3HkvKKQZOXhEUlnHP1yLxX0EZ6XaU/TFjgdlP8jR1NRgKDp0rKIBLV1A6cZLz3+Hk+3nLviV7ai2IlI5ZV1TUDJhpPNbHMLyyuq28wXr/n2/Hzc7jVtXgxqpNoQG02wT/odmC4qp5xZo54ONTmwKl3hs+gYVB1Ta3xpsdPFOubWPbRNrpxi/RfgZe1dfXfayxISs1s45jkev0WBC5e84Y3ISE53Yh7b0GmlrZwgJ5+IRBuab2/aN2ukTMs+GZT1dTWaS9cB9jOLxIvjsYMmupy4zYN5xUU99dbDI1khpC1Rees2ErjL171hHegtr7x2FmCxotXvXprL0pISTfdRP6bANQemgt/NVwO/1/axYfaVfUWb9p7gq+CBujtVElp+Zi5ODCLQqFeOXU8L1GKFD8ei0KhUKhOFfJSuYW/aEShUCjFCHmJQqFQKJR8IS9RKBQKhZIv5CUKhUKhUPKFvEShUCgUSr6QlygUCoVCyRfyEoVCoVAo+UJeolAoFAolX8hLFAqFQqHkC3mJQqFQKJR8IS9RKBQKhZIv5CUKhUKhUPKFvEShUCgUSr6QlygUCoVCyRfyEoVCoVAo+UJeolAoFAolX8hLFAqFQqHkC3mJQqFQKJR8IS9RKBQKhZIv5CUKhUKhUPKFvEShUCgUSr6QlygUCoVCydf/A0fM8AMOuo7/AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,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>