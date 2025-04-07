from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def logi_sakums():
    return render_template("login.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
         lietotajvards = request.form(['lietotajvards'])
         parole =request.form(['parole'])
         print(lietotajvards)
         print(parole)
         return render_template('dashboard.html')