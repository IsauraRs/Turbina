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
import enviarCorreo as enviar

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
    return render_template("busqueda.html" , datos = l[0] , bandera = "7") #tiempo

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
        correo = reques.form['correo']
        today = date.today()
    cg.pdfCarga(nombre , str(today))
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
        enviar.enviar_correo_archivo2(correo,"Reporte SdAD")
    flash("El reporte fue enviado")
    return render_template('index.html')

@app.route('/Exit')
def exit1():
    exit()
    return "Adiós"

if __name__ == '__main__':
    app.run(debug=True)