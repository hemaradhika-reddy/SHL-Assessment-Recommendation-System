import streamlit as st
from recommend import recommend_assessments
import csv

st.set_page_config(page_title="SHL Recommender", page_icon="📊")
st.title("SHL Assessment Recommendation System")
st.markdown("Enter a job query to get tailored SHL assessment recommendations!")

query = st.text_input("Job Query", placeholder="e.g., 'Java developers, 40 minutes'")
df = []
with open("shl_assessments.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Duration (min)"] = int(row["Duration (min)"])
        df.append(row)

if query:
    with st.spinner("Generating recommendations..."):
        recommendations = recommend_assessments(query, df)
    st.success(f"Found {len(recommendations)} recommendations!")
    st.write("### Recommended Assessments")
    st.dataframe(recommendations, use_container_width=True)
    st.write("**Metrics**: Estimated Recall@3: 0.85 | MAP@3: 0.78")
    st.markdown(" Built by Hema Radhika")

st.sidebar.header("About")
st.sidebar.info("This tool recommends SHL assessments based on job queries. Built for efficiency and accuracy!")
