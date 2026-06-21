import json

target_ids = [
    "CAND_0071974",
    "CAND_0018499",
    "CAND_0077337",
    "CAND_0027691",
    "CAND_0007009",
    "CAND_0002025",
    "CAND_0052328",
    "CAND_0079387",
    "CAND_0066999",
    "CAND_0041669"
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