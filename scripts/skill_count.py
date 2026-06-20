import json

skill_count = {}

with open("candidates.jsonl") as f:
    for line in f:
        c = json.loads(line)

        exp = c["profile"]["years_of_experience"]

        if not (5 <= exp <= 9):
            continue

        title = c["profile"]["current_title"].lower()

        if not any(k in title for k in [
            "ai",
            "ml",
            "machine learning",
            "data scientist",
            "recommendation",
            "search",
            "nlp"
        ]):
            continue

        signals = c["redrob_signals"]

        if not (
            signals["open_to_work_flag"]
            and signals["recruiter_response_rate"] >= 0.5
        ):
            continue

        for skill in c["skills"]:
            name = skill["name"]

            if name not in skill_count:
                skill_count[name] = 1
            else:
                skill_count[name] += 1

sorted_skills = sorted(
    skill_count.items(),
    key=lambda x: x[1],
    reverse=True
)

for skill, count in sorted_skills[:30]:
    print(skill, ":", count)