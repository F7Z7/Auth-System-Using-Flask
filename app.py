from flask import Flask, request, render_template, redirect, jsonify


app=Flask(__name__)



@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    role=request.form.get("selection")
    username=request.form.get("username")
    password=request.form.get("password")

    print(role, username, password)

    if username=="admin" and password=="farza@2004":
        return f"Welcome {role} {username}"

    return "Invalid credentials", 401

if __name__ == '__main__':
    app.run(debug=True)