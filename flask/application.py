from flask import Flask,render_template

app = Flask(__name__)


#@app.route("/")
#def index():
#	return "Hello World"


#@app.route("/<string:name>")
#def hello(name):
#	return f"<h1>Hello {name}!!!<h1>"

@app.route("/")
def index():
	return render_template("index.html")
