import sqlite3
import pandas as pd
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

from fewshots import few_shot_examples

embeddings = HuggingFaceEmbeddings()

def create_db(csv_path, table_name):
    db = sqlite3.connect("my_rdb.db")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, db, if_exists="replace", index=False)

def parse_sql_query(query):
    return query.strip("```sqlite\n").strip("\n```")

def get_vector_db():
    to_vectorize = [" ".join(dic.values()) for dic in few_shot_examples]
    vector_db = Chroma.from_texts(texts=to_vectorize, embedding=embeddings, metadatas=few_shot_examples)
    return vector_db

def get_few_shot_prompt(query):
    vector_db = get_vector_db()
    example_selector = SemanticSimilarityExampleSelector(vectorstore=vector_db, k=2)
    template = "User input: {input}\nSQL query: {query}"
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["input", "query"]
    )
    prompt = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = prompt_template,
        prefix = "You are a SQLite expert. Given an input question, create a syntactically correct SQLite query to run. Unless otherwise specified, do not return more than {top_k} rows.\n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of question and their corresponding SQL Queries.\n\n",
        suffix = "User input: {input}\nSQL query: ",
        input_variables=["input", "top_k", "table_info"]
    )
    return prompt

def generate(llm, db, query):
    prompt = get_few_shot_prompt(query)
    sql_query_generator = create_sql_query_chain(llm, db, prompt)
    query_db = QuerySQLDatabaseTool(db=db)
    chain = sql_query_generator | parse_sql_query | query_db
    rdb_resp = chain.invoke({"question": f"{query}"})
    print("RDB Response: ", rdb_resp)

    llm_template = f'''
    You are a helpful assistant. Given a question and answer retrieved from SQL Database. Reformat the answer according to the question. NO PREAMBLE.
    Question: {query}
    SQL Answer: {rdb_resp}
    Answer:
    '''
    answer = llm.invoke(llm_template.format(query=query, rdb_resp=rdb_resp))
    return answer
