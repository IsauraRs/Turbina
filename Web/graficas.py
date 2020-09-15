import matplotlib as mlp
mlp.use('Agg')
import matplotlib.pyplot as plt
#Módulos propios
from datos_Serial import * 
from generadorPDF import *
r = (12/1.87) #[Ohm]
#print(arduino_lectures)

def graficaPotencia(arduino_lectures):
    mlp.rcParams.update({'font.size': 10})
    if len(arduino_lectures) >= 3:
        listaP = []
        listaRPM = []
        listaR = []
        listaefm = []
        listaeft = []
        fig = plt.figure()
        ax = plt.axes()
        axem = plt.axes()
        axet = plt.axes()
        for i in range(len(arduino_lectures)):
            vs = float(arduino_lectures[i][3])
            vi = float(arduino_lectures[i][5])
            #Rdp = ((10000*(100-float(str(arduino_lectures[i][0]))))/arduino_lectures[i][0])+40 #Ohm

            try:
                Rdp = ((10000*(100-float(str(arduino_lectures[i][0]))))/arduino_lectures[i][0])+40 #Ohm
                Ie = float(arduino_lectures[i][3])/Rdp #Amperes
                Is = float(arduino_lectures[i][5])/Rdp #Amperes
                #print(Ie)
                P = ((((vi+vs)-(Ie-Is)*r)*Ie*Is)/(Ie+Is))
                em = (P/(Ie*vi))*100
                ed = ((Is*vs)/P)*100
                rpm = float(str(arduino_lectures[i][1]))
                listaP.append(P)
                listaRPM.append(rpm)
                listaefm.append(em)
                listaeft.append(ed)
                listaR.append(Rdp)
            except ZeroDivisionError:
                pass

            #Rw = 40 [Ohm] 100 taps
        #print(listaIe)
        #print(listaIs)
        ax.plot(listaP,listaRPM, 'o-')
        #ax.plot(listaRPM, listaP,'o-')
        ax.set_xlabel('Potencia')
        ax.set_ylabel('RPM')
        #plt.show()
        plt.savefig('static/img/image.jpg') 
        
        axem.plot(listaR , listaefm , 'o-')
        #axem.plot(listaefm , listaR  , 'o-')
        axem.set_xlabel('R[Ohm]')
        axem.set_ylabel('e_motor[%]')
        plt.savefig('static/img/imageEfmotor.jpg')

        axet.plot(listaR , listaeft , 'o-')
        #axet.plot(listaeft , listaR , 'o-')
        axet.set_xlabel('R[Ohm]')
        axet.set_ylabel('e_turbina[%]')
        plt.savefig('static/img/imageEfTurbina.jpg')
#arduino_lectures = [[398.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1213.0], [399.0, 0.0, -225.0, -0.0422, -1.0, -0.0002, 1216.0], [400.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1219.0], [401.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1222.0], [402.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1225.0], [403.0, 0.0, 5.0, 0.0009, 1.0, 0.0002, 1228.0], [404.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1231.0], [405.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1234.0], [406.0, 0.0, 4.0, 0.0007, 0.0, 0.0, 1237.0], [407.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1240.0], [408.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1243.0], [409.0, 0.0, 2.0, 0.0004, 1.0, 0.0002, 1246.0], [410.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1249.0], [411.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1252.0]]
#graficaPotencia(arduino_lectures)