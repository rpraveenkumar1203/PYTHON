import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

image_url = "https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/Portfolio/images/PKR.png"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
descrpiton = '''🌟 Enthusiastic developer exploring Python, Golang, AI, and Machine Learning. Focused on clean, efficient code and always learning and innovating. 🚀'''

st.set_page_config(layout='wide')

col1, col2 = st.columns([0.25,0.75])

with col1:
    st.image(image=image,width=200)

with col2 :
    st.title("PraveenKumar Ramesh")
    st.info(descrpiton)
    st.link_button('Github',url='https://github.com/rpraveenkumar1203')


st.subheader('Below are the Apps developed by me from scratch')


col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv('https://raw.githubusercontent.com/rpraveenkumar1203/PYTHON/main/PYTHON_APPS/Portfolio/data.csv',sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Sourcecode]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Sourcecode]({row['url']})")

