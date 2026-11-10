# Redrob AI Ranker

A transparent, rule-based system that ranks candidates for a **Senior AI Engineer** role (retrieval, recommendation and semantic-search focus) and explains every ranking decision. Built by Team **Straw Hat Luffy** for the Redrob AI Hiring Challenge.

**[▶ Live demo](https://redrob-ai-ranker-63refykqyydt9n98nvyco6.streamlit.app/)** — browse the Top 100, see scores and reasoning, download the CSV.
<!-- ![Streamlit app](docs/app.png)  ← add a screenshot -->

> **What this is and isn't.** The ranker is a hand-weighted, interpretable scoring baseline. It is **not** a trained machine-learning model. That is deliberate: a recruiter can read exactly why candidate A outranks candidate B. See [Limitations](#limitations).

## Result

Top 100 of the challenge pool, scores 305 (rank 1) down to 173 (rank 100). Every row carries a one-line, human-readable reason:

```
CAND_0071974,1,305,"Senior AI Engineer with 7.8 years experience, 11 JD skill matches, GitHub activity score 82.8, recruiter response rate 0.76, and 45 day notice period."
```

## How scoring works

Each candidate gets points from independent components (all weights live in [`ranker/scoring.py`](ranker/scoring.py)); the total is their sum.

| Component | Rule | Points |
|---|---|---|
| Experience | 6–8 yrs / 5–9 yrs | 20 / 15 |
| Current title | Recommendation Systems / Search / Applied ML / Senior AI Engineer | 25 |
| | ML / Machine Learning / NLP Engineer, Sr SWE (ML) | 20 |
| | Data Scientist, AI Specialist / AI Research Engineer / other | 15 / 10 / 5 |
| Industry | software, internet, e-commerce, SaaS / IT services, consulting | +10 / −5 |
| GitHub activity | ≥80 / ≥60 / ≥40 / ≥20 | 20 / 15 / 10 / 5 |
| Recruiter response rate | ≥0.8 / ≥0.6 / ≥0.4 / ≥0.2 | 20 / 15 / 10 / 5 |
| Notice period | ≤15 / ≤30 / ≤60 / ≤90 days / longer | 20 / 15 / 10 / 5 / −10 |
| Open to work | flag set | 10 |
| Interview completion | ≥0.8 / ≥0.6 | 10 / 5 |
| Saved by recruiters (30d) | ≥20 / ≥10 | 10 / 5 |
| Profile completeness | ≥90 | 5 |
| JD skills (16 listed) | per match: 5 + proficiency (expert 5 … beginner 1) + duration (≥36 mo 5 … ≥6 mo 1) | up to 15 each |
| Retrieval bonus | 3 per retrieval skill held (Embeddings, IR, Learning to Rank, RecSys, Semantic Search, BM25) | 3 each |
| Critical-skill bonus | Embeddings, Information Retrieval, Learning to Rank, Recommendation Systems | 5 each |

Ties are broken by `candidate_id` ascending, as the challenge requires.

### Why signals beyond skills

Early versions ranked mostly on skill keyword matches. Reviewing top results showed that keyword-heavy profiles weren't always the strongest, which led to adding recruiter-behaviour and hiring-readiness signals (see [`docs/findings.md`](docs/findings.md) and the version history in [`docs/evolution_v1_v9.md`](docs/evolution_v1_v9.md)).

## Run it

```bash
pip install -r requirements-dev.txt

# 1. Put the challenge's candidates.jsonl in data/  (not stored in git)
python scripts/generate_submission.py            # writes submission.csv
python scripts/validate_submission.py submission.csv

# 2. Tests
pytest tests -v

# 3. Demo app
pip install -r requirements.txt
streamlit run app.py
```

Use as a library:

```python
from ranker import score_candidate
result = score_candidate(candidate_dict)
result.total, result.breakdown   # the score and its per-component points
```

## Project structure

```
ranker/scoring.py          all scoring rules + score_candidate / rank_candidates
scripts/generate_submission.py   produce the Top-100 CSV
scripts/validate_submission.py   check the CSV against challenge rules
scripts/README.md          what every other script is (earlier versions, exploration helpers)
tests/test_scoring.py      hand-computed expected scores, tie-breaking, edge cases
app.py                     Streamlit demo of the final submission
docs/                      methodology, findings, V1→V9 evolution, challenge documents
submission.csv             the final Top-100
```

## Verification

The refactor into `ranker/` was checked against the originally submitted script: both produce byte-identical Top-100 CSVs on 600 randomly generated candidates built to hit every threshold boundary.

## Limitations

- **Weights are hand-tuned**, not learned. There is no labelled relevance data in this repo, so there is no quantitative quality metric (e.g. NDCG@k, precision@k). With labelled data the next step is to fit the weights and report those metrics.
- **GitHub activity is a proxy**, and a biased one: strong engineers with private or no public work are penalised. Notice period and "open to work" measure availability, not ability. A production system should reduce or audit these signals for fairness.
- Skill matching is exact-string on a fixed list; synonyms ("vector search", "dense retrieval") are not matched. Embedding-based matching would address this.
- Candidate-level data used here is the challenge's; do not publish real personal data in a public repo.

## Team

Team Straw Hat Luffy — Manav Dhupar (team lead).
