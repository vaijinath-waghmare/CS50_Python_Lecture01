import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:37ScZu147O3qAgSQG4Nh@database-1.cqtrommiv6nk.ap-south-1.rds.amazonaws.com:5432/postgres')

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for orig,dest,dura in reader:
        db.execute("insert into flights (origin,destination,duration) values (:origin,:destination,:duration)",{"origin":orig,"destination":dest,"duration":dura})
        print(f"Added flight from {orig} to {dest},{dura} minute")
    db.commit()    
if __name__ == "__main__":
    main()
