print("Tere maailm!")
#1
nimi = input("Mis on sinu nimi?")
vanus=int(input("kui vana sa oled?"))
print("Tere tulemast!"  ,nimi, "Sa oled",vanus,"aastat vana")
print("Tere tulemast! {0} sa oled {1} aastat vana".format(nimi,vanus))
print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))
#3
from random import *
from tkinter import Pack

kokku=randint(10,100)
print("kokku: ",kokku)
mitu = int(input("mitu kommi  tahad ära võtta?"))
kokku-=mitu
print("Nüüd Laua peal on",kokku,"kommid")
#4
ümbermõõt = float(input("kirjutage puu umbermõõt: "))
diameeter = ümbermõõt / 3.14159
print("Puu diameeter:", diameeter)
#5
N = float(input("Sisestage ristküliku pikkus N meetrites: "))
M = float(input("Sisestage ristküliku laius M meetrites: "))
diagonaali_pikkus = (N ** 2 + M ** 2) ** 0.5
print("Ristküliku diagonaali pikkus on:", diagonaali_pikkus , "meetrit")
#6
try:
    aeg=float(input("Mitu tundi kulus sõiduks? ")) #aeg ie saa olla 0
    teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
    kiirus=teepikkus/aeg
    print("Sinu kiirus oli " + str(kiirus)+ "km/h")
except :
    print("Viga andmetüübiga")


#7
# 8 @..@
#  (----)
# ( \__/ )
# ^^ "" ^^
#9
a =float(input("Sisestage numbrit: "))
b = float(input("Sisestage numbrit: "))
c = float(input("Sisestage numbrit: "))
P = a + b + c
print(P)
#10 
P=randint(1,5)
hind=12.90
hind*=1.1 #hind koos jätatega
osa=round(hind/P,2) 
print("Iga sõber maksab",osa)
