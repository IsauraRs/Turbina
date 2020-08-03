from tkinter import *
from tkinter import messagebox, ttk
#import datos_Serial as datap
from view import *
import view as c

class Menu():

    def __init__(self):

        self.root = Tk()
        self.root.config(bg = "light sea green")
        self.root.title("Inicio")
        
        #Botones
        begin_Button = Button(self.root , text = 'Begin test' , command = self.inicio).pack()
        query_Button = Button(self.root , text = 'Query' , command = self.consulta).pack()
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

    def dpq(self):

        self.dpqt = Toplevel()
        self.dpqt.title("Search by DP")
        self.dpp = StringVar()

        dpvLabel = Label(self.dpqt , text = "Valor")
        dpvLabel.grid(row = 1, column = 5, padx = 10, pady = 10)

        dpven = Entry(self.dpqt)
        dpven.config(textvariable = self.dpp)
        dpven.grid(row = 2 , column = 2 , padx = 10 , pady = 10)
        
        sbp = Button(self.dpqt , text = 'Buscar', command = self.dpqsd)
        sbp.grid(row = 6, column = 5, padx = 10, pady = 10)

        #vLabel = Label(self.dpqt , text = )
        #vLabel.grid(row = 8 , column = 5 , padx = 10, pady = 10) 



    def consulta(self):

        self.qry = Toplevel()
        self.qry.title("Query")

        tcLabel = Label(self.qry , text = "Search by: ")
        tcLabel.grid(row = 1, column = 5, padx = 10, pady = 10)

        dpB = Button(self.qry , text = 'Digiatal Potentiometer' , command = self.dpq)
        dpB.grid(row = 2 , column = 6 , padx = 10, pady = 10)

        

         

def main():
    
    ap = Menu()
    #datap.testc()

if __name__ == '__main__':
    main()