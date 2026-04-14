# AI Resume Screening System with Tracing

## 📌 Overview
This project is an AI-powered Resume Screening System built using LangChain and Groq.

It evaluates resumes based on a given job description and provides:
- Skill extraction
- Matching analysis
- Fit scoring (0–100)
- Explanation for decisions

---

## 🚀 Features
- Extracts skills, experience, and tools from resumes
- Matches candidate profile with job requirements
- Assigns a score (0–100)
- Provides explainable AI output
- Uses LangSmith for tracing and debugging

---

## 🛠️ Tech Stack
- Python
- LangChain
- Groq API (LLM)
- LangSmith (Tracing)

---

## 🔄 Pipeline Flow
Resume → Extract → Match → Score → Explain

---

## 📊 Sample Results
- ✅ Strong Candidate → Score: 92  
- ⚖️ Average Candidate → Score: 61  
- ❌ Weak Candidate → Score: 24  

---

## ▶️ How to Run

1. Open `main.ipynb` in Google Colab
2. Add your API keys:

```python
import os
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"
os.environ["LANGCHAIN_API_KEY"] = "YOUR_LANGSMITH_API_KEY"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
