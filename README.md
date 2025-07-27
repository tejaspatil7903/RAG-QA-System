# 🧠 AI-Powered PDF Q&A System using LangChain & Mistral-7B

This project is a smart question-answering system that reads any PDF document and answers questions **only based on its content** using advanced Retrieval-Augmented Generation (RAG) techniques.

## 🚀 Features

- 🔍 PDF document loader with chunking
- 🧠 HuggingFace embeddings + Chroma vector store
- 💬 Mistral-7B instruct model via LangChain
- 🤖 Chat-style prompting with context-grounded answers
- 🧾 PDF ingestion, vectorization, and retrieval
- ✅ Open-source, customizable, and easy to use

## 🛠️ Tech Stack

- Python 🐍
- LangChain 🦜
- Mistral-7B via `langchain-openai`
- HuggingFace Embeddings
- Chroma Vector Store
- dotenv for environment management

## 📂 Folder Structure

pdf-rag-qa/
│
├── app.py # Main logic
├── attention.pdf # Sample input PDF
├── .env # API keys
├── requirements.txt # Dependencies
├── README.md # This file
└── docs/
└── summary.pdf # 1-page case study
