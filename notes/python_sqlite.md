# Using SQLite w/ Python

SQLite is a is a C library that provides a lightweight disk-based database. It doesn't require a separate server process and allows accessing the database using a nonstandard variant of SQL.

Python's standard library includes a module (`sqlite3`) for interacting with SQLite databases.

## Summary - Interacting w/ SQLite

```python
import sqlite3

# Setup / Connect to DB
DB_NAME = "data.db"
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    # Execute your Queries
    cursor.execute("<YOUR SQL QUERY HERE>")
    connection.commit()  # Save changes to the DB
```

OR

```python
import sqlite3

# Setup / Connect to DB
DB_NAME = "data.db"
connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# Execute your Queries
cursor.execute("<YOUR SQL QUERY HERE>")
connection.commit()  # Save changes to the DB

# Close Connections
cursor.close()
connection.close()
```

## Connecting to SQLite Database

```python
import sqlite3

DB_NAME = "data.db"  # Can be any name but this is conventional

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(DB_NAME)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
```

OR, using a context manager to automatically close the connection and cursor

```python
import sqlite3

# Setup / Connect to DB
# Connections will automatically be cleaned up
# If no error occurs, changes are also automatically committed
DB_NAME = "data.db"
with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
```

OR, Use a Custom Context Manager

```python
"""
# database_connection.py

Usage:
with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    ...
"""

# database_connection.py
import sqlite3

class DBConnection:
    def __init__(self, host):
        # Define connection and host
        self.connection = None
        self.host = host

    # Run this code when entering the context manager
    def __enter__(self):
        # Setup the connection
        self.connection = sqlite3.connect(self.host)
        return self.connection

    # Run this code when exiting the context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        # If there is an issue close the connection without saving
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            # Save DB changes, then close the connection to the DB
            self.connection.commit()
            self.connection.close()
```

```python

```

### What is a cursor object?

A cursor object in the context of databases, like SQLite, acts as an intermediary or a handle that allows you to interact with and manipulate the data stored in a database through SQL queries.

- You can have a single connection, but multiple cursors reading data at the same time, (only one cursor can write to the DB at a time)

Here's a breakdown of why and how cursor objects are used:

**1. Execution of SQL Commands:** A cursor is used to execute queries such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.

**2. Handling Query Results:** When you execute a `SELECT` query, the cursor fetches the data from the database and holds the result set in memory. You can then retrieve the rows one at a time or all at once.

**3. Transaction Management:** Cursors keep track of the context of the SQL commands, facilitating transaction management. When you modify data (insert, update, delete), the changes are not actually committed to the database until you call `commit()` on the connection object. This allows you to roll back changes if an error occurs.

**4. Resource Management:** Cursors help in efficiently managing resources. For instance, when dealing with large result sets, fetching rows one at a time prevents loading the entire data into memory.

Here's an example illustrating the use of a cursor object in Python with SQLite:

```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('lotr.db')

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL command using the cursor
cursor.execute('SELECT * FROM characters')

# Fetch and print all rows from the result set
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor
cursor.close()

# Close the connection
conn.close()
```

In this example:

- We create a cursor object `cursor` from the connection `conn`.
- The cursor is used to execute an SQL `SELECT` query.
- We then fetch all rows from the query result using `fetchall()`.
- Finally, we close the cursor and the connection.

By using a cursor, you can ensure that the interaction with the database is efficient and manageable.

## Executing SQL Commands

Use `cursor.execute(<SQL Query>)` to execute a SQL command

## Saving Results of SQL Query

Use `cursor.commit()` to save changes to the DB

## SQLite Data Types

SQLite has 5 data types:

- `NULL` -- Represents missing data or an unknown value
- `INTEGER` -- Signed integer
- `REAL` -- Floating point value
- `TEXT` -- String
- `BLOB` -- A blob of data (images, documents, binary data)

## SQL CRUD Operations

### Create a Table

```python
# SQL command to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    race TEXT NOT NULL,
    realm TEXT
)
'''

# Execute the SQL command
cursor.execute(create_table_query)
```

### Insert Data

```python
# SQL command to insert data
insert_data_query = '''
INSERT INTO characters (name, race, realm) VALUES (?, ?, ?)
'''

# LOTR character data
characters = [('Frodo', 'Hobbit', 'Shire'),
              ('Aragorn', 'Human', 'Gondor'),
              ('Gandalf', 'Maia', 'Valinor')]

# Execute the SQL command for each character
for character in characters:
    cursor.execute(insert_data_query, character)

# Commit the transaction
conn.commit()
```

### Query Data

```python
# SQL command to query data
query_data = '''
SELECT * FROM characters
'''

# Execute the SQL command
cursor.execute(query_data)

# Fetch all rows (returns an array of tuples)
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)
```

`fetchall()`, `fetchone()`, and `fetchmany(size)` are methods to retrieve data from the result set returned by executing a `SELECT` query in SQLite

- `fetchall()`
  - Retrieves all rows of a query result
  - Returns a list of tuples where each tuple corresponds to a row in the result set
  - If there are no rows to fetch, it returns an empty list
- `fetchone()`
  - Retrieves the next row of a query result
  - Returns a single tuple representing a row or `None` if there are no more rows to fetch
- `fetchmany(<size>)`
  - Fetches the next set of rows of a query result, returning a list of tuples
  - Optional `size` parameter can be provided to specify the number of rows to retrieve (default value is set to 1)
  - If no more rows are available, it returns an empty list

```python
import sqlite3

# Sample data
data = [(1, "Explore the dungeon"), (2, "Defeat the orcs"), (3, "Find the treasure")]

# Connect to an in-memory SQLite database and insert sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE quests (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL
)
''')
cursor.executemany('INSERT INTO quests (id, description) VALUES (?, ?)', data)
conn.commit()

# fetchall() example
cursor.execute("SELECT * FROM quests")
print("fetchall():", cursor.fetchall())

# fetchone() example
cursor.execute("SELECT * FROM quests")
print("fetchone():", cursor.fetchone())

# fetchmany(size) example
cursor.execute("SELECT * FROM quests")
print("fetchmany(2):", cursor.fetchmany(2))

conn.close()
```

```txt
fetchall(): [(1, 'Explore the dungeon'), (2, 'Defeat the orcs'), (3, 'Find the treasure')]
fetchone(): (1, 'Explore the dungeon')
fetchmany(2): [(1, 'Explore the dungeon'), (2, 'Defeat the orcs')]
```

### Update / Delete Data

```python
# Update data
cursor.execute("UPDATE characters SET realm = 'Rivendell' WHERE name = 'Aragorn'")
conn.commit()

# Delete data
cursor.execute("DELETE FROM characters WHERE name = 'Gandalf'")
conn.commit()
```

## Resources / References

- [Sqlite](https://www.sqlite.org/index.html)
- [Python - sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [freeCodeCamp - SQLite Databases with Python](https://www.youtube.com/watch?v=byHcYRpMgI4)
- [Real Python - Data Management w/ Python, SQLite, and SQLAlchemy](https://realpython.com/python-sqlite-sqlalchemy/)
