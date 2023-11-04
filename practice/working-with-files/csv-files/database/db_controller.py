"""
Responsible for Interfacing with the DB (.txt file)

Shape of File:
id,msg,complete
"""

import os
import csv

DB_NAME = "db.csv"
HEADERS = ["id", "msg", "complete"]

# Create a mapping between strings and their boolean types
bool_mapping = {"True": True, "False": False}


def create_db_if_not_exists():
    """
    Create a new DB (txt file) if one does not exist in the directory
    :return: None
    """
    if not os.path.exists(DB_NAME):
        with open(DB_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def get_todos():
    """
    Return a list of all Todos in the DB
    :return: List of Todo Dictionaries
    """
    with open(DB_NAME, "r") as file:
        reader = csv.DictReader(file)
        todos = list(reader)

    # Convert the 'id' and 'complete' fields to their appropriate types
    for todo in todos:
        todo["id"] = int(todo["id"])
        todo["complete"] = bool_mapping[todo["complete"]]

    return todos


def get_todo_by_id(id: int):
    """
    Retrieve a Todo of specified ID from the DB
    :param id: The ID of the Todo to return
    :return: Todo of specified ID or None if not found
    """
    with open(DB_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["id"]) == id:
                return {
                    "id": int(row["id"]),
                    "msg": row["msg"],
                    "complete": bool_mapping[row["complete"]],
                }


def add_todo(msg: str):
    """
    Create a new Todo and add it to the DB
    :param msg: The message of the new Todo
    :return: Boolean representing if the book was updated or not
    """
    todo_count = _get_todos_count()
    with open(DB_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        # If the file is empty, write the headers first
        if (
            file.tell() == 0
        ):  # .tell() returns current position of file cursor, 0 if file is empty
            writer.writeheader()
        # Append the new todo
        writer.writerow({"id": todo_count, "msg": msg, "complete": False})
        return True


def update_todo(id: int, new_msg: str = None, new_complete: bool = None):
    """
    Update a Todo Item in the DB
    :param id: The ID of the Todo Item to update
    :param new_msg: The new message
    :param new_complete: The new completion status
    :return: Boolean representing if book was updated or not
    """
    todos = get_todos()
    updated = False

    for todo in todos:
        if todo["id"] == id:
            todo["msg"] = new_msg if new_msg is not None else todo["msg"]
            todo["complete"] = (
                new_complete if new_complete is not None else todo["complete"]
            )
            updated = True
            break

    if updated:
        _write_todos(todos)

    return updated


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
    todos = get_todos()

    # Filter out todo w/ specified id
    new_todos = [todo for todo in todos if int(todo["id"]) != id]

    if len(todos) == len(new_todos):
        return False  # No item was deleted

    _write_todos(new_todos)
    return True


def _get_todos_count():
    """
    Return the number of todos in the DB
    :return: Integer representing the number of todos in the DB
    """
    return len(get_todos())


def _write_todos(todos):
    """
    Writes a list of dictionaries into a csv file
    :param todos: Dictionary w/ following headers: "id", "msg", "complete"
    """
    with open(DB_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(todos)
