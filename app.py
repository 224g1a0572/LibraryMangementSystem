# from flask import Flask, render_template, request, redirect, session, flash, url_for
# import sqlite3
# import os

# app = Flask(__name__)
# app.secret_key = 'secretkey'

# DB_PATH = 'library.db'

# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------- Home ----------
# @app.route('/')
# def index():
#     return render_template('index.html')

# # ---------- Admin Routes ----------
# @app.route('/admin/login', methods=['GET', 'POST'])
# def admin_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         admin = conn.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password)).fetchone()
#         conn.close()
#         if admin:
#             session['admin'] = username
#             return redirect('/admin/dashboard')
#         flash("Invalid admin credentials", "error")
#         return redirect('/admin/login')
#     return render_template('admin_login.html')
# import sqlite3

# @app.route('/add_book', methods=['GET', 'POST'])
# def add_book():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         isbn = request.form['isbn']

#         # Store in SQLite
#         conn = sqlite3.connect('library.db')
#         cur = conn.cursor()
#         cur.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
#         conn.commit()
#         conn.close()

#         flash("Book added successfully!", "success")
#         return redirect('/add_book')

#     return render_template('add_book.html')  
# def init_db():
#     conn = sqlite3.connect('library.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         title TEXT NOT NULL,
#                         author TEXT NOT NULL,
#                         isbn TEXT NOT NULL
#                       )''')
#     conn.commit()
#     conn.close()

# init_db()

# @app.route('/admin/signup', methods=['GET', 'POST'])
# def admin_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         conn.execute("INSERT INTO admins (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()
#         flash("Admin account created!", "success")
#         return redirect('/admin/login')
#     return render_template('admin_signup.html')

# @app.route('/view-books')
# def view_books():
#     return render_template('view_books.html')  # Or return any content for now



# @app.route('/admin/dashboard')
# def admin_dashboard():
#     if 'admin' not in session:
#         return redirect('/admin/login')
#     return render_template('admin_dashboard.html', admin=session['admin'])

# # ---------- Member Routes ----------
# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         member = conn.execute("SELECT * FROM members WHERE username=? AND password=?", (username, password)).fetchone()
#         conn.close()
#         if member:
#             session['member'] = username
#             return redirect('/member/dashboard')
#         flash("Invalid member credentials", "error")
#         return redirect('/member/login')
#     return render_template('member_login.html')


# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         conn.execute("INSERT INTO members (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()
#         flash("Member account created!", "success")
#         return redirect('/member/login')
#     return render_template('member_signup.html')


# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member' not in session:
#         return redirect('/member/login')
#     return render_template('member_dashboard.html', member=session['member'])

# # ---------- Logout ----------
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully!", "success")
#     return redirect('/')

# # ---------- Init DB (Run once to create tables) ----------
# def init_db():
#     if not os.path.exists(DB_PATH):
#         conn = get_db_connection()
#         conn.execute('''
#             CREATE TABLE admins (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL UNIQUE,
#                 password TEXT NOT NULL
#             )
#         ''')
#         conn.execute('''
#             CREATE TABLE members (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL UNIQUE,
#                 password TEXT NOT NULL
#             )
#         ''')
#         conn.commit()
#         conn.close()

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # -------------------------------
# # Database Setup (Optional)
# # -------------------------------
# def init_db():
#     conn = sqlite3.connect('library.db')
#     cursor = conn.cursor()
    
#     # Create books table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             author TEXT NOT NULL,
#             isbn TEXT NOT NULL
#         )
#     ''')
    
#     # Create members table (optional)
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS members (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT
#         )
#     ''')

#     conn.commit()
#     conn.close()

# # -------------------------------
# # Routes
# # -------------------------------

# @app.route('/')
# def home():
#     return render_template('index.html')  # You can create this later

# @app.route('/admin/dashboard')
# def admin_dashboard():
#     return render_template('admin_dashboard.html')

# @app.route('/admin/add_book', methods=['GET', 'POST'])
# def add_book():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         isbn = request.form['isbn']

#         conn = sqlite3.connect('library.db')
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
#         conn.commit()
#         conn.close()

#         return redirect(url_for('view_books'))
    
#     return render_template('add_book.html')

# @app.route('/admin/view-books')
# def view_books():
#     conn = sqlite3.connect('library.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM books")
#     books = cursor.fetchall()
#     conn.close()
#     return render_template('view_books.html', books=books)

# @app.route('/admin/view-members')
# def view_members():
#     # Placeholder: implement as needed
#     return render_template('view_members.html')

# @app.route('/admin/issue-book')
# def issue_book():
#     # Placeholder: implement as needed
#     return render_template('issue_book.html')

# @app.route('/admin/return-book')
# def return_book():
#     # Placeholder: implement as needed
#     return render_template('return_book.html')

# @app.route('/admin/reports')
# def reports():
#     return render_template('reports.html')

# @app.route('/admin/notifications')
# def notifications():
#     return render_template('notifications.html')


# # -------------------------------
# # Start the App
# # -------------------------------
# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, session, flash, url_for
# import sqlite3
# import os

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'
# DB_PATH = 'library.db'

# # ----------------------------
# # Database Connection
# # ----------------------------
# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ----------------------------
# # Database Initialization
# # ----------------------------
# def init_db():
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS members (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         author TEXT NOT NULL,
#         isbn TEXT NOT NULL
#     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS issues (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         member_id INTEGER,
#         book_id INTEGER,
#         issue_date TEXT,
#         return_date TEXT,
#         FOREIGN KEY (member_id) REFERENCES members(id),
#         FOREIGN KEY (book_id) REFERENCES books(id)
#     )''')

#     conn.commit()
#     conn.close()

# # ----------------------------
# # Routes
# # ----------------------------

# @app.route('/')
# def index():
#     return render_template('index.html')

# # Admin Signup/Login/Dashboard
# @app.route('/admin/signup', methods=['GET', 'POST'])
# def admin_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         conn.execute("INSERT INTO admins (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()
#         flash("Admin account created!", "success")
#         return redirect('/admin/login')
#     return render_template('admin_signup.html')

# @app.route('/admin/login', methods=['GET', 'POST'])
# def admin_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         admin = conn.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password)).fetchone()
#         conn.close()
#         if admin:
#             session['admin'] = username
#             return redirect('/admin/dashboard')
#         flash("Invalid admin credentials", "error")
#     return render_template('admin_login.html')

# @app.route('/admin/dashboard')
# def admin_dashboard():
#     if 'admin' not in session:
#         return redirect('/admin/login')
#     return render_template('admin_dashboard.html', admin=session['admin'])

# # Add Book
# @app.route('/add_book', methods=['GET', 'POST'])
# def add_book():
#     if 'admin' not in session:
#         return redirect('/admin/login')

#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         isbn = request.form['isbn']

#         conn = get_db_connection()
#         conn.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
#         conn.commit()
#         conn.close()

#         flash("Book added successfully!", "success")
#         return redirect(url_for('add_book'))

#     return render_template('add_book.html')

# # View Books
# @app.route('/admin/view-books')
# def view_books():
#     if 'admin' not in session:
#         return redirect('/admin/login')

#     conn = get_db_connection()
#     books = conn.execute("SELECT * FROM books").fetchall()
#     conn.close()
#     return render_template('view_books.html', books=books)

# # Issue Book
# @app.route('/admin/issue_book', methods=['GET', 'POST'])
# def issue_book():
#     if 'admin' not in session:
#         return redirect('/admin/login')

#     conn = get_db_connection()
#     cursor = conn.cursor()

#     if request.method == 'POST':
#         member_id = request.form['member_id']
#         book_id = request.form['book_id']
#         issue_date = request.form['issue_date']
#         return_date = request.form['return_date']

#         cursor.execute('''
#             INSERT INTO issues (member_id, book_id, issue_date, return_date)
#             VALUES (?, ?, ?, ?)
#         ''', (member_id, book_id, issue_date, return_date))
#         conn.commit()
#         flash("Book issued successfully!", "success")
#         return redirect(url_for('issue_book'))

#     members = cursor.execute('SELECT id, username FROM members').fetchall()
#     books = cursor.execute('SELECT id, title FROM books').fetchall()

#     conn.close()
#     return render_template('issue_book.html', members=members, books=books)

# # Member Signup/Login/Dashboard
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         conn.execute("INSERT INTO members (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         conn.close()
#         flash("Member account created!", "success")
#         return redirect('/member/login')
#     return render_template('member_signup.html')

# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         member = conn.execute("SELECT * FROM members WHERE username=? AND password=?", (username, password)).fetchone()
#         conn.close()
#         if member:
#             session['member'] = username
#             return redirect('/member/dashboard')
#         flash("Invalid member credentials", "error")
#     return render_template('member_login.html')

# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member' not in session:
#         return redirect('/member/login')
#     return render_template('member_dashboard.html', member=session['member'])

# # Logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully!", "success")
#     return redirect('/')

# # ----------------------------
# # Start the App
# # ----------------------------
# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3
import os
from datetime import datetime,timedelta 

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
DB_PATH = 'library.db'

# ----------------------------
# Database Connection
# ----------------------------
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ----------------------------
# Database Initialization
# ----------------------------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows dictionary-like row access
    return conn
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS issues (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  member_id TEXT,
  member_name TEXT,
  book_id TEXT,
  book_title TEXT,
  issue_date TEXT,
  return_date TEXT
);
''')

    conn.commit()
    conn.close()

# ----------------------------
# Routes
# ----------------------------

@app.route('/')
def index():
    return render_template('index.html')

# Admin Signup/Login/Dashboard
@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        conn.execute("INSERT INTO admins (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        flash("Admin account created!", "success")
        return redirect('/admin/login')
    return render_template('admin_signup.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        admin = conn.execute("SELECT * FROM admins WHERE username=? AND password=?", (username, password)).fetchone()
        conn.close()
        if admin:
            session['admin'] = username
            return redirect('/admin/dashboard')
        flash("Invalid admin credentials", "error")
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin' not in session:
        return redirect('/admin/login')
    return render_template('admin_dashboard.html', admin=session['admin'])

# Add Book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if 'admin' not in session:
        return redirect('/admin/login')

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']

        conn = get_db_connection()
        conn.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", (title, author, isbn))
        conn.commit()
        conn.close()

        flash("Book added successfully!", "success")
        return redirect(url_for('add_book'))

    return render_template('add_book.html')

books = [
    {'id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565', 'edition': '1st'},
    {'id': '2', 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '9780060935467', 'edition': '2nd'},
    {'id': '3', 'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935', 'edition': '3rd'},
    {'id': '4', 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'isbn': '9780141439518', 'edition': '2nd'},
    {'id': '5', 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'isbn': '9780316769488', 'edition': '1st'},
    {'id': '6', 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '9780547928227', 'edition': '4th'},
    {'id': '7', 'title': 'Moby Dick', 'author': 'Herman Melville', 'isbn': '9781503280786', 'edition': '2nd'},
    {'id': '8', 'title': 'War and Peace', 'author': 'Leo Tolstoy', 'isbn': '9780199232765', 'edition': '3rd'},
    {'id': '9', 'title': 'Jane Eyre', 'author': 'Charlotte Brontë', 'isbn': '9780142437209', 'edition': '1st'},
    {'id': '10', 'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'isbn': '9780486415871', 'edition': '2nd'},
    {'id': '11', 'title': 'Brave New World', 'author': 'Aldous Huxley', 'isbn': '9780060850524', 'edition': '3rd'},
    {'id': '12', 'title': 'The Odyssey', 'author': 'Homer', 'isbn': '9780140268867', 'edition': '2nd'},
    {'id': '13', 'title': 'Harry Potter and the Sorcerer\'s Stone', 'author': 'J.K. Rowling', 'isbn': '9780590353427', 'edition': '1st'},
    {'id': '14', 'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'isbn': '9780618640157', 'edition': '3rd'},
    {'id': '15', 'title': 'The Alchemist', 'author': 'Paulo Coelho', 'isbn': '9780061122415', 'edition': '2nd'}
]

@app.route('/admin/view-books')
def view_books():
    return render_template('view_books.html', books=books)

@app.route('/admin/edit-book/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['isbn'] = request.form['isbn']
        book['edition'] = request.form['edition']
        return redirect(url_for('view_books'))

    return render_template('edit_book.html', book=book)
# Issue Book
@app.route('/admin/issue_book', methods=['GET', 'POST'])
def issue_book():
    if 'admin' not in session:
        return redirect('/admin/login')

    # ✅ At least 15 predefined books
    books = [
        {'id': '1', 'title': 'The Great Gatsby'},
        {'id': '2', 'title': 'To Kill a Mockingbird'},
        {'id': '3', 'title': '1984'},
        {'id': '4', 'title': 'Pride and Prejudice'},
        {'id': '5', 'title': 'The Catcher in the Rye'},
        {'id': '6', 'title': 'The Hobbit'},
        {'id': '7', 'title': 'Moby Dick'},
        {'id': '8', 'title': 'War and Peace'},
        {'id': '9', 'title': 'Jane Eyre'},
        {'id': '10', 'title': 'Crime and Punishment'},
        {'id': '11', 'title': 'Brave New World'},
        {'id': '12', 'title': 'The Odyssey'},
        {'id': '13', 'title': 'Harry Potter and the Sorcerer\'s Stone'},
        {'id': '14', 'title': 'The Lord of the Rings'},
        {'id': '15', 'title': 'The Alchemist'}
    ]

    if request.method == 'POST':
        member_id = request.form['member_id']
        member_name = request.form['member_name']
        book_id = request.form['book_id']
        book_title = next((book['title'] for book in books if book['id'] == book_id), '')
        issue_date = request.form['issue_date']
        return_date = request.form['return_date']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO issues (member_id, member_name, book_id, book_title, issue_date, return_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (member_id, member_name, book_id, book_title, issue_date, return_date))
        conn.commit()
        conn.close()

        flash("Book issued successfully!", "success")
        return redirect(url_for('issue_book'))

    return render_template('issue_book.html', books=books)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            branch TEXT,
            section TEXT,
            phone TEXT,
            email TEXT UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route to display member login page
# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = get_db_connection()
#         member = conn.execute(
#             'SELECT * FROM members WHERE email = ? AND password = ?',
#             (email, password)
#         ).fetchone()
#         conn.close()

#         if member:
#             session['member_email'] = email
#             return redirect('/member/dashboard')
#         else:
#             return "Invalid email or password"

#     return render_template('member_login.html')

# # # Route to show member dashboard
# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member_email' not in session:
#         return redirect('/member/login')

#     conn = get_db_connection()
#     member = conn.execute(
#         'SELECT * FROM members WHERE email = ?',
#         (session['member_email'],)
#     ).fetchone()
#     conn.close()

#     return render_template('member_dashboard.html', member=member)

# Member logout
# @app.route('/member/logout')
# def member_logout():
#     session.pop('member_email', None)
#     return redirect('/member/login')

# @app.route('/return-book', methods=['GET', 'POST'])
# def return_book():
#     if request.method == 'POST':
#         member_id = request.form.get('member_id')
#         conn = sqlite3.connect('library.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM issues WHERE member_id = ? AND return_date IS NULL", (member_id,))
#         books = cursor.fetchall()
#         conn.close()
#         return render_template('return_book.html', books=books)

#     return render_template('return_book.html')

# make sure this import exists

# @app.route('/return-book', methods=['GET', 'POST'])
# def return_book():
#     if request.method == 'POST':
#         member_id = request.form.get('member_id')
#         conn = sqlite3.connect('library.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM issues WHERE member_id = ? AND return_date IS NULL", (member_id,))
#         books = cursor.fetchall()
#         conn.close()
#         return render_template('return_book.html', books=books)

#     return render_template('return_book.html')

# @app.route('/return-book', methods=['GET', 'POST'])
# def return_book():
#     books = []
#     if request.method == 'POST':
#         member_id = request.form.get('member_id')
#         conn = sqlite3.connect('library.db')
#         conn.row_factory = sqlite3.Row  # So you can use book['book_title'] or book.book_title
#         cursor = conn.cursor()

#         # Fetch books issued to this member that are not returned yet
#         cursor.execute("SELECT * FROM issues WHERE member_id = ? AND return_date IS NULL", (member_id,))
#         books = cursor.fetchall()

#         conn.close()
#         return render_template('return_book.html', books=books)

#     return render_template('return_book.html', books=None)

# @app.route('/return-book/<int:issue_id>', methods=['POST'])
# def process_return(issue_id):
#     conn = sqlite3.connect('library.db')
#     cursor = conn.cursor()

#     # Get issue details
#     cursor.execute("SELECT issue_date FROM issues WHERE id = ?", (issue_id,))
#     result = cursor.fetchone()

#     if result:
#         issue_date_str = result[0]
#         issue_date = datetime.strptime(issue_date_str, "%Y-%m-%d")
#         return_date = datetime.now()
#         days_taken = (return_date - issue_date).days
#         fine = 0
#         if days_taken > 7:
#             fine = (days_taken - 7) * 10  # ₹10 per extra day

#         # Update return info
#         cursor.execute("""
#             UPDATE issues
#             SET return_date = ?, fine = ?
#             WHERE id = ?
#         """, (return_date.strftime("%Y-%m-%d"), fine, issue_id))
#         conn.commit()
#         conn.close()
#         return render_template("return_book.html", fine=fine)

#     return "Issue ID not found", 404

@app.route('/return-book', methods=['GET', 'POST'])
def return_book():
    books = []
    if request.method == 'POST':
        member_id = request.form['member_id']

        conn = sqlite3.connect('library.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM issues WHERE member_id = ? AND fine IS NOT NULL", (member_id,))
        rows = cur.fetchall()

        for row in rows:
            # Fine calculation
            issue_date = datetime.strptime(row['issue_date'], '%Y-%m-%d')
            return_date = datetime.strptime(row['return_date'], '%Y-%m-%d')
            current_date = datetime.now()
            
            fine = 0
            if current_date > return_date:
                days_late = (current_date - return_date).days
                fine = days_late * 5  # ₹5 per late day
            
            books.append({
                'id': row['id'],
                'member_id': row['member_id'],
                'member_name': row['member_name'],
                'book_title': row['book_title'],
                'issue_date': row['issue_date'],
                'return_date': row['return_date'],
                'fine': fine
            })

        conn.close()

    return render_template('return_book.html', books=books)


@app.route('/reports', methods=['GET', 'POST'])
def reports():
    reports = []
    if request.method == 'POST':
        report_type = request.form['report_type']
        conn = sqlite3.connect('library.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        today = datetime.today().date()

        if report_type == 'daily':
            start_date = today
        elif report_type == 'weekly':
            start_date = today - timedelta(days=7)
        elif report_type == 'monthly':
            start_date = today - timedelta(days=30)
        else:
            start_date = today  # Default to daily

        cursor.execute('''
            SELECT * FROM issues 
            WHERE issue_date >= ?
            ORDER BY issue_date DESC
        ''', (start_date.strftime('%Y-%m-%d'),))

        records = cursor.fetchall()

        for row in records:
            report_line = f"Member: {row['member_name']}, Book: {row['book_title']}, Issued: {row['issue_date']}"
            if row['return_date']:
                report_line += f", Returned: {row['return_date']}"
            else:
                report_line += ", Not Returned"
            reports.append(report_line)

        conn.close()

    return render_template('reports.html', reports=reports)


# Member Signup/Login/Dashboard
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         c.execute("INSERT INTO members (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#         conn.commit()
#         conn.close()

#         flash('Signup successful! Please login.')
#         return redirect(url_for('member_login'))

#     return render_template('member_signup.html')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )''')
init_db()

# Member Signup Route
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         with sqlite3.connect(DB_PATH) as conn:
#             try:
#                 conn.execute("INSERT INTO members (name, email, password) VALUES (?, ?, ?)",
#                              (name, email, password))
#                 conn.commit()
#                 flash('Signup successful! Please log in.', 'success')
#                 return redirect(url_for('member_login'))
#             except sqlite3.IntegrityError:
#                 flash('Email already exists.', 'error')
#     return render_template('member_signup.html')

# # Member Login Route
# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM members WHERE email=? AND password=?", (email, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session['member_id'] = user[0]
#             session['member_name'] = user[1]
#             return redirect(url_for('member_dashboard'))  # Redirect to dashboard
#         else:
#             flash("Invalid email or password", "error")
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')

# --------------------------------------------
# Route: Member Signup (with auto-login)
# --------------------------------------------
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         # Create table if it doesn't exist
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS member_users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 email TEXT UNIQUE,
#                 password TEXT
#             )
#         ''')

    #     try:
    #         cursor.execute("INSERT INTO member_users (name, email, password) VALUES (?, ?, ?)", 
    #                        (name, email, password))
    #         conn.commit()

    #         # Set session and redirect to dashboard
    #         session['member_email'] = email
    #         session['member_name'] = name
    #         return redirect(url_for('member_dashboard'))

    #     except sqlite3.IntegrityError:
    #         flash("Email already exists. Please login.")
    #         return redirect(url_for('member_login'))

    #     finally:
    #         conn.close()

    # # 👉 Correct rendering for GET request (show signup form)
    # return render_template('member_signup.html')

# # --------------------------------------------
# # Route: Member Login
# # --------------------------------------------
# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute("SELECT name FROM member_users WHERE email = ? AND password = ?", (email, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session['member_email'] = email
#             session['member_name'] = user[0]
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash("Invalid credentials. Try again.")

#     return render_template('member_login.html')

# # --------------------------------------------
# # Route: Member Dashboard

# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member_email' in session:
#         return f"<h2>Welcome, {session['member_name']}!</h2><p>This is your member dashboard.</p>"
#     else:
#         return redirect(url_for('member_login'))



# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = get_db_connection()
#         member = conn.execute("SELECT * FROM members WHERE username=? AND password=?", (username, password)).fetchone()
#         conn.close()
#         if member:
#             session['member'] = username
#             return redirect('/member/dashboard')
#         flash("Invalid member credentials", "error")
#     return render_template('member_login.html')

# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         # Match email and password
#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         member = cursor.fetchone()
#         conn.close()

#         if member:
#             session['member_email'] = email
#             session['member_name'] = member[1]  # name is 2nd column
#             return redirect(url_for('member_dashboard'))
#         else:
#             return "Invalid email or password"

#     return render_template('member_login.html')


# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member' not in session:
#         return redirect('/member/login')
#     return render_template('member_dashboard.html', member=session['member'])



# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session['member_email'] = user[2]
#             session['member_name'] = user[1]
#             return redirect(url_for('member_dashboard'))
#         else:
#             return "Invalid email or password"
#     return render_template('member_login.html')

# Logout
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("Logged out successfully!", "success")
#     return redirect('/')
# def insert_sample_member():
#     conn = get_db_connection()
#     conn.execute('''
#         INSERT OR IGNORE INTO members (name, branch, section, phone, email, password)
#         VALUES (?, ?, ?, ?, ?, ?)
#     ''', ('John', 'CSE', 'A', '9876543210', 'john@example.com', 'password123'))
#     conn.commit()
#     conn.close()


# ----------------------------
# Start the App
# ----------------------------


# --- Member Signup ---
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS member_users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 password TEXT NOT NULL
#             )
#         ''')

#         try:
#             cursor.execute('INSERT INTO member_users (name, email, password) VALUES (?, ?, ?)',
#                            (name, email, password))
#             conn.commit()
#             session['member_email'] = email
#             session['member_name'] = name
#             return redirect(url_for('member_dashboard'))
#         except sqlite3.IntegrityError:
#             flash("Email already registered. Please login.")
#             return redirect(url_for('member_login'))
#         finally:
#             conn.close()

#     return render_template('member_signup.html')


# --- Member Login ---
# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         print("Login form submitted")
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session['member_email'] = user[2]   # user[2] = email
#             session['member_name'] = user[1]   # user[1] = name
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash("Invalid email or password")
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')


# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         print("Login form submitted")
#         email = request.form['email']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         user = cursor.fetchone()
#         conn.close()

#         if user:
#             session['member_email'] = user[2]   # user[2] = email
#             session['member_name'] = user[1]   # user[1] = name
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash("Invalid email or password")
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')

# --- Member Dashboard ---

# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         print("Login form submitted")
#         email = request.form['email']
#         password = request.form['password']
#         print("Email:", email)
#         print("Password:", password)

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         user = cursor.fetchone()
#         print("User fetched from DB:", user)
#         conn.close()

#         if user:
#             session['member_email'] = user[2]
#             session['member_name'] = user[1]
#             print("Login success, redirecting to dashboard")
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash("Invalid email or password")
#             print("Invalid login attempt")
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')

# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         print("Form submitted.")
#         email = request.form.get('email')
#         password = request.form.get('password')
#         print(f"Email: {email}, Password: {password}")

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM member_users WHERE email = ? AND password = ?', (email, password))
#         user = cursor.fetchone()
#         print("User from DB:", user)
#         conn.close()

#         if user:
#             session['member_email'] = user[2]
#             session['member_name'] = user[1]
#             print("Login successful.")
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash("Invalid email or password")
#             print("Login failed.")
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')


# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member_email' in session:
#         return render_template('member_dashboard.html', name=session['member_name'])
#     else:
#         flash("Please login first.")
#         return redirect(url_for('member_login'))


# # --- Member Logout ---
# @app.route('/member/logout')
# def member_logout():
#     session.clear()
#     return redirect(url_for('member_login'))
# @app.route('/member/login')
# def member_options():
#     return render_template('member_options.html')

# # Member Signup
# @app.route('/member/signup', methods=['GET', 'POST'])
# def member_signup():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO members (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#         conn.commit()
#         conn.close()
#         session['member'] = name
#         return redirect('/member/dashboard')
#     return render_template('member_signup.html')

# # Member Login
# @app.route('/member/loginform', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("SELECT name FROM members WHERE email = ? AND password = ?", (email, password))
#         user = cursor.fetchone()
#         conn.close()
#         if user:
#             session['member'] = user[0]
#             return redirect('/member/dashboard')
#         else:
#             flash("Invalid login details")
#             return redirect('/member/loginform')
#     return render_template('member_login.html')

# # Member Dashboard
# @app.route('/member/dashboard')
# def member_dashboard():
#     if 'member' in session:
#         return f"<h1>Welcome {session['member']} to your Member Dashboard!</h1>"
#     else:
#         return redirect('/member/login')

# --- Database Connection ---
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- Create Table if Not Exists ---
def create_member_table():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

create_member_table()

# --- Home Page ---
@app.route('/')
def home():
    return render_template('home.html')

# --- Member Signup ---
@app.route('/member/signup', methods=['GET', 'POST'])
def member_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        try:
            conn.execute("INSERT INTO members (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            flash('Signup successful! Please log in.')
            return redirect('/member/login')
        except sqlite3.IntegrityError:
            flash('Email already exists!')
            return redirect('/member/signup')
        finally:
            conn.close()
    return render_template('member_signup.html')

# --- Member Login ---
@app.route('/member/login', methods=['GET', 'POST'])
def member_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("SELECT * FROM members WHERE email=? AND password=?", (email, password))
        member = cur.fetchone()
        con.close()

        if member:
            session['member_id'] = member[0]
            session['member_name'] = member[1]
            return redirect('/member/dashboard')
        else:
            flash("Invalid credentials", "danger")
            return render_template('member_login.html')
    return render_template('member_login.html')
# @app.route('/member_login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         con = sqlite3.connect(DB_PATH)
#         cur = con.cursor()
#         cur.execute("SELECT * FROM members WHERE username=? AND password=?", (username, password))
#         user = cur.fetchone()
#         con.close()

#         if user:
#             session['member_id'] = user[0]
#             session['member_name'] = user[1]
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash('Invalid credentials. Please try again.', 'danger')
#             return redirect(url_for('member_login'))

#     return render_template('member_login.html')


# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         con = sqlite3.connect(DB_PATH)
#         cur = con.cursor()
#         cur.execute("SELECT * FROM members WHERE email=? AND password=?", (email, password))
#         member = cur.fetchone()
#         con.close()

#         if member:
#             session['member_email'] = email  # ✅ this must match what's checked in protected routes
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash('Invalid credentials')
#             return render_template('member_login.html')

#     return render_template('member_login.html')
# @app.route('/thank-you')
# def thank_you():
#     return render_template('thank_you.html')



# @app.route('/member/login', methods=['GET', 'POST'])
# def member_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM member_users WHERE email=? AND password=?", (email, password))
#         user = cursor.fetchone()
#         conn.close()
#         if user:
#             session['member_id'] = user[0]
#             session['member_email'] = user[2]  # Assuming user[2] is email
#             return redirect(url_for('member_dashboard'))
#         else:
#             flash('Invalid credentials')
#     return render_template('member_login.html')
@app.route('/member/request-book', methods=['GET', 'POST'])
def request_book():
    # if 'member_email' not in session:
    #     flash('Please login first')
    #     return redirect(url_for('member_login'))

    if request.method == 'POST':
        name = request.form['name']
        branch = request.form['branch']
        section = request.form['section']
        book_name = request.form['book_name']
        author = request.form['author']
        edition = request.form['edition']

        # Optional: Save request in DB here

        # Optional: Send email notification (mocked)
        flash("Book request submitted successfully! You will be notified.")
        return redirect(url_for('thank_you'))

    return render_template('request_book.html')

# --- Member Dashboard ---
@app.route('/member/dashboard')
def member_dashboard():
    if 'member_id' not in session:
        return redirect('/member/login')

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM members WHERE id=?", (session['member_id'],))
    member = cur.fetchone()
    con.close()

    return render_template("member_dashboard.html", member=member)
@app.route('/member/view-issued')
def view_issued_books():
    if 'member_email' not in session:
        return redirect(url_for('member_login'))

    member_id = session['member_id']

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT book_title, issue_date, return_date FROM issued_books WHERE member_id=?", (member_id,))
    books = cursor.fetchall()
    conn.close()

    return render_template('view_issued_books.html', books=books)


# --- Logout ---
# @app.route('/logout')
# def logout():
#     session.clear()
#     flash("You have been logged out.")
#     return redirect('/')
@app.route('/member/logout')
def member_logout():
    session.clear()
    return redirect(url_for('member_login'))
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # Create thank_you.html in templates/



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
