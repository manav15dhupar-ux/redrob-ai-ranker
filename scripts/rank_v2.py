import json

scores = []

for line in open("candidates.jsonl", "r"):

    candidate = json.loads(line)

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    signals = candidate["redrob_signals"]

    github = signals["github_activity_score"]
    response = signals["recruiter_response_rate"]
    notice = signals["notice_period_days"]

    score = 0

    # Experience Score
    if 6 <= exp <= 8:
        score += 20
    elif 5 <= exp <= 9:
        score += 15

    # Title Score
    title_lower = title.lower()

    if "recommendation" in title_lower:
        score += 25

    elif "search" in title_lower:
        score += 25

    elif "applied ml" in title_lower:
        score += 25

    elif "senior ai engineer" in title_lower:
        score += 25

    elif "ml engineer" in title_lower:
        score += 20

    elif "machine learning" in title_lower:
        score += 20

    elif "nlp" in title_lower:
        score += 20

    elif "senior software engineer (ml)" in title_lower:
        score += 20

    elif "data scientist" in title_lower:
        score += 15

    elif "ai specialist" in title_lower:
        score += 15

    elif "ai research engineer" in title_lower:
        score += 10

    # GitHub Score
    if github >= 80:
        score += 20

    elif github >= 60:
        score += 15

    elif github >= 40:
        score += 10

    elif github >= 20:
        score += 5

    # Response Rate Score
    if response >= 0.8:
        score += 20

    elif response >= 0.6:
        score += 15

    elif response >= 0.4:
        score += 10

    elif response >= 0.2:
        score += 5

    # Notice Period Score
    if notice <= 30:
        score += 15

    elif notice <= 60:
        score += 10

    elif notice <= 90:
        score += 5

    scores.append(
        (
            score,
            candidate["candidate_id"],
            title
        )
    )

scores.sort(reverse=True)

print("TOP 10 CANDIDATES")
print("-" * 50)

for row in scores[:10]:
    print(row)