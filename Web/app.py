from flask import Flask
from flask import render_template , request , flash
from flask import redirect , url_for , session
import threading
from datetime import date
from datetime import datetime

from numba import jit 

#import alertMsg as alert
import Models2Consulta as mc 
import Models1Cargar as cg
import graficas as gf
import enviarCorreo as enviar
import generadorPDF as gp
import spreadSheetReport as ss

#import gatheringData as gaD
#from gatheringData import gdList

try:

    #Módulos propios 
    import datos_Serial as ds
    
except:
    alert.altPort()

app = Flask(__name__)
app.secret_key = "El dibujo de la llave"
i=0

@jit
#Ruta de inicio
@app.route('/')
def hello_world():
    return render_template('index.html')

#Ruta de encendido 
@jit
@app.route('/EncendidoArduino')
def EncendidoArduino():
    global i
    if i==0:
        threadFunc = threading.Thread(target = ds.testc)
        #threadFuncG = threading.Thread(target = gf.graficaPotencia)
        #threadMostrar = threading.Thread(target=graficarmostrar)
        #threadSpread = threading.Thread(target = ss.setData)
        threadFuncP = threading.Thread(target = gp.generar_PDF)
        threadFunc.start()
        #threadFuncG.start()
        #threadMostrar.start()
        threadFuncP.start()
        #threadSpread.start()
        i=1
    #ds.vfl=[]
    #datos = ds.vfl
    ################
    datos = ds.vfl           
    gf.graficaPotencia(datos)
    #datos2 = gf.displayList
    #gaD.gathD(datos1)
    #datos = gaD.gdList
    #Nuevo
    #u = gp.generar_PDF(datos)
    return render_template("datos.html" , datos = datos)

#Ruta de consultas
@app.route('/Ruta')
def Ruta():
    return render_template("busqueda.html")

@app.route('/consulta/potdigital', methods = ['POST'])
def consulta_potdigital():
    if request.method == 'POST':
        potdigital = request.form['pd']
        n = mc.vista(potdigital)
    #print(n[1][0])
    return render_template("busqueda.html" , datos = n[1] , bandera = "1") #potdigital


@app.route('/consulta/rpm', methods = ['POST'])
def consulta_rpm():

    if request.method == 'POST':
        rpm = request.form['rpm']
        o = mc.vistarpm(rpm)
    return render_template("busqueda.html" , datos = o[0] , bandera = "2") #rpm

@app.route('/consulta/difv', methods = ['POST'])
def consulta_difv():

    if request.method == 'POST':
        difv = request.form['dv']
        j = mc.vistadifvolt(difv)
        
    return render_template("busqueda.html" , datos = j[0] , bandera = "3")  #difv

@app.route('/consulta/volt', methods = ['POST'])
def consulta_volt():

    if request.method == 'POST':
        volt = request.form['v']
        m = mc.vistavolt(volt)

    return render_template("busqueda.html" , datos = m[0] , bandera = "4") #potdigital #volt

@app.route('/consulta/difvolin' , methods = ['POST'])
def consulta_difvolin():

    if request.method == 'POST':
        difv23 = request.form['dv23']
        n = mc.vistadifvoltin(difv23)
    return render_template("busqueda.html" , datos = n[0] , bandera = "5")

@app.route('/consulta/voltin' , methods = ['POST'])
def consultavoltin():

    if request.method == 'POST':
        vin = request.form['vin']
        q = mc.vistaVoltin(vin)
    return render_template("busqueda.html" , datos = q[0] , bandera = "6")
    
@app.route('/consulta/tiempo', methods = ['POST'])
def consulta_tiempo():

    if request.method == 'POST':
        tiempo = request.form['t']
        l = mc.vistaTiempo(tiempo)
        tl = gp.generar_PDFC(l[0])
    return render_template("busqueda.html" , datos = l[0] , bandera = "7") #tiempo

@app.route('/consulta/potencia', methods = ['POST'])
def consulta_potencia():

    if request.method == 'POST':
        potencia = request.form['pot']
        pv = mc.vistaPotencia(potencia)
        pvl = gp.generar_PDFC(pv[0])
    return render_template("busqueda.html" , datos = pv[0] , bandera = "8") #potencia

@app.route('/consulta/efgenerador', methods = ['POST'])
def consulta_efgenerador():

    if request.method == 'POST':
        efgen = request.form['efg']
        efgv = mc.vistaEfg(efgen)
        efgvl = gp.generar_PDFC(efgv[0])
    return render_template("busqueda.html" , datos = efgv[0] , bandera = "9") #eficienciaGenerador

@app.route('/consulta/efturbina', methods = ['POST'])
def consulta_efturbina():

    if request.method == 'POST':
        eftur = request.form['eft']
        eftv = mc.vistaEft(eftur)
        eftvl = gp.generar_PDFC(eftv[0])
    return render_template("busqueda.html" , datos = eftv[0] , bandera = "10") #eficienciaTurbina


#@jit
@app.route('/graficarmostrar')
def graficarmostrar():

    
    datos = ds.vfl          
    gf.graficaPotencia(datos) #datos

    cg.imCarga()
    return render_template ("datos.html" , datos = datos , bandera = 1) #datos = datos

@app.route('/Regresar', methods = ['POST'])
def inicio2():
    datos = ds.vfl
    u = gp.generar_PDF(datos)
    ssr = ss.setData(datos)
    d1 = gf.displayList
    d2 = gf.displayList1
    d3 = gf.displayList2
    d4 = gf.displayList3
    a = ss.createGraphs(d1,d2)
    b = ss.createGraph2(d1,d3)
    c = ss.createGraph3(d1,d3)
    ds.cerrar()
    if request.method =="POST":
        nombre = request.form['nombre']
        correo = request.form['correo']
        today = date.today()
    cg.pdfCarga(nombre , str(today))
    cg.xlsxCarga(nombre,str(today))
    flash("El reporte fue enviado a: " + str(correo))
    enviar.enviar_correo_archivo(correo , "Reporte" + str(nombre))
    return render_template("index.html")

@app.route('/Reportes')
def Reportes():
    datos = mc.vistaReporte()
    return render_template("reporte.html",datos = datos)

@app.route('/layout')
def las():
    return render_template('layout.html')

@app.route('/EnviarReporte/<id>', methods = ["POST"])
def EnviarReporte(id):
    if request.method == "POST":
        correo = request.form["correo"]
        mc.vistagraph(id)
        mc.vistaSS(id)
        enviar.enviar_correo_archivo2(correo,"Reporte SdAD")
    flash("El reporte fue enviado a: " + str(correo))
    return render_template('index.html')

@app.route('/Exit')
def exit1():
    exit()
    return "Adiós"

if __name__ == '__main__':
    app.run(debug=True)