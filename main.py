# Tech Architecture:
# DB Creation
# Query Processing (Query -> SQL Query from LLM -> Fire in DB -> Answer)
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import GoogleGenerativeAI
# from langchain_community.llms import Ollama
import helper

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///my_rdb.db")
llm = GoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", google_api_key=os.environ["GEMINI_API_KEY"], temperature=0)
# llm = Ollama(model="llama3.2:3b")

st.title("Relational DataBase GPT")

st.sidebar.header("Add CSV to DB")
csv_file = st.sidebar.file_uploader(label='Add CSV to DB', type='.csv', label_visibility='collapsed')
if csv_file:
    if not os.path.exists("./uploaded_files"):
        os.makedirs("./uploaded_files")
    csv_path = f"./uploaded_files/{csv_file.name}"
    with open(csv_path, 'wb') as f:
        f.write(csv_file.getbuffer())
    helper.create_db(csv_path, csv_file.name.strip(".csv")[0])
    st.sidebar.success("Data added to DB Successfully!!!")

query = st.text_input("Question: ")
if query:
    response = helper.generate(llm, db, query)
    st.write(response)