from modulefinder import packagePathMap
from struct import pack
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
import random


aken = Tk()
aken.title("Tahvel")
tahvel = Canvas(aken, width=990, height=630, background="white")
tahvel.grid()


#-------------------------------------------------------------------------------------------------------Harjutus. Lipud------------------------------------------------------------------------------------

#Bahamas lip
Bahamas = Canvas(aken, width = 990, height = 495, background = "#00778B")
Bahamas.grid()
Bahamas.create_rectangle(0,0,990,630,fill="#007788")
Bahamas.create_rectangle(0,330,990,165,fill="#FFC72C")
triangle = [0, 0, 0, 495, 495, 247.5]
Bahamas.create_polygon(triangle, fill = "#000000")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Eesti lip
tahvel.create_rectangle(0, 0, 990, 630,  fill = "#FFFFFF")
tahvel.create_rectangle(0, 0,  990, 420, fill = "#000000")
tahvel.create_rectangle(0, 0,  990, 210, fill = "#0072CE")

#-------------------------------------------------------------------------------------------------------Harjutus. Muster------------------------------------------------------------------------------------

#koridoris
rsyc = Canvas(aken, width = 400,height = 400, background = "#000000")
rsyc.grid(row = 0,column = 1, sticky = NW)
def koridoris(canvas,x,y,size,depth):
    if depth<=0:
        return
    
    k1 = size/2
    k2 = x+k1
    k3 = y+k1
    i1 = k1*2/(2**0.5)
    i2 = k2-i1/2
    i3 = k3-i1/2
    
    canvas.create_rectangle(x, y, x+size, y+size, outline = "#000000", fill = "#8e0287")
    canvas.create_oval(k2-k1, k3-k1, k2+k1, k3+k1, outline = "#000000", fill = "#028E09")
    koridoris(canvas, i2, i3, i1, depth-1)
koridoris(rsyc,0, 0, 400, 14)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Malelaud
malelaud=Canvas(aken,width=400/2,height=400/2,background="#FFFFFF")
malelaud.grid(row=0,column=2,sticky=NW)
malelaud.create_rectangle(0,0,400/2,400/2,fill="#FFFFFF")
s1=400/2/8
for x in range(8):
    for y in range(8):
        if (x+y)%2 == 0:
            malelaud.create_rectangle(x*s1,y*s1,(x+1)*s1,(y+1)*s1,fill="#000000")
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ringid ringides

def choice(list):
    random.choice(list)


colors=["black","cyan","magenta","red","blue","gray","yellow","green","lightblue","pink","gold"]

x0=0
y0=0
x1=500
y1=500
p=2

idk=Canvas(aken,width=500,height=500,background="#FFFFFF")
idk.grid(row=1,column=1,rowspan=2,columnspan=2,sticky=SE)

for i in range(150):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    idk.create_oval(x0,y0,x1,y1,fill=random.choice(colors))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#valgusfoor


canvas = Canvas(aken, width=150, height=400, bg="white")
canvas.grid(row=1,column=3,sticky=NW)

canvas = Canvas(aken, width=150, height=400, bg="white")
canvas.grid(row=1, column=3, sticky=NW)


color_var = StringVar()
color_var.set("punane")


def update_traffic_light():
    color = color_var.get()
    canvas.delete("lights")
    canvas.create_text(75, 25, text="valgusfoor", font=("Arial", 14, "bold"), tag="lights")
    canvas.create_rectangle(50, 50, 100, 350, fill="black", tag="lights")
    if color == "punane":
        canvas.create_oval(60, 60, 90, 90, fill="red", tag="lights")
    elif color == "kollane":
        canvas.create_oval(60, 120, 90, 150, fill="yellow", tag="lights")
    elif color == "roheline":
        canvas.create_oval(60, 190, 90, 220, fill="green", tag="lights")

def on_radio_button_change():
    update_traffic_light()

red_radio = Radiobutton(aken, text="punane", variable=color_var, value="punane", command=on_radio_button_change)
red_radio.grid(row=1, column=1, sticky=NW)

yellow_radio = Radiobutton(aken, text="kollane", variable=color_var, value="kollane", command=on_radio_button_change)
yellow_radio.grid(row=1, column=3, sticky=NW)

green_radio = Radiobutton(aken, text="roheline", variable=color_var, value="roheline", command=on_radio_button_change)
green_radio.grid(row=1, column=2, sticky=NW)
update_traffic_light()



aken.mainloop()
