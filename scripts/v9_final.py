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
    # COMPANY SCORE
    # =====================

    industry = candidate["profile"].get(
        "current_industry",
        ""
    ).lower()

    if any(
        x in industry
        for x in [
            "software",
            "internet",
            "e-commerce",
            "consumer internet",
            "saas"
        ]
    ):
        score += 10

    elif any(
        x in industry
        for x in [
            "it services",
            "consulting"
        ]
    ):
        score -= 5

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

    if notice <= 15:
        score += 20

    elif notice <= 30:
        score += 15

    elif notice <= 60:
        score += 10

    elif notice <= 90:
        score += 5

    else:
        score -= 10

    # =====================
    # OPEN TO WORK SCORE
    # =====================

    if candidate["redrob_signals"]["open_to_work_flag"]:
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
    # JD SKILLS
    # =====================

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
        "Recommendation Systems",
        "Information Retrieval",
        "Learning to Rank",
        "RAG",
        "PEFT",
        "LoRA",
        "QLoRA"
    ]

    skill_matches = 0

    skills = candidate["skills"]

    skill_names = []

    for skill in skills:

        skill_names.append(skill["name"])

        if skill["name"] in jd_skills:

            skill_matches += 1

            # Skill exists
            score += 5

            # Proficiency score
            proficiency = skill.get("proficiency", "")

            if proficiency == "expert":
                score += 5

            elif proficiency == "advanced":
                score += 4

            elif proficiency == "intermediate":
                score += 2

            elif proficiency == "beginner":
                score += 1

            # Duration score
            duration = skill.get("duration_months", 0)

            if duration >= 36:
                score += 5

            elif duration >= 24:
                score += 4

            elif duration >= 12:
                score += 2

            elif duration >= 6:
                score += 1

    # =====================
    # RETRIEVAL BONUS
    # =====================

    retrieval_skills = [
        "Embeddings",
        "Information Retrieval",
        "Learning to Rank",
        "Recommendation Systems",
        "Semantic Search",
        "BM25"
    ]

    retrieval_count = 0

    for skill in retrieval_skills:

        if skill in skill_names:
            retrieval_count += 1

    score += retrieval_count * 3

    # =====================
    # CRITICAL SKILLS BONUS
    # =====================

    critical_skills = [
        "Embeddings",
        "Information Retrieval",
        "Learning to Rank",
        "Recommendation Systems"
    ]

    for skill in critical_skills:

        if skill in skill_names:
            score += 5

    # =====================
    # SAVE RESULT
    # =====================

    scores.append(
    (
        score,
        candidate["candidate_id"],
        title,
        exp,
        skill_matches,
        github,
        response,
        notice
    )
)

# =====================
# SORT RESULTS
# =====================

scores.sort(
    key=lambda x: (
        x[0],   # score
        x[5],   # github
        x[6]    # response rate
    ),
    reverse=True
)

# =====================
# PRINT TOP 10
# =====================

print("TOP 100 CANDIDATES")
print("-" * 80)

for row in scores[:100]:

    print(
        row[1],
        "|",
        row[2],
        "| Exp:",
        row[3],
        "| Score:",
        row[0],
        "| Skill Matches:",
        row[4],
        "| GitHub:",
        row[5],
        "| Response:",
        row[6],
        "| Notice:",
        row[7]
    ) 