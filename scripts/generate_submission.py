"""
Generate the Top-100 submission CSV.

    python scripts/generate_submission.py                       # data/candidates.jsonl -> submission.csv
    python scripts/generate_submission.py --input path.jsonl --output out.csv

The candidate pool (data/candidates.jsonl) comes from the challenge and is not
committed to the repo (it is listed in .gitignore).
"""

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from ranker import rank_candidates  # noqa: E402


def read_jsonl(path):
    """Yield one candidate dict per non-empty line."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", default=str(ROOT / "data" / "candidates.jsonl"))
    parser.add_argument("--output", default="submission.csv")
    parser.add_argument("--top", type=int, default=100)
    args = parser.parse_args()

    if not Path(args.input).exists():
        sys.exit(f"Input not found: {args.input}\nPlace the challenge's candidates.jsonl in data/ (it is not stored in git).")

    top = rank_candidates(read_jsonl(args.input), top_n=args.top)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for rank, r in enumerate(top, start=1):
            writer.writerow([r.candidate_id, rank, r.total, r.reasoning()])
    print(f"Wrote {len(top)} rows to {args.output}")


if __name__ == "__main__":
    main()
