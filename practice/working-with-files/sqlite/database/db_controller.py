"""
Responsible for Interfacing with the DB (SQLite file)
"""

import sqlite3

DB_NAME = "data.db"


def create_db_if_not_exists() -> None:
    """
    Create a new DB (SQLite) if one does not exist in the directory
    :return: None
    """
    _create_table_todos()


def get_todos() -> list[dict[str, any]]:
    """
    Return a list of all Todos in the DB
    :return: List of Todo Dictionaries
    """
    todos = []

    # Connect to SQLite DB
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Execute the SELECT query to fetch all records from the todos table
        cursor.execute("SELECT * FROM todos")
        rows = (
            cursor.fetchall()
        )  # fetch all rows returned from db query result set and store as list of tuples

        # Iterate through rows and create dictionary for each record
        for row in rows:
            todo = {"id": row[0], "msg": row[1], "complete": bool(row[2])}
            todos.append(todo)

    return todos


def get_todo_by_id(id: int) -> dict[str, any] | None:
    """
    Retrieve a Todo of specified ID from the DB
    :param id: The ID of the Todo to return
    :return: Todo of specified ID or None if not found
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Execute a SELECT query to fetch a record with the specified id
        cursor.execute("SELECT * FROM todos WHERE id = ?", (id,))
        row = cursor.fetchone()  # Retrieve 1st for (if any) from the result set

        # If a record is found, create a dictionary and return it
        if row:
            todo = {"id": row[0], "msg": row[1], "complete": bool(row[2])}
            return todo
        # If no record is found, return None
        else:
            return None


def add_todo(msg: str) -> bool:
    """
    Create a new Todo and add it to the DB
    :param msg: The message of the new Todo
    :return: Boolean representing if the book was updated or not
    """
    try:
        # Connect to the SQLite database
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Insert the new todo item with the given message and complete set to 0
            cursor.execute("INSERT INTO todos (msg, complete) VALUES (?, ?)", (msg, 0))

        # Return True if the operation is successful
        return True
    except sqlite3.Error as e:
        # Print the error and return False if the operation fails
        print(f"SQLite error: {e}")
        return False


def update_todo(id: int, new_msg: str = None, new_complete: bool = None) -> bool:
    """
    Update a Todo Item in the DB
    :param id: The ID of the Todo Item to update
    :param new_msg: The new message
    :param new_complete: The new completion status
    :return: Boolean representing if book was updated or not
    """
    try:
        # Connect to the SQLite database
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Prepare the update query
            query = "UPDATE todos SET "
            params = []

            if new_msg is not None:
                query += "msg = ?, "
                params.append(new_msg)

            if new_complete is not None:
                query += "complete = ?, "
                params.append(int(new_complete))

            # Remove trailing comma and space
            query = query.rstrip(", ")
            query += " WHERE id = ?"
            params.append(id)

            # Execute the update query
            cursor.execute(query, params)

            # Check if any rows were affected (meaning the update was successful)
            if cursor.rowcount == 0:
                return False

        # Return True if the operation is successful
        return True

    except sqlite3.Error as e:
        # Print the error and return False if the operation fails
        print(f"SQLite error: {e}")
        return False


def toggle_complete(id: int) -> bool | None:
    """
    Toggle the completion status of the todo
    :param id: ID of the todo
    :return: Boolean value representing completion status after toggle
    """
    try:
        # Connect to the SQLite database
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Fetch the current completion status of the todo with the given id
            cursor.execute("SELECT complete FROM todos WHERE id = ?", (id,))
            row = cursor.fetchone()

            # If there's no todo with the given id, return None
            if row is None:
                return None

            # Toggle the completion status
            current_complete = row[0]
            new_complete = not bool(current_complete)

            # Update the todo using update_todo function
            updated = update_todo(id, new_complete=new_complete)

            # If the update is successful, return the new completion status
            if updated:
                return new_complete

    except sqlite3.Error as e:
        # Print the error
        print(f"SQLite error: {e}")

    # Return None in case of any errors or if the todo was not found
    return None


def delete_todo(id: int) -> bool:
    """
    Delete the TODO w/ specified ID from the DB
    :param id: ID of the TODO to remove from the DB
    :return: Boolean value representing success or failure of todo deletion
    """
    try:
        # Connect to the SQLite database
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Delete the todo with the given id
            cursor.execute("DELETE FROM todos WHERE id = ?", (id,))

            # Check if any rows were affected (meaning delete was successful)
            if cursor.rowcount == 0:
                return False

        # Return True if the operation is successful
        return True

    except sqlite3.Error as e:
        # Print the error and return False if the operation fails
        print(f"SQLite error: {e}")
        return False


def _create_table_todos() -> None:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY, -- This column will be auto-populated
            msg TEXT NOT NULL,
            complete INTEGER NOT NULL
        )
        """

        cursor.execute(create_table_query)
