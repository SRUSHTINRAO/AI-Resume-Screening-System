from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["resume", "job_description", "score"],
    template="""
You are an AI assistant explaining resume evaluation results.

Task:
Explain why the candidate received the given score.

Include:
- Strengths
- Weaknesses
- Final justification

Rules:
- Be clear and concise
- Do NOT assume anything

Output format:
Explanation: ...

Score: {score}

Job Description:
{job_description}

Resume:
{resume}
"""
)
