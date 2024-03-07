from random import *
#1.juku
nimi=input("Mis on sinu nimi").capitalizm()
print("Tere,",nimi)
if nimi=="Juku":
    print("Lahme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) # Ilus ja õige vastus! "Vale vanus" või "On vaja osta..."
else:
    print("Ma ootan Jukut")
print()








#2
person1 = input("Sisestage esimese inimese nimi")
person2 = input("Sisestage esimese inimese nimi")
print("Täna")+(person1 and person2)+("lähimad naabrid")
#3
length = float(input("Sisestage ruumi pikkus meetrites"))
width = float(input("Sisestage ruumi laius meetrites"))
area = length * width
print("Ruumi põrandapind")+(area)+("ruutmeetrit")
wants_renovation = input("Kas soovite teha renoveerimistöid? (jah/ei)")
if wants_renovation.lower() == "jah":
    price_per_square_meter = float(input("Kui palju ruutmeeter maksab?"))
    total_cost = price_per_square_meter * area
    print("Põranda vahetuse maksumus on")+(total_cost)+("Euro")


#4
alghind = 1000
if alghind > 700:
    soodus = alghind * 0.3
    print(alghind - soodus)


#5
temperature = float(input("Sisestage temperatuurid"))
if temperature > 18:
    print("Temperatuur üle 18 kraadi.")
else:
    print("Temperatuur ei ületa 18 kraadi.")
    
#6
height = float(input("Sisestage oma pikkus cm-des"))
if height < 160:
    print("Sa oled lühike.")
elif height >= 160 and height < 180:
    print("Oled keskmist kasvu.")
else:
    print("Sa oled pikk.")
    
#7 Ei saanud aru

#8
import random
products = ["piim", "leib", "munad", "just", "või"]
total_cost = 0
for product in products:
    want_to_buy = input("Kas soovite osta")+(product)+("?")+("jah/ei")
    if want_to_buy.lower() == "jah":
        price = random.uniform(1, 10)
        quantity = int(input("kui palju")+(product)+("tahad osta? "))
        total_cost += price * quantity
        delivery_time = input("Millal soovite saada")+(product)+("?")
        print("Tahad osta")+(quantity)+("asju")+(product)+("taga")+(price)+("euro igaüks.")
        print("Kaup tuuakse kohale")+(delivery_time)
    else:
        continue
print("Maksta kokku")+(total_cost)+("eurot.") 


#9
side1 = float(input("Sisestage ruudu esimese külje pikkus"))
side2 = float(input("Sisestage ruudu teise külje pikkus"))
if side1 == side2:
    print("See on ruut.")
else:
    print("See ei ole ruut.")
    
#10
num1 = float(input("Sisestage esimene number"))
num2 = float(input("Sisestage teine ​​number"))
operation = input("Millist toimingut soovite teha? (+, -, *)")
if operation == "+":
    result = num1 + num2
    print("Lisamise tulemus")+(result)
elif operation == "-":
    result = num1 - num2
    print("Lahutamise tulemus")+(result)
elif operation == "*":
    result = num1 * num2
    print("Korrutamise tulemus")+(result)
else:
    print("Toiming sisestati valesti.")
    
#11 Ei saanud aru
from datetime import *
from random import *
ta=date.today().year
sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
if (ta-sp)%5==0:
    print("Juubell")
else:
    print("Tavaline sünnipäev")










#12
price = float(input("Sisesta toote hind eurodes"))
if price >= 10:
    discounted_price = price -(price * 0.1)
else:
    discounted_price = price -(price * 0.2)
print("Toote lõplik hind") (discounted_price) ("euro.")

#13
gender = input("Sisestage oma sugu (mees/naine): ")
if gender.lower() == "n":
    age = int(input("Sisestage oma vanus"))
    if age >= 16 and age <= 18:
        print("Sa oled selle meeskonna jaoks õige.")
    else:
        print("Sa ei sobi sellesse meeskonda.")
        
#14
people = int(input("Sisestage inimeste arv"))
bus_size = int(input("Sisestage bussi suurus"))
buses_needed = people // bus_size
remaining_people = people % bus_size
if remaining_people > 0:
    buses_needed += 1
print("Нужно")+(buses_needed)+("автобусов, и в последнем автобусе будет")+(remaining_people)+("человек.")



#8(0.2)
from datetime import *
from random import *

arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
    summa+=mitu+hind
toode="Leib"
hind=randint(200,1000)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
    summa+=mitu+hind
    toode="Kommid"
hind=randint(600,1500)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
    summa+=mitu+hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Maksa "+str(summa)))
if raha==summa:
    print("Tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))
else:
    print("Maksa veel"+str(summa-raha))



8(0.3)
from datetime import *
from random import *

arve_nr= date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
for toode in ["Piim","Leib","Komm"]:
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
      mitu=int(input("Mitu?"))
      tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
      summa+=mitu+hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
while True:
    raha=float(input("Maksa "+str(summa)))
    if raha==summa:
        print("Tänan ostu eest!")
        break
    elif raha>summa:
        print("Tänan ostu eest! Tagasi "+str(raha-summa))
        break
    else:
        summa-=raha
        print("Maksa veel"+str(summa))



#14(0.2)
maht=int(input("Bussi math: "))
i=int(input("Inimeste arv: "))
ba=round(i/maht) #2,3->2
if i%maht!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))
