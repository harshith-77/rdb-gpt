import streamlit as st
import os
import requests
from langchain_community.utilities import SQLDatabase

st.title("Relational DataBase GPT")

st.sidebar.header("Add CSV to DB")
csv_file = st.sidebar.file_uploader(label='Add CSV to DB', type='.csv', label_visibility='collapsed')
if csv_file:
    if not os.path.exists("./uploaded_files"):
        os.makedirs("./uploaded_files")
    csv_path = f"./uploaded_files/{csv_file.name}"
    with open(csv_path, 'wb') as f:
        f.write(csv_file.getbuffer())

    body = {
        "csv_path": csv_path,
        "csv_name": csv_file.name
    }
    response = requests.post("http://localhost:2911/upload_csv", json=body)
    if response.status_code==200:
        st.sidebar.success("Data added to DB Successfully!!!")
        db = SQLDatabase.from_uri("sqlite:///my_rdb.db")
        st.sidebar.write(f"Current Table Info in RDB:\n{db.table_info}")
    else:
        st.sidebar.write(response.json()['content'])

query = st.text_input("Question: ")
if query:
    body = {
        "query": query
    }
    response = requests.post("http://localhost:2911/get_answer", json=body)
    if response.status_code == 200:
        answer = response.json()['answer']
        st.subheader("Answer:")
        st.write(answer)
    else:
        st.write(response.json()['content'])