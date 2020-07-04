#Recibe los datos del puerto serial, los guarda en la lista "lecturas_arduino" y los imprime
import serial
#Revisar que el puerto serial sea el que se está utilizando en arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600)
lecturas_arduino = [] #Se declara la lista
while True:
    values = arduino.readline()
    lecturas_arduino.append(values) #Agrega los datos a la lista
    print (lecturas_arduino)