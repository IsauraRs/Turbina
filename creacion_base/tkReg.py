from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image 

#import datos_Serial as datap
from view import *
import view as c


class Menu():

    def __init__(self):

        self.root = Tk()
        self.root.geometry("1130x600")
        self.root.config(bg = "light sea green")
        self.root.title("Inicio")

        self.resultado = StringVar()
        self.dato = StringVar()
        self.dpqr1 = StringVar()
        self.dpqr2 = StringVar()
        
        #Imágenes
        imC = PhotoImage(file = "image317.png") 
        imag1 = Label(self.root , image = imC)
        imag1.place(x = 0 , y = 0)

        imi = PhotoImage(file = "image233.png")
        imag2 = Label(self.root , image = imi)
        imag2.place(x = 719 , y = 0)

        #Botones
        begin_Button = Button(self.root , text = 'Begin test' , command = self.inicio , height = 10 , width = 20).pack()
        query_Button = Button(self.root , text = 'Query' , command = self.consulta , height = 10 , width = 20).pack()
        #exit_Button = Button(self.root , text = 'Exit' , command = self.salir).pack()
        self.root.mainloop()
    
    def inicio(self):

        self.bgn = Toplevel()
        self.bgn.title("Test")

        runningLabel = Label(self.bgn , text = "Reading data")
        runningLabel.grid(row = 1, column = 5, padx = 10, pady =10)
        
        #a = datap.testc()
        #datap.testc()
    
    def dpqsd(self):

        self.dpt = str(self.dpp.get())

        c.vista(str(self.dpt))

        self.resultado.set(dl)
        print(dl)
        

    def dpq(self):

        self.dpqt = Toplevel()
        self.dpqt.title("Search by DP")
        self.dpp = StringVar()

        dpvLabel = Label(self.dpqt , text = "Valor")
        dpvLabel.grid(row = 1, column = 2, padx = 10, pady = 10)

        dpven = Entry(self.dpqt)
        dpven.config(textvariable = self.dpp)
        dpven.grid(row = 1 , column = 5 , padx = 10 , pady = 10)
        
        sbp = Button(self.dpqt , text = 'Buscar', command = self.dpqsd)
        sbp.grid(row = 8, column = 2, padx = 10, pady = 10)

        vLabel = Label(self.dpqt , textvariable = self.resultado)
        vLabel.grid(row = 8 , column = 5 , padx = 10, pady = 10) 



    def consulta(self):

        self.qry = Toplevel()
        self.qry.title("Query")

        tcLabel = Label(self.qry , text = "Search by: ")
        tcLabel.grid(row = 1, column = 5, padx = 10, pady = 10)

        dpB = Button(self.qry , text = 'Digital Potentiometer' , command = self.dpq)
        dpB.grid(row = 2 , column = 6 , padx = 10, pady = 10)

        

         

def main():
    
    ap = Menu()
    #datap.testc()

if __name__ == '__main__':
    main()