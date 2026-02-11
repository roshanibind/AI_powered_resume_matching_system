def find_missing_skills(resume, job, skills):
    resume_skills = {s for s in skills if s in resume}
    job_skills = {s for s in skills if s in job}
    return list(job_skills - resume_skills)
