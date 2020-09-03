#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial
from tkReg import *
from serial import Serial
import Models1 as conex


#Check if the serial port is the same you're using in arduino
arduino = serial.Serial('/dev/rfcomm0', 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino_lectures = [] #The list is declared
nl=[]
vfl = []
def testc():
    arduino_lectures = []
    arduino.write(b'Y')

    while True:

        values = arduino.readline()
        vd = values.decode() #Decodes the values from byte to string
        
        #nl=[]
        if len(arduino_lectures) < 5: 
            n = vd.replace('\r\n', '') #Removes the \r\n characters from the string and replace them with a space
            arduino_lectures.append(n) #Adds the values to the list 
        if len(arduino_lectures) ==5:    
            #conex.carga(arduino_lectures[0],arduino_lectures[1],arduino_lectures[2],arduino_lectures[3],arduino_lectures[4])
            time.sleep(3)
            print(arduino_lectures)
            arduino_lectures = []
testc()