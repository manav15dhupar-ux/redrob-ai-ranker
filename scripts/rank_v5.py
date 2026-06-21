import json
FILE_PATH = "../data/candidates.jsonl"


scores = []

for line in open(FILE_PATH, "r"):

    candidate = json.loads(line)

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    score = 0

    # =====================
    # EXPERIENCE SCORE
    # =====================

    if 6 <= exp <= 8:
        score += 20

    elif 5 <= exp <= 9:
        score += 15

    # =====================
    # TITLE SCORE
    # =====================

    title_lower = title.lower()

    if "recommendation systems engineer" in title_lower:
        score += 25

    elif "search engineer" in title_lower:
        score += 25

    elif "applied ml engineer" in title_lower:
        score += 25

    elif "senior ai engineer" in title_lower:
        score += 25

    elif "ml engineer" in title_lower:
        score += 20

    elif "machine learning engineer" in title_lower:
        score += 20

    elif "nlp engineer" in title_lower:
        score += 20

    elif "senior software engineer (ml)" in title_lower:
        score += 20

    elif "data scientist" in title_lower:
        score += 15

    elif "ai specialist" in title_lower:
        score += 15

    elif "ai research engineer" in title_lower:
        score += 10

    else:
        score += 5

    # =====================
    # GITHUB SCORE
    # =====================

    github = candidate["redrob_signals"]["github_activity_score"]

    if github >= 80:
        score += 20

    elif github >= 60:
        score += 15

    elif github >= 40:
        score += 10

    elif github >= 20:
        score += 5

    # =====================
    # RESPONSE RATE SCORE
    # =====================

    response = candidate["redrob_signals"]["recruiter_response_rate"]

    if response >= 0.8:
        score += 20

    elif response >= 0.6:
        score += 15

    elif response >= 0.4:
        score += 10

    elif response >= 0.2:
        score += 5

    # =====================
    # NOTICE PERIOD SCORE
    # =====================

    notice = candidate["redrob_signals"]["notice_period_days"]

    if notice <= 30:
        score += 15

    elif notice <= 60:
        score += 10

    elif notice <= 90:
        score += 5

    # =====================
    # OPEN TO WORK SCORE
    # =====================

    open_to_work = candidate["redrob_signals"]["open_to_work_flag"]

    if open_to_work:
        score += 10

    # =====================
    # INTERVIEW COMPLETION SCORE
    # =====================

    interview_rate = candidate["redrob_signals"]["interview_completion_rate"]

    if interview_rate >= 0.8:
        score += 10

    elif interview_rate >= 0.6:
        score += 5

    # =====================
    # SAVED BY RECRUITERS SCORE
    # =====================

    saved = candidate["redrob_signals"]["saved_by_recruiters_30d"]

    if saved >= 20:
        score += 10

    elif saved >= 10:
        score += 5

    # =====================
    # PROFILE COMPLETENESS SCORE
    # =====================

    profile_score = candidate["redrob_signals"]["profile_completeness_score"]

    if profile_score >= 90:
        score += 5

    # =====================
    # JD SKILLS SCORE
    # =====================

    skills = [skill["name"] for skill in candidate["skills"]]

    jd_skills = [
        "Embeddings",
        "Sentence Transformers",
        "OpenSearch",
        "BM25",
        "Qdrant",
        "Pinecone",
        "Weaviate",
        "FAISS",
        "Semantic Search",
        "Recommendation Systems"
    ]

    skill_matches = 0

    for skill in jd_skills:
        if skill in skills:
            skill_matches += 1

    score += skill_matches * 5

    scores.append(
        (
            score,
            candidate["candidate_id"],
            title,
            skill_matches,
            github,
            response,
            notice
        )
        
    )

# =====================
# SORT RESULTS
# =====================

scores.sort(reverse=True)

print("TOP 10 CANDIDATES")
print("-" * 50)

for row in scores[:10]:

    print(
        row[1],
        "|",
        row[2],
        "| Score:",
        row[0],
        "| Skill Matches:",
        row[3],
        "| GitHub:",
        row[4],
        "| Response:",
        row[5],
        "| Notice:",
        row[6]
    )