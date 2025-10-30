from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import PyPDF2
import openai

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------------
# Functions
# -------------------------
def extract_pdf_text(uploaded_file):
    """Extract text from uploaded PDF file."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()

def get_openai_response(prompt, max_tokens=512):
    """Send prompt to OpenAI and return response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # cheap and fast
            messages=[
                {"role": "system", "content": "You are an expert ATS evaluator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# -------------------------
# Streamlit App
# -------------------------
st.set_page_config(page_title="ATS Resume Expert", layout="wide")
st.title("ATS Resume Expert")
st.write("Upload your resume and a job description to get an ATS evaluation.")

# Job description input
job_description = st.text_area("Paste Job Description Here:", height=200)

# Resume upload
uploaded_file = st.file_uploader("Upload your Resume (PDF):", type=["pdf"])
if uploaded_file:
    st.success("PDF Uploaded Successfully!")

# Buttons
col1, col2 = st.columns(2)
with col1:
    submit_eval = st.button("Evaluate Resume")
with col2:
    submit_match = st.button("Percentage Match")

# Prompts templates
PROMPT_EVAL = """
You are an experienced Technical Human Resource Manager. Review the provided resume against the job description.
Highlight strengths and weaknesses relative to the role.
Resume: {resume_text}
Job Description: {jd_text}
"""

PROMPT_MATCH = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Evaluate the resume against the job description. Return:
1. Percentage match
2. Missing keywords
3. Final thoughts
Resume: {resume_text}
Job Description: {jd_text}
"""

# -------------------------
# Button actions
# -------------------------
if submit_eval:
    if uploaded_file and job_description.strip():
        resume_text = extract_pdf_text(uploaded_file)
        prompt = PROMPT_EVAL.format(resume_text=resume_text, jd_text=job_description)
        response = get_openai_response(prompt, max_tokens=600)
        st.subheader("Resume Evaluation:")
        st.write(response)
    else:
        st.warning("Please upload a resume and provide a job description.")

if submit_match:
    if uploaded_file and job_description.strip():
        resume_text = extract_pdf_text(uploaded_file)
        prompt = PROMPT_MATCH.format(resume_text=resume_text, jd_text=job_description)
        response = get_openai_response(prompt, max_tokens=400)
        st.subheader("ATS Percentage Match Result:")
        st.write(response)
    else:
        st.warning("Please upload a resume and provide a job description.")
