# 🧠 AI-Powered PDF Q&A System using LangChain & Mistral-7B

## 📌 Overview
This project implements a smart Question Answering (QA) system that reads PDF files and answers user queries using only the document's content. It leverages Retrieval-Augmented Generation (RAG) with Mistral-7B to ensure accurate and grounded responses.

---

## 🧩 Problem Statement
Reading large PDFs like research papers, manuals, or legal documents is time-consuming. Users often need specific answers without going through hundreds of pages.

---

## 💡 Solution
Using LangChain’s document loading and retrieval tools, the system breaks the PDF into chunks, embeds them with HuggingFace embeddings, stores them in a Chroma vector database, and retrieves relevant sections to answer user queries through a Mistral-7B instruct model.

---

## ⚙️ Architecture

- **PDF Loader**: `PyPDFLoader` (LangChain)
- **Text Splitter**: `RecursiveCharacterTextSplitter`
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
- **Vector Store**: ChromaDB
- **LLM**: Mistral-7B-Instruct (via `langchain-openai`)
- **Prompt Template**: Custom instruction to restrict answers to context only
- **Chain**: RAG using `create_retrieval_chain`

---

## 🧪 Example

**Input Question**: *"What are encoder and decoder tasks?"*  
**Output**: Accurate explanation extracted only from `attention.pdf`, ignoring irrelevant or external data.

---

## ✅ Key Features

- Pure context-based Q&A
- Works with any PDF
- Fast retrieval and inference
- Ready for Streamlit/web integration

---

## 🛠️ Technologies

- Python, LangChain
- Mistral-7B, HuggingFace
- Chroma VectorDB
- dotenv for API key management

---

## 👨‍💻 Author

**Tejas Vinod Patil**  
📧 tejasvpatil03@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/tejasvpatil7903)  
🔗 [GitHub](https://github.com/tejaspatil7903/pdf-rag-qa)

---

## 🔗 GitHub

[github.com/tejaspatil7903/pdf-rag-qa](https://github.com/tejaspatil7903/RAG-QA-System)
