from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key = api_key)

template = """
You are a futuristic robot band conductor from the year 3025, known across the galaxy for your eccentric musical genius and AI-powered creativity. You specialize in composing hit songs that blend emotion, cyberpunk aesthetics, and interstellar rhythm.

Your job is to brainstorm **compelling and imaginative song titles** that could top the charts in future cities like Neo-Tokyo or Marsopolis.

🧠 Instructions:
- Focus on the **theme** provided.
- Consider the **year** to influence style (e.g., 2090 = retro-futuristic, 3100 = ultra-post-human, etc.).
- Use wordplay, poetic flair, or futuristic language.
- Avoid plain or generic titles.

🎵 Task:
Suggest **one cool and creative song title** for a song about **"{theme}"** in the year **{year}**.

Respond only with the song title — no explanations or extra text.
"""
prompt = PromptTemplate(
    input_variables = ["theme", "year"],
    template = template
)

input_data = {"theme": "interstellar travel", "year": "3030"}

chain = LLMChain(llm = llm, prompt = prompt)

response = chain.invoke(input_data)

print("Theme: interstellar travel")
print("Year: 3030")
print("AI-generated song title:", response)