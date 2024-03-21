from random import *
from re import *
nimed=["Mati","Meelis","Kati","Mati"]
while True:
    print("-------------------")
    v=input("N-näita andmed\nL-lisada andmeid\nK-andmete kustutamine\nH-andmete haldus\nH-andmete haldus\nD-Vanus")
    if v=="N":
        v=input("Kas Juhuslik(j) nimi või loetelu(t)?")
        if v=="t":
            print (nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas nimikirja lõppu(l) või positsioonile(p)")
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi: ")
            ind=int(input("Mis kohale: "))
            nimed.insert(ind-1,nimi)
    elif v=="K":
        v==input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed(K)")
        if v=="i":
            ind=int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
        elif v=="K":
            nimed.clear()
        elif v=="n":
            nimi=input("Sisesta nimi: ")
            mitu=nimed.count(nimi)
            if mitu>0:
                if mitu>1:
                    ind= -1
                    indlist=[]                   
                    for e in nimed:
                        ind +=1
                        if e == nimi:
                            indlist.append(ind)
                    print(indlist)
                    v= int(input("Mis indeks?"))
                    nimed.pop(v)
                else:
                    nimed.remove(nimi)
            else:
                print(f"{nimi} ei ole loetelus")
    elif v=="H":
        v=input("Sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
        if v=="s":
            v=int(input("A-z?(1) või Z-a(2)"))
            if v==1:
                nimed.sort()
            elif v==2:
                nimed.sort(reverse=True)
            nimed.sort()
        elif v=="K":
            nimed.copy()
        elif v=="p":
            nimed.reverse()
    elif v=="D":
        aeg = [25, 30, 40, 20, 35]
        v=input("Max aeg(b), min aeg(f), sum aeg(t),len aeg(z) ")
        if v=="b":
            max_aeg = max(aeg)
            print(f"Maximum aeg: {max_aeg}")
        elif v=="f":
            min_aeg = min(aeg)
            print(f"Minimum aeg: {min_aeg}")
        elif v=="t":
            total_aeg = sum(aeg)
            print(f"Total aeg: {total_aeg}")
        elif v=="z":
            average_aeg = total_aeg / len(aeg)
            print(f"Average aeg: {average_aeg}")            



#2.3
vanused=[]
for i in range(5):
    vaanus=int(input("Sisesta vanus: "))
    vanused.append(vanus) #
maksimum=max(vanused)
minimum=min(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)
print("maksimum=",max(vanused),"\nminimum=",min(vanused),"\nsumma=",sum(vanused),"\nkeskmine=",summa/len(vanused))

#Kuva ekranile nimi koos vanusega
for i in range(5):
    print(nimed[i],"on", vanused[i],"aastat vana")


#3 Tärnid
from random import *
arvud=[]
N=int(input("Mitu rida joonistame?"))
S=input("Sisesta sümbol: ")
#loendi täitmine
for p in range(N):
    arvud.append(randint(1,100))
#diagrammi loomine
for p in range(N):
    print(arvud[p]*S)


#4 Postiindex
linnad=["Tallinn" "Narva, Narva-Jõesuu" "Kohtla-Järve" "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa" "Tartu linn" "Tartumaa, Põlvamaa, Võrumaa, Valgamaa" "Viljandimaa, Järvamaa, Harjumaa,Raplamaa" "Pärnumaa Läänemaa" "Hiiumaa, Saaremaa"]
while True:    
    while True:
        try:
           indeks=int(input("Sisesta viienumbrilinr indeks: "))
           #if 10000<=indeks<=99999:
           indeks_elemendide_arv=len(str(indeks))
           if indeks_elemendide_arv==5:
                print("5numbriline indeks ")
                break
           else:
               print("On vaja 5numbriline arv(indeks)")
        except:
                print("Vale andmetüüp!")
    arv1=indeks//10000
    print(arv1)
    #symbolid=list(str(indeks))
    print(f"Sa elad piirkonnas {linnad[arv1-1]}")


#5 Vahetus
from string import *
rida=[]
N=randint(2,25)
for i in range(N):
    rida.apped(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elmendi vahetama oma vahel "))
if len(rida)//22>=kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
print(rida)


#6: Бесполезные числа
numbers = input("Введите числа через пробел: ").split()
numbers = list(map(int, numbers))
if not numbers:
    print("Ошибка: список чисел пуст.")
else:
    max_number = max(numbers)
    numbers[numbers.index(max_number)] = max_number / len(numbers)
    print("Список после замены:", numbers)

#6.1
nimekirja1=[]
nimekirja=[]
n=int(input("Nimekirja suurus:"))
for i in range(n):
    arv=randint(10,100)
    nimekirja1.append(arv)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
        vajavarv=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=vajavarv 
print(nimekirja1)
print(nimekirja)



#9: Nimi kontroll

try:
    nimi=input("Sisestage oma nimi: ")
    if nimi.isalpha():
       print("Tere, {}!".format(nimi.capitalize()))
       letter_count=len(nimi)
       print("Tähtede arv nimes:", letter_count)
       täishäälikud="aeiouAEIOU"
       kaashäälikud="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
       täishäälikute_arv=sum(1 for letter in nimi if letter in täishäälikud)
       kaashäälikute_arv=sum(1 for letter in nimi if letter in kaashäälikud)
       print("Täishäälikute arv:", täishäälikute_arv)
       print("Konsonantide arv:", kaashäälikute_arv)
       sorteeritud_tähed=sorted(nimi.lower())  # Teisenda väiketähtedeks ja sorteeri
       unikaalsed_tähed=[]
       for kiri in sorteeritud_tähed:
           if kiri not in unikaalsed_tähed:
               unikaalsed_tähed.append(kiri)
       print("Nimetage tähed tähestikulises järjekorras:", ", ".join(unikaalsed_tähed))
    else:
       print("Nimi peab sisaldama ainult tähti.")
except Exception as e:
    print("An error occurred:", e)



#12
import random

try:
    # Koostage loend 10 juhuslikust numbrist 1 kuni 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Algne nimekiri:", random_numbers)
    # Minimaalsete ja maksimumelementide indeksi leidmine
    min_index = random_numbers.index(min(random_numbers))
    max_index = random_numbers.index(max(random_numbers))
    # Vahetage loendi minimaalsed ja maksimaalsed elemendid
    random_numbers[min_index], random_numbers[max_index] = random_numbers[max_index], random_numbers[min_index]
    print("Nimekiri pärast asendamist:", random_numbers)
except Exception as e:
    print("An error occurred:", e)


##13 Arva sõna ära
import random

## Список слов


try:
    import random
    sõnad = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'melon', 'pineapple', 'peach']
    # Выбираем случайное слово
    sõna = random.choice(sõnad)
    # Перемешиваем буквы в слове
    segatud_sõna = ''.join(random.sample(sõna, len(sõna)))
    # Инициализируем переменные
    katsed = 0
    arvatud_tähed=[]
    valed_tähed=[]
    # Начинаем игру
    print("Alustame mängu!")
    print("Arva ära sõna tähtedest:", segatud_sõna)
    while katsed < 20:
       arvan=input("Sisestage täht: ").lower()
       katsed += 1
       if arvan in sõna:
           print("Palju õnne! Sa arvasid kirja ära!")
           arvatud_tähed.append(arvan)
       else:
           print("Kahjuks sellist tähte sõnas pole.")
           valed_tähed.append(arvan)
       # Отображаем отгаданные буквы на своих местах и оставшиеся попытки
       paljastatud_sõna = ''.join(letter if letter in arvatud_tähed else '_' for letter in sõna)
       print("Arvatud sõna:", paljastatud_sõna)
       print("Arvamata kirjad:", ', '.join(valed_tähed))
       if paljastatud_sõna == sõna:
           print("Palju õnne! Sa arvasid sõna '{}' oma {} katsed.".format(sõna, katsed))
           break
    else:
       print("Kahjuks olete kõik oma katsed ära kasutanud. Varjatud sõna oli '{}'.".format(sõna))
except Exception as e:
    print("An error occurred:", e)



#17
# Создаем список слов
try:
    jarjend = ["kass", "koer", "lind", "elevant", "kala", "madu", "hunt"]
    # Просим пользователя ввести искомое слово
    otsingusona = input("Palun sisestage otsitav sõna: ")
    # Проходим по всем элементам списка
    for sona in jarjend:
        # Проверяем, содержится ли искомое слово в текущем элементе списка
        if otsingusona in sona:
            # Если слово найдено, выводим его на экран
            print("Sõna", sona, "sisaldab otsitavat sõna", otsingusona)
except Exception as e:
    print("An error occurred:", e)

#15
try:
    arv = [1, 2, 3, 4]
    eesti = ['üks', 'kaks', 'kolm', 'neli']
    inglise = ['one', 'two', 'three', 'four']
    itaalia = ['uno', 'due', 'tre', 'quattro']
    
    # Printing elements in a table
    print("Arv - Eesti - Inglise - Itaalia")
    for i in range(len(arv)):
        print(f"{arv[i]} - {eesti[i]} - {inglise[i]} - {itaalia[i]}")
    
    # Adding two elements to the eesti list
    eesti.extend(['viis', 'kuus'])
    
    # Checking if 'tre' exists in itaalia list
    if 'tre' in itaalia:
        print("'tre' exists in the itaalia list")
    
    # Sorting and printing elements in alphabetical order
    print("Sorted elements:")
    for element in sorted(arv):
        print(element, end=" ")
    print()
    for element in sorted(eesti):
        print(element, end=" ")
    print()
    for element in sorted(inglise):
        print(element, end=" ")
    print()
    for element in sorted(itaalia):
        print(element, end=" ")
except Exception as e:
    print("An error occurred:", e)
