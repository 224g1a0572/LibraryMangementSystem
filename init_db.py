# import sqlite3

# conn = sqlite3.connect('library.db')  # Use the same DB your Flask app uses
# cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS issues (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   member_id INTEGER,
#   book_id INTEGER,
#   issue_date TEXT,
#   return_date TEXT,
#   FOREIGN KEY (member_id) REFERENCES members(id),
#   FOREIGN KEY (book_id) REFERENCES books(id)
# )
# ''')

# conn.commit()
# conn.close()

# print("Table 'issues' created successfully.")
# Inside your app.py or a setup script
# import sqlite3

# conn = sqlite3.connect('library.db')  # or your DB_PATH
# cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS member_users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')
# conn.commit()
# conn.close()
import sqlite3

conn = sqlite3.connect('library.db')  # or your DB_PATH
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_email TEXT,
    book_name TEXT,
    issue_date TEXT,
    return_date TEXT
);

''')
conn.commit()
conn.close()
