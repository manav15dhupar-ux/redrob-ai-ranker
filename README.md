# Redrob Hackathon 2026 – AI Candidate Ranking System

## Overview

This repository contains my solution for the Redrob Hackathon 2026.

The goal is to identify and rank the most relevant candidates for an AI Search & Recommendation Systems role using candidate profiles, skills, experience, and recruiter signals.

The ranking system evolved through multiple versions (V1 → V9), with each version improving candidate selection quality and ranking accuracy.

---

## Project Objective

Build an explainable candidate ranking system that:

- Identifies strong AI/ML candidates
- Rewards relevant Search and Recommendation experience
- Utilizes recruiter behavior signals
- Prioritizes retrieval-focused skills
- Produces a ranked candidate list with transparent scoring

---

## Dataset

Provided files:

- candidates.jsonl
- candidate_schema.json
- sample_candidates.json
- sample_submission.csv
- submission_template.yml
- submission_spec.md
- redrob_signals.md

---

## Ranking Features

### Experience Score

Candidates with experience closest to the job requirements receive higher scores.

### Title Score

Higher weight assigned to:

- Recommendation Systems Engineer
- Search Engineer
- AI Engineer
- NLP Engineer
- Machine Learning Engineer
- Applied ML Engineer

### Recruiter Signals

Used signals include:

- GitHub Activity Score
- Recruiter Response Rate
- Notice Period
- Open To Work Flag
- Interview Completion Rate
- Saved By Recruiters (30 Days)
- Profile Completeness Score

### Skill Matching

Core skills evaluated:

- Embeddings
- Sentence Transformers
- OpenSearch
- BM25
- Qdrant
- Pinecone
- Weaviate
- FAISS
- Semantic Search
- Recommendation Systems
- Information Retrieval
- Learning to Rank
- RAG
- PEFT
- LoRA
- QLoRA

### Retrieval Bonus

Additional weight assigned for:

- Embeddings
- Information Retrieval
- Learning to Rank
- Semantic Search
- BM25
- Recommendation Systems

### Critical Skill Bonus

Additional scoring for:

- Embeddings
- Information Retrieval
- Learning to Rank
- Recommendation Systems

---

## Evolution of the Ranking System

### V1
Basic filtering using experience and titles.

### V2
Improved title relevance matching.

### V3
Introduced recruiter signals.

### V4
Implemented weighted candidate scoring.

### V5
Added interview completion and recruiter engagement signals.

### V6
Expanded retrieval and recommendation skill coverage.

### V7
Introduced stronger ranking prioritization and tie-breaking.

### V8
Improved signal balancing and ranking stability.

### V9
Final retrieval-focused ranking strategy with advanced skill weighting.

Detailed evolution available in:

```text
docs/evolution_v1_v9.md
```

---

## Project Structure

```text
Redrob-Hackathon-2026/
│
├── data/
│   └── candidates.jsonl
│
├── scripts/
│   ├── v1.py
│   ├── v2.py
│   ├── v3.py
│   ├── v4.py
│   ├── v5.py
│   ├── v6.py
│   ├── v7.py
│   ├── v8.py
│   ├── v9.py
│   └── generate_submission.py
│
├── docs/
│   ├── methodology.md
│   ├── findings.md
│   └── evolution_v1_v9.md
│
├── submission.csv
├── submission_metadata.yaml
└── README.md
```

---

## Key Findings

- Retrieval-focused candidates consistently ranked highest.
- Strong recruiter signals improved candidate quality.
- Low notice period candidates received additional preference.
- GitHub activity acted as a useful quality indicator.
- Retrieval and recommendation skills were highly predictive of relevance.

Detailed findings available in:

```text
docs/findings.md
```

---

## Methodology

Detailed methodology available in:

```text
docs/methodology.md
```

---

## Reproducing Results

Run:

```bash
python scripts/v9.py
```

Generate submission:

```bash
python scripts/generate_submission.py
```

---

## Author

**Manav Dhupar**

B.Tech AI/ML Student

Redrob Hackathon 2026 Participant