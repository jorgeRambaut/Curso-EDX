import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


"""TODO VER CONEXIONES DE BASE DE DATOS!!"""
engine=create_engine('postgresql://postgres:maradona@localhost/')
db= scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT id,origin,destination,duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination},{flight.duration} minutes.")

    flight_id = int(input("\n Flight ID: "))
    flight=db.execute("SELECT origin,destination,duration FROM flights WHERE id = :id",
    {"id":flight_id}).fetchone()


    if flight is None:
        print("Error no such Flight")
        return
     #mucha atencion a : para los placeholders
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
    {"flight_id":flight_id}).fetchall()

    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) ==0:
        print("No passangers.")

if __name__ == "__main__":
    main()
