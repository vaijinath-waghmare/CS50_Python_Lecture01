import datetime

from flask import Flask,render_template

app = Flask(__name__)


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

@app.route("/")
def index():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	#return f"Today's date(dd/mm/yyyy):{now.day}/{now.month}/{now.year}"
	new_year = True
	return render_template("index.html",new_year=new_year)


@app.route("/bye")
def bye():
	bye = "GoodBye!!!"
	return render_template("index.html",headline=bye)
