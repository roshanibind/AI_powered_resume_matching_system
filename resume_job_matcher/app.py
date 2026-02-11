# import streamlit as st
# from src.parser import extract_text_from_pdf , extract_text_from_docx
# from src.preprocessing import clean_text
# from src.matcher import calculate_match_score
# from src.skill_gap import find_missing_skills

# st.set_page_config(page_title = "AI Resume Matcher")
# st.title("AI- Powered Resume-Job Matching System")

# uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
# job_desc = st.text_area("Paste Job Description")

# if uploaded_file is not None and job_desc.strip()!="":
#     if uploaded_file.name.lower().endswith(".pdf"):
#         resume_text = extract_text_from_pdf(uploaded_file)
#     else:
#         resume_text = extract_text_from_docx(uploaded_file)
     
# # Temporarily add this in app.py before clean_text:
#     st.write("Type of resume_text:", type(resume_text))

#     resume_clean= clean_text(resume_text)
#     job_clean = clean_text(job_desc)


#     score = calculate_match_score(resume_clean , job_clean)

#     # skills = open("data/skills_list.txt").read().splitlines()
#     with open("data/skills_list.txt") as f:
#         skills = f.read().splitlines()

#     missing = find_missing_skills(resume_clean , job_clean , skills)

#     st.subheader(f"Match Score:{score}%")
#     st.write("Missing Skills:", missing)

#     if missing:
#         st.subheader(" Required Skills")
#         for skill in missing:
#             st.write(".", skill)
#     else:
#         st.success("Great match! No major skill gaps.")

import os
import streamlit as st
from src.parser import extract_text_from_pdf, extract_text_from_docx
from src.preprocessing import clean_text
from src.matcher import calculate_match_score
from src.skill_gap import find_missing_skills

st.set_page_config(page_title="AI Resume Matcher")
st.title("AI-Powered Resume–Job Matching System")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file is not None and job_desc.strip() != "":
    # ---- Extract Resume Text ----
    if uploaded_file.name.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    # ---- Clean Text ----
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    # ---- Match Score ----
    score = calculate_match_score(resume_clean, job_clean)

    # ---- Load Skills ----
    # with open("data/skills_list.txt") as f:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    skills_path = os.path.join(BASE_DIR, "data", "skills_list.txt")

    with open(skills_path, "r", encoding="utf-8") as f:
    # skills = f.read().splitlines()
     skills = [s.lower() for s in f.read().splitlines()]

    resume_tokens = set(resume_clean.split())
    job_tokens = set(job_clean.split())

    # ---- Skill Categorization ----
    required_skills = sorted([s for s in skills if s in job_tokens])
    matched_skills = sorted([s for s in required_skills if s in resume_tokens])
    missing_skills = sorted([s for s in required_skills if s not in resume_tokens])

    # ---- UI Output ----
    st.subheader(f"Match Score: {score}%")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(" Required Skills")
        if required_skills:
            for skill in required_skills:
                st.write("•", skill)
        else:
            st.write("No skills detected")

    with col2:
        st.subheader("Matched Skills")
        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.warning("No matched skills")

    with col3:
        st.subheader("Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No skill gaps ")
