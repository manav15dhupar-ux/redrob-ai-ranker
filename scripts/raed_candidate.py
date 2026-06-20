# import json

# with open("candidates.jsonl", "r") as f:
#     for i in range(10):   # First 10 candidates
#         candidate = json.loads(next(f))

#         print("\n" + "="*50)
#         print("Candidate:", candidate["candidate_id"])
#         print("Title:", candidate["profile"]["current_title"])
#         print("Experience:", candidate["profile"]["years_of_experience"])
#         print("Industry:", candidate["profile"]["current_industry"])





# import json

# keywords = [
#     "ai",
#     "machine learning",
#     "ml engineer",
#     "data scientist",
#     "nlp",
#     "search engineer",
#     "recommendation"
# ]
# count = 0

# with open("candidates.jsonl", "r") as f:
#     for line in f:
#         candidate = json.loads(line)

#         title = candidate["profile"]["current_title"].lower()

#         for word in keywords:
#             if word in title:
#                 print(
#                     candidate["candidate_id"],
#                     candidate["profile"]["current_title"],
#                     candidate["profile"]["years_of_experience"]
#                 )
#                 count += 1
#                 break
# print(count)





# import json

# count = 0

# with open("candidates.jsonl", "r") as f:
#     for line in f:
#         candidate = json.loads(line)

#         exp = candidate["profile"]["years_of_experience"]

#         if 5 <= exp <= 9:
#             count += 1

# print("Candidates in JD experience range:", count)




# import json

# keywords = [
#     "ai",
#     "machine learning",
#     "ml",
#     "data scientist",
#     "nlp",
#     "deep learning",
#     "search",
#     "recommendation"
# ]

# count = 0

# with open("candidates.jsonl", "r") as f:
#     for line in f:
#         candidate = json.loads(line)

#         exp = candidate["profile"]["years_of_experience"]

#         if not (5 <= exp <= 9):
#             continue

#         title = candidate["profile"]["current_title"].lower()

#         for word in keywords:
#             if word in title:
#                 count += 1
#                 break

# print("Potential AI candidates:", count)





# import json

# keywords = [
#     "ai",
#     "machine learning",
#     "ml",
#     "data scientist",
#     "nlp",
#     "search",
#     "recommendation"
# ]

# found = 0

# with open("candidates.jsonl", "r") as f:
#     for line in f:
#         candidate = json.loads(line)

#         exp = candidate["profile"]["years_of_experience"]

#         if not (5 <= exp <= 9):
#             continue

#         title = candidate["profile"]["current_title"].lower()

#         for word in keywords:
#             if word in title:
#                 print(
#                     candidate["candidate_id"],
#                     candidate["profile"]["current_title"],
#                     exp
#                 )

#                 found += 1

#                 if found == 20:
#                     break

#                 break

#         if found == 20:
#             break


# import json
# from pprint import pprint

# target_id = "CAND_0066999"

# with open("candidates.jsonl", "r") as f:
#     for line in f:
#         candidate = json.loads(line)

#         if candidate["candidate_id"] == target_id:
#             pprint(candidate)
#             break





# import json

# count = 0

# with open("candidates.jsonl") as f:
#     for line in f:
#         c = json.loads(line)

#         exp = c["profile"]["years_of_experience"]

#         if not (5 <= exp <= 9):
#             continue

#         title = c["profile"]["current_title"].lower()

#         if any(k in title for k in [
#             "ai",
#             "ml",
#             "machine learning",
#             "data scientist",
#             "recommendation",
#             "search",
#             "nlp"
#         ]):

#             signals = c["redrob_signals"]

#             if (
#                 signals["open_to_work_flag"]
#                 and signals["recruiter_response_rate"] >= 0.5
#             ):
#                 count += 1

# print(count)

# import json

# candidates = []

# with open("candidates.jsonl") as f:
#     for line in f:
#         c = json.loads(line)

#         exp = c["profile"]["years_of_experience"]

#         if not (5 <= exp <= 9):
#             continue

#         title = c["profile"]["current_title"].lower()

#         if not any(k in title for k in [
#             "ai",
#             "ml",
#             "machine learning",
#             "data scientist",
#             "recommendation",
#             "search",
#             "nlp"
#         ]):
#             continue

#         signals = c["redrob_signals"]

#         if not (
#             signals["open_to_work_flag"]
#             and signals["recruiter_response_rate"] >= 0.5
#         ):
#             continue

#         candidates.append(
#             (
#                 signals["github_activity_score"],
#                 c["candidate_id"],
#                 c["profile"]["current_title"]
#             )
#         )

# candidates.sort(reverse=True)

# for row in candidates[:20]:
#     print(row)