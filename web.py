import streamlit as st
import todo_functions as functions


todos = functions.get_todos()
def add_todo():
    todolocal = st.session_state["newtodo"] + "\n"
    todos.append(todolocal)
    functions.write_todos(todos)

st.title("My Todo-List")

st.subheader("To complete/delete a todo, just select it.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


user_input = st.text_input(label="", placeholder="Enter a todo...",
on_change=add_todo, key="newtodo")
