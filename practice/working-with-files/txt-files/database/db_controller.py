"""
Responsible for Interfacing with the DB (.txt file)

Shape of File:
id,msg,complete
"""

import os

DB_NAME = "db.txt"

# Create a mapping between strings and their boolean types
bool_mapping = {"True": True, "False": False}


def create_db_if_not_exists():
    """
    Create a new DB (txt file) if one does not exist in the directory
    :return: None
    """
    if not os.path.exists(DB_NAME):
        with open(DB_NAME, "w") as file:
            pass


def get_todos():
    """
    Return a list of all Todos in the DB
    :return: List of Todo Dictionaries
    """
    todos = []
    with open(DB_NAME, "r") as file:
        for line in file:
            id, msg, complete = line.strip().split(",")
            todos.append(
                {"id": int(id), "msg": msg, "complete": bool_mapping[complete]}
            )
    return todos


def get_todo_by_id(id: int):
    """
    Retrieve a Todo of specified ID from the DB
    :param id: The ID of the Todo to return
    :return: Todo of specified ID or None if not found
    """
    with open(DB_NAME, "r") as file:
        for line in file:
            id_, msg, complete = line.strip().split(",")
            if int(id_) == id:
                return {"id": int(id_), "msg": msg, "complete": bool_mapping[complete]}


def add_todo(msg: str):
    """
    Create a new Todo and add it to the DB
    :param msg: The message of the new Todo
    :return: Boolean representing if the book was updated or not
    """
    todo_count = _get_todos_count()
    with open(DB_NAME, "a") as file:
        file.write(f"{todo_count},{msg},{False}\n")
        return True


def update_todo(id: int, new_msg: str = None, new_complete: bool = None):
    """
    Update a Todo Item in the DB
    :param id: The ID of the Todo Item to update
    :param new_msg: The new message
    :param new_complete: The new completion status
    :return: Boolean representing if book was updated or not
    """
    todos = []  # Will hold the existing todos
    updated = False  # Whether or not the specified todo was successfully updated

    # Read through the todos and replace the specific todo with updated information
    with open(DB_NAME, "r") as file:
        for line in file:
            id_, msg, complete = line.strip().split(",")
            if int(id_) == id:
                updated_msg = new_msg if new_msg is not None else msg
                updated_complete = (
                    str(new_complete) if new_complete is not None else complete
                )
                todos.append(f"{id},{updated_msg},{updated_complete}")
                updated = True
            else:
                todos.append(line.strip())  # append the line without modifications

    if not updated:
        return False

    # Write back all todos to the DB, including the updated todo
    with open(DB_NAME, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")
    return True


def toggle_complete(id: int):
    """
    Toggle the completion status of the todo
    :param id: ID of the todo
    :return: Boolean value representing completion status after toggle
    """
    todo = get_todo_by_id(id)
    todo_complete = todo["complete"]
    if todo:
        update_todo(id, None, (not todo_complete))
    return not todo_complete


def delete_todo(id: int):
    """
    Delete the TODO w/ specified ID from the DB
    :param id: ID of the TODO to remove from the DB
    :return: Boolean value representing success or failure of todo deletion
    """
    todos = []  # Will hold the existing todos

    # Read through the todos and filter out the desired todo
    with open(DB_NAME, "r") as file:
        for line in file:
            id_, msg, complete = line.strip().split(",")
            if int(id_) != id:
                todos.append(f"{id_},{msg},{complete}")

    # Write back all todos to the DB, including the updated todo
    with open(DB_NAME, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")

    return True


def _get_todos_count():
    """
    Return the number of todos in the DB
    :return: Integer representing the number of todos in the DB
    """
    with open(DB_NAME, "r") as file:
        return len(file.readlines())
