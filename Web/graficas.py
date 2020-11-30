import matplotlib as mlp
mlp.use('Agg')
import matplotlib.pyplot as plt
#from numba import  jit
#Módulos propios
#import gatheringData as gDa

#Poner conex
r = (12/1.87) #[Ohm]
listaP = []
listaRPM = []
listaR = []
listaR1 = []
listaR2 = []
listaR3 = []
listaRp = []
listaefm = []
listaeft = []
listaS = []
listalr = []
listalP = []
listalEm = []
listalEt = []
displayList = []
sR = 0
promsR = 0
P = 0
em = 0
ed = 0

'''ax.plot(rpm, em,'o-')
ax.set_xlabel('RPM')
ax.set_ylabel('ef_m[%]')'''

#axem.plot(R , em)#, 'o-')
#axem.set_xlabel('R[Ohm]')
#axem.set_ylabel('e_generador[%]')
'''axet.plot(R , ed , 'o')
axet.set_xlabel('R[Ohm]')
axet.set_ylabel('e_motor[%]')'''
#axet.plot(rpm , P , 'o-')
#plt.show()  
 
#@jit 
def graficaPotencia(arduino_lectures):
    
    displayList = []
    #Res DP
    listaR = []
    listalr = []
    #Potencia
    listaR1 = []
    listalP = []
    #Ef_motor
    listaR2 = []
    listalEm = []
    #Ef dinamo
    listaR3 = []
    listalEd = []
    #RPM
    listaR4 = []
    listalRpms = []
    mlp.rcParams.update({'font.size': 10})
    pivote2=1
    
    '''for j in range(len(arduino_lectures)):
        RList = arduino_lectures[j][0]
        rpmList = arduino_lectures[j][1]'''
        #PList = arduino_lectures[j][7]
        #efgList = arduino_lectures[j][8]
        #efmList = arduino_lectures[j][9]
    
    if len(arduino_lectures) >= 7:
        for i in range(len(arduino_lectures)):
            #print("AL", arduino_lectures)
            Rdp = float (arduino_lectures[i][0])#Ohm[i]
            vRpm = float(arduino_lectures[i][1])
            vDv01 = float(arduino_lectures[i][2])
            vVg = float(arduino_lectures[i][3]) #Generador
            vDv23 = float(arduino_lectures[i][4])
            vVd = float(arduino_lectures[i][5]) #Dinamo
            vT = float(arduino_lectures[i][6])
            
            if Rdp == pivote2:

                try:
                    if Rdp >=1:
                        print("Es " + str(Rdp))
                        Ie = (vVg/Rdp)#/1000 #Amperes
                        Is = (vVd/Rdp)#/1000#Amperes
                        P = ((((vVg+vVd)-(Ie-Is)*r)*Ie*Is)/(Ie+Is))
                        em = (P/(Ie*vVg))*100
                        ed = ((Is*vVd)/P)*100
                        rpm = float(str(arduino_lectures[i][1]))
                        print(P)
                        print(em)
                        print(ed)
                        print(rpm)
                        listaP.append(P)
                        listaRPM.append(rpm)
                        listaefm.append(em)
                        listaeft.append(ed)
                        listaR.append(Rdp) #Listas de elementos
                        listaR1.append(P)
                        listaR2.append(em)
                        listaR3.append(ed)
                        listaR4.append(rpm)
                        print("En C")
                        print("lidts: ", listaR)
                        print("lidtsP: ", listaR1)
                        print("lidtsEM: " , listaR2)
                        print("lidtsED: " , listaR3)
                        #global listaR1

                            
                except ZeroDivisionError:
                    print("errors")
            if len(listaR)==49:
                print("final antes de agregar: ",listalr)
                print("final Pot antes de agregar: ",listalP)
                print("final Em antes de agregar: ",listalEm)
                print("lista R:", listaR)
                print("lista R1: " , listaR1)
                print("lista R2: " , listaR2)
                l=listaR.copy()
                l1 = listaR1.copy()
                l2 = listaR2.copy()
                l3 = listaR3.copy()
                l4 = listaR4.copy()
                print("Copia", l)
                print("Copia", l1)
                print("Copia", l2)
                print("Copia", l3)
                print("Copia", l4)
                listalr.append(l)
                listalP.append(l1)
                listalEm.append(l2)
                listalEd.append(l3)
                listalRpms.append(l4)
                print("Esta es la final: ", listalr)
                print("Esta es la final P: " , listalP)
                print("Esta es la final EM: " , listalEm)
                print("Esta es la final RPM: " , listalRpms)
                #
                sR = 0
                psR = 0
                sP = 0
                psP = 0
                sEm = 0
                psEm = 0
                sEd = 0
                psEd = 0
                sRpm = 0
                psRpm = 0

                for y in range(len(l)):
                    sR += l[y]
                    sP += l1[y]
                    sEm += l2[y]
                    sEd += l3[y]
                    sRpm += l4[y]
                
                psR = (sR/len(l))
                psP = (sP/len(l1))
                psEm = (sEm/len(l2))
                psEd = (sEd/len(l3))
                psRpm = (sRpm/len(l4))

                print("Promedio Res", psR)
                print("Promedio Pot", psP)
                print("Promedio Em", psEm)
                print("Promedio Ed" , psEd)
                ##Aquí estaba el for

                '''listaR.clear()
                listaR1.clear()
                listaR2.clear()
                print("Lista vacía" , listaR)
                print("Lista P vacía: " , listaR1)
                print("Lista Em vacía: " , listaR2)'''
                #exit()
                pivote2 += 1
                #input()

                fig= plt.figure()
                axem = plt.axes()
                
                axem.plot(psR , psEm , 'o-') #ed o-
                #axet.plot(psR , psRpm  , 'o-')
                #ax.plot(psR , rpm  , 'o-')
                axem.set_ylim([0,100])
                axem.set_xlabel('R[Ohm]')
                axem.set_ylabel('e_generador[%]')
                plt.savefig('static/img/imageEfmotor.jpg')
                
                fig2 = plt.figure()
                axet = plt.axes()

                axet.plot(psR , psRpm  , 'o-')
                axet.set_xlabel('R[Ohm]')
                axet.set_ylabel('RPM')#('e_motor[%]')
                plt.savefig('static/img/image.jpg')

                fig3 = plt.figure()
                ax = plt.axes()

                ax.plot(psR, psEd,'o-')
                ax.set_xlabel('R[Ohm]')
                ax.set_ylabel('e_dinamo[%]')
                listaR.clear()
                listaR1.clear()
                listaR2.clear()
                listaR3.clear()
                listaR4.clear()
                displayList.clear()
                print("Lista vacía" , listaR)
                print("Lista P vacía: " , listaR1)
                print("Lista Em vacía: " , listaR2)
                print("Lista RPM vacía:" , listaR4)
    
    #ax.plot(PList,rpmList, 'o-')
    ##ax.plot(rpm, ed,'o-')
    #ax.plot(listaefm, listaRPM,'o-')
    #ax.plot(listaRPM, listaefm,'o-')
    #ax.set_xlabel('RPM')
    #ax.set_ylabel('ef_m[%]')
    #plt.show()
    #plt.savefig('static/img/image.jpg') 
    
    '''
    axem.plot(psR , ed , 'o-')
    axem.plot(listaefm , listaR  , 'o-')
    axem.plot(listaR , listaeft  , 'o-')
    axem.set_xlab0el('R[Ohm]')
    axem.set_ylabel('e_generador[%]')
    plt.savefig('static/img/imageEfmotor.jpg')

    #axet.plot(R , em , 'o-')
    #axet.plot(listaefm , listaR , 'o-')
    ##axet.plot(listaR , listaefm , 'o-')
    axet.set_xlabel('R[Ohm]')
    axet.set_ylabel('e_motor[%]')
    plt.savefig('static/img/imageEfTurbina.jpg')'''

    
#arduino_lectures = [[398.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1213.0], [399.0, 0.0, -225.0, -0.0422, -1.0, -0.0002, 1216.0], [400.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1219.0], [401.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1222.0], [402.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1225.0], [403.0, 0.0, 5.0, 0.0009, 1.0, 0.0002, 1228.0], [404.0, 0.0, 0.0, 0.0, 1.0, 0.0002, 1231.0], [405.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1234.0], [406.0, 0.0, 4.0, 0.0007, 0.0, 0.0, 1237.0], [407.0, 0.0, 0.0, 0.0, -1.0, -0.0002, 1240.0], [408.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1243.0], [409.0, 0.0, 2.0, 0.0004, 1.0, 0.0002, 1246.0], [410.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1249.0], [411.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1252.0]]
#graficaPotencia(1)