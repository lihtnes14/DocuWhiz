import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from streamlit_extras.stylable_container import stylable_container
import streamlit.components.v1 as components
import os
from htmlTemplates import css, bot_template, user_template
from datetime import datetime
from groq import Groq

load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def get_text_chunk(text):
    text_splitter = CharacterTextSplitter(
        separator= "\n",
        chunk_size=1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks,db_path):
    storename = "abcd"
    persist_dir = os.path.join(db_path,storename)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embeddings, persist_directory=persist_dir)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handleuser_input(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

   
    conversation_blocks = []

    for i in range(0, len(st.session_state.chat_history), 2):
        timestamp = datetime.now().strftime("%B %d at %I:%M %p")
        
        user_message = st.session_state.chat_history[i].content
        bot_message = st.session_state.chat_history[i+1].content if i+1 < len(st.session_state.chat_history) else ""
        
        formatted_block = (
            user_template.replace("{{MSG}}", f"{timestamp} - {user_message}") +
            bot_template.replace("{{MSG}}", f"{timestamp} - {bot_message}")
        )
        
        conversation_blocks.append(formatted_block)

    for block in reversed(conversation_blocks):
        st.write(block, unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
def main():
    load_dotenv()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(current_dir,"db","db_store")

    st.set_page_config(page_title="Chat with multiple pdf's 📄")
    
    st.write(css, unsafe_allow_html=True) 

    if "conversation" not in  st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.markdown(
        """
        <style>
        .stApp {
            background-color:#081C15;
        }
        h1.highlight{
            margin:10px;
        }
        [data-testid="stSidebarContent"] {
            background:#1B4332;
        }
        [data-testid="stSidebarUserContent"] {
            background:#1B4332;
        }
        [data-testid="stHeading"] {
            color:#52B788;
        }
        [data-testid="stFileUploaderDropzone"] {
            color:#52B788;
            background:#B7E4C7;
        }
        [data-testid="baseButton-secondary"] {
            color:#52B788;
            background:#081C15;
        }
        [data-testid="stButton"] {
            color:#52B788;
            
        }
        [data-testid="stHeadingWithActionElements"] {
            color:#B7E4C7;
        }
        [data-testid="stMarkdownContainer"] {
            color:#95D5B2;
        }
        [data-testid="stFileUploaderDropzone"] span {
            color: #081C15; 
        }
         [data-testid="stFileUploaderDropzone"] small {
            color: #081C15; 
        }
        .stTextInput > div > div {
            background-color: #D8F3DC;
            color:#081C15;
        }
        .stTextInput input {
            color: #000000; 
            border: 4px solid #52B788;
        }
        .stTextInput input:focus {
            outline: none; 
            }
        [data-testid="stWidgetLabel"] {
            background:#2D6A4F;
            border-radius: 10px;
            font-weight: 700;
            letter-spacing: 1px;
            padding-left:10px;
            padding-right:10px;
            display:inline-block;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    components.html(
    """
    <html lang="en">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat with PDFs</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap">
        <style>
            .highlight {
                color: #D8F3DC;
                background: #40916C;
                font-size: 50px;
                font-weight: 700;
                letter-spacing: 1px;
                box-shadow: 0px 4px 6px rgba(82, 183, 136, 0.3), 0px 6px 12px rgba(82, 183, 136, 0.2);
                padding: 15px 25px;
                border-radius: 10px;
                text-align: center;
                font-family: 'Roboto', sans-serif;
            }
        </style>
        <div>
            <center>
                <h1 class="highlight">Chat with Multiple PDFs</h1>
            </center>
        </div>
    """
)

    with stylable_container(
        key="sub",
        css_styles="""
        {
            background-color:#081C15;
        }
        """
    ):
        st.subheader("Instant Q&A with Your Documents 📄")
        st.write("Upload one or more PDF documents and ask questions to extract useful insights instantly. It's like chatting with your files—smart, fast, and efficient!")

    user_question = st.text_input("Ask me anything about the Resumes")

    if user_question:
        if st.session_state.conversation:
            handleuser_input(user_question)
        else:
            st.warning("⚠️ Please upload and process PDFs before asking questions.")


    with st.sidebar:
        st.markdown(":green[YOUR DOCUMENTS]", unsafe_allow_html=True)
        pdf_docs = st.file_uploader("Upload your files here", accept_multiple_files=True, type=['pdf'])
        if st.button("Process"):
            with st.spinner("Processing"):
                if pdf_docs:
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunk(raw_text)
                    vectorstores = get_vectorstore(text_chunks,db_path=db_dir)
                    st.session_state.conversation = get_conversation_chain(vectorstore=vectorstores)

if __name__ == "__main__":
    main()
