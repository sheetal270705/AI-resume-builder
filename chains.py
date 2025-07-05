import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI  

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

def generate_summary(name, job_role, education):
    try:
        with open("prompts/summary.txt", "r", encoding="utf-8") as file:
            template_text = file.read()

        prompt = PromptTemplate.from_template(template_text)
        final_prompt = prompt.format(name=name, job_role=job_role, education=education)

        response = llm.predict(final_prompt)
        return response

    except Exception as e:
        return f"Error generating summary: {e}"

def generate_experience(name, job_role, experience):
    try:
        with open("prompts/experience.txt", "r", encoding="utf-8") as file:
            template_text = file.read()

        prompt = PromptTemplate.from_template(template_text)
        final_prompt = prompt.format(name=name, job_role=job_role, experience=experience)

        response = llm.predict(final_prompt)
        return response

    except Exception as e:
        return f"Error generating experience: {e}"