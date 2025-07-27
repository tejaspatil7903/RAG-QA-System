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


## ⚙️ How It Works

1. Load and split a PDF using LangChain’s `PyPDFLoader`.
2. Convert text chunks to vector embeddings using HuggingFace.
3. Store embeddings in a Chroma vector store.
4. Create a RAG chain using a Mistral-7B instruct model.
5. Ask a question — the model will only respond based on the document.

## 🧪 Sample Question

> ❓ *"What are encoder and decoder tasks?"*

🧠 The system searches relevant chunks from the PDF and answers using the Mistral-7B model.

## 📦 Installation

```bash
git clone https://github.com/tejaspatil7903/pdf-rag-qa.git
cd pdf-rag-qa
pip install -r requirements.txt
