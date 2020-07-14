#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial

#Check if the serial port is the same you're using in arduino
arduino = serial.Serial('/dev/rfcomm0', 9600)
arduino_lectures = [] #The list is declared

while True:
    values = arduino.readline()
    vd = values.decode() #Decodes the values from byte to string
    arduino_lectures.append(vd) #Adds the values to the list  
    for i in range(len(arduino_lectures)):
        n = arduino_lectures[i].replace('\r\n', '') #Removes the \r\n characters from the string and replace them with a space
    print(n)