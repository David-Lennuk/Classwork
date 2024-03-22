from tkinter import *
from tkinter import ttk
import math

aken=Tk()
aken.title("Решение квадратного уравнения") 
aken.geometry("600x200")
aken.title("Tkinteri kasutamine")
tekst = "Pealkiri\n"

lbl=Label(aken, text = "Решение квадратного уравнения",font = "Arial 16",bg = "#f0e4c7")
ent=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl2=Label(aken, text = "x**2+",font = "Arial 16")
ent2=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl3=Label(aken, text = "x+",font = "Arial 16")
ent3=Entry(aken, font = "Arial 20",fg = "#1c4226",bg = "#f0e4c7",width = 4) 
lbl4=Label(aken, text = "=0",font = "Arial 16")
lbl5=Label(aken, text = "Решено",font = "Arial 16",bg = "#c7d3f0")
btn=Button(aken, text = "Решать",font = "Arial 12",fg = "#1c4226",bg = "#aee8be",width = 14, heigh = 3,relief = RAISED)

btn.bind("<Button-1>",klikker)



lbl5.pack(side = BOTTOM)
lbl.pack()
ent.pack(side = LEFT)
lbl2.pack(side = LEFT)

ent2.pack(side = LEFT)
lbl3.pack(side = LEFT)
ent3.pack(side = LEFT)
lbl4.pack(side = LEFT)
btn.pack(side = LEFT)
aken.mainloop()
