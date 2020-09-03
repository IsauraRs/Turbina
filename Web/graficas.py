import matplotlib as mlp
import matplotlib.pyplot as plt
from datos_Serial import * 
Rdp = 78.74 #[Ohm]
r = (12/1.87) #[Ohm]
print(arduino_lectures)

def graficaPotencia(arduino_lectures):
    mlp.rcParams.update({'font.size': 21})
    if len(arduino_lectures) >= 3:
        v = arduino_lectures[1]
        listaIe = []
        listaIs = []
        fig = plt.figure()
        ax = plt.axes()
        for i in range(len(arduino_lectures)):
            Ie = float(arduino_lectures[i][3])
            Is = float(arduino_lectures[i][5])
            listaIe.append(Ie)
            listaIs.append(Is)
        #print(listaIe)
        #print(listaIs)
        ax.scatter(listaIe,listaIs)
        ax.set_xlabel('Ie')
        ax.set_ylabel('Is')
        #plt.show()
        plt.savefig('static/img/image.jpg') 
#arduino_lectures = [[398.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1213.0], [399.0, 0.0, -225.0, -0.0422, -1.0, -0.0002, 1216.0], [400.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1219.0], [401.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1222.0], [402.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1225.0], [403.0, 0.0, 5.0, 0.0009, 1.0, 0.0002, 1228.0], [404.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1231.0], [405.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1234.0], [406.0, 0.0, 4.0, 0.0007, 0.0, 0.0, 1237.0], [407.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1240.0], [408.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1243.0], [409.0, 0.0, 2.0, 0.0004, 1.0, 0.0002, 1246.0], [410.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1249.0], [411.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1252.0]]
#graficaPotencia(arduino_lectures)

