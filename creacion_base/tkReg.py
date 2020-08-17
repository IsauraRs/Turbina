from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image 

#from datos_Serial import *
#import datos_Serial as datap

from view import *
import view as c

nnl = []

class Menu():

    def __init__(self):

        self.root = Tk()
        #self.root.geometry("1150x600")
        self.root.config(bg = "light sea green")
        #self.root.resizable(0,0)
        self.root.title("Inicio")

        self.resultado = StringVar()
        self.dato = StringVar()
        self.voltajer = StringVar()
        self.volset = StringVar()
        
        #Imágenes1
        imC = PhotoImage(file = "logocemieo.png") #"image317.png") 
        imag1 = Label(self.root , image = imC)
        #imag1.place(x = 0 , y = 0)
        imag1.grid(row = 0 , column = 1 , padx =  10, pady = 10) 
        imag1.config(bg = "light sea green")

        imi = PhotoImage(file = "image72.png")
        imag2 = Label(self.root , image = imi)
        imag2.grid(row = 0 , column = 1100 , padx = 10, pady = 10)
        #imag2.grid(row = 0 , column = 45 , padx = 0, pady = 0) 
        #imag2.place(x = 719 , y = 0)
        imag2.config(bg = "light sea green")

        #Botones
        begin_Button = Button(self.root , text = 'Begin test' , command = self.inicio , height = 8 , width = 16)#.pack()
        begin_Button.grid(row = 0 , column = 10 , padx = 95 , pady = 5)
        #place(x = 400 , y = 10) #grid(row = 0 , column = 80 , padx = 0 , pady = 0)
        begin_Button.config(font = ('Helvetica' , 16))

        query_Button = Button(self.root , text = 'Query' , command = self.consulta , height = 8 , width = 16)#.pack()
        query_Button.grid(row = 2 , column  = 10 , padx = 5 , pady = 5)
        #place(x = 400 , y = 210) #grid(row = 4 , column  = 80 , padx = 0 , pady = 0)
        query_Button.config(font = ('Helvetica' , 16))

        exit_Button = Button(self.root , text = 'Exit' , command = self.root.destroy , height = 8 , width = 16)#.pack()
        exit_Button.grid(row = 6 , column = 10 , padx = 5 , pady = 5)
        #place(x = 400 , y = 410) #grid(row = 8 , column = 80 , padx = 0 , pady = 0)
        exit_Button.config(font = ('Helvetica' , 16))

        self.root.mainloop()

    def t1(self):

        self.datk.set(nl)
        print(nl)
    
    def inicio(self):

        self.bgn = Toplevel()
        self.bgn.title("Test")
        self.bgn.config(bg = "light sea green")


        self.datk = StringVar()

        #self.datk.set(nl)

        runningLabel = Label(self.bgn , text = "Reading data")
        runningLabel.grid(row = 1, column = 5, padx = 10, pady = 10)
        runningLabel.config(font = ('Helvetica' , 16))

        exit_Button = Button(self.bgn , text = 'Exit' , command = self.root.destroy) #, height = 10 , width = 20)
        exit_Button.grid(row = 4 , column = 5 , padx = 10 , pady = 10)
        exit_Button.config(font = ('Helvetica' , 16))

        bm_Button = Button(self.bgn , text = 'Back' , command = self.bgn.destroy)
        bm_Button.grid(row = 4 , column = 10 , padx = 10 , pady = 10)
        bm_Button.config(font = ('Helvetica' , 16))
        
        #datap.testc()
        #for j in range(len(nl)):
         #   self.datk.set(nl)
        #a = datap.testc()
        
    
    def dpqsd(self):

        self.dpt = str(self.dpp.get())

        c.vista(str(self.dpt))

        self.resultado.set(dl)
        print(dl)

        self.dato.set(cd)



    def newq(self):
    
            #self.dpven.delete(0,'END')
            #vLabel.delete('0' , 'END')
            #dpven.delete(0 , 'end')
            self.dato.set("")
            self.resultado.set("")
            self.dpt.set('')
            self.dpp.set('')
            dpven.delete("0" , "end")
            self.dpt = str(self.dpp.get())

            c.vista(str(self.dpt))

            self.resultado.set(dl)
            print(dl)

            self.dato.set(cd)

            #vLabel.set(0)
            #self.dpp.set("")
            #sself.dpqsd()

    def dpq(self):

        self.dpqt = Toplevel()
        self.dpqt.title("Search by DP")
        self.dpp = StringVar()

        #self.dpqt.geometry("1150x600")
        self.dpqt.config(bg = "light sea green")
        self.dpqt.resizable(0,0)

        self.imC1 = PhotoImage(file = "logocemieo.png")#"image317.png") 
        self.imag11 = Label(self.dpqt , image = self.imC1)
        self.imag11.grid(row = 0 , column = 0 , padx =  0, pady = 0) 
        self.imag11.config(bg = "light sea green")

        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.dpqt , image = self.imi)
        self.imag2.grid(row = 0 , column = 8 , padx = 0, pady = 0) 
        self.imag2.config(bg = "light sea green")    

        dpvLabel = Label(self.dpqt , text = "Valor: ")
        dpvLabel.grid(row = 1, column = 1 , padx = 0, pady = 5)
        dpvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dpven = Entry(self.dpqt)
        dpven.config(textvariable = self.dpp , font = ('Helvetica' , 16))
        dpven.grid(row = 1 , column = 2 , padx = 5 , pady = 5)
        
        sbp = Button(self.dpqt , text = 'Buscar', command = self.dpqsd)
        sbp.grid(row = 1, column = 3, padx = 2, pady = 2)
        sbp.config(font = ('Helvetica' , 16))

        rLabel = Label(self.dpqt , text = "Resultado de la búsqueda: ")
        rLabel.grid(row = 29 , column = 0 , padx = 0 , pady = 0)
        rLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dLabel = Label(self.dpqt , text = "Datos que se muestran (en orden): ")
        dLabel.grid(row = 28 , column = 0 , padx = 5 , pady = 5)
        dLabel.config(bg = "light sea green" , font = ('Helvetica' , 16) , wraplength = 200)

        resLabel = Label(self.dpqt , text = "ID , potenciómetro digital , RPMs , diferencia de voltaje , voltaje, tiempo")
        resLabel.grid(row = 28 , column = 1 , padx = 5 , pady = 1)
        resLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))


        vLabel = Label(self.dpqt , textvariable = self.resultado) #, yscrollcommand = scb.set)
        vLabel.grid(row = 29 , column = 1 , padx = 0, pady = 50)
        vLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 400)

        ccLabel = Label(self.dpqt , text = "Número de coincidencias: ")
        ccLabel.grid(row = 28 , column = 3 , padx = 5 , pady = 5)
        ccLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 150)

        cLabel = Label(self.dpqt , textvariable = self.dato)
        cLabel.grid(row = 28 , column = 4)
        cLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16))

        exit_Button = Button(self.dpqt , text = 'Exit' , command = self.root.destroy) 
        exit_Button.grid(row = 30 , column = 9 , padx = 5 , pady = 5)
        exit_Button.config(font = ('Helvetica' , 16))

        bm_Button = Button(self.dpqt , text = 'Back' , command = self.dpqt.destroy)
        bm_Button.grid(row = 30 , column = 8 , padx = 5 , pady = 5)
        bm_Button.config(font = ('Helvetica' , 16))

        nq_Button = Button(self.dpqt , text = 'New' , command = self.newq)
        nq_Button.grid(row = 30 , column = 7 , padx = 5 , pady = 5)
        nq_Button.config(font = ('Helvetica' , 16))

    def vsd(self):

        self.vvt = str(self.vv.get())


    def volt(self):

        self.vtp = Toplevel()
        self.vtp.title("Search by voltage")
        self.vv = StringVar()

        self.imC1 = PhotoImage(file = "logocemieo.png")#"image317.png") 
        self.imag11 = Label(self.dpqt , image = self.imC1)
        self.imag11.grid(row = 0 , column = 0 , padx =  0, pady = 0) 
        self.imag11.config(bg = "light sea green")

        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.dpqt , image = self.imi)
        self.imag2.grid(row = 0 , column = 90 , padx = 0, pady = 0) 
        self.imag2.config(bg = "light sea green")
        

    def consulta(self):

        self.qry = Toplevel()
        self.qry.title("Query")

        #self.qry.geometry("1150x600")
        self.qry.config(bg = "light sea green")

        self.imC = PhotoImage(file = "logocemieo.png")#"image317.png") 
        self.imag1 = Label(self.qry , image = self.imC)
        self.imag1.grid(row = 0 , column = 0 , padx = 0 , pady = 0)
        self.imag1.config(bg = "light sea green")
        
        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.qry , image = self.imi)
        self.imag2.grid(row = 0 , column = 45 , padx = 1, pady = 1)
        self.imag2.config(bg = "light sea green")

        tcLabel = Label(self.qry , text = "Search by: ")
        tcLabel.grid(row = 1, column = 1, padx = 0 , pady = 0)
        tcLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dpB = Button(self.qry , text = 'Digital Potentiometer' , command = self.dpq)
        dpB.grid(row = 2 , column = 10 , padx = 0 , pady = 1)
        dpB.config(font = ('Helvetica' , 16))

        vB = Button(self.qry , text = 'Voltage' , command = self.volt)
        vB.grid(row = 3 , column = 10 , padx = 0 , pady = 10)
        vB.config(font = ('Helvetica' , 16))

        exit_Button = Button(self.qry , text = 'Exit' , command = self.root.destroy) 
        exit_Button.grid(row = 7000 , column = 10 , padx = 10 , pady = 10)
        exit_Button.config(font = ('Helvetica' , 16))

        bm_Button = Button(self.qry , text = 'Back' , command = self.qry.destroy)
        bm_Button.grid(row = 7000 , column = 40 , padx = 10 , pady = 10)
        bm_Button.config(font = ('Helvetica' , 16))

        

         

def main():
    
    ap = Menu()
    #datap.testc()

if __name__ == '__main__':
    main()