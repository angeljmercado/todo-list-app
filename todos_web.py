import os
import streamlit as st
import todos_functions as functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


todos = functions.get_todos()


def add_todo():
    """Adding todo to the list, and checking to 
    see if the input already exist in the list"""
    todolocal = st.session_state["newtodo"] + "\n"
    if todolocal not in todos:
        todos.append(todolocal)
        functions.write_todos(todos)
        st.session_state["newtodo"] = ""


st.title("My Todo-List")

st.subheader("To complete/delete a todo, just select it.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


user_input = st.text_input(label="Enter a todo...",
on_change=add_todo, key="newtodo")
