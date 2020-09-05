#####################################################33
#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial
#from tkReg import *
from serial import Serial
import Models1Cargar as conex
import time

nl = []
vfl = []
#Check if the serial port is the same you're using in arduino
#arduino = serial.Serial('/dev/rfcomm0', 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#arduino = serial.Serial('/dev/ttyACM0', 9600)
def cerrar():
    arduino.close()
arduino_lectures = [] #The list is declared

def testc():
    arduino_lectures = []
    arduino.write(b'Y')
    global nl
    global vfl
    while True:

        values = arduino.readline()
        vd = values.decode() #Decodes the values from byte to string
        
        if len(arduino_lectures) < 7: 
            n = vd.replace('\r\n', '') #Removes the \r\n characters from the string and replace them with a space
            arduino_lectures.append(float(n)) #Adds the values to the list 
        if len(arduino_lectures) ==7:    
            #time.sleep(3)
            #print("RPM: "+str(arduino_lectures[1])+" diff: "+str(arduino_lectures[2])+" Voltaje: "+str(arduino_lectures[3])+ "dif2: " + str(arduino_lectures[4]) + " Tiempo: "+str(arduino_lectures[4])+" Pot Digt: "+str(arduino_lectures[0]))
            #4 dif vol23 5 volt in
            conex.carga(arduino_lectures[0],arduino_lectures[1],arduino_lectures[2],arduino_lectures[3],arduino_lectures[4],arduino_lectures[5],arduino_lectures[6])
            for i in range(7):
                nl.append(arduino_lectures[i])
            nl = list(nl)
            vfl.append(nl)
            nl=[]
            arduino_lectures = []
            #print(vfl)
 
#######################################################
