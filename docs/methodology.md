Methodology

Objective

The objective of this project is to identify and rank the most suitable candidates for a Senior AI Engineer role focused on retrieval systems, recommendation systems, semantic search, and modern AI infrastructure.

The challenge requires selecting the Top 100 candidates from the provided candidate pool while maximizing relevance to the target job description.

⸻

Approach

A rule-based ranking framework was developed to evaluate candidates across multiple dimensions.

The system combines:

* Professional experience
* Current job role
* Industry relevance
* Technical skills
* Recruiter engagement signals
* Hiring readiness indicators

Each candidate receives a final score based on weighted contributions from these factors.

⸻

Feature Engineering

1. Experience Scoring

The target role requires approximately 6–8 years of experience.

Scoring priorities:

Experience Range	Score
6–8 years	        Highest
5–9 years	        Medium
Others	            Lower

This ensures candidates closely matching the hiring requirements receive priority.

⸻

2. Job Title Relevance

Current job titles provide a strong signal regarding candidate suitability.

Examples of highly weighted titles:

* Recommendation Systems Engineer
* Search Engineer
* Applied ML Engineer
* Senior AI Engineer
* Machine Learning Engineer
* NLP Engineer

Candidates already working in relevant domains are considered more likely to succeed in the target role.

⸻

3. Industry Relevance

Candidates from industries closely aligned with modern AI systems receive additional weighting.

Preferred industries:

* Software
* SaaS
* Internet
* Consumer Internet
* E-commerce

Lower weighting is assigned to consulting and generic IT service roles.

⸻

4. GitHub Activity

GitHub activity is used as an indicator of technical engagement and engineering contribution.

Higher GitHub scores receive higher ranking weights.

This helps identify candidates actively involved in development work.

⸻

5. Recruiter Signals

Several Redrob-provided behavioral signals are incorporated:

Recruiter Response Rate

Measures candidate responsiveness.

Open To Work

Indicates active job-seeking behavior.

Interview Completion Rate

Measures interview follow-through.

Saved By Recruiters

Acts as a market-demand signal.

Profile Completeness

Measures profile quality and completeness.

⸻

6. Skill Matching

The job description was analyzed and converted into a target skill set.

Target skills include:

* Embeddings
* Sentence Transformers
* OpenSearch
* BM25
* Qdrant
* Pinecone
* Weaviate
* FAISS
* Semantic Search
* Information Retrieval
* Recommendation Systems
* Learning To Rank
* RAG
* LoRA
* QLoRA
* PEFT

Candidates receive points for:

* Skill presence
* Proficiency level
* Skill duration

⸻

7. Retrieval Expertise Bonus

Retrieval-focused skills receive additional weighting.

Key retrieval skills:

* Embeddings
* Information Retrieval
* Learning to Rank
* Recommendation Systems
* Semantic Search
* BM25

This bonus aligns the ranking system with the role’s primary responsibilities.

⸻

8. Critical Skill Bonus

Certain skills are considered core requirements.

Additional bonuses are assigned to:

* Embeddings
* Information Retrieval
* Learning to Rank
* Recommendation Systems

These skills directly align with retrieval and recommendation system engineering.

⸻

Ranking Pipeline

1. Load candidate records.
2. Compute experience score.
3. Compute title relevance score.
4. Compute industry score.
5. Compute recruiter signal scores.
6. Compute GitHub score.
7. Compute skill-match score.
8. Apply retrieval bonus.
9. Apply critical skill bonus.
10. Generate final score.
11. Sort candidates by score.
12. Apply candidate_id tie-break rule.
13. Generate Top 100 submission.

⸻

Tie-Breaking Strategy

When multiple candidates have identical scores:

1. Higher score ranks first.
2. If scores are equal, candidate_id is sorted in ascending order.

This follows the official submission requirements.

⸻

Output

The final system produces:

* Top 100 candidates
* Final score
* Rank
* Human-readable reasoning

Output format:

candidate_id, rank, score, reasoning

The final CSV passes the official validation checks.