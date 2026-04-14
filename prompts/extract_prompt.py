from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI system that extracts structured information from resumes.

Extract the following:
1. Skills
2. Experience
3. Tools/Technologies

Rules:
- Only extract what is present
- Do NOT assume anything
- Keep output clean

Output format:
Skills: ...
Experience: ...
Tools: ...

Resume:
{resume}
"""
)
