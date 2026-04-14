from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from prompts.match_prompt import match_prompt

llm = ChatGroq(model="llama-3.1-8b-instant")

match_chain = match_prompt | llm | StrOutputParser()
