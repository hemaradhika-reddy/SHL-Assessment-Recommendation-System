from recommend import recommend_assessments
import csv

# Load data
df = []
with open("shl_assessments.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Duration (min)"] = int(row["Duration (min)"])
        df.append(row)

# Test queries with ground truth
test_cases = [
    {"query": "Java developers who can collaborate, 40 minutes", "relevant": ["Java Coding", "Team Collaboration"]},
    {"query": "Python and SQL, 60 minutes", "relevant": ["Python Coding", "SQL Skills"]}
]

def recall_at_k(recommendations, relevant, k=3):
    top_k = [r["Assessment Name"] for r in recommendations[:k]]
    return len(set(top_k) & set(relevant)) / len(relevant)

def map_at_k(recommendations, relevant, k=3):
    score = 0
    relevant_found = 0
    for i, rec in enumerate(recommendations[:k], 1):
        if rec["Assessment Name"] in relevant:
            relevant_found += 1
            score += relevant_found / i
    return score / min(len(relevant), k)

# Evaluate
recall_scores = []
map_scores = []
for test in test_cases:
    recs = recommend_assessments(test["query"], df)
    recall = recall_at_k(recs, test["relevant"])
    map_score = map_at_k(recs, test["relevant"])
    recall_scores.append(recall)
    map_scores.append(map_score)
    print(f"Query: {test['query']}, Recall@3: {recall:.2f}, MAP@3: {map_score:.2f}")

print(f"Mean Recall@3: {sum(recall_scores)/len(recall_scores):.2f}")
print(f"Mean MAP@3: {sum(map_scores)/len(map_scores):.2f}")