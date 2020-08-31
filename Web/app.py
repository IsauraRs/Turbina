from flask import Flask
from flask import render_template , request , flash
from flask import redirect , url_for , session
import threading
#Módulos propios 
import datos_Serial as ds

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

@app.route('/Ruta')
def Ruta():
    return render_template("busqueda.html")
@app.route('/consulta/potdigital', methods = ['POST'])
def consulta_potdigital():
    if request.method == 'POST':
        potdigital = request.form['pd']
    return potdigital
@app.route('/consulta/rpm', methods = ['POST'])
def consulta_rpm():
    if request.method == 'POST':
        rpm = request.form['rpm']
        
    return rpm
@app.route('/consulta/difv', methods = ['POST'])
def consulta_difv():
    if request.method == 'POST':
        difv = request.form['dv']
    return difv
@app.route('/consulta/volt', methods = ['POST'])
def consulta_volt():
    if request.method == 'POST':
        volt = request.form['v']
    return volt
@app.route('/consulta/tiempo', methods = ['POST'])
def consulta_tiempo():
    if request.method == 'POST':
        tiempo = request.form['t']
    return tiempo
if __name__ == '__main__':
    app.run(debug=True)