import streamlit as st
import todo_functions as functions


todos = functions.get_todos()
def add_todo():
    todolocal = st.session_state["newtodo"] + "\n"
    todos.append(todolocal)
    functions.write_todos(todos)

st.title("My Todo App")

st.subheader("This is my todo app.")

st.write("This app is to increase your productivity")
for todo in todos:
    st.checkbox(todo)

user_input = st.text_input(label="", placeholder="Enter a todo...",
on_change=add_todo, key="newtodo")

st.session_state
