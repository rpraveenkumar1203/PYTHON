import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo_to_be_added = st.session_state['new_todo'] + '\n'
    todos.append(todo_to_be_added)
    functions.write_todos(todos)
    #del st.session_state(todo_to_be_added)

st.title("My Todo for the the day ")
st.write("In this app we can add, edit and mark as done the todo")


# deleting the todo which has been complelted 

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


#asking the input from user and adding displaying

st.text_input(label= "" ,key = 'new_todo',placeholder='Please enter a new todo',on_change=add_todo)






