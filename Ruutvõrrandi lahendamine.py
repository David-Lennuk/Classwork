from tkinter import *
from tkinter import messagebox as mb
import math
import matplotlib.pyplot  as plt
import numpy as np
global D,t,graf

def lahenda_virand(event):
    ent1_ = float(ent1.get())
    ent2_ = float(ent2.get())
    ent3_ = float(ent3.get())
    if not (ent1=="" or ent2=="" or ent3==""):
        D=(int(ent2)**2)-(4*int(ent1)*int(ent3))
        if D>0:
            x1_ = round((-1*ent2_+math.sqrt(D))/(2*ent1_),2)
            x2_ = round((-1*ent2_-math.sqrt(D))/(2*ent1_),2)
            t = f"X1 = {x1_}, \nX2 = {x2_}"
            graf = True
        elif D == 0:
            x1_ = round((-1*ent2_)/(2*ent1_),2)
            t = f"X1 = x1_"
            graf = True
        else:
            t = "Lahendusi"
            graf = False
            lbl5.configure(text = f"D  = {D}\n{t}")
    else:
        mb.showwarning("Tähelepanu!","On vaja sisestada numbreid!")

def graafik(graf:bool, D:float):
    if graf == True:
        ent1_ = float(ent1.get())
        ent2_ = float(ent2.get())
        ent3_ = float(ent3.get())
        x0 = (-ent2_)/(2*ent1_)
        y0 = ent1_*x0*x0+ent2_*x0+ent3_
        x1 = np.arange(x0-10, x0+10, 0.5)
        y1 = ent1_*x1*x1+ent2_*x1+ent3_
        fig = plt.figure()
        plt.plot(x1, y1, 'r-d')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show
        text = f"Porabula tipp ({x0}, {y0})"
    else:
        text = f"Graafikut ei saa kuidagi luua"
    lbl5.configure(text = f"D = {D}\n{t}\n{text}")






aken=Tk()
aken.title("Решение квадратного уравнения") 
aken.geometry("600x200")
aken.title("Tkinteri kasutamine")
tekst = "Pealkiri\n"

lbl=Label(aken, text = "Решение квадратного уравнения",font = "Arial 16",bg = "#f0e4c7")
ent1=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl2=Label(aken, text = "x**2+",font = "Arial 16")
ent2=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl3=Label(aken, text = "x+",font = "Arial 16")
ent3=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl4=Label(aken, text = "=0",font = "Arial 16")
lbl5=Label(aken, text = "Решено",font = "Arial 16",bg = "#c7d3f0")
btn=Button(aken, text = "Решать",font = "Arial 12",fg = "#1c4226",bg = "#aee8be",width = 14, heigh = 3,relief = RAISED)




lbl5.pack(side = BOTTOM)
lbl.pack()
ent1.pack(side = LEFT)
lbl2.pack(side = LEFT)

ent2.pack(side = LEFT)
lbl3.pack(side = LEFT)
ent3.pack(side = LEFT)
lbl4.pack(side = LEFT)
btn.pack(side = LEFT)
aken.mainloop()
