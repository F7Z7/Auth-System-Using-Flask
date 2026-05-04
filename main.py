from flask import Flask, request, render_template, redirect, jsonify
from db import get_db_connection
from auth import check_password_hash,generate_password_hash

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    role=request.form.get("selection")
    username=request.form.get("username")
    password=request.form.get("password")

    hashed_password=generate_password_hash(password)
    conn=get_db_connection()

    conn.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, hashed_password, role)
    )

    conn.commit()
    conn.close()

    return "User registered successfully"
if __name__ == '__main__':
    app.run(debug=True)