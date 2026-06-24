Redrob AI Ranker

AI-powered candidate ranking system developed by Team Straw Hat Luffy for the Redrob AI Hiring Challenge.

Overview

Redrob AI Ranker is a candidate ranking system designed to identify the most suitable candidates for a Senior AI Engineer role.

The solution evaluates candidates using a multi-factor scoring framework that combines:

* Experience relevance
* Current role relevance
* Industry fit
* GitHub activity
* Recruiter engagement signals
* Notice period
* Interview completion history
* Profile completeness
* Job-description skill matching
* Retrieval and recommendation-system expertise

The final output is a ranked list of the Top 100 candidates along with transparent reasoning for every ranking decision.

⸻

Problem Statement

The objective is to rank candidates for a Senior AI Engineer position specializing in:

* Retrieval Systems
* Recommendation Systems
* Semantic Search
* Information Retrieval
* Vector Databases
* RAG Pipelines
* Learning-to-Rank Systems

The system must identify candidates who demonstrate both technical expertise and strong hiring-readiness signals.

⸻

Ranking Methodology

The ranking pipeline evaluates candidates across multiple dimensions:

Experience Fit

Candidates with experience closest to the target range receive higher scores.

Title Relevance

Current roles closely aligned with the target position receive additional weight.

Examples:

* Recommendation Systems Engineer
* Search Engineer
* Applied ML Engineer
* Senior AI Engineer
* Machine Learning Engineer
* NLP Engineer

Industry Fit

Candidates from software, SaaS, internet, and e-commerce industries receive positive weighting.

Recruiter Signals

Behavioral hiring signals are incorporated, including:

* Recruiter response rate
* Interview completion rate
* Open-to-work status
* Saved by recruiters count
* Profile completeness

GitHub Activity

GitHub activity score is used as a proxy for engineering engagement and technical contribution.

Skill Matching

Skills are matched against the job requirements including:

* Embeddings
* Sentence Transformers
* BM25
* OpenSearch
* Pinecone
* Qdrant
* Weaviate
* FAISS
* Semantic Search
* Information Retrieval
* Recommendation Systems
* Learning to Rank
* RAG
* LoRA
* QLoRA
* PEFT

Retrieval Expertise Bonus

Additional bonuses are assigned to candidates demonstrating strong retrieval-system expertise.

Critical Skill Bonus

Higher weights are assigned to:

* Embeddings
* Information Retrieval
* Learning to Rank
* Recommendation Systems

⸻

Project Structure

redrob-ai-ranker/
├── data/
├── docs/
├── scripts/
├── submission_metadata.yaml
└── README.md

⸻

Output Format

The final output is generated in CSV format:

candidate_id,rank,score,reasoning

Each candidate receives:

* Rank
* Final score
* Human-readable reasoning

⸻

Reproducibility

Generate submission:

python scripts/generate_submission.py

Validate submission:

python scripts/validate_submission.py submission.csv

⸻

Live Demo

Streamlit Application:

https://redrob-ai-ranker-63refykqyydt9n98nvyco6.streamlit.app/

⸻

GitHub Repository

https://github.com/manav15dhupar-ux/redrob-ai-ranker

⸻

Technology Stack

* Python
* Streamlit
* JSONL
* CSV

⸻

Team

Team Name: Straw Hat Luffy

⸻

Submission Status

✅ Ranking Engine Complete

✅ Submission CSV Generated

✅ Submission Validator Passed

✅ Streamlit Demo Deployed

✅ Documentation Completed