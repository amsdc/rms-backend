from flask import Flask

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return "Hello Wrld"

@app.route("/api/greet/<string:name>")
def greet(name):
    return "Hello" + " " + name