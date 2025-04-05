from fastapi import FastAPI
import csv
from recommend import recommend_assessments

app = FastAPI()

# Load CSV manually
df = []
with open("shl_assessments.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Duration (min)"] = int(row["Duration (min)"])  # Convert duration to int
        df.append(row)

@app.get("/recommend")
async def get_recommendations(query: str):
    recommendations = recommend_assessments(query, df)
    return {"query": query, "recommendations": recommendations}
