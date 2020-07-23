import psycopg2
import pprint
import sys
def main():
    cadenaconexion="host='localhost' dbname='mydb' user='postgres' password='maradona'"
    print("Cadena conexion a la bd \n ->%s"%(cadenaconexion))

    obj=psycopg2.connect(cadenaconexion)
    objcursor=obj.cursor()
    objcursor.execute("SELECT * FROM flights;")
    registros=objcursor.fetchall()
    pprint.pprint(registros)





main()
