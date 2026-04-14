from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
You are an AI system that scores resumes based on job fit.

Task:
- Assign a score from 0 to 100

Scoring Rules:
- 90–100 → Excellent match
- 70–89 → Good match
- 50–69 → Average match
- Below 50 → Weak match

Rules:
- Do NOT assume missing skills
- Penalize missing important skills

Output format:
Score: <number>
Reason: <short reason>

Job Description:
{job_description}

Resume:
{resume}
"""
)
