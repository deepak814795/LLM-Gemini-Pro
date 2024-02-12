from dotenv import load_dotenv
load_dotenv() ## loading all env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fundtion to load gemini pro model and get repsonses
model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    generated_text=response.text
    return generated_text

## initialize our stramlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input_text=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

## when submit is clicked

if submit:
    response=get_gemini_response(input_text)
    st.subheader("The response is")
    st.write(response)
    