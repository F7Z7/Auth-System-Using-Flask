from flask import Flask, request, render_template, redirect, jsonify


app=Flask(__name__)



@app.route("/")
def home():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)