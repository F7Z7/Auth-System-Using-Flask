from flask import Flask, request, render_template, redirect, url_for

from auth import generate_password_hash
from db import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        role = request.form.get("selection")
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()

        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_password, role)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("/login"))
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
