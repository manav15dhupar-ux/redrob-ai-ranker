Findings and Insights

Overview

During development, multiple ranking iterations were explored to improve candidate selection quality.

The final version (V9) was created after analyzing candidate profiles, recruiter signals, skill distributions, and ranking behavior across earlier versions.

⸻

Key Findings

1. Skill Match Alone Is Not Enough

Early ranking versions heavily rewarded skill matches.

Observation:

Candidates with many matching skills were not always the strongest candidates overall.

Some profiles contained relevant keywords but lacked strong recruiter engagement or hiring-readiness indicators.

Conclusion:

Skill matching should be combined with behavioral and hiring signals.

⸻

2. Recruiter Signals Are Strong Indicators

Several recruiter-related signals consistently appeared among high-quality candidates.

Important signals included:

* Recruiter response rate
* Interview completion rate
* Saved by recruiters count
* Open-to-work status

Candidates performing well on these metrics were generally stronger ranking candidates.

Conclusion:

Behavioral signals provide valuable hiring insights beyond technical skills.

⸻

3. GitHub Activity Improves Candidate Quality

Candidates with strong GitHub activity often demonstrated:

* Better technical engagement
* Stronger engineering backgrounds
* Greater evidence of hands-on work

Conclusion:

GitHub activity provides an additional quality signal beyond resumes and profiles.

⸻

4. Retrieval Skills Are Highly Predictive

The target role focuses heavily on retrieval and recommendation systems.

The strongest candidates frequently possessed:

* Embeddings
* Information Retrieval
* Learning to Rank
* Recommendation Systems
* Semantic Search
* BM25

Conclusion:

Retrieval-specific expertise should receive additional weighting.

⸻

5. Experience Alignment Matters

Candidates closest to the desired experience range consistently performed better.

Target range:

6–8 years

Observation:

Very junior candidates lacked required experience.

Very senior candidates were sometimes less aligned with the role requirements.

Conclusion:

Experience alignment improves ranking precision.

⸻

6. Current Job Title Provides Strong Context

Candidates already working in relevant AI engineering roles consistently ranked higher.

Examples:

* Recommendation Systems Engineer
* Search Engineer
* Senior AI Engineer
* Applied ML Engineer
* Machine Learning Engineer

Conclusion:

Current title serves as a strong proxy for domain expertise.

⸻

Evolution of Ranking System

V1

Basic scoring:

* Experience
* Job title

Limitation:

Insufficient differentiation between candidates.

⸻

V2–V4

Added:

* Industry relevance
* Recruiter signals
* Notice period

Result:

Improved ranking stability.

⸻

V5–V7

Added:

* Skill matching
* Proficiency scoring
* Duration scoring

Result:

Better identification of technically relevant candidates.

⸻

V8

Added:

* Notice period refinements
* Hiring readiness improvements

Result:

Improved recruitment practicality.

⸻

V9

Added:

* Retrieval expertise bonus
* Critical skill bonus
* Improved final ranking logic
* Official tie-break compliance

Result:

Most balanced ranking system developed during the project.

⸻

Final Observations

The highest-ranked candidates typically shared the following characteristics:

* Relevant AI engineering titles
* Strong retrieval-system expertise
* High GitHub activity
* Strong recruiter engagement
* Good interview completion rates
* Appropriate experience levels
* Shorter notice periods

These patterns closely aligned with the target role requirements.

⸻

Future Improvements

Potential future enhancements include:

* Embedding-based semantic skill matching
* Learning-to-rank models
* Automated feature importance analysis
* Explainable AI ranking reports
* Hybrid rule-based and ML-based ranking systems

These improvements could further increase ranking accuracy and scalability.