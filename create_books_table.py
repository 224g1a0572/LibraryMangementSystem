# import sqlite3

# # Connect to (or create) the database file
# conn = sqlite3.connect('library.db')  # This will create library.db in your folder
# cursor = conn.cursor()

# # Create the books table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS b (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         author TEXT NOT NULL,
#         isbn TEXT NOT NULL
#     )
               
#     CREATE TABLE members (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL
# );



# ''')

# conn.commit()
# conn.close()

# print("📚 Table 'b' created successfully in 'library.db'!")

import sqlite3

# Connect to your database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Drop the old table if it exists (optional for development)
cursor.execute("DROP TABLE IF EXISTS members")

# Create a new members table
cursor.execute('''
CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

print("Table 'members' created successfully.")

conn.commit()
conn.close()
