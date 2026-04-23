import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/contact/")
def contact():
    return "<p>Hello, contact page!</p>"

if __name__ == "__main__":
    app.run()