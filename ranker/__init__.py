"""Redrob AI Ranker: transparent, rule-based candidate scoring."""
from .scoring import score_candidate, rank_candidates, ScoreResult

__all__ = ["score_candidate", "rank_candidates", "ScoreResult"]
