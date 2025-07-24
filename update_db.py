import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Add member_name column
try:
    cursor.execute('ALTER TABLE issues ADD COLUMN member_name TEXT')
    print("Column 'member_name' added.")
except sqlite3.OperationalError:
    print("Column 'member_name' already exists.")

# Add book_title column
try:
    cursor.execute('ALTER TABLE issues ADD COLUMN book_title TEXT')
    print("Column 'book_title' added.")
except sqlite3.OperationalError:
    print("Column 'book_title' already exists.")

conn.commit()
conn.close()
