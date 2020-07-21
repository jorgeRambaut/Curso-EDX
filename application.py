""" importamos Flask"""
from flask import Flask
""" nueva app """
app = Flask(__name__)
"""default page"""
@app.route("/")
def index():
    return "hello,world!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>hola,{name}!<h1>"
