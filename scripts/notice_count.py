import json
FILE_PATH = "../data/candidates.jsonl"

notice_count = {}

with open(FILE_PATH) as f:
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

        notice = signals["notice_period_days"]

        if notice not in notice_count:
            notice_count[notice] = 1
        else:
            notice_count[notice] += 1

for notice, count in sorted(notice_count.items()):
    print(notice, "days :", count)