import pandas as pd
from typing import List, Dict
import re  # Ensure this line is present

def parse_query(query: str) -> Dict:
    skills = []
    duration = None
    
    if "Java" in query:
        skills.append("Java")
    if "Python" in query:
        skills.append("Python")
    if "SQL" in query:
        skills.append("SQL")
    if "collaborate" in query or "team" in query:
        skills.append("Collaboration")
    if "cognitive" in query:
        skills.append("Cognitive")
    if "personality" in query:
        skills.append("Personality")
    
    duration_match = re.search(r"(\d+)\s*(minutes|mins)", query)
    if duration_match:
        duration = int(duration_match.group(1))
    
    return {"skills": skills, "duration": duration}

def recommend_assessments(query: str, df: pd.DataFrame) -> List[Dict]:
    parsed = parse_query(query)
    skills = parsed["skills"]
    max_duration = parsed["duration"]

    filtered_df = df.copy()
    if skills:
        filtered_df = filtered_df[filtered_df["Test Type"].str.contains("|".join(skills), case=False, na=False)]
    if max_duration:
        filtered_df = filtered_df[filtered_df["Duration (min)"] <= max_duration]
    
    filtered_df["Relevance"] = filtered_df["Test Type"].apply(
        lambda x: sum(skill.lower() in x.lower() for skill in skills)
    )
    ranked_df = filtered_df.sort_values(by="Relevance", ascending=False).head(10)
    
    result = ranked_df[["Assessment Name", "URL", "Remote Testing", "Adaptive/IRT", "Duration (min)", "Test Type"]].to_dict(orient="records")
    return result if result else [df.iloc[0].to_dict()]  # Min 1 recommendation

if __name__ == "__main__":
    df = pd.read_csv("shl_assessments.csv")
    query = "Java developers who can collaborate, 40 minutes"
    recommendations = recommend_assessments(query, df)
    print(recommendations)
