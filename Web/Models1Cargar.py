import psycopg2

host = 'ec2-34-225-82-212.compute-1.amazonaws.com'

database= 'd60lbn7ubp9jlb'
user= 'kgsvsidlipqnoy'
password='3e3c54e483c6797261dad22ef4735c24fa2b8df1fc993252f572bb1618019073'

def carga(param2, param3, param4, param5, param6, param7, param8, param9, param10, param11):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO lectura(valor_pot_digt, rev_min, dif_01, voltaje_in, dif_23, voltaje_out, tiemp, potencia, ef_generador, ef_turbina) VALUES (%s, %s, %s, %s, %s , %s, %s, %s, %s , %s);",(param2, param3, param4, param5, param6, param7, param8, param9, param10, param11 ))
    conexion.commit()
    cursor.close()
    conexion.close()

def readIm():
    imm = open("static/img/image.jpg" , "rb")
    imag = imm.read()
    return imag

def readIm2():
    imm = open("static/img/imageEfmotor.jpg" , "rb")
    imag2 = imm.read()
    return imag2

def readIm3():
    imm = open("static/img/imageEfTurbina.jpg" , "rb")
    imag3 = imm.read()
    return imag3



def imCarga():

    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    iml = readIm()
    binary = psycopg2.Binary(iml)
    iml2 = readIm2()
    binary2 = psycopg2.Binary(iml2)
    iml3 = readIm3()
    binary3 = psycopg2.Binary(iml3)
    cursor.execute("INSERT INTO efgraph(grafica , grafica2, grafica3) VALUES (%s, %s, %s);",(binary,binary2,binary3 ))
    conexion.commit()
    cursor.close()
    conexion.close()

def readPdf():
    imm = open("table.pdf" , "rb")
    imag = imm.read()
    return imag

def pdfCarga(nombre, fecha):
    if nombre=="":
        nombre="Noname"
    if fecha=="":
        fecha="NoDate"
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    pdl = readPdf()
    binary = psycopg2.Binary(pdl)
    cursor.execute("INSERT INTO reporte(nombre , fecha , archivo) VALUES (%s , %s , %s);",(nombre, fecha , binary ))
    conexion.commit()
    cursor.close()
    conexion.close()

def readExcel():
    xl = open("ReporteSpreadsheet.xlsx" , "rb")
    xlr = xl.read()
    return xlr

def xlsxCarga(nombre, fecha):

    if nombre=="":
        nombre="Noname"
    if fecha=="":
        fecha="NoDate"
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    xll = readExcel()
    binary = psycopg2.Binary(xll)
    cursor.execute("INSERT INTO reportess(nombre , fecha , archivo_ss) VALUES (%s , %s , %s);",(nombre, fecha , binary ))
    conexion.commit()
    cursor.close()
    conexion.close()


#o = pdfCarga("" , "")