# SHL-Assessment-Recommendation-System
# SHL Assessment Recommendation System

A web-based tool to recommend SHL assessments based on job queries or descriptions, built for efficiency and accuracy. This project fulfills the Gen AI Task by providing a Streamlit demo for user interaction and a FastAPI endpoint for programmatic access.

## Features
- **Natural Language Query Support**: Enter job requirements (e.g., "Java developers, 40 minutes") to get tailored SHL assessment recommendations.
- **Tabular Output**: Displays up to 10 assessments with Name, URL, Remote Testing, Adaptive/IRT, Duration, and Test Type.
- **Polished Demo**: Streamlit UI with spinner, success messages, sidebar, and estimated metrics for a professional look.
- **API Access**: FastAPI endpoint returns JSON recommendations for integration or automated testing.
- **Extras**:
  - Expanded dataset (10+ assessments) for better coverage.
  - Optional LLM integration (e.g., Gemini API) for advanced query parsing.
  - Evaluation metrics (Recall@3, MAP@3) tested internally.

![This is an image](https://github.com/hemaradhika-reddy/SHL-Assessment-Recommendation-System/blob/main/Process%20Flow.png)

## Live Links
1. **Demo**: [Streamlit URL] (e.g., `https://shl-assessment-recommendation-system-6i5dinxbyhgkhetpygk38p.streamlit.app/`)
2. **API Endpoint**: [Vercel URL]/recommend (e.g., `https://shl-assessment-recommendation-system-jvcxifgub.vercel.app/recommend?query=Java developers, 40 minutes`)
3. **Code**: [GitHub URL] (e.g., `https://github.com/hemaradhika-reddy/SHL-Assessment-Recommendation-System`)


## Installation & Local Setup
### Prerequisites
- Python 3.8+
- Git
### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hemaradhika/shl-recommendation-system.git
   cd shl-recommendation-system
   
2.Set Up Virtual Environment:
   ``` python -m venv venv
source venv/bin/activate ```

3.Install Dependencies
pip install -r requirements.txt

4.Run the demo
streamlit run app.py

5.run the api
uvicorn api:app --reload

shl-recommendation-system/
├── shl_assessments.csv  # Assessment dataset
├── recommend.py         # Core recommendation logic with tracing
├── api.py              # FastAPI endpoint
├── app.py              # Streamlit demo
├── requirements.txt    # Dependencies
├── vercel.json         # Vercel config
└── README.md           # This file




