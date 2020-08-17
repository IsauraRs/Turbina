#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial
import csv
import Models1 as conex

#Check if the serial port is the same you're using in arduino
arduino = serial.Serial('/dev/rfcomm0', 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
arduino_lectures = [] #The list is declared
nl=[]

def testc():
    while True:
        values = arduino.readline()
        vd = values.decode() #Decodes the values from byte to string
        arduino_lectures.append(vd) #Adds the values to the list 
        #nl=[]
        for i in range(len(arduino_lectures)):
            n = arduino_lectures[i].replace('\r\n', '') #Removes the \r\n characters from the string and replace them with a space
            nl.append(n) #Adds to the list nl the values without the "\r\n" characters
        if len(nl) > 5:
            conex.carga(nl[0],nl[1],nl[2],nl[3],nl[4]) #Loads the values sent from arduino to the table
        print(nl)