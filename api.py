from fastapi import FastAPI
import pandas as pd
from recommend import recommend_assessments

app = FastAPI()
df = pd.read_csv("shl_assessments.csv")

@app.get("/recommend")
async def get_recommendations(query: str):
    recommendations = recommend_assessments(query, df)
    return {"query": query, "recommendations": recommendations}