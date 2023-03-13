import sqlite3

# Step 1 — Creating a Connection to a SQLite Database
connection = sqlite3.connect("test.db")
print(connection.total_changes)
"""
connection.total_changes is the total number of database rows that have been 
changed by connection. Since we have not executed any SQL commands yet, 
0 total_changes is correct.

If, at any time, we find we want to start this tutorial again, we can delete 
the aquarium.db file from our computer.

Note: It is also possible to connect to a SQLite database that resides strictly 
in memory (and not in a file) by passing the special string ":memory:" into 
sqlite3.connect(). For example, sqlite3.connect(":memory:"). A ":memory:" 
SQLite database will disappear as soon as your Python program exits. This might 
be convenient if you want a temporary sandbox to try something out in SQLite, 
and don’t need to persist any data after your program exits.
"""

# Step 2 — Adding Data to the SQLite Database
cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER);")
# cursor.execute("INSERT INTO users VALUES ('Гвидо', 66)")

# Step 3 — Reading Data from the SQLite Database
rows = cursor.execute("SELECT name, age FROM users").fetchall()
print(rows)

connection.commit()
connection.close()
# 27:45

connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute("""create table if not exists users(name, age);""")
cursor.execute("""insert into users values ('Гвидо', 66);""")
connection.commit()
connection.close()
# 27:34
