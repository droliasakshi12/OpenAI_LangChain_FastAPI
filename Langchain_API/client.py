import requests 
import streamlit as st 

def get_eassy(text_input):
    response = requests.post("http://localhost:8000/eassy/invoke",
                             json = {'input':{'topic':text_input}})
    
    return response.json()['output']['content']

def get_poem(text_input):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json= {"input":{'topic':text_input}})
    
    return response.json()['output']['content']

st.title("Langchain demo with openai")
eassy_input = st.text_input("write an eassy")
poem_input = st.text_input("Write a poem")

if eassy_input :
    st.write(get_eassy(eassy_input))
    
if poem_input :
    st.write(get_poem(poem_input))

