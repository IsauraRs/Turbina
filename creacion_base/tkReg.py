from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image 
import threading
import serial
import time

from datos_Serial import *
import datos_Serial as datap

from view import *
import view as c


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
        self.rpmr = StringVar()
        self.rpmset = StringVar()
        self.ardat = StringVar()
        
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

        def meb():
    
            arduino.close()
            self.root.destroy()

        exit_Button = Button(self.root , text = 'Exit' , command = meb , height = 8 , width = 16)#.pack()
        exit_Button.grid(row = 6 , column = 10 , padx = 5 , pady = 5)
        #place(x = 400 , y = 410) #grid(row = 8 , column = 80 , padx = 0 , pady = 0)
        exit_Button.config(font = ('Helvetica' , 16))

        self.root.mainloop()

    #def t1(self):

        #self.datk.set(nl)
        #print(nl)
    def endTest(self):

        arduino.close()
        self.root.destroy()
    
    
    def inicio(self):

        self.bgn = Toplevel()
        self.bgn.title("Test")
        self.bgn.config(bg = "light sea green")


        self.datk = StringVar()

        #self.datk.set(nl)

        runningLabel = Label(self.bgn , text = "Reading data")
        runningLabel.grid(row = 1 , column = 5 , padx = 10 , pady = 10)
        runningLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16))

        exit_Button = Button(self.bgn , text = 'Exit' , command = self.endTest) #, height = 10 , width = 20)
        exit_Button.grid(row = 4 , column = 5 , padx = 10 , pady = 10)
        exit_Button.config(font = ('Helvetica' , 16))

        def backt():
            arduino.close()
            self.bgn.destroy()

        bm_Button = Button(self.bgn , text = 'Back' , command = backt)
        bm_Button.grid(row = 4 , column = 10 , padx = 10 , pady = 10)
        bm_Button.config(font = ('Helvetica' , 16))

        dtLabel = Label(self.bgn , textvariable = self.datk)
        dtLabel.grid(row = 10 , column = 1 )
        dtLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 400)

        self.scrollbar = Scrollbar(self.bgn)

        self.log = Text( self.bgn, width=30, height=30, takefocus=0)
        self.log.grid(row = 9 , column = 4)
        self.log.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.log.yview)

        print(vfl)
        self.log.insert(END, vfl)
        time.sleep(5)
        
        #self.datk.set()

        threadFunc = threading.Thread(target = testc)
        threadFunc.start()

        
        #self.ardat.set(self.sdar)

        
    def dpqsd(self):

        self.dpt = str(self.dpp.get())

        a = c.vista(str(self.dpt))

        self.resultado.set(a[1])
        #print(dl)

        self.dato.set(a[0])


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

        dpvLabel = Label(self.dpqt , text = "Value: ")
        dpvLabel.grid(row = 1, column = 1 , padx = 0, pady = 5)
        dpvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dpven = Entry(self.dpqt)
        dpven.config(textvariable = self.dpp , font = ('Helvetica' , 16))
        dpven.grid(row = 1 , column = 2 , padx = 5 , pady = 5)
        
        sbp = Button(self.dpqt , text = 'Search', command = self.dpqsd)
        sbp.grid(row = 1, column = 3, padx = 2, pady = 2)
        sbp.config(font = ('Helvetica' , 16))

        rLabel = Label(self.dpqt , text = "Search results: ")
        rLabel.grid(row = 29 , column = 0 , padx = 0 , pady = 0)
        rLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dLabel = Label(self.dpqt , text = "Displayed data (in order): ")
        dLabel.grid(row = 28 , column = 0 , padx = 5 , pady = 5)
        dLabel.config(bg = "light sea green" , font = ('Helvetica' , 16) , wraplength = 200)

        resLabel = Label(self.dpqt , text = "ID , digital potentiometer , RPM , voltage difference , voltage, time")
        resLabel.grid(row = 28 , column = 1 , padx = 5 , pady = 1)
        resLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))


        vLabel = Label(self.dpqt , textvariable = self.resultado)
        vLabel.grid(row = 29 , column = 1 , padx = 0, pady = 50)
        vLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 400)

        ccLabel = Label(self.dpqt , text = "Number of matches: ")
        ccLabel.grid(row = 28 , column = 3 , padx = 5 , pady = 5)
        ccLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 150)

        cLabel = Label(self.dpqt , textvariable = self.dato)
        cLabel.grid(row = 28 , column = 4)
        cLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16))

        exit_Button = Button(self.dpqt , text = 'Exit' , command = self.root.destroy) 
        exit_Button.grid(row = 30 , column = 9 , padx = 5 , pady = 5)
        exit_Button.config(font = ('Helvetica' , 16))

        def back1():
            self.dato.set("")
            self.resultado.set("")
            dpven.delete("0" , "end")
            self.dpqt.destroy()

        bm_Button = Button(self.dpqt , text = 'Back' , command = back1)
        bm_Button.grid(row = 30 , column = 8 , padx = 5 , pady = 5)
        bm_Button.config(font = ('Helvetica' , 16))

        def newq():
            
            self.dato.set("")
            self.resultado.set("")
            dpven.delete("0" , "end")

        nq_Button = Button(self.dpqt , text = 'New' , command = newq)
        nq_Button.grid(row = 30 , column = 7 , padx = 5 , pady = 5)
        nq_Button.config(font = ('Helvetica' , 16))

        
    def vsd(self):

        self.vvt = str(self.vv.get())
        
        b = c.vistavolt(str(self.vvt))

        self.voltajer.set(b[0])

        self.volset.set(b[1])

    def volt(self):

        self.vtp = Toplevel()
        self.vtp.title("Search by voltage")
        self.vv = StringVar()
        self.vtp.config(bg = "light sea green")

        #Imágenes
        self.imC1 = PhotoImage(file = "logocemieo.png")#"image317.png") 
        self.imag11 = Label(self.vtp , image = self.imC1)
        self.imag11.grid(row = 0 , column = 0 , padx =  0, pady = 0) 
        self.imag11.config(bg = "light sea green")

        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.vtp , image = self.imi)
        self.imag2.grid(row = 0 , column = 90 , padx = 0, pady = 0) 
        self.imag2.config(bg = "light sea green")

        vvLabel = Label(self.vtp , text = "Value: ")
        vvLabel.grid(row = 1, column = 1 , padx = 0, pady = 5)
        vvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))
        
        vven = Entry(self.vtp)
        vven.config(textvariable = self.vv , font = ('Helvetica' , 16))
        vven.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

        sbb = Button(self.vtp , text = 'Search' , command = self.vsd)
        sbb.grid(row = 1, column = 3, padx = 2, pady = 2)
        sbb.config(font = ('Helvetica' , 16))

        rvLabel = Label(self.vtp , text = "Search results: ")
        rvLabel.grid(row = 29 , column = 0 , padx = 0 , pady = 0)
        rvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        dvLabel = Label(self.vtp , text = "Displayed data (in order): ")
        dvLabel.grid(row = 28 , column = 0 , padx = 5 , pady = 5)
        dvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16) , wraplength = 200)

        resvLabel = Label(self.vtp , text = "ID , digital potentiometer , RPM , voltage difference , voltage, time")
        resvLabel.grid(row = 28 , column = 1 , padx = 5 , pady = 1)
        resvLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        Labeln = Label(self.vtp , textvariable = self.voltajer)
        Labeln.grid(row = 29 , column = 1 , padx = 0, pady = 50)
        Labeln.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 400)

        cvLabel = Label(self.vtp , text = "Number of matches: ")
        cvLabel.grid(row = 28 , column = 3 , padx = 5 , pady = 5)
        cvLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 150)

        crLabel = Label(self.vtp , textvariable = self.volset)
        crLabel.grid(row = 28 , column = 4)
        crLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16))

        exit_Button = Button(self.vtp , text = 'Exit' , command = self.root.destroy) 
        exit_Button.grid(row = 30 , column = 9 , padx = 5 , pady = 5)
        exit_Button.config(font = ('Helvetica' , 16))

        def back2():
            self.voltajer.set("")
            self.volset.set("")
            vven.delete("0" , "end")
            self.vtp.destroy()

        bm_Button = Button(self.vtp , text = 'Back' , command = back2)
        bm_Button.grid(row = 30 , column = 8 , padx = 5 , pady = 5)
        bm_Button.config(font = ('Helvetica' , 16))

        def newq2():
            
            self.volset.set("")
            self.voltajer.set("")
            vven.delete("0" , "end")

        nq_Button = Button(self.vtp , text = 'New' , command = newq2)
        nq_Button.grid(row = 30 , column = 7 , padx = 5 , pady = 5)
        nq_Button.config(font = ('Helvetica' , 16))

    def rsd(self):

        self.rpmvf = str(self.rpmv.get())

        d = c.vistarpm(str(self.rpmvf))

        self.rpmr.set(d[0])

        self.rpmset.set(d[1])

    def rpm(self):

        self.rpmt = Toplevel()
        self.rpmt.title("RPM")
        self.rpmv = StringVar()
        self.rpmt.config(bg = "light sea green")

        #Imágenes
        self.imC1 = PhotoImage(file = "logocemieo.png")#"image317.png") 
        self.imag11 = Label(self.rpmt , image = self.imC1)
        self.imag11.grid(row = 0 , column = 0 , padx =  0, pady = 0) 
        self.imag11.config(bg = "light sea green")

        self.imi = PhotoImage(file = "image72.png")
        self.imag2 = Label(self.rpmt , image = self.imi)
        self.imag2.grid(row = 0 , column = 90 , padx = 0, pady = 0) 
        self.imag2.config(bg = "light sea green")

        rmLabel = Label(self.rpmt , text = "Value: ")
        rmLabel.grid(row = 1, column = 1 , padx = 0, pady = 5)
        rmLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        rpven = Entry(self.rpmt)
        rpven.config(textvariable = self.rpmv , font = ('Helvetica' , 16))
        rpven.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

        rsb = Button(self.rpmt , text = 'Search' , command = self.rsd)
        rsb.grid(row = 1, column = 3, padx = 2, pady = 2)
        rsb.config(font = ('Helvetica' , 16))

        rrLabel = Label(self.rpmt , text = "Search results: ")
        rrLabel.grid(row = 29 , column = 0 , padx = 0 , pady = 0)
        rrLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        rdLabel = Label(self.rpmt , text = "Displayed data (in order): ")
        rdLabel.grid(row = 28 , column = 0 , padx = 5 , pady = 5)
        rdLabel.config(bg = "light sea green" , font = ('Helvetica' , 16) , wraplength = 200)

        rresLabel = Label(self.rpmt , text = "ID , digital potentiometer , RPM , voltage difference , voltage, time")
        rresLabel.grid(row = 28 , column = 1 , padx = 5 , pady = 1)
        rresLabel.config(bg = "light sea green" , font = ('Helvetica' , 16))

        rpLabel = Label(self.rpmt , textvariable = self.rpmr)
        rpLabel.grid(row = 29 , column = 1 , padx = 0, pady = 50)
        rpLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 400)

        ccrLabel = Label(self.rpmt , text = "Number of matches: ")
        ccrLabel.grid(row = 28 , column = 3 , padx = 5 , pady = 5)
        ccrLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16) , wraplength = 150)

        crLabel = Label(self.rpmt , textvariable = self.rpmset)
        crLabel.grid(row = 28 , column = 4)
        crLabel.config(bg = "light sea green"  , font = ('Helvetica' , 16))

        exit_Button = Button(self.rpmt , text = 'Exit' , command = self.root.destroy)
        exit_Button.grid(row = 30 , column = 9 , padx = 5 , pady = 5)
        exit_Button.config(font = ('Helvetica' , 16))

        def back3():
            self.dato.set("")
            self.resultado.set("")
            dpven.delete("0" , "end")
            self.dpqt.destroy()
        
        bm_Button = Button(self.rpmt , text = 'Back' , command = back3)
        bm_Button.grid(row = 30 , column = 8 , padx = 5 , pady = 5)
        bm_Button.config(font = ('Helvetica' , 16))

        def newq3():
            
            self.dato.set("")
            self.resultado.set("")
            dpven.delete("0" , "end")
        
        nq_Button = Button(self.rpmt , text = 'New' , command = newq3)
        nq_Button.grid(row = 30 , column = 7) # , padx = 5 , pady = 5)
        nq_Button.config(font = ('Helvetica' , 16))

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

        rpmB =  Button(self.qry , text = 'RPM' , command = self.rpm)
        rpmB.grid(row = 4 , column = 10 , padx = 0 , pady = 10)
        rpmB.config(font = ('Helvetica' , 16))

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