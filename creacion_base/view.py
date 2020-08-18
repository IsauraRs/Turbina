import psycopg2
from tkReg import *
import tkReg as w


dl = []
cd = []

vl = []
vlc = []

host = 'ec2-34-225-82-212.compute-1.amazonaws.com'

database= 'd60lbn7ubp9jlb'
user= 'kgsvsidlipqnoy'
password='3e3c54e483c6797261dad22ef4735c24fa2b8df1fc993252f572bb1618019073'

def vista(dpVal):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    #cursor.execute("SELECT * FROM lectura;")
    cursor.execute("SELECT lectura_id, valor_pot_digt, rev_min, dif_01, voltaje, tiemp FROM lectura WHERE valor_pot_digt = %s" , (dpVal, ))
    #("SELECT valor_pot_digt FROM lectura WHERE valor_pot_digt = %s", (dpVal,))
    datos = cursor.fetchall()

    for g in datos:
        dl.append(g)

    #print(datos)
    cursor.execute("SELECT COUNT (*) FROM lectura WHERE valor_pot_digt = %s" , (dpVal, ))
    cdata = cursor.fetchall()

    for j in cdata:

        cd.append(j)

    #print(cdata)
    conexion.commit()
    cursor.close()
    conexion.close()
    lisn = []
    lisn.append(cd)
    lisn.append(dl)
    return lisn

def vistavolt(voltVal):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    #cursor.execute("SELECT * FROM lectura;")
    cursor.execute("SELECT lectura_id, valor_pot_digt, rev_min, dif_01, voltaje, tiemp FROM lectura WHERE voltaje = %s" , (voltVal, ))
    vd = cursor.fetchall()

    for u in vd:
        vl.append(u)
    
    cursor.execute("SELECT COUNT (*) FROM lectura WHERE voltaje = %s" , (voltVal, ))
    cdata1 = cursor.fetchall()

    for h in cdata1:
        vlc.append(h)
    
    conexion.commit()
    cursor.close()
    conexion.close()


#vista(str(570))