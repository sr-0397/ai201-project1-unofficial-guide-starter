# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
UGA dorms and dining hall review
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | https://housing.uga.edu/explore-options/?nav=ps| Russel| |
| 2 | https://housing.uga.edu/explore-options/?nav=ps| Creswell| |
| 3 | https://housing.uga.edu/explore-options/?nav=ps| Myers Community| |
| 4 | https://www.reddit.com/r/UGA/comments/1hd44d6/freshman_guide_to_dorms/| Freshman Housing Experience at UGA| |
| 5 | https://www.reddit.com/r/UGA/comments/1hd44d6/freshman_guide_to_dorms/|Choosing the Best UGA Dorm | |
| 6 | https://housing.uga.edu/explore-options/?nav=ps| | |
| 7 | https://dining.uga.edu/locations/| Bolton| |
| 8 | https://dining.uga.edu/locations/| Oglethorpe House Dining| |
| 9 | https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.reddit.com/r/UGA/comments/1eqk8yp/which_dining_halls_have_the_healthiest_options/&ved=2ahUKEwiN6vvltviUAxVMLtAFHZqjKXkQFnoECBsQAQ&usg=AOvVaw3OCSxSa64XoM7ioleVyXlg| UGA Dining Commons System| |
| 10 | https://dining.uga.edu/locations/| | |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** more than for the lab like 300-500?

**Overlap:** maybe 100

**Reasoning:**I think this is reddit posts with lots of content that require to understand the context bc it is a information based document.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

**Milestone 3 — Ingestion and chunking:**
Using claude to get the chunking code and test it.

**Milestone 4 — Embedding and retrieval:**
Will use claude for the embeding part to ask how to get the vector embedding and using chromadb as default.

**Milestone 5 — Generation and interface:**
Cluade and the lab to see how to do the generation part.
