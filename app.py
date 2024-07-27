import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while processing your request: {e}")
        return None

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

#  Prompt template
input_prompt_template = """
You are a highly experienced ATS (Application Tracking System) with expertise in the tech field, including software engineering, data science, data analytics, and big data engineering. Your task is to evaluate the provided resume against the given job description.

Here's the input you need to analyze:
- Resume: {resume_text}
- Job Description: {jd_text}

Please provide a detailed analysis of the resume against the job description. Ensure the response includes the following information in the specified format:
- JD Match percentage
- Missing Keywords
- Profile Summary
- CV Score
- Things that can be improved in CV
- Skills Improvement Suggestions
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume with AI")

jd = st.text_area("Paste the Job Description", height=200)
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload your resume in PDF format.")

if st.button("Submit"):
    if uploaded_file is not None and jd:
        resume_text = input_pdf_text(uploaded_file)
        input_prompt = input_prompt_template.format(resume_text=resume_text, jd_text=jd)
        response = get_gemini_response(input_prompt)
        
        if response:
            st.subheader("Response:")
            st.text(response)
        else:
            st.error("Failed to get a response from the API.")
    else:
        st.error("Please upload a resume and provide a job description.")
