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

**Model used:**
sentence-transformers/all-MiniLM-L6-v2; This is a lightweight transformer-based sentence embedding model that generates dense vector representations of text optimized for semantic similarity search.
**Top-k:**
2
*Production tradeoff reflection:**
Larger models (e.g., OpenAI text-embedding-3-large or higher-end transformer encoders) generally produce better semantic representations, especially for nuanced or ambiguous queries, but introduce higher inference latency and cost.

---

#	Question	Expected answer
1	Which UGA dorm is best for students who want a social freshman experience?	Russell Hall, Brumby Hall, and Creswell Hall are the best options for a social freshman experience because they are large freshman residence halls with strong community interaction and active social environments.
2	What food options does Bolton Dining Commons offer?	Bolton Dining Commons offers stations such as The Wok, Tanyard Grill, Taqueria, and Buon Appetito, along with a variety of buffet-style and allergen-friendly options.
3	Which dining halls are available at UGA and how do students use meal plans?	UGA dining halls include Bolton Dining Commons, Oglethorpe House Dining Commons, Snelling Dining Commons, and Village Summit. Students use meal plans, Paw Points, and other campus payment methods to access these dining locations.
4	What makes O-House popular among students?	O-House is popular due to its food quality, convenient layout, and comfortable atmosphere, as well as its accessibility for students on East Campus.
5	Which UGA dining hall is best for vegetarians?	UGA dining halls offer vegetarian-friendly options across multiple locations, including salads, international cuisine, and plant-based dishes; no single dining hall is definitively “best,” but all major dining commons (Bolton, O-House, Snelling) provide vegetarian options.
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
