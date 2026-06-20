import json

count = 0

for line in open("candidates.jsonl"):
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

    skills = [s["name"] for s in c["skills"]]

    has_embeddings = "Embeddings" in skills

    has_vector_db = any(
        x in skills
        for x in ["Qdrant", "Pinecone", "Weaviate"]
    )

    if has_embeddings and has_vector_db:
        count += 1

print(count)