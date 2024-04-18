from msilib import RadioButtonGroup
from msilib.schema import RadioButton
from tkinter import *
from tkinter import *
from math import *
import numpy
import matplotlib.pyplot  as plt
import numpy as np
global D,t,graf,K
D = -1
t = "Lahendusi pole"
graf = False

x=500
y=500
bg="#000000"
fg="#00FF00"
height=0
roundTo=2
step=5
canGraph=False
K=True

def solve():
    ent1_=float(ent1.get())
    ent2_=float(ent2.get())
    ent3_=float(ent3.get())
    D = ent2_*ent2_-4*ent1_*ent3_
    if D>0:
        x1_ = round((-1*ent2_+sqrt(D))/(2*ent1_),2)
        x2_ = round((-1*ent2_-sqrt(D))/(2*ent1_),2)
        t = f"X1 = {x1_}, \nX2 = {x2_}"
        graf = True
    elif D ==0:
        x1_ = round((-1*ent2_)/(2*ent1_),2)
        t = f"X1 = {x1_}"
        graf = True
    lbl5.configure(text = f"D = {D}\n{t}")
    return D,graf

def graafik(graf:bool, D:float):
    D,graf=solve()
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
        plt.title("Ruutvõrrand")
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text = f"Porabula tipp ({x0}, {y0})"
    else:
        text = f"Graafikut ei saa kuidagi luua"
    lbl5.configure(text = f"D = {D}\n{t}\n{text}")

def fish():
    """
    """
    x1=numpy.arange(0,9.5,0.5)
    y1=(2/27)*x1**2-3
    x2=numpy.arange(-10,0.5,0.5)
    y2=0.04*x2**2-3
    x3=numpy.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=numpy.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=numpy.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=numpy.arange(5,7.95,0.05)
    y6=(1/8)*(x6-7)**2+1.5
    x7=numpy.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=numpy.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=numpy.arange(-15,-9.5,0.5)
    y9=[1]*len(x9)
    x10=numpy.arange(3,4,0.5)
    y10=[3]*len(x10)
    whaleGraph=plt.figure()
    for i in range(10):
        plt.plot(locals()[f'x{i+1}'],locals()[f'y{i+1}'])
    plt.title('Vaal')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def frog():
    """
    """
    x1=numpy.arange(-7,7,0.5)
    y1=(-3/49)*x1**2+8
    x2=numpy.arange(-7,7,0.5)
    y2=(4/49)*x2**2+1
    x3=numpy.arange(-6.8,-2,0.5)
    y3=(-0.75)*(x3+4)**2+11
    x4=numpy.arange(2,6.8,0.5)
    y4=(-0.75)*(x4-4)**2+11
    x5=numpy.arange(-5.8,-2.8,0.5)
    y5=(-x5+4)**2+4
    x6=numpy.arange(2.8,5.8,0.5)
    y6=(-x6-4)**2+4
    x7=numpy.arange(-4,4,0.5)
    y7=(4/9)*x7**2-5
    x8=numpy.arange(-5.2,5.2,0.5)
    y8=(4/9)*x8**2-9
    x9=numpy.arange(-7,-2.8,0.5)
    y9=(-1/16)*(x9+3)**2-6
    x10=numpy.arange(2.8,7,0.5)
    y10=(-1/16)*(x10-3)**2-6
    x11=numpy.arange(7,0,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=numpy.arange(0,7,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=numpy.arange(-7,-4.5,0.5)
    y13=(-x13+5)**2
    x14=numpy.arange(4.5,7,0.5)
    y14=(-x14-5)**2
    x15=numpy.arange(-3,3,0.5)
    y15=(2/9)*x15**2+2
    frogGraph=plt.figure()
    for i in range(15):
        plt.plot(locals()[f'x{i+1}'],locals()[f'y{i+1}'])
    plt.title('Konn')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def butterfly():
    """
    """
    x1=numpy.arange(-9,-1,0.5)
    y1=(-1/8)*(x1+9)**2+8
    x2=numpy.arange(1,9,0.5)
    y2=(-1/8)*(x2-9)**2+8
    x3=numpy.arange(-9,-8,0.5)
    y3=7*(x3+8)**2+1
    x4=numpy.arange(8,9,0.5)
    y4=7*(x4-8)**2+1
    x5=numpy.arange(-8,-1,0.5)
    y5=(1/49)*(x5+1)**2
    x6=numpy.arange(1,8,0.5)
    y6=(1/49)*(x6-1)**2
    x7=numpy.arange(-8,-1,0.5)
    y7=(-4/49)*(x7+1)**2
    x8=numpy.arange(1,8,0.5)
    y8=(-4/49)*(x8-1)**2
    x9=numpy.arange(-8,-2,0.5)
    y9=(1/3)*(x9+5)**2-7
    x10=numpy.arange(2,8,0.5)
    y10=(1/3)*(x10-5)**2-7
    x11=numpy.arange(-2,-1,0.5)
    y11=(-2)*(x11+1)**2-2
    x12=numpy.arange(1,2,0.5)
    y12=(-2)*(x12-1)**2-2
    x13=numpy.arange(-1,1,0.5)
    y13=(-1)*(4*x13**2)+2
    x14=numpy.arange(-1,1,0.5)
    y14=4*x14**2-6
    x15=numpy.arange(-2,0,0.5)
    y15=(-1)*(1.5*x15)+2
    x16=numpy.arange(0,2,0.5)
    y16=1.5*x16+2
    butterflyGraph=plt.figure()
    for i in range(16):
        plt.plot(locals()[f'x{i+1}'],locals()[f'y{i+1}'])
    plt.title('Liblikas')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def extend():
    """
    """
    global K, whaleRB, frogRB, butterflyRB, solve2B, choice
    if K==True:
        K=not K
        extendB.config(text="Kahanda aken")
        choice=IntVar()
        whaleRB=Radiobutton(aken,
            text="Vaal",
            bg=bg,
            fg=fg,
            font="Arial 24",
            height=height,
            width=x,
            variable=choice,
            value=1,
            command=choice)
        frogRB=Radiobutton(aken,
            text="Konn",
            bg=bg,
            fg=fg,
            font="Arial 24",
            height=height,
            width=x,
            variable=choice,
            value=2,
            command=choice)
        butterflyRB=Radiobutton(aken,
            text="Liblikas",
            bg=bg,
            fg=fg,
            font="Arial 24",
            height=height,
            width=x,
            variable=choice,
            value=3,
            command=choice)
        solve2B=Button(aken,
            text="Näita graafikut",
            bg=bg,
            fg=fg,
            font="Arial 24",
            height=height,
            width=x,
            command=solve2)
        whaleRB.pack(side="top")
        frogRB.pack(side="top")
        butterflyRB.pack(side="top")
        solve2B.pack(side="top")
    elif K==False:
        K=not K
        extendB.config(text="Pikenda aken")
        whaleRB.destroy()
        frogRB.destroy()
        butterflyRB.destroy()
        solve2B.destroy()

def solve2():
    """
    """
    var=choice.get()
    if var==1:
        fish()
    elif var==2:
        frog()
    elif var==3:
        butterfly()
    else:
        pass









aken=Tk()
aken.title("Решение квадратного уравнения") 
aken.geometry("600x400")
aken.title("Tkinteri kasutamine")
tekst = "Pealkiri\n"

var=IntVar()

lbl=Label(aken, text = "Решение квадратного уравнения",font = "Arial 16",bg = "#f0e4c7")
ent1=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl2=Label(aken, text = "x**2+",font = "Arial 16")
ent2=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl3=Label(aken, text = "x+",font = "Arial 16")
ent3=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl4=Label(aken, text = "=0",font = "Arial 16")
lbl5=Label(aken, text = "Решено",font = "Arial 16",bg = "#c7d3f0")
btn1=Button(aken, text = "Решать",font = "Arial 12",fg = "#1c4226",bg = "#aee8be", width = 14, height = 3, relief = RAISED, command =lambda: solve())
btn2=Button(aken, text = "graafik", font = "Arial 12", bg ="#aee8be", width = 14, height = 3, relief = RAISED, command = lambda :graafik(graf, D))
btn3=Button(aken, text = "Suurenda akent", font = "Arial 12", fg = "#1c4226",bg = "#aee8be",width = 14, height = 3, relief = RAISED)
extendB=Button(aken, text = "Suurenda akent", font = "Arial 12", fg = "#1c4226",bg = "#aee8be",width = 14, height = 3 width=x, command=extend

lbl5.pack(side = BOTTOM)
btn3.pack(side = BOTTOM)
lbl.pack()
ent1.pack(side = LEFT)
lbl2.pack(side = LEFT)
ent2.pack(side = LEFT)
lbl3.pack(side = LEFT)
ent3.pack(side = LEFT)
lbl4.pack(side = LEFT)
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
extendB.pack(side = BOTTOM)

aken.mainloop()
