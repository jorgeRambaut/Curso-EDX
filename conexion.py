from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pprint
import sys

def main():
    cadenaconexion="host='localhost' dbname='mydb' user='postgres' password='maradona'"
    """print("Cadena conexion a la bd \n ->%s"%(cadenaconexion))"""

    obj=psycopg2.connect(cadenaconexion)
    objcursor=obj.cursor()
    algo=objcursor.execute("SELECT * FROM flights;")
    flights=objcursor.fetchall()
    pprint.pprint(flights)
    for flight in algo:
        print(f"{flight.origin} to {flight.destination},{flight.duration} minutes.")


main()
