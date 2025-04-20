# Chat with Multiple PDFs

A powerful **Streamlit web app** that lets you **chat with multiple PDF documents** using **Google Gemini** and **LangChain**. Upload your files, ask questions, and get intelligent answers extracted directly from your PDFs.

## ✨ Features

- 📁 **Upload multiple PDFs**: Easily upload multiple PDF files for processing.
- 📄 **Extract and chunk text**: Automatically extract and chunk the text from PDFs for more efficient querying.
- 🧠 **Vector embeddings**: Use **Google Gemini** (`gemini-1.5-flash`) for generating embeddings.
- 🔍 **Semantic search**: Perform semantic search with **ChromaDB** to retrieve the most relevant information.
- 💬 **Conversational Q&A**: Engage in dynamic Q&A with memory to keep track of your interactions.
- 🎨 **Clean, dark-themed UI**: A stylish and user-friendly design powered by Streamlit.

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **LLM:** Google Gemini (`gemini-1.5-flash`)
- **Embeddings:** `embedding-001` via Google Generative AI
- **Text Processing:** PyPDF2 + LangChain
- **Vector Store:** ChromaDB
- **Memory:** ConversationBufferMemory from LangChain

---

## 🚀 Getting Started

Follow these steps to set up and run the app locally:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/chat-with-multiple-pdfs.git
cd chat-with-multiple-pdfs
```
### 2. Create .env file and enter the GEMINI API Key
```bash
touch .env
```
### 3. Create virtual environment and install the required dependcies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requiements.txt
```

### 4. Run the def.py in streamlit
```bash
streamlit run def.py
```

