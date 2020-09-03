from flask import Flask
from flask import render_template , request , flash
from flask import redirect , url_for , session
import threading
from datetime import date
from datetime import datetime

#Módulos propios 
import datos_Serial as ds
import Models2Consulta as mc 
import Models1Cargar as cg
import graficas as gf

app = Flask(__name__)
app.secret_key = "El dibujo de la llave"
i=0

#Ruta de inicio
@app.route('/')
def hello_world():
    return render_template('index.html')

#Ruta de encendido 
@app.route('/EncendidoArduino')
def EncendidoArduino():
    global i
    if i==0:
        threadFunc = threading.Thread(target = ds.testc)
        threadFunc.start()
        i=1
    datos = ds.vfl
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
    print(n[1][0])
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

@app.route('/consulta/tiempo', methods = ['POST'])
def consulta_tiempo():
    if request.method == 'POST':
        tiempo = request.form['t']
        l = mc.vistaTiempo(tiempo)
    return render_template("busqueda.html" , datos = l[0] , bandera = "5") #tiempo

@app.route('/graficarmostrar')
def graficarmostrar():
    datos = ds.vfl
    gf.graficaPotencia(datos)
    cg.imCarga()
    return render_template ("datos.html" , datos = datos , bandera = 1)

@app.route('/Regresar', methods = ['POST'])
def inicio2():
    ds.cerrar()
    if request.method =="POST":
        nombre = request.form['nombre']
        today = date.today()
    cg.pdfCarga(nombre , str(today))
    return render_template("index.html")

@app.route('/Reportes')
def Reportes():
    datos = mc.vistaReporte()
    return render_template("reporte.html",datos = datos)

@app.route('/layout')
def las():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)