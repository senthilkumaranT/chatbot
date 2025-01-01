import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


##langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


#prompt template 

promt = ChatPromptTemplate.from_messages(
[
    ("system","you are a helpful assistant .please respond to the question asked"),
     ("user","Question :{question}")
]

)




## streamlit framework 
st.title("langchain Demo with LLAMA3.2")
input_text = st.text_input("what qeustion you have in mind ")

##ollama llama 3.2 model 

llm=Ollama(model = "llama3.2:1b")
outpraser = StrOutputParser()

chain = promt | llm | outpraser

if input_text:
    st.write(chain.invoke({"question":input_text}))



