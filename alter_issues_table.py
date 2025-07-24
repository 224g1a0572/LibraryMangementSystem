import sqlite3

def add_column_if_not_exists(cursor, table_name, column_name, column_type):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [info[1] for info in cursor.fetchall()]
    if column_name not in columns:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        print(f"Added column '{column_name}'")
    else:
        print(f"Column '{column_name}' already exists.")

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

add_column_if_not_exists(cursor, 'issues', 'fine', 'INTEGER DEFAULT 0')
add_column_if_not_exists(cursor, 'issues', 'return_date', 'TEXT')
add_column_if_not_exists(cursor, 'issues', 'issue_date', 'TEXT')

conn.commit()
conn.close()

print("Column update complete.")
