from tkinter import *
from PIL import Image 

from tkReg import *

def imag():
    imlog = Toplevel()
    #imlog.geometry("800xx800")
    imlog.resizable(0,0)

    imC = PhotoImage(file = "image317.png") 
    imag1 = Label(self.root , image = imC)
    imag1.place(x = 0 , y = 0)

    imi = PhotoImage(file = "image233.png")
    imag2 = Label(self.root , image = imi)
    imag2.place(x = 719 , y = 0)