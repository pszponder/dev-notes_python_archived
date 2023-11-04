"""
Responsible for Interfacing with the DB (.json file)

Shape of File:
[
    {
        id: 0,
        msg: "some message"
        complete: false
    }
]
"""

import os
import json

DB_NAME = "db.json"

# Create a mapping between strings and their boolean types
bool_mapping = {"True": True, "False": False}


def create_db_if_not_exists():
    """
    Create a new DB (json file) if one does not exist in the directory
    :return: None
    """
    if not os.path.exists(DB_NAME):
        with open(DB_NAME, "w") as file:
            json.dump([], file)


def get_todos():
    """
    Return a list of all Todos in the DB
    :return: List of Todo Dictionaries
    """
    with open(DB_NAME, "r") as file:
        todos = json.load(file)
        return todos


def get_todo_by_id(id: int):
    """
    Retrieve a Todo of specified ID from the DB
    :param id: The ID of the Todo to return
    :return: Todo of specified ID or None if not found
    """
    # Retrieve todos from DB
    todos = get_todos()

    # Search and return specific todo if found
    for todo in todos:
        if todo["id"] == id:
            return todo


def add_todo(msg: str):
    """
    Create a new Todo and add it to the DB
    :param msg: The message of the new Todo
    :return: Boolean representing if the book was updated or not
    """
    # Retrieve todos from DB
    todos = get_todos()

    # Create new todo and append it to retrieved todos
    todos_count = len(todos)
    new_todo = {"id": todos_count, "msg": msg, "complete": False}
    todos.append(new_todo)

    # Write new todo list back to JSON file
    _write_todos(todos)

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
            if new_msg is not None:
                todo["msg"] = new_msg
            if new_complete is not None:
                todo["complete"] = new_complete
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
    if todo:
        new_complete = not todo["complete"]
        update_todo(id, None, new_complete)
        return new_complete


def delete_todo(id: int):
    """
    Delete the TODO w/ specified ID from the DB
    :param id: ID of the TODO to remove from the DB
    :return: Boolean value representing success or failure of todo deletion
    """
    todos = get_todos()

    # Filter out todo we don't want
    new_todos = [todo for todo in todos if todo["id"] != id]

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
    with open(DB_NAME, "w") as file:
        json.dump(todos, file)
