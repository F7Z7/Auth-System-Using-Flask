from flask import Flask, request, render_template, redirect, url_for,session

from auth import generate_password_hash,check_password_hash
from db import get_db_connection

app = Flask(__name__)

app.secret_key="#011911"
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

        return render_template("login.html")
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login_user():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    user = check_user(username)

    if user:
        hash_pass=user["password"]

        if check_password_hash(hash_pass, password):
            session['user'] = user["username"]

            return redirect(url_for('welcome'))

        else:
            return "Wrong password"

    else:
        return "User does not exist"

@app.route('/welcome')
def welcome():
    user = session.get("user")

    return render_template("welcome.html", user=user)




def check_user(username):
    conn=get_db_connection()

    result=conn.execute("SELECT * FROM users WHERE username = ?", (username,)) #the comma indicates it is a value not tuple


    user=result.fetchone()

    conn.close()

    return user

if __name__ == '__main__':
    app.run(debug=True)
