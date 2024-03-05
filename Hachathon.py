from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
import streamlit as st
import textwrap
import spacy
import os

def run_all (txt_file_path, question):
    text = read_txt_file_to_text(txt_file_path)
    docs = split_text(text)
    result2 = call_model_pass_prompt(model_name, docs, question)
    return result2
def read_txt_file_to_text (txt_file_path):
    with open(txt_file_path, 'r') as file:
        # Read the entire contents of the file into a variable
        file_contents = file.read()
    return file_contents

def split_text(news_article):
    #text_splitter = CharacterTextSplitter.from_tiktoken_encoder(model_name=model_name)
    text_splitter = CharacterTextSplitter(chunk_size=100000, chunk_overlap=200)
    texts = text_splitter.split_text(news_article)
    docs = [Document(page_content=t) for t in texts]
    return docs

def call_model_pass_prompt(model_name, docs, question):
    prompt_template = """ summarize :
    "{text}"
    "Answer the following question based solely on the provided document & " \
    "do not use any outside knowledge or information " \
    "is separated by a string of 11-13-2023-CSPC- and then a three digit number, please quote "\
    "in your answer which section(s) you found the answer from, now here is the question: " ? :"""
    print (prompt_template)
    test2 = question
    prompt_template = prompt_template + test2
    #print(prompt_template)
    prompt = PromptTemplate.from_template(prompt_template)
    print(prompt)
    OPENAI_API_KEY: str = "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"
    llm = ChatOpenAI(temperature=0.3, openai_api_key=OPENAI_API_KEY, model_name=model_name)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    result3 = stuff_chain.run(docs)
    return result3

def print_long_text(result):
    wrapped_text = textwrap.wrap(result, 100)
    for line in wrapped_text:
        print(line)

def get_question_and_provide_answer(file):
    st.title("Welcome to MTO's Driver Instructor Preparation Center, I am am your AI Chatbot!")
    question = st.text_input("Ask your question about content of MTO materials:")
    response = " "
    if st.button("Submit"):
        response = run_all(file, question)
    return response

spacy.load("en_core_web_sm")
model_name = "gpt-4-1106-preview"

uploaded_file = r"F:\Olgoo\CSPC2\Summaries\DrivingInstructorTraining.txt"
if st.checkbox('Answers to your inquiry will be solely based on CSPC panels'):
    response = get_question_and_provide_answer(uploaded_file)
    st.write(response)
