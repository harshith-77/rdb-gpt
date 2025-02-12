import sqlite3
import pandas as pd
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDatabaseTool

def create_db(csv_path, table_name):
    db = sqlite3.connect("my_rdb.db")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, db, if_exists="replace", index=False)

def parse_sql_query(query):
    return query.strip("```sqlite\n").strip("\n```")

def generate(llm, db, query):
    sql_query_generator = create_sql_query_chain(llm, db)
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
