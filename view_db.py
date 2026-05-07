from db import get_db_connection

conn = get_db_connection()

users = conn.execute("SELECT * FROM users").fetchall()

for user in users:
    print(dict(user))

conn.close()