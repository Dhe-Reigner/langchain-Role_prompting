######## ROLE PROMPTING ##########
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template = "You are an intelligent song writter from the future" \
"You are tasked to compose a song entitled {title} for the year {year}"

prompt = PromptTemplate(
    input_variables=["title", "year"],
    template=template
)

input = {
    "title":"Humanity in Mars",
    "year":"3020"
}

chain = prompt | llm | StrOutputParser()

response = chain.invoke(input)

print(response)