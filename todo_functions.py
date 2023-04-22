def get_todos(filepath="todos.txt"):
    """Read the todos"""
    with open(filepath, "r", encoding="utf-8") as file_read:
        list_of_todos = file_read.readlines()
    return list_of_todos


def write_todos(list_to_use, filepath="todos.txt"):
    """Write to the todos file"""
    with open(filepath, "w", encoding="utf-8") as file_write:
        file_write.writelines(list_to_use)