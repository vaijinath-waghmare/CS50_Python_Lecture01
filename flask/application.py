#import datetime

from flask import Flask,render_template, request, session
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#@app.route("/")
#def index():
#	return "Hello World"


#@app.route("/<string:name>")
#def hello(name):
#	return f"<h1>Hello {name}!!!<h1>"

#@app.route("/")
#def index():
#	hello = "Hello"
#	return render_template("index.html",headline=hello)

#@app.route("/")
#def index():
#	now = datetime.datetime.now()
#	new_year = now.month == 1 and now.day == 1
#	#return f"Today's date(dd/mm/yyyy):{now.day}/{now.month}/{now.year}"
#	new_year = True
#	return render_template("index.html",new_year=new_year)


#@app.route("/bye")
#def bye():
#	bye = "GoodBye!!!"
#	return render_template("index.html",headline=bye)

#@app.route("/list")
#def list():
#	names = ["name1","name2","name3","name4"]
#	return render_template("index.html",names=names)

#@app.route("/")
#def index():
#	return render_template("index.html")

#@app.route("/more")
#def more():
#	return render_template("more.html")

#@app.route("/")
#def index():
#	return render_template("index.html")

#@app.route("/hello", methods=["GET","POST"])
#def hello():
#	if request.method == "GET":
#		return "Please submit the form instead"
#	else:
#		name = request.form.get("name")
#		return render_template("hello.html",name=name)

notes = []
@app.route("/", methods = ["GET", "POST"])
def index():
	if session.get("notes") is None:
		session["notes"] = []
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("index.html", notes=notes)
