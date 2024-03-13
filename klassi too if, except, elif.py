print("Tere! Olen sinu uus sõber -Python!")
try:
    nimi=input("Mis on sinu nimi?")
except:
    ValueError
print(nimi+", oi kui ilus nimi!")
try:
    number=(int(input(nimi+"! Kas leian Sinu keha indeksi?i 0-ei, 1-jah =>")))
except:
    ValueError
if number==1:
    try:
        pikkus=float(input("Pikkus= "))
    except:
        ValueError
    try:
        mass=float(input("mass= "))
    except:
        ValueError
    indeks=mass/(0.01*pikkus)**2
    print("!Sinu keha indeks on:",round(indeks,1))
if indeks<16:
    print("Tervisele ohtlik alakaal")
elif indeks>=16 and indeks<=19:
    print("Alakaal")
elif indeks>=19 and indeks<=25:
    print("Normaalkaal")
elif indeks>=25 and indeks<=30:
    print("Ülekaal")
elif indeks>=30 and indeks<=35:
    print("Rasvumine")
elif indeks>=35 and indeks<=40:
    print("Tugev rasvumine")
elif indeks>40:
    print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
    print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
