import psycopg2
from app import *

host = 'ec2-34-225-82-212.compute-1.amazonaws.com'

database= 'd60lbn7ubp9jlb'
user= 'kgsvsidlipqnoy'
password='3e3c54e483c6797261dad22ef4735c24fa2b8df1fc993252f572bb1618019073'

def vista(dpVal):
    
    dl = []
    cd = []
    lisn = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    #cursor.execute("SELECT * FROM lectura;")
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje, tiemp, voltajein, dif_23 FROM lectura WHERE valor_pot_digt = %s" , (dpVal, ))
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
    lisn.append(cd)
    lisn.append(dl)
    return lisn

def vistavolt(voltVal):

    vl = []
    vlc = []
    ll = []
    
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
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
    ll.append(vl)
    ll.append(vlc)
    return ll

def vistadifvolt(difVoltVal):

    difvl = []
    difvcl = []
    lff = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT lectura_id, valor_pot_digt, rev_min, dif_01, voltaje, tiemp FROM lectura WHERE dif_01 = %s" , (difVoltVal, ))
    vf = cursor.fetchall()

    for e in vf:

        difvl.append(e)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE dif_01 = %s" , (difVoltVal, ))
    
    cvf = cursor.fetchall()

    for q in cvf:

        difvcl.append(q)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    lff.append(difvl)
    lff.append(difvcl)
    return lff


def vistarpm(rpmVal):

    rpml = []
    rpmcl = []
    rpmfl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT lectura_id, valor_pot_digt, rev_min, dif_01, voltaje, tiemp FROM lectura WHERE rev_min = %s" , (rpmVal, ))
    rd = cursor.fetchall()

    for e in rd:
        rpml.append(e)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE rev_min = %s" , (rpmVal, ))
    cdata2 = cursor.fetchall()

    for q in cdata2:
        rpmcl.append(q)
    
    conexion.commit()
    cursor.close()
    conexion.close()

    rpmfl.append(rpml)
    rpmfl.append(rpmcl)
    return rpmfl

def vistaTiempo(tiempoVal):

    timeSelectList = []
    timeCountList = []
    timeFinalList = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT lectura_id, valor_pot_digt, rev_min, dif_01, voltaje, tiemp FROM lectura WHERE tiemp = %s" , (tiempoVal, ))
    x = cursor.fetchall()

    for t in x:
        timeSelectList.append(t)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  tiemp = %s" , (tiempoVal, ))
    tn = cursor.fetchall()

    for w in tn:
        timeCountList.append(w)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    timeFinalList.append(timeSelectList)
    timeFinalList.append(timeCountList)
    #print(timeFinalList[0])
    return timeFinalList

def writeImage(siq):

    imout = open('newim.png' , 'wb')
    imout.write(siq)

def vistagraph():

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica FROM efgraph")
    siq = cursor.fetchone()[0]
    writeImage(siq)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaReporte():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre , fecha  FROM reporte")
    siq = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return siq

#vista(str(570))
#vistagraph()
#vistaTiempo(str(655))