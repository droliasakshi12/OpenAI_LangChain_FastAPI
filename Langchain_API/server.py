import os 
from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from fastapi import FastAPI 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn 
from langchain_openai import ChatOpenAI


load_dotenv(dotenv_path=r"api.env")  #your own path

os.environ['OPENAI_API_KEY'] = os.getenv("openai_api")


app = FastAPI(
    title="Langchain server",
    version='1.0',
    description= "A simple API server"
)


add_routes(
    app,
    ChatOpenAI(),
    path  = "/openai")

model = ChatOpenAI()

prompt1 = PromptTemplate.from_template("Write me an eassy about {topic} with 100 words.")
prompt2 = PromptTemplate.from_template("Write me an  poem about {topic} in 50 words")


add_routes(
    app , 
    prompt1 | model,
    path = "/eassy")

add_routes(
    app , 
    prompt2 | model , 
    path = "/poem"
)


if __name__ == "__main__":
    uvicorn.run("server:app", host='localhost' , port = 8000 , reload = True)
