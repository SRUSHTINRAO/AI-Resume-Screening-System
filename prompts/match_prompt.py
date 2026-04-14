from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
You are an AI system that compares a resume with a job description.

Tasks:
1. Identify matching skills
2. Identify missing skills
3. Evaluate how well the resume fits the job

Rules:
- Do NOT assume skills
- Only use given data
- Be accurate

Output format:
Matching Skills: ...
Missing Skills: ...
Summary: ...

Job Description:
{job_description}

Resume:
{resume}
"""
)
