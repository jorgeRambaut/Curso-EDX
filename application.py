""" importamos Flask"""
from flask import Flask, render_template, request, session
from flask_session import Session



""" nueva app """
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes=[]

@app.route("/", methods=["GET", "POST"])
def notas():
    """""sesiones particulares"""
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method== "POST":
        note = request.form.get("note")
        session["notes"].append(note)
        """notes.append(note)"""

    return render_template("notas.html",notes=session["notes"])



"""@app.route("/")
def index():
    return render_template("Prueba.html")

@app.route("/hello",methods=["POST"])
def hello():
    name= request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/")
def Prueba():
    names=["Alice","Bob","Charlie"]
    return render_template("Prueba.html",names=names)

default page
@app.route("/")
def index():
    headline="hola, paso headline por python"
    return render_template("index.html",headline=headline)


@app.route("/bye")
def bye():
    headline="paso headline por python, adios"
    return render_template("index.html",headline=headline)


@app.route("/")

def index():
    now=datetime.datetime.now()
    new_year=now.month==1 and now.day==1
    return render_template("index.html",new_year=new_year)"""
