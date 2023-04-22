import time
from functions import get_todos, write_todos

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is currently {current_time}")

while True:
    # Get user input and strip space chars
    user_input = input("Type add/new, show, complete, edit or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add") or user_input.startswith("new"):
        todo = user_input[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif user_input.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
    elif user_input.startswith("edit"):
        todos = get_todos()
        if len(todos) == 0:
            print("There's nothing in the list! Add something to the Todo List First")
            continue
        print(f"Choose an Item in the list 1 to {len(todos)} ")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
        number = int(input("Choose a number: "))
        number = number - 1
        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"
        write_todos(todos)
    elif user_input.startswith("complete"):
        try:
            number = int(input("Number of the todo to complete: "))
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("That is not a valid input, Try again!")