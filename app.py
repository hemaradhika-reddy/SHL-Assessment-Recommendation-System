import streamlit as st
import pandas as pd
from recommend import recommend_assessments

st.title("SHL Assessment Recommendation System")
query = st.text_input("Enter your query (e.g., 'Java developers, 40 minutes')")

if query:
    df = pd.read_csv("shl_assessments.csv")
    recommendations = recommend_assessments(query, df)
    st.write("### Recommended Assessments")
    st.table(pd.DataFrame(recommendations))