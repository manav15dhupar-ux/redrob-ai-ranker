import json

target_ids = [
    "CAND_0018499",
    "CAND_0066999",
    "CAND_0011687"
]

for line in open("../data/candidates.jsonl"):

    candidate = json.loads(line)

    if candidate["candidate_id"] in target_ids:

        print("\n" + "=" * 60)

        print(candidate["candidate_id"])

        print("TITLE:",
              candidate["profile"]["current_title"])

        print("EXPERIENCE:",
              candidate["profile"]["years_of_experience"])

        print("OPEN TO WORK:",
              candidate["redrob_signals"]["open_to_work_flag"])

        print("RESPONSE RATE:",
              candidate["redrob_signals"]["recruiter_response_rate"])

        print("NOTICE:",
              candidate["redrob_signals"]["notice_period_days"])

        print("GITHUB:",
              candidate["redrob_signals"]["github_activity_score"])

        print("\nSKILLS:")

        for skill in candidate["skills"]:
            print("-", skill["name"])