#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial

#Check if the serial port is the same you're using in arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
arduino_lectures = [] #The list is declared

while True:
    values = arduino.readline()
    vd = values.decode() #Decodes the values from byte to string
    arduino_lectures.append(vd) #Adds the values to the list
    print(arduino_lectures)