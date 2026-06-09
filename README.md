# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- Uga dorms and dining, thee is ot a chat bot that finds this level of information. I used some reddit sites as well as uga official website. -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->


| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | https://housing.uga.edu/explore-options/?nav=ps| Russel| offical uga site|
| 2 | https://housing.uga.edu/explore-options/?nav=ps| Creswell|offical uga site |
| 3 | https://housing.uga.edu/explore-options/?nav=ps| Myers Community|offical uga site |
| 4 | https://www.reddit.com/r/UGA/comments/1hd44d6/freshman_guide_to_dorms/| Freshman Housing Experience at UGA| |
| 5 | https://www.reddit.com/r/UGA/comments/1hd44d6/freshman_guide_to_dorms/|Choosing the Best UGA Dorm | reddit|
| 6 | https://housing.uga.edu/explore-options/?nav=ps| | offical uga site|
| 7 | https://dining.uga.edu/locations/| Bolton| |
| 8 | https://dining.uga.edu/locations/| Oglethorpe House Dining|offical uga site |
| 9 | https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.reddit.com/r/UGA/comments/1eqk8yp/which_dining_halls_have_the_healthiest_options/&ved=2ahUKEwiN6vvltviUAxVMLtAFHZqjKXkQFnoECBsQAQ&usg=AOvVaw3OCSxSa64XoM7ioleVyXlg| UGA Dining Commons System| offical uga site|
| 10 | https://dining.uga.edu/locations/| Locations for dining|offical uga site |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
300 characters per chunk (controlled by chunk_size = 300). This size was chosen to keep each chunk small enough for precise embedding retrieval while still preserving enough context from the original documen

**Overlap:**
100 characters overlap between consecutive chunks (overlap = 50). This ensures that important information near chunk boundaries is not lost and improves retrieval quality when relevant text spans across two chunks.
**Why these choices fit your documents:**
The documents are plain .txt game-related texts, which typically contain short descriptive sections rather than long structured paragraphs. A 300-character chunk keeps semantic meaning focused and reduces noise in embeddings, while still being large enough to capture meaningful context like people's full opinions about the dorms in a long sentence with bullets or comma list.
**Final chunk count:**
400
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*



Evaluation Report

QUESTION 1 : Which UGA dorm is best for students who want a social freshman experience?
[Bestdorm] (dist: 0.321) Choosing the best dorm at the University of Georgia depends on a student's prior...
[Highrise] (dist: 0.373) r differences, all three halls provide a classic freshman living experience and ...
[Brumby] (dist: 0.374) leading to the building, many believe the social opportunities and facilities ou...
[Russel] (dist: 0.376) athrooms are shared by residents on each floor, but many students report that th...
[Freshmanhousing] (dist: 0.384) Housing plays a major role in the freshman experience at the University of Georg...

ANSWER: According to the context from the "Bestdorm" and "Freshmanhousing" documents, students seeking a highly social freshman experience often prefer Russell Hall, Brumby Hall, or Creswell Hall because these residence halls house large numbers of first-year students. Additionally, the "Russel" document mentions that Russell is considered one of the most desirable freshman dorms due to its location, renovated interior, and active student community. The "Brumby" document also notes that Brumby remains one of the most sought-after residence halls for freshmen who want a traditional and highly social college experience. Therefore, Russell Hall, Brumby Hall, or Creswell Hall would be a good choice for students who want a social freshman experience.
SOURCES: ['Bestdorm', 'Highrise', 'Brumby', 'Russel', 'Freshmanhousing']

RETRIEVED CHUNKS:
- Bestdorm (dist=0.3208) Choosing the best dorm at the University of Georgia depends on a student's priorities and lifestyle. Students seeking a highly social freshman experience often prefer Russell Hall,
- Highrise (dist=0.3733) r differences, all three halls provide a classic freshman living experience and offer opportunities to meet other students and become involved in campus life.
- Brumby (dist=0.3736) leading to the building, many believe the social opportunities and facilities outweigh the inconvenience. Brumby remains one of the most sought-after residence halls for freshmen w
- Russel (dist=0.3764) athrooms are shared by residents on each floor, but many students report that the facilities are cleaner and more private than those found in older residence halls. Russell is cons
- Freshmanhousing (dist=0.3840) Housing plays a major role in the freshman experience at the University of Georgia. Many first-year students live in traditional residence halls where they share rooms, bathrooms, 

QUESTION 2 : What food options does Bolton Dining Commons offer?
[Bolton] (dist: 0.226) include The Wok, Tanyard Grill, Taqueria, and Buon Appetito. Bolton is especiall...
[Bolton] (dist: 0.289) it a dependable option for students with varying schedules. Many students apprec...
[Bolton] (dist: 0.302) Bolton Dining Commons is one of the most popular dining locations at the Univers...
[Ugadininghalls] (dist: 0.404) es provide students with access to a wide range of meal options throughout the a...
[Ugadininghalls] (dist: 0.434) The University of Georgia operates multiple dining commons that serve students a...


ANSWER: Bolton Dining Commons offers a wide variety of food options, including The Wok, Tanyard Grill, Taqueria, and Buon Appetito, as well as allergen-friendly and gluten-friendly meal options through its Special Selections station. (Game: Bolton)
SOURCES: ['Bolton', 'Ugadininghalls']

RETRIEVED CHUNKS:
- Bolton (dist=0.2257) include The Wok, Tanyard Grill, Taqueria, and Buon Appetito. Bolton is especially convenient for residents of Russell, Brumby, and Creswell Halls because it is within a short walki
- Bolton (dist=0.2886) it a dependable option for students with varying schedules. Many students appreciate the large seating areas and the extensive variety of food available. Bolton also provides aller
- Bolton (dist=0.3016) Bolton Dining Commons is one of the most popular dining locations at the University of Georgia and is the largest dining commons on campus. Located near the freshman high-rise resi
- Ugadininghalls (dist=0.4043) es provide students with access to a wide range of meal options throughout the academic year. Dining commons typically offer buffet-style service and allow students to choose from 
- Ugadininghalls (dist=0.4337) The University of Georgia operates multiple dining commons that serve students across campus. Major dining locations include Bolton Dining Commons, Oglethorpe House Dining Commons,

QUESTION 3 : Which dining halls are available at UGA and how do students use meal plans?
[Ugadininghalls] (dist: 0.247) nce by locating dining halls near major residential communities. Dining commons ...
[Ugadininghalls] (dist: 0.276) sfaction, UGA continuously updates menus and dining offerings to meet student pr...
[Ugadininghalls] (dist: 0.344) lude salads, sandwiches, grilled foods, international cuisine, vegetarian dishes...
[Ohouse] (dist: 0.354) upperclassmen continue to visit it even after moving off campus. The dining comm...
[Ugadininghalls] (dist: 0.361) The University of Georgia operates multiple dining commons that serve students a...

ANSWER: According to the Ugadininghalls doc, the University of Georgia operates multiple dining commons, including Bolton Dining Commons, Oglethorpe House Dining Commons, Snelling Dining Commons, and Village Summit. 

Students can use meal plans, as well as Paw Points and other payment methods, at these dining facilities (Ugadininghalls doc).
SOURCES: ['Ugadininghalls', 'Ohouse']
RETRIEVED CHUNKS:
- Ugadininghalls (dist=0.2469) nce by locating dining halls near major residential communities. Dining commons are important gathering places where students study, socialize, and meet friends between classes. Be
- Ugadininghalls (dist=0.2765) sfaction, UGA continuously updates menus and dining offerings to meet student preferences. The dining system is widely regarded as one of the strengths of student life at the unive
- Ugadininghalls (dist=0.3439) lude salads, sandwiches, grilled foods, international cuisine, vegetarian dishes, desserts, and allergen-conscious selections. Students can use meal plans, Paw Points, and other pa
- Ohouse (dist=0.3540) upperclassmen continue to visit it even after moving off campus. The dining commons often experiences heavy traffic during lunch and dinner hours due to its popularity. Students ap
- Ugadininghalls (dist=0.3608) The University of Georgia operates multiple dining commons that serve students across campus. Major dining locations include Bolton Dining Commons, Oglethorpe House Dining Commons,

QUESTION 4 : What makes O-House popular among students?
[Ohouse] (dist: 0.317) , convenient layout, and comfortable atmosphere. The dining hall serves a variet...
[Ohouse] (dist: 0.331) ronment. Online student discussions frequently highlight positive experiences wi...
[Ohouse] (dist: 0.384) artments. O-House helps distribute dining traffic across campus and provides stu...
[Ohouse] (dist: 0.451) Oglethorpe House Dining Commons, commonly called "O-House" by students, is a pop...
[Freshmanhousing] (dist: 0.505) eriences vary, many students report that residence hall communities become an im...

ANSWER: According to the Ohouse doc, O-House is popular among students because of its "food quality, convenient layout, and comfortable atmosphere." (Game: Ohouse, Rule: Oglethorpe House Dining Commons...)
SOURCES: ['Ohouse', 'Freshmanhousing']
RETRIEVED CHUNKS:
- Ohouse (dist=0.3168) , convenient layout, and comfortable atmosphere. The dining hall serves a variety of meals throughout the day and attracts students from nearby residence halls and academic buildin
- Ohouse (dist=0.3315) ronment. Online student discussions frequently highlight positive experiences with O-House staff and dining operations. Because it is located on East Campus, it serves as an import
- Ohouse (dist=0.3841) artments. O-House helps distribute dining traffic across campus and provides students with another high-quality alternative to larger dining commons such as Bolton.
- Ohouse (dist=0.4513) Oglethorpe House Dining Commons, commonly called "O-House" by students, is a popular dining hall located on the east side of the University of Georgia campus. Many students conside
- Freshmanhousing (dist=0.5047) eriences vary, many students report that residence hall communities become an important part of their first year. Shared living environments help students develop communication ski

QUESTION 5 : Is Russell Hall close to dining and campus facilities?
[Russel] (dist: 0.271) ity areas. Students often choose Russell because it balances convenience and soc...
[Russel] (dist: 0.291) Russell Hall is one of the most popular freshman residence halls at the Universi...
[Russel] (dist: 0.334) athrooms are shared by residents on each floor, but many students report that th...
[Highrise] (dist: 0.392) Russell Hall, Brumby Hall, and Creswell Hall are collectively known as the fresh...
[Russel] (dist: 0.433) one thousand first-year students and is known for combining a strong social atmo...

ANSWER: Yes, Russell Hall is within walking distance of Bolton Dining Commons, Tate Student Center, the Miller Learning Center, and many academic buildings (Game: Russel Rule: ity areas...).
SOURCES: ['Russel', 'Highrise']
RETRIEVED CHUNKS:
- Russel (dist=0.2707) ity areas. Students often choose Russell because it balances convenience and social opportunities. The hall is within walking distance of Bolton Dining Commons, Tate Student Center
- Russel (dist=0.2912) Russell Hall is one of the most popular freshman residence halls at the University of Georgia. Located on Baxter Street, it is part of the group commonly known as the freshman high
- Russel (dist=0.3337) athrooms are shared by residents on each floor, but many students report that the facilities are cleaner and more private than those found in older residence halls. Russell is cons
- Highrise (dist=0.3919) Russell Hall, Brumby Hall, and Creswell Hall are collectively known as the freshman high-rises at the University of Georgia. These three residence halls house thousands of first-ye
- Russel (dist=0.4332) one thousand first-year students and is known for combining a strong social atmosphere with relatively modern facilities. The building underwent a major renovation and reopened in 




QUESTION: Which UGA dining hall is best for vegetarians?
[Ugadininghalls] (dist: 0.410) nce by locating dining halls near major residential communities. Dining commons ...
[Ugadininghalls] (dist: 0.448) lude salads, sandwiches, grilled foods, international cuisine, vegetarian dishes...
[Ugadininghalls] (dist: 0.478) sfaction, UGA continuously updates menus and dining offerings to meet student pr...
[Ohouse] (dist: 0.503) Oglethorpe House Dining Commons, commonly called "O-House" by students, is a pop...
[Bolton] (dist: 0.505) Bolton Dining Commons is one of the most popular dining locations at the Univers...
ANSWER: I couldn't find that information in the loaded Rag documents.
SOURCES: ['Ugadininghalls', 'Ohouse', 'Bolton']
RETRIEVED:
- Ugadininghalls (dist=0.4097) nce by locating dining halls near major residential communities. Dining commons are important gathering places where students study, socialize, and meet friends between classes. Because food quality a
- Ugadininghalls (dist=0.4479) lude salads, sandwiches, grilled foods, international cuisine, vegetarian dishes, desserts, and allergen-conscious selections. Students can use meal plans, Paw Points, and other payment methods at din
- Ugadininghalls (dist=0.4781) sfaction, UGA continuously updates menus and dining offerings to meet student preferences. The dining system is widely regarded as one of the strengths of student life at the university.
- Ohouse (dist=0.5029) Oglethorpe House Dining Commons, commonly called "O-House" by students, is a popular dining hall located on the east side of the University of Georgia campus. Many students consider O-House one of the
- Bolton (dist=0.5047) Bolton Dining Commons is one of the most popular dining locations at the University of Georgia and is the largest dining commons on campus. Located near the freshman high-rise residence halls, Bolton 