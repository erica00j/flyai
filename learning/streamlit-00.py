import streamlit as st

st.header('welcome to GPT Bot')
st.write('welcome to GPT CHATBOT')

query = st.text_input('Query: ')
if query:
    st.write('Your query is '+query)

button_result = st.button('RUN')
if button_result:
    st.write('Thanks!')