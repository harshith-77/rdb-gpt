# 🚀 Relational Database GPT

## 📝 Overview
Relational Database GPT is an AI-powered system that takes user queries in natural language, converts them into SQL queries using a Large Language Model (LLM), executes them on a relational database (RDB), and returns the relevant output. Additionally, users can insert data into the RDB through the UI.

## ✨ Features
- 🔍 Converts natural language queries to SQL.
- ⚡ Executes SQL queries on a relational database.
- 🖥️ Provides a user-friendly interface with Streamlit.
- 📂 Supports inserting CSV data into the database.
- 🤖 Implemented dynamic **Few-Shot Prompting** to improve SQL query generation accuracy.

## 🔬 What is Few-Shot Prompting?

Few-Shot Prompting is a technique in which an AI model is provided with a small set of relevant examples to guide its response generation. Unlike zero-shot prompting (where the model generates answers without examples) or fine-tuning (which requires extensive training), few-shot prompting balances flexibility and accuracy, ensuring the LLM generates more precise answers.

I have enhanced few-shot prompting by dynamically selecting the most relevant examples, further improving accuracy.

### How Few-Shot Prompting Improves SQL Query Accuracy:
- Vector Database Creation: A set of past queries and their corresponding SQL statements are embedded and stored in a vector database (using ChromaDB).
- Dynamic Example Selection: When a new user query is received, the system retrieves the two most similar examples from the vector database.
- Prompt Enhancement: These examples are included in the prompt to guide the LLM in generating a more accurate SQL query.
- Execution & Refinement: The generated SQL query is executed on the RDB, and the response is further formatted for clarity.

By leveraging contextual examples, the model can generate syntactically correct and contextually relevant SQL queries, significantly reducing errors and improving the quality of the results. 

Note: Makesure to add the question and the correct SQL query to fewshots file if the LLM still generates a wrong SQL query to your question so that it will become an example for the future searches.

## 🛠️ Installation Guidelines
Follow these steps to set up the News Research Tool:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/harshith-77/rdb-gpt.git
   cd rdb-gpt

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
      
4. **Set up your Gemini API key by creating a .env file in the project root and add your API**
   ```
   GEMINI_API_KEY = "Your API Key"

5. **Run Application**
   ```bash
   streamlit run main.py

## 🚀 Usage
1. Run the application:
   ```sh
   streamlit run app.py
   ```
2. 📤 Upload a CSV file via the sidebar to populate the database.
3. 📝 Enter a natural language question in the input field.
4. 🔄 The model will generate a SQL query, execute it, and return the result in a readable format.

## 🛠️ Tech Stack
- **Frontend:** 🎨 Streamlit
- **LLM:** 🤖 Google Generative AI
- **Relational Database:** 🗄️ SQLite
- **Vector Database:** 🔍 ChromaDB
- **Libraries:** 🏗️ LangChain, Pandas