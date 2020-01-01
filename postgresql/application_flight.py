from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:37ScZu147O3qAgSQG4Nh@database-1.cqtrommiv6nk.ap-south-1.rds.amazonaws.com:5432/postgres')

db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("select * from flights").fetchall()
    return render_template("index.html",flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """ Book a flight. """
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueEroor:
        return render_template("error.html",message="Invalid Flight Number")
    if db.execute("select * from flights where id = :fid",{"fid":flight_id}).rowcount == 0:
        return render_template("error.html",message = "No such flight with that id.")
    db.execute("insert into passengers (flight_id,name) values (:fid,:pname)",{"fid":flight_id,"pname":name})
    db.commit()
    return render_template("success.html")
