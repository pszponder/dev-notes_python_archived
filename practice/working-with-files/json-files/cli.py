"""
This file contains functions for requesting user via the CLI
"""

import database.db_controller as db

HELP_MSG = """
Help:
- 'a' to add a new todo
- 'l' to list all todos
- 'e' to edit a todo
- 'c' to toggle a todo's completion status
- 'd' to delete a specific todo
- 'q' to quit the application
- 'h' display help
"""


def prompt_add_todo():
    print("Creating new TODO...")
    msg = input("Enter your TODO message: ")

    created = False
    if msg:
        created = db.add_todo(msg)

    if created:
        print("New TODO successfully created!")
    else:
        print("Unable to create new TODO")


def prompt_list_todos():
    print("Listing TODOS...")
    todos = db.get_todos()
    for todo in todos:
        print(todo)


def prompt_edit_todo_msg():
    print("Preparing to edit TODO message...")
    id = input("Enter TODO ID to Edit: ")
    msg = input("Enter new TODO msg: ")

    updated = False
    if id and msg:
        updated = db.update_todo(int(id), msg, None)

    if updated:
        print(f"TODO with id {id} successfully updated")
    else:
        print(f"Unable to update TODO with ID {id}")


def prompt_toggle_complete():
    print("Toggling TODO completion status")
    id = input("Enter TODO ID to toggle completion status: ")

    if id:
        completed = db.toggle_complete(int(id))
        print(f"TODO with id {id} completion status: {completed}")


def prompt_delete_todo():
    print("Preparing to delete TODO...")
    id = input("Enter ID of TODO to delete: ")

    deleted = False
    if id:
        deleted = db.delete_todo(int(id))

    if deleted:
        print(f"Successfully deleted TODO with ID {id}")
    else:
        print(f"Unable to delete TODO with ID {id}")


def prompt_help():
    """
    Displays the help message to the console
    """
    print(HELP_MSG)


# Mapping of character keys to corresponding function
cli_options = {
    "a": prompt_add_todo,
    "l": prompt_list_todos,
    "e": prompt_edit_todo_msg,
    "c": prompt_toggle_complete,
    "d": prompt_delete_todo,
    "h": prompt_help,
}


def start_cli():
    """
    Prompts User for Input
    :return: None
    """
    db.create_db_if_not_exists()
    print(HELP_MSG)
    user_input = input("Please specify an option: ")
    while user_input != "q":
        if user_input in cli_options:
            cli_options[user_input]()
        user_input = input("Please specify an option: ")
    print("Exiting application...")
