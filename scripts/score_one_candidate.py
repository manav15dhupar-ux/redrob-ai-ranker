import json
FILE_PATH = "../data/candidates.jsonl"


def title_score(title):

    title = title.lower()

    if "recommendation systems engineer" in title:
        return 25
    elif "search engineer" in title:
        return 25
    elif "applied ml engineer" in title:
        return 25
    elif "senior ai engineer" in title:
        return 25
    elif "ml engineer" in title:
        return 20
    elif "machine learning engineer" in title:
        return 20
    elif "nlp engineer" in title:
        return 20
    elif "senior software engineer (ml)" in title:
        return 20
    elif "data scientist" in title:
        return 15
    elif "ai specialist" in title:
        return 15
    elif "ai research engineer" in title:
        return 10

    return 5


def github_score(score):

    if score >= 80:
        return 20
    elif score >= 60:
        return 15
    elif score >= 40:
        return 10
    elif score >= 20:
        return 5

    return 0


def response_score(rate):

    if rate >= 0.8:
        return 20
    elif rate >= 0.6:
        return 15
    elif rate >= 0.4:
        return 10
    elif rate >= 0.2:
        return 5

    return 0


def notice_score(days):

    if days <= 30:
        return 15
    elif days <= 60:
        return 10
    elif days <= 90:
        return 5

    return 0


def experience_score(exp):

    if 6 <= exp <= 8:
        return 20
    elif 5 <= exp <= 9:
        return 15

    return 0


with open(FILE_PATH, "r") as f:

    candidate = json.loads(next(f))

title = candidate["profile"]["current_title"]
github = candidate["redrob_signals"]["github_activity_score"]
response = candidate["redrob_signals"]["recruiter_response_rate"]
notice = candidate["redrob_signals"]["notice_period_days"]
exp = candidate["profile"]["years_of_experience"]

total = (
    title_score(title)
    + github_score(github)
    + response_score(response)
    + notice_score(notice)
    + experience_score(exp)
)

print(candidate["candidate_id"])
print(title)
print("Score =", total)