Evolution of Ranking System (V1 → V9)

V1 – Basic Filtering

The initial version focused on simple candidate filtering.

Criteria:

* Years of experience between 5 and 9 years
* AI/ML related titles
* Basic candidate ranking

Limitations:

* No recruiter signals
* No skill matching
* No ranking differentiation

⸻

V2 – Improved Title Matching

Added title-based scoring.

High priority roles:

* Recommendation Systems Engineer
* Search Engineer
* Applied ML Engineer
* Senior AI Engineer

Medium priority roles:

* ML Engineer
* Machine Learning Engineer
* NLP Engineer

Benefits:

* Better alignment with the job description
* Reduced irrelevant candidates

⸻

V3 – JD Skill Matching

Added matching against required job skills.

Examples:

* Embeddings
* Pinecone
* Qdrant
* Weaviate
* OpenSearch
* FAISS

Benefits:

* Improved technical relevance
* Higher quality recommendations

⸻

V4 – Skill Match Analysis

Added skill match counting.

Enhancements:

* Number of matching skills displayed
* Easier candidate inspection
* Better explainability

Benefits:

* Transparent ranking decisions
* Easier manual verification

⸻

V5 – Recruiter Signal Integration

Added Redrob behavioral signals.

Signals:

* GitHub Activity Score
* Recruiter Response Rate
* Notice Period
* Open To Work

Benefits:

* Ranking based on real-world hiring readiness
* Better candidate prioritization

⸻

V6 – Retrieval-Focused Ranking

Expanded retrieval-specific skill coverage.

Added:

* Information Retrieval
* Learning to Rank
* RAG
* PEFT
* LoRA
* QLoRA

Benefits:

* Better alignment with retrieval and recommendation systems roles
* Stronger relevance to job requirements

⸻

V7 – Multi-Factor Ranking

Introduced additional ranking dimensions.

Added:

* Interview Completion Rate
* Saved by Recruiters
* Profile Completeness

Benefits:

* Better hiring likelihood estimation
* More balanced ranking

⸻

V8 – Candidate Validation

Focused on manual verification.

Activities:

* Inspected top-ranked candidates
* Reviewed skills manually
* Checked recruiter signals
* Verified experience levels

Findings:

* Top candidates possessed realistic skill sets
* No obvious honeypot candidates detected

⸻

V9 – Final Production Ranker

Final ranking system combining all previous improvements.

Components:

* Experience Score
* Title Score
* Industry Score
* GitHub Activity
* Recruiter Response Rate
* Notice Period
* Open To Work Status
* Interview Completion Rate
* Recruiter Saves
* Profile Completeness
* Skill Match Count
* Retrieval Bonus
* Critical Skill Bonus
* Skill Proficiency
* Skill Duration

Outcome:

* Most robust ranking system developed during the hackathon
* Strong alignment with retrieval and recommendation engineering requirements
* Improved explainability and reproducibility