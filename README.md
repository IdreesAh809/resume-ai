# ATS Resume Matching System

This project is a **Smart ATS (Applicant Tracking System) Resume Evaluator** built using **Streamlit** and **OpenAI GPT models**. It allows users to upload their resumes (PDF) and compare them against a given job description to get a professional evaluation and a percentage match.

---

## Features

- Upload your **Resume (PDF)**.
- Paste or write a **Job Description**.
- Get a **detailed evaluation** of your resume:
  - Strengths & weaknesses
  - Missing keywords
  - Overall percentage match
- Designed for **AI Engineer, Data Scientist, and related tech roles**.
- Uses **OpenAI GPT-3.5 Turbo** for natural language evaluation.

---

## Installation

1. Clone the repository:

```
git clone <your-repo-link>
cd <repo-folder>
```

## Create and activate a virtual environment:
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Create a .env file and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Run the App:
```
streamlit run app.py
```