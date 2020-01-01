#import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("DATABASE_URL"))

engine = create_engine('postgresql://postgres:37ScZu147O3qAgSQG4Nh@database-1.cqtrommiv6nk.ap-south-1.rds.amazonaws.com:5432/postgres')

db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("select origin,destination,duration from flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination},{flight.duration} minute")
if __name__ == "__main__":
    main()
