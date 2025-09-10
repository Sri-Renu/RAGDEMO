# Mini RAG Demo with Google Search 🔎

This is a **mini Retrieval-Augmented Generation (RAG)-style demo** powered by **Google Custom Search API** and **Streamlit**.  
Unlike traditional RAG that relies on local documents or embeddings, this project fetches **real-time search results from Google** and displays them in a clean web interface.

It’s a **lightweight, beginner-friendly project** to demonstrate how RAG-like retrieval can work in practice.

---

## 🚀 Features
- 🎨 Simple **Streamlit UI** for interactive search  
- 🔍 Uses **Google Custom Search API** to fetch results  
- 📑 Displays **title, snippet, and link** for each result  
- 🐍 **Beginner-friendly code** — short and easy to understand  

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/RAGDEMO.git
cd RAGDEMO
```

2. (Optional) Create a Virtual Environment
# Mac/Linux
python -m venv venv
source venv/bin/activate
# Windows
python -m venv venv
venv\Scripts\activate
---
3. Install Dependencies
pip install -r requirements.txt
---
🛠️ Requirements
Your requirements.txt should include:

streamlit
google-api-python-client

---
🔑 API Setup
You’ll need two things from Google:

API Key → Get from Google Cloud Console

Custom Search Engine (CSE) ID → Create from Programmable Search Engine
---

▶️ Run the App

Start the Streamlit server:

streamlit run app.py

Then open http://localhost:8501
 in your browser.
