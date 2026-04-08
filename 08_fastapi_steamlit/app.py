import streamlit as st
import requests 

st.set_page_config(
    page_title= "My First App"

)
st.write("Hello WOrld")

st.write("<h1>Hello</h1>", unsafe_allow_html=True)


st.markdown("""
<style>
    button{
            color:white;
            background: red;
            border: 1px solid #ccc;
            border-radius:12px;
            padding:10px;
            width:100px
            }       
</style>
<button>click</button>

""", unsafe_allow_html=True)
name = st.text_input("Enter your name")
st.number_input("Enter your age", min_value=0, max_value=100, value= 0)
st.markdown("---") #<hr>

if st.button("Submit"):
        st.error("Error")

r = requests.get('http://127.0.0.1:8000/items')

for item in r.json():
        st.write(item["name"])



