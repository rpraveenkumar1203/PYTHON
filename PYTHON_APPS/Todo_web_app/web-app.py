import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo for the the day ")
st.write("In this app we can add, edit and mark as done the todo")


for todo in todos :
    st.checkbox(todo)

