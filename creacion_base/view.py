import psycopg2
from tkReg import *

host = 'ec2-34-225-82-212.compute-1.amazonaws.com'

database= 'd60lbn7ubp9jlb'
user= 'kgsvsidlipqnoy'
password='3e3c54e483c6797261dad22ef4735c24fa2b8df1fc993252f572bb1618019073'

def vista(dpVal):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt FROM lectura WHERE valor_pot_digt = %s", (dpVal,))
    datos = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    print(datos)
#vista(str(570))