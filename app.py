import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    conn = sqlite3.connect('faebakery.db')
    conn.row_factory = sqlite3.Row
    return conn

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123'

# Landing
@app.route("/")
def index():
    return render_template("index.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session['username'] = username
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("error"))
    return render_template("login.html")



# Error
@app.route("/error")
def error():
    return render_template("error.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists"
    return render_template("register.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html", username=session['username'])
    return redirect(url_for("login"))


# Articles
@app.route("/articles")
def articles():
    return render_template("articles.html")


# Generator
@app.route("/generator")
def generator():
    return render_template("generator.html")


# About
@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        comment = request.form["comment"]
        
        print(f"New comment: {comment}")
    return render_template("about.html")


# Logout
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("login"))
