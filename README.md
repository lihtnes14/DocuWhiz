# 📚 Chat with Multiple PDFs

A powerful Streamlit web app that lets you **chat with multiple PDF documents** using Google Gemini and LangChain. Upload your files, ask questions, and get intelligent answers extracted directly from your PDFs.

---

## ✨ Features

- 📁 Upload multiple PDFs
- 📄 Extract and chunk text
- 🧠 Vector embeddings using Google Gemini
- 🔍 Semantic search with ChromaDB
- 💬 Conversational Q&A with memory
- 🎨 Clean, dark-themed custom UI

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **LLM:** Google Gemini (`gemini-1.5-flash`)
- **Embeddings:** `embedding-001` via Google Generative AI
- **Text Processing:** PyPDF2 + LangChain
- **Vector Store:** ChromaDB
- **Memory:** ConversationBufferMemory from LangChain

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chat-with-multiple-pdfs.git
cd chat-with-multiple-pdfs
