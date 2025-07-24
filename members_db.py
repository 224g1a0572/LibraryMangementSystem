import sqlite3

conn = sqlite3.connect('library.db')  # Use the same DB your Flask app uses
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Table 'members' created successfully.")
