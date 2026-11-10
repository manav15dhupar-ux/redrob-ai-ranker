import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ranker import rank_candidates, score_candidate  # noqa: E402


def make(cid="CAND_0000001", **over):
    c = {
        "candidate_id": cid,
        "profile": {"current_title": "Senior AI Engineer", "years_of_experience": 7, "current_industry": "SaaS"},
        "redrob_signals": {
            "github_activity_score": 85, "recruiter_response_rate": 0.9, "notice_period_days": 10,
            "open_to_work_flag": True, "interview_completion_rate": 0.9, "saved_by_recruiters_30d": 25,
            "profile_completeness_score": 95,
        },
        "skills": [
            {"name": "Embeddings", "proficiency": "expert", "duration_months": 40},
            {"name": "Python", "proficiency": "expert", "duration_months": 80},
        ],
    }
    for k, v in over.items():
        section, key = k.split("__")
        c[section][key] = v
    return c


def test_hand_computed_total_and_breakdown():
    r = score_candidate(make())
    # 25 title + 20 exp + 10 industry + 20 github + 20 response + 20 notice + 10 open
    # + 10 interview + 10 saved + 5 profile + 15 (Embeddings 5+5+5) + 3 retrieval + 5 critical
    assert r.total == 173
    assert sum(r.breakdown.values()) == r.total
    assert r.breakdown["jd_skills"] == 15 and r.skill_matches == 1


def test_notice_period_beyond_90_days_is_penalised():
    assert score_candidate(make(redrob_signals__notice_period_days=120)).breakdown["notice_period"] == -10


def test_title_first_match_wins():
    # "applied ml engineer" must score 25 (not the 20 of the shorter "ml engineer" rule)
    assert score_candidate(make(profile__current_title="Applied ML Engineer")).breakdown["title"] == 25
    assert score_candidate(make(profile__current_title="Marketing Manager")).breakdown["title"] == 5


def test_experience_bands():
    for years, pts in [(7, 20), (5, 15), (9, 15), (4.9, 0), (9.1, 0)]:
        assert score_candidate(make(profile__years_of_experience=years)).breakdown["experience"] == pts


def test_ranking_orders_by_score_then_candidate_id():
    a, b, c = make("CAND_0000003"), make("CAND_0000001"), make("CAND_0000002", redrob_signals__github_activity_score=0)
    ranked = rank_candidates([a, b, c], top_n=3)
    assert [r.candidate_id for r in ranked] == ["CAND_0000001", "CAND_0000003", "CAND_0000002"]


def test_reasoning_mentions_key_facts():
    text = score_candidate(make()).reasoning()
    assert "Senior AI Engineer" in text and "7.0 years" in text and "10 day notice" in text
