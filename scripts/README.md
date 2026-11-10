# scripts/

| Script | Purpose |
|---|---|
| `generate_submission.py` | **The one to run.** Scores every candidate with `ranker/scoring.py` and writes the Top-100 CSV. |
| `validate_submission.py` | Checks the CSV against the challenge format rules (header, 100 rows, ID pattern, ranks). |
| `rank_v1.py` … `rank_v6.py`, `v7_skill_quality.py`, `v8_notice_penalty.py`, `v9_career_fit.py`, `v9_final.py` | **History.** Earlier iterations of the ranker, kept to show how it evolved (see `docs/evolution_v1_v9.md`). Not needed to reproduce the result. |
| `inspect_*.py`, `top10_candidates.py`, `score_one_candidate.py`, `*_count.py`, `embedding_*.py`, `raed_candidate.py` | One-off exploration helpers used while analysing the candidate pool. |

The history scripts read `../data/candidates.jsonl` relative to the **current directory**, so run them from inside `scripts/`.
