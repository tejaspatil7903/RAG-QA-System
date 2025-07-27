from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate
load_dotenv()

llm=ChatOpenAI(model="mistralai/mistral-7b-instruct")

loader=PyPDFLoader("attention.pdf")
document=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
documents=text_splitter.split_documents(document)

db=Chroma.from_documents(documents=documents,embedding=HuggingFaceEmbeddings())

prompt=ChatPromptTemplate.from_template(
    """
    Answer the question on the basis of the provided context only don't go outside of the context
    If your answer is seems useful to user i will tip you $10000
    <context>
    {context}
    </context>
    Question: {input}
    """
)

retriver=db.as_retriever()

document_chain=create_stuff_documents_chain(llm,prompt)
retrival_chain=create_retrieval_chain(retriver,document_chain)

result=retrival_chain.invoke({"input":"What are encoder and decoder tasks"})
print(result['answer'])
