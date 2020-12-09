#####################################################
#Modules
#Receives data from serial port, saves them into the list "arduino_lectures" and prints them
import serial
from serial import Serial
import time
import sys

#Created modules
#Calcular
#from tkReg import *
import Models1Cargar as conex
import readPorts as rp


nl = []
vfl = []
ndat = []
pivote3 = 1
r1 = (12/1.87)
#Check if the serial port is the same you're using in arduino
#arduino = serial.Serial('/dev/rfcomm0', 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#arduino = serial.Serial('/dev/ttyACM0', 9600)

try:

    if sys.platform =='win32':
        prt = rp.readPortW()
        prt = prt[0:4]
        print(prt)
        
    #prt= 'COM3'
    else:
        prt = rp.readPort()
    #print(prt)
    arduino = serial.Serial(str(prt), 9600)
    #arduino.close()
    #arduino.open()
    #print(arduino)
    def cerrar():
        arduino.close()

    arduino_lectures = [] #The list is declared

    def testc():
        arduino_lectures = []
        arduino.write(b'Y')
        #global nl
        nl = []
        ndat = []
        global vfl
        while True:
            try:

                #time.sleep(3)
                #print("Entra a testc")
                values = arduino.readline()
                vd = values.decode() #Decodes the values from byte to string
                if len(arduino_lectures) < 7: 
                    n = vd.replace('\r\n', '') #Removes the \r\n characters from the string and replace them with a space
                    arduino_lectures.append(float(n)) #Adds the values to the list 
                if len(arduino_lectures) ==7: 
                    ####
                    for i in range(len(arduino_lectures)):
                        #print("AL", arduino_lectures)
                        Rdp = float (arduino_lectures[0])#Ohm[i]
                        vVg = float(arduino_lectures[3]) #Generador
                        vVd = float(arduino_lectures[5]) #Dinamo
                        
                        #if Rdp == pivote3:

                        try:
                            if Rdp >=1:
                                #print("Es " + str(Rdp))
                                Ie = (vVg/Rdp)/1000 #Amperes
                                Is = (vVd/Rdp)/1000#Amperes
                                P = ((((vVg+vVd)-(Ie-Is)*r1)*Ie*Is)/(Ie+Is))
                                em = (P/(Ie*vVg))*100
                                ed = ((Is*vVd)/P)*100

                                print("P",P)
                                print("em",em)
                                print("ed",ed)
                    
                            else:
                                P = 0
                                em = 0
                                ed = 0

                            Rdp = float (arduino_lectures[0])

                            ndat.append(P)
                            ndat.append(em)
                            ndat.append(ed)
                            print("ndat: ", ndat)

                            

                        except ZeroDivisionError:
                            print("errors in ds")

                        #Aquí estaba lo de ndat

                    arduino_lectures.append(ndat[0])
                    arduino_lectures.append(ndat[1])
                    arduino_lectures.append(ndat[2])
                    print("ardL: " , arduino_lectures)
                    # ####   
                    #time.sleep(3)
                    #print("RPM: "+str(arduino_lectures[1])+" diff: "+str(arduino_lectures[2])+" Voltaje: "+str(arduino_lectures[3])+ "dif2: " + str(arduino_lectures[4]) + " Tiempo: "+str(arduino_lectures[4])+" Pot Digt: "+str(arduino_lectures[0]))
                    #4 dif vol23 5 volt in
                    conex.carga(arduino_lectures[0],arduino_lectures[1],arduino_lectures[2],arduino_lectures[3],arduino_lectures[4],arduino_lectures[5],arduino_lectures[6],arduino_lectures[7],arduino_lectures[8],arduino_lectures[9])
                    for i in range(10):  #7
                        nl.append(arduino_lectures[i])
                    nl = list(nl)
                    vfl.append(nl)
                    #print(arduino_lectures)
                    #time.sleep(3)
                    #print("vfl: ", vfl)
                    nl=[]
                    arduino_lectures = []
                    ndat = []
                    print("ndatL: ", ndat)

            except serial.serialutil.SerialException:
                print("Ex1")
                pass

            except ValueError:
                print("Ex2")
                pass
except:
    import alertMsg as am
    am.altPort()
    pass
        #print(vfl)
#######################################################
#testc()
