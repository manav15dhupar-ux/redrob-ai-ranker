import json

title_count = {}

with open("candidates.jsonl") as f:
    for line in f:
        c = json.loads(line)

        exp = c["profile"]["years_of_experience"]

        if not (5 <= exp <= 9):
            continue

        title = c["profile"]["current_title"]

        if any(k in title.lower() for k in [
            "ai",
            "ml",
            "machine learning",
            "data scientist",
            "recommendation",
            "search",
            "nlp"
        ]):

            signals = c["redrob_signals"]

            if (
                signals["open_to_work_flag"]
                and signals["recruiter_response_rate"] >= 0.5
            ):

                if title not in title_count:
                    title_count[title] = 1
                else:
                    title_count[title] += 1

for title, count in sorted(title_count.items(),
                           key=lambda x: x[1],
                           reverse=True):
    print(title, ":", count)