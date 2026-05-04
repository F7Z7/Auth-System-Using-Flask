import sqlite3

def get_db_connection():
    conn=sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # makes results like dict
    return conn

conn=get_db_connection()
conn.execute('''CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
username varchar(255) NOT NULL UNIQUE,
password TEXT NOT NULL,
role TEXT NOT NULL
)
''')

conn.commit()
conn.close()