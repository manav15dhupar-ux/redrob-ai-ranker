"""
Scoring rules for the Senior AI Engineer (retrieval / recommendation systems) role.

Every rule is data, so the weights are readable in one place and every score
can be explained as a per-component breakdown. This module reproduces the
scoring of the original submitted script (scripts/generate_submission.py as
submitted) exactly; tests/test_scoring.py pins that behaviour.

This is a hand-weighted, interpretable baseline. It is NOT a trained model.
"""

from dataclasses import dataclass, field

# (substring of lowercased title, points). First match wins, so order matters.
TITLE_POINTS = [
    ("recommendation systems engineer", 25),
    ("search engineer", 25),
    ("applied ml engineer", 25),
    ("senior ai engineer", 25),
    ("ml engineer", 20),
    ("machine learning engineer", 20),
    ("nlp engineer", 20),
    ("senior software engineer (ml)", 20),
    ("data scientist", 15),
    ("ai specialist", 15),
    ("ai research engineer", 10),
]
TITLE_DEFAULT = 5

# (minimum value, points), checked from the highest threshold down.
GITHUB_TIERS = [(80, 20), (60, 15), (40, 10), (20, 5)]
RESPONSE_TIERS = [(0.8, 20), (0.6, 15), (0.4, 10), (0.2, 5)]
INTERVIEW_TIERS = [(0.8, 10), (0.6, 5)]
SAVED_TIERS = [(20, 10), (10, 5)]
# notice period: lower is better -> (maximum days, points); beyond the last = penalty
NOTICE_TIERS = [(15, 20), (30, 15), (60, 10), (90, 5)]
NOTICE_PENALTY = -10

GOOD_INDUSTRIES = ("software", "internet", "e-commerce", "consumer internet", "saas")
BAD_INDUSTRIES = ("it services", "consulting")

JD_SKILLS = [
    "Embeddings", "Sentence Transformers", "OpenSearch", "BM25", "Qdrant", "Pinecone",
    "Weaviate", "FAISS", "Semantic Search", "Recommendation Systems",
    "Information Retrieval", "Learning to Rank", "RAG", "PEFT", "LoRA", "QLoRA",
]
RETRIEVAL_SKILLS = [
    "Embeddings", "Information Retrieval", "Learning to Rank",
    "Recommendation Systems", "Semantic Search", "BM25",
]
CRITICAL_SKILLS = ["Embeddings", "Information Retrieval", "Learning to Rank", "Recommendation Systems"]

PROFICIENCY_POINTS = {"expert": 5, "advanced": 4, "intermediate": 2, "beginner": 1}
DURATION_TIERS = [(36, 5), (24, 4), (12, 2), (6, 1)]  # (minimum months, points)
SKILL_MATCH_POINTS = 5
RETRIEVAL_BONUS_EACH = 3
CRITICAL_BONUS_EACH = 5
OPEN_TO_WORK_POINTS = 10
PROFILE_COMPLETE_MIN, PROFILE_COMPLETE_POINTS = 90, 5


@dataclass
class ScoreResult:
    candidate_id: str
    total: int
    breakdown: dict = field(default_factory=dict)  # component name -> points
    title: str = ""
    years_experience: float = 0.0
    skill_matches: int = 0
    github: float = 0
    response_rate: float = 0
    notice_days: int = 0

    def reasoning(self) -> str:
        """The one-line explanation written to the submission CSV."""
        return (
            f"{self.title} with {self.years_experience:.1f} years experience, "
            f"{self.skill_matches} JD skill matches, "
            f"GitHub activity score {self.github}, "
            f"recruiter response rate {self.response_rate}, "
            f"and {self.notice_days} day notice period."
        )


def _tier(value, tiers, default=0):
    """Points for the first (threshold, points) tier that value meets or exceeds."""
    for threshold, points in tiers:
        if value >= threshold:
            return points
    return default


def _experience(years):
    if 6 <= years <= 8:
        return 20
    if 5 <= years <= 9:
        return 15
    return 0


def _title(title_lower):
    for needle, points in TITLE_POINTS:
        if needle in title_lower:
            return points
    return TITLE_DEFAULT


def _industry(industry_lower):
    if any(x in industry_lower for x in GOOD_INDUSTRIES):
        return 10
    if any(x in industry_lower for x in BAD_INDUSTRIES):
        return -5
    return 0


def _notice(days):
    for maximum, points in NOTICE_TIERS:
        if days <= maximum:
            return points
    return NOTICE_PENALTY


def score_candidate(candidate: dict) -> ScoreResult:
    """Score one candidate record (the challenge's JSON schema) with a full breakdown."""
    profile = candidate["profile"]
    signals = candidate["redrob_signals"]
    title = profile["current_title"]
    years = profile["years_of_experience"]

    b = {
        "experience": _experience(years),
        "title": _title(title.lower()),
        "industry": _industry(profile.get("current_industry", "").lower()),
        "github": _tier(signals["github_activity_score"], GITHUB_TIERS),
        "recruiter_response": _tier(signals["recruiter_response_rate"], RESPONSE_TIERS),
        "notice_period": _notice(signals["notice_period_days"]),
        "open_to_work": OPEN_TO_WORK_POINTS if signals["open_to_work_flag"] else 0,
        "interview_completion": _tier(signals["interview_completion_rate"], INTERVIEW_TIERS),
        "saved_by_recruiters": _tier(signals["saved_by_recruiters_30d"], SAVED_TIERS),
        "profile_completeness": (
            PROFILE_COMPLETE_POINTS if signals["profile_completeness_score"] >= PROFILE_COMPLETE_MIN else 0
        ),
    }

    skill_points, matches, names = 0, 0, []
    for skill in candidate["skills"]:
        names.append(skill["name"])
        if skill["name"] in JD_SKILLS:
            matches += 1
            skill_points += SKILL_MATCH_POINTS
            skill_points += PROFICIENCY_POINTS.get(skill.get("proficiency", ""), 0)
            skill_points += _tier(skill.get("duration_months", 0), DURATION_TIERS)
    b["jd_skills"] = skill_points
    b["retrieval_bonus"] = sum(1 for s in RETRIEVAL_SKILLS if s in names) * RETRIEVAL_BONUS_EACH
    b["critical_skill_bonus"] = sum(CRITICAL_BONUS_EACH for s in CRITICAL_SKILLS if s in names)

    return ScoreResult(
        candidate_id=candidate["candidate_id"],
        total=sum(b.values()),
        breakdown=b,
        title=title,
        years_experience=years,
        skill_matches=matches,
        github=signals["github_activity_score"],
        response_rate=signals["recruiter_response_rate"],
        notice_days=signals["notice_period_days"],
    )


def rank_candidates(candidates, top_n=100):
    """Top-N by score (descending), ties broken by candidate_id ascending, as the challenge requires."""
    scored = [score_candidate(c) for c in candidates]
    scored.sort(key=lambda r: (-r.total, r.candidate_id))
    return scored[:top_n]
