# 🚀 Relational Database GPT

## 📝 Overview
Relational Database GPT is an AI-powered system that takes user queries in natural language, converts them into SQL queries using a Large Language Model (LLM), executes them on a relational database (RDB), and returns the relevant output. Additionally, users can insert data into the RDB through the UI.

## ✨ Features
- 🔍 Converts natural language queries to SQL.
- ⚡ Executes SQL queries on a relational database.
- 🖥️ Provides a user-friendly interface with Streamlit.
- 📂 Supports inserting CSV data into the database.

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
- **Database:** 🗄️ SQLite
- **Libraries:** 🏗️ LangChain, Pandas