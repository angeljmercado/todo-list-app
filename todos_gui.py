import os
import time
import PySimpleGUI as gui
import todos_functions as functions


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

gui.theme("Black")


clock = gui.Text("", key="clock")
label = gui.Text("Type in a To-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key="todos",
enable_events=True, size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")
window = gui.Window("My To-do App",
layout=[[clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]],
font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                gui.popup("Please select an item first.", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            exit()
        case gui.WIN_CLOSED:
            break
window.close()
