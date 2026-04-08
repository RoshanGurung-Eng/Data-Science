import streamlit as st
import requests

st.write("Hello World",unsafe_allow_html=True)
r = requests.get("http://localhost:8000/items")
st.write(r.json())
