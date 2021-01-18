import psycopg2


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
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina FROM lectura WHERE valor_pot_digt = %s" , (dpVal, ))
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
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina FROM lectura WHERE voltaje_in = %s" , (voltVal, ))
    vd = cursor.fetchall()

    for u in vd:
        vl.append(u)
    
    cursor.execute("SELECT COUNT (*) FROM lectura WHERE voltaje_in = %s" , (voltVal, ))
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
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina FROM lectura WHERE dif_01 = %s" , (difVoltVal, ))
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
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina FROM lectura WHERE rev_min = %s" , (rpmVal, ))
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
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina FROM lectura WHERE tiemp = %s" , (tiempoVal, ))
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

def vistadifvoltin(difv2):

    difVolt23l = []
    difVolt23c = []
    difVolt23fl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina  FROM lectura WHERE dif_23 = %s" , (difv2, ))
    d23 = cursor.fetchall()

    for z in d23:
        difVolt23l.append(z)
    
    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  dif_23 = %s" , (difv2, ))
    dvc = cursor.fetchall()

    for y in dvc:
        difVolt23c.append(y)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    difVolt23fl.append(difVolt23l)
    difVolt23fl.append(difVolt23c)
    
    return difVolt23fl

def vistaVoltin(vinVal):

    voltinl = []
    voltinc = []
    voltinfl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina  FROM lectura WHERE voltaje_out = %s" , (vinVal, ))
    vinf = cursor.fetchall()

    for h in vinf:
        voltinl.append(h)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  voltaje_out = %s" , (vinVal, ))
    vcf = cursor.fetchall()

    for r in vcf:
        voltinc.append(r)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    voltinfl.append(voltinl)
    voltinfl.append(voltinc)

    return voltinfl


def writeImage(siq):

    imout = open('ReporteAEnviar.pdf' , 'wb')
    imout.write(siq)

def vistagraph(id):

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT archivo FROM reporte AS r, reportess AS rs WHERE r.nombre  = rs.nombre AND r.reporte_id = %s" , (id,))
    siq = cursor.fetchone()[0]
    writeImage(siq)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaReporte():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT r.nombre,r.fecha,reporte_id, rs.nombre, rs.fecha, id_excel FROM reporte AS r, reportess AS rs WHERE r.nombre  = rs.nombre")
    siq = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return siq

def writeXl(wx):
    xlOut = open('ReporteSpreadAEnviar.xlsx','wb')
    xlOut.write(wx)

def vistaSS(id):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT rs.archivo_ss FROM reporte AS r, reportess AS rs WHERE r.nombre  = rs.nombre AND r.reporte_id = %s", (id,))
    wx = cursor.fetchone()[0]
    writeXl(wx)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaRSS():

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre , fecha , id_excel FROM reportess")
    #cursor.execute("SELECT r.nombre,r.fecha,reporte_id, rs.nombre, rs.fecha, id_excel FROM reporte AS r, reportess AS rs WHERE r.nombre  = rs.nombre")
    wx = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return wx

#Consulta a valores de potencia
def vistaPotencia(potVal):

    potl = []
    pc = []
    pfl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina  FROM lectura WHERE potencia = %s" , (potVal, ))
    pcf = cursor.fetchall()

    for w in pcf:
        potl.append(w)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  potencia = %s" , (potVal, ))
    pcfa = cursor.fetchall()

    for b in pcfa:
        pc.append(b)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    pfl.append(potl)
    pfl.append(pc)

    return pfl

#Consulta a valores de eficiencia del generador
def vistaEfg(efgVal):
    
    efgl = []
    efgc = []
    efgfl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina  FROM lectura WHERE ef_generador = %s" , (efgVal, ))
    efgcf = cursor.fetchall()

    for g in efgcf:
        efgl.append(g)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  ef_generador = %s" , (efgVal, ))
    efgcfa = cursor.fetchall()

    for b in efgcfa:
        efgc.append(b)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    efgfl.append(efgl)
    efgfl.append(efgc)

    return efgfl

#Consulta a valores de eficiencia de la turbina 
def vistaEft(eftVal):
    
    eftl = []
    eftc = []
    eftfl = []

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina  FROM lectura WHERE ef_turbina = %s" , (eftVal, ))
    eftcf = cursor.fetchall()

    for g in eftcf:
        eftl.append(g)

    cursor.execute("SELECT COUNT (*) FROM lectura WHERE  ef_turbina = %s" , (eftVal, ))
    eftcfa = cursor.fetchall()

    for b in eftcfa:
        eftc.append(b)
    
    conexion.commit()
    cursor.close()
    conexion.close()
    eftfl.append(eftl)
    eftfl.append(eftc)

    return eftfl

#Consulta a gráficas de resistencia vs RPM
def writeGraph(g1c):
    
    imout = open('static/img/RvsRPM.JPEG' , 'wb')
    imout.write(g1c)

def vistagraph1(date1):

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica FROM efgraph WHERE fecha = %s" , (date1,))
    g1c = cursor.fetchone()[0]
    writeGraph(g1c)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaGrafica1():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica , pic_id FROM efgraph")
    #cursor.execute("SELECT nombre , fecha , id_excel FROM reportess")
    g1c = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return g1c

#Consulta a gráficas de Resistencia vs eficiencia del generador
def writeGraph2(g2c):
    
    imout2 = open('static/img/RvsEfG.JPEG' , 'wb')
    imout2.write(g2c)

def vistagraph2(date2):

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica2 FROM efgraph WHERE fecha = %s" , (date2,))
    g2c = cursor.fetchone()[0]
    writeGraph2(g2c)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaGrafica2():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica2 , pic_id FROM efgraph")
    #cursor.execute("SELECT nombre , fecha , id_excel FROM reportess")
    g2c = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return g2c

#Consulta a gráficas de Resistencia vs eficiencia de la turbina

def writeGraph3(g3c):
    
    imout3 = open('static/img/RvsEfT.JPEG' , 'wb')
    imout3.write(g3c)

def vistagraph3(date):

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica3 FROM efgraph WHERE fecha = %s" , (date,))
    g3c = cursor.fetchone()[0]
    writeGraph3(g3c)

    conexion.commit()
    cursor.close()
    conexion.close()

def vistaGrafica3():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT grafica3 , pic_id FROM efgraph")
    #cursor.execute("SELECT nombre , fecha , id_excel FROM reportess")
    g3c = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return g3c



#vista(str(570))
#vistagraph(194)
#vistaTiempo(str(655))
#vistagraph1(2827)
#vistaSS(2)