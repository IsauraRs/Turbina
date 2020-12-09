import matplotlib as mlp
mlp.use('Agg')
import matplotlib.pyplot as plt
#from spreadSheetReport import createGraphs as cg

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
gLem = []
gLet = []
gLr = []
gLrpm = []
sR = 0
promsR = 0
P = 0
em = 0
ed = 0


def graficaPotencia(arduino_lectures):
    
    global displayList, displayList1, displayList2,displayList3

    displayList = []
    displayList1 = []
    displayList2 = []
    displayList3 = []
    
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
                        Ie = (vVg/Rdp)/1000 #Amperes
                        Is = (vVd/Rdp)/1000#Amperes
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
                        '''print("lidts: ", listaR)
                        print("lidtsP: ", listaR1)
                        print("lidtsEM: " , listaR2)
                        print("lidtsED: " , listaR3)'''
                        #global listaR1

                            
                except ZeroDivisionError:
                    print("errors")
            if len(listaR)==39:
                '''print("final antes de agregar: ",listalr)
                print("final Pot antes de agregar: ",listalP)
                print("final Em antes de agregar: ",listalEm)
                print("lista R:", listaR)
                print("lista R1: " , listaR1)
                print("lista R2: " , listaR2)'''
                l=listaR.copy()
                l1 = listaR1.copy()
                l2 = listaR2.copy()
                l3 = listaR3.copy()
                l4 = listaR4.copy()
                '''print("Copia", l)
                print("Copia", l1)
                print("Copia", l2)
                print("Copia", l3)
                print("Copia", l4)'''
                listalr.append(l)
                listalP.append(l1)
                listalEm.append(l2)
                listalEd.append(l3)
                listalRpms.append(l4)
                '''print("Esta es la final: ", listalr)
                print("Esta es la final P: " , listalP)
                print("Esta es la final EM: " , listalEm)
                print("Esta es la final RPM: " , listalRpms)'''
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

                #print("Promedio Res", psR)
                #print("Promedio Pot", psP)
                #print("Promedio Em", psEm)
                #print("Promedio Ed" , psEd)
                
                displayList.append(psR)
                displayList1.append(psRpm)
                displayList2.append(psEm)
                displayList3.append(psEd)
                #cg(displayList,displayList1) #,displayList2,displayList3)
                print("dl:",displayList)
                print("dl1:", displayList1)
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
                
                axem.plot(displayList, displayList2, 'o-')
                #axem.plot(psR , psEm , 'o-') #ed o-
                #axet.plot(psR , psRpm  , 'o-')
                #ax.plot(psR , rpm  , 'o-')
                #axem.set_ylim([0,110])
                axem.set_xlabel('R[Ω]')
                axem.set_ylabel('e_generador[%]')
                plt.savefig('static/img/imageEfmotor.jpg')
                
                fig2 = plt.figure()
                axet = plt.axes()

                axet.plot(displayList,displayList1,'o-')
                #axet.plot(psR , psRpm  , 'o-')
                axet.set_xlabel('R[Ω]')
                axet.set_ylabel('RPM')#('e_motor[%]')
                plt.savefig('static/img/image.jpg')

                fig3 = plt.figure()
                ax = plt.axes()

                ax.plot(displayList,displayList3,'o-')
                #ax.plot(psR, psEd,'o-')
                ax.set_ylabel([0,110])
                ax.set_xlabel('R[Ω]')
                ax.set_ylabel('e_turbina[%]')
                plt.savefig('static/img/imageEfTurbina.jpg')

                listaR.clear()
                listaR1.clear()
                listaR2.clear()
                listaR3.clear()
                listaR4.clear()

                print("Lista vacía" , listaR)
                print("Lista P vacía: " , listaR1)
                print("Lista Em vacía: " , listaR2)
                print("Lista RPM vacía:" , listaR4)
    