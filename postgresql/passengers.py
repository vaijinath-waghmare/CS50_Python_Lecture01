
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:37ScZu147O3qAgSQG4Nh@database-1.cqtrommiv6nk.ap-south-1.rds.amazonaws.com:5432/postgres')

db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("select id, origin,destination,duration from flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id} from {flight.origin} to {flight.destination},{flight.duration} minute")

    flight_id = int(input("\nEndter Flight Id:"))
    flight = db.execute("select id from flights where id = :id ",{"id":flight_id}).fetchone()

    if flight is None:
        print("Error : No such flight.")
        return
    else:
        print(f"Printing passengers in flight no {flight_id} :")
        passengers = db.execute("select flight_id,name from passengers where flight_id = :fid",{"fid":flight_id}).fetchall()
        if len(passengers) == 0:
            print("No passengers in flight")
        else:
            for passenger in passengers:
                print(passenger.name)
if __name__ == "__main__":
    main()
