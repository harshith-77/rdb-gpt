# Tech Architecture:
# DB Creation
# Query Processing (Query -> SQL Query from LLM -> Fire in DB -> Answer)
import os

import uvicorn
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import GoogleGenerativeAI
from fastapi.responses import JSONResponse

# from langchain_community.llms import Ollama
import helper
from fastapi import FastAPI, Request

load_dotenv()

app = FastAPI(title="RelationalDB-GPT")

llm = GoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", google_api_key=os.environ["GEMINI_API_KEY"], temperature=0)
# llm = Ollama(model="llama3.2:3b")


@app.post("/upload_csv")
async def upload_csv(request: Request):
    try:
        body = await request.json()
        print(body)
        csv_path = body.get("csv_path")
        csv_name = body.get("csv_name")
        helper.create_db(csv_path, csv_name)
        return JSONResponse(content="Table Creation Successful", status_code=200)
    except Exception as e:
        return JSONResponse(content=f"Table Creation Failed with exception {e}", status_code=400)

@app.post("/get_answer")
async def get_answer(request:Request):
    try:
        body = await request.json()
        query = body.get("query")
        db = SQLDatabase.from_uri("sqlite:///my_rdb.db")
        response = helper.generate(llm, db, query)
        return JSONResponse(content={"answer": response}, status_code=200)
    except Exception as e:
        return JSONResponse(content=f"Generating Answer Failed with exception {e}", status_code=400)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=2911)