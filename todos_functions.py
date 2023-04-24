def get_todos(filepath="todos.txt"):
    """Read the contents of the todos.txt file"""
    with open(filepath, "r", encoding="utf-8") as file_read:
        list_of_todos = file_read.readlines()
    return list_of_todos


def write_todos(list_to_use, filepath="todos.txt"):
    """Write the updated list to the todos.txt file"""
    with open(filepath, "w", encoding="utf-8") as file_write:
        file_write.writelines(list_to_use)
        