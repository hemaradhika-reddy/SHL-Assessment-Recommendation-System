import requests
from typing import List, Dict
import re


GEMINI_API_KEY = "AIzaSyCft1Q6g7wP5uOIM7FPaSt0mHAJYb18kkI"  
GEMINI_API_URL = "https://api.gemini.com/v1/completions"  # Placeholder; use actual endpoint

def parse_query(query: str) -> Dict:
    # Use LLM to extract skills and duration
    prompt = f"Extract skills and max duration (in minutes) from this query: '{query}'. Return as JSON: {{'skills': [], 'duration': null}}"
    response = requests.post(
        GEMINI_API_URL,
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
        json={"prompt": prompt, "max_tokens": 100}
    )
    result = response.json().get("choices", [{}])[0].get("text", "{}")
    parsed = eval(result)  # Convert string JSON to dict (use json.loads in production)
    
    # Fallback to regex if LLM fails
    if not parsed.get("skills"):
        skills = []
        if "Java" in query: skills.append("Java")
        if "Python" in query: skills.append("Python")
        if "SQL" in query: skills.append("SQL")
        if "collaborate" in query or "team" in query: skills.append("Collaboration")
        if "cognitive" in query: skills.append("Cognitive")
        if "personality" in query: skills.append("Personality")
        parsed["skills"] = skills
    
    if not parsed.get("duration"):
        duration_match = re.search(r"(\d+)\s*(minutes|mins)", query)
        parsed["duration"] = int(duration_match.group(1)) if duration_match else None
    
    return parsed

def recommend_assessments(query: str, df: List[Dict]) -> List[Dict]:
    parsed = parse_query(query)
    skills = parsed["skills"]
    max_duration = parsed["duration"]

    filtered = df.copy()
    if skills:
        filtered = [item for item in filtered if any(skill.lower() in item["Test Type"].lower() for skill in skills)]
    if max_duration:
        filtered = [item for item in filtered if item["Duration (min)"] <= max_duration]
    
    for item in filtered:
        item["Relevance"] = sum(skill.lower() in item["Test Type"].lower() for skill in skills)
    ranked = sorted(filtered, key=lambda x: x["Relevance"], reverse=True)[:10]
    
    for item in ranked:
        del item["Relevance"]
    
    return ranked if ranked else [df[0]]


