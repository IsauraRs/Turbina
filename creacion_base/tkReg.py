from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image 

#from datos_Serial import *
#import datos_Serial as datap

from view import *
import view as c

class Menu():

    def __init__(self):

        self.root = Tk()
        self.root.geometry("1130x600")
        self.root.config(bg = "light sea green")
        self.root.resizable(0,0)
        self.root.title("Inicio")

        self.resultado = StringVar()
        self.dato = StringVar()
        self.dpqr1 = StringVar()
        self.dpqr2 = StringVar()
        
        #Imágenes
        imC = PhotoImage(file = "image317.png") 
        imag1 = Label(self.root , image = imC)
        imag1.place(x = 0 , y = 0)
        imag1.config(bg = "light sea green")

        imi = PhotoImage(file = "image72.png")
        imag2 = Label(self.root , image = imi)
        imag2.place(x = 719 , y = 0)
        imag2.config(bg = "light sea green")

        #Botones
        begin_Button = Button(self.root , text = 'Begin test' , command = self.inicio , height = 10 , width = 20).pack()
        query_Button = Button(self.root , text = 'Query' , command = self.consulta , height = 10 , width = 20).pack()
        exit_Button = Button(self.root , text = 'Exit' , command = self.root.destroy , height = 10 , width = 20).pack()
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

        exit_Button = Button(self.bgn , text = 'Exit' , command = self.root.destroy) #, height = 10 , width = 20)
        exit_Button.grid(row = 4 , column = 5 , padx = 10 , pady = 10)

        bm_Button = Button(self.bgn , text = 'Back' , command = self.bgn.destroy)
        bm_Button.grid(row = 4 , column = 10 , padx = 10 , pady = 10)
        
        #datap.testc()
        #for j in range(len(nl)):
         #   self.datk.set(nl)
        #a = datap.testc()
        
    
    def dpqsd(self):

        self.dpt = str(self.dpp.get())

        c.vista(str(self.dpt))

        self.resultado.set(dl)
        print(dl)
        

    def dpq(self):

        self.dpqt = Toplevel()
        self.dpqt.title("Search by DP")
        self.dpp = StringVar()


        self.dpqt.geometry("1150x600")
        self.dpqt.config(bg = "light sea green")

        self.imC1 = PhotoImage(file = "image317.png") 
        self.imag11 = Label(self.dpqt , image = self.imC1)
        self.imag11.grid(row = 0 , column = 0 , padx = 1 , pady = 1) 
        self.imag11.config(bg = "light sea green")

        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.dpqt , image = self.imi)
        self.imag2.grid(row = 0 , column = 48 , padx = 1, pady = 1) 
        self.imag2.config(bg = "light sea green")

        dpvLabel = Label(self.dpqt , text = "Valor: ")
        dpvLabel.grid(row = 1, column = 10, padx = 10, pady = 10)
        dpvLabel.config(bg = "light sea green")

        dpven = Entry(self.dpqt)
        dpven.config(textvariable = self.dpp)
        dpven.grid(row = 1 , column = 20 , padx = 10 , pady = 10)
        
        sbp = Button(self.dpqt , text = 'Buscar', command = self.dpqsd)
        sbp.grid(row = 1, column = 30, padx = 1, pady = 1)

        vLabel = Label(self.dpqt , textvariable = self.resultado)
        vLabel.grid(row = 50 , column = 60 , padx = 10, pady = 10)
        vLabel.config(bg = "light sea green")

        exit_Button = Button(self.dpqt , text = 'Exit' , command = self.root.destroy) #, height = 10 , width = 20)
        exit_Button.grid(row = 80 , column = 10 , padx = 10 , pady = 10)

        bm_Button = Button(self.dpqt , text = 'Back' , command = self.dpqt.destroy)
        bm_Button.grid(row = 80 , column = 40 , padx = 10 , pady = 10)



    def consulta(self):

        self.qry = Toplevel()
        self.qry.title("Query")

        self.qry.geometry("1130x600")
        self.qry.config(bg = "light sea green")

        self.imC = PhotoImage(file = "image317.png") 
        self.imag1 = Label(self.qry , image = self.imC)
        self.imag1.grid(row = 0 , column = 0 , padx = 1 , pady = 1)
        self.imag1.config(bg = "light sea green")
        
        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.qry , image = self.imi)
        self.imag2.grid(row = 0 , column = 60 , padx = 1, pady = 1)
        self.imag2.config(bg = "light sea green")

        tcLabel = Label(self.qry , text = "Search by: ")
        tcLabel.grid(row = 1, column = 5, padx = 10 , pady = 10)
        tcLabel.config(bg = "light sea green")

        dpB = Button(self.qry , text = 'Digital Potentiometer' , command = self.dpq)
        dpB.grid(row = 2 , column = 40 , padx = 10 , pady = 10)

        exit_Button = Button(self.qry , text = 'Exit' , command = self.root.destroy) 
        exit_Button.grid(row = 7000 , column = 10 , padx = 10 , pady = 10)

        bm_Button = Button(self.qry , text = 'Back' , command = self.qry.destroy)
        bm_Button.grid(row = 7000 , column = 40 , padx = 10 , pady = 10)

        

         

def main():
    
    ap = Menu()
    #datap.testc()

if __name__ == '__main__':
    main()