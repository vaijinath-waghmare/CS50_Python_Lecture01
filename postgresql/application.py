from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:37ScZu147O3qAgSQG4Nh@database-1.cqtrommiv6nk.ap-south-1.rds.amazonaws.com:5432/postgres')

db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    
