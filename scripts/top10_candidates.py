import json

scores = []

for line in open("candidates.jsonl"):

    candidate = json.loads(line)

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    score = 0

    if 5 <= exp <= 9:
        score += 20

    title_lower = title.lower()

    if "ai" in title_lower:
        score += 20
    elif "ml" in title_lower:
        score += 20
    elif "machine learning" in title_lower:
        score += 20
    elif "recommendation" in title_lower:
        score += 20
    elif "search" in title_lower:
        score += 20
    elif "nlp" in title_lower:
        score += 20

    scores.append(
        (
            score,
            candidate["candidate_id"],
            title
        )
    )

scores.sort(reverse=True)

for row in scores[:10]:
    print(row)