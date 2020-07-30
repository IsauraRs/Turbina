import psycopg2

host = 'ec2-34-225-82-212.compute-1.amazonaws.com'

database= 'd60lbn7ubp9jlb'
user= 'kgsvsidlipqnoy'
password='3e3c54e483c6797261dad22ef4735c24fa2b8df1fc993252f572bb1618019073'

def carga(param2, param3, param4, param5):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO lectura(valor_pot_digt, rev_min, dif_01, voltaje) VALUES (%s, %s, %s, %s);",(param2, param3, param4, param5))
    conexion.commit()
    cursor.close()
    conexion.close()

#carga(nl[0,1,2,3])
