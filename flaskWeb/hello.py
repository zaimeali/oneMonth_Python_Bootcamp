# code . => to open current dir from terminal

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

# FLASK_APP=hello.py flask run