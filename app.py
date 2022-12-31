import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Run test")

URL = "http://10.1.0.3/"
page = requests.get(URL, verify=False, timeout=1)
st.code(page.text)