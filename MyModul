from asyncio import subprocess
from dataclasses import dataclass
from msvcrt import LK_LOCK
from pickle import FALSE
from subprocess import SubprocessError


def Summa(arv1:int,arv2:int,arv3=0)->int:
    """Funktsioon tagastab kolme arvu summa
       Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3
    return s 

#1.1
def IntKontroll(sõned:int,viga=False)->int:
    try:
        x= int(x)
        return "int"
    except:
        try:
            x = float(x)
            return "float"
        except:
            return "str"
 
        

#1.2
def TuubiKontroll(x:any)->any:
    """Teeb andmete tüübi kontroll ja tagastab x leitud formaatis


    """
    try:
        t= int(x)
        return x
    except:
        try:
            t=float(x)
            return x
        except:
            return x




#1.1
def arithmetic(x: int, y: int, op:str) -> float:
    """ Funktsioon tagastab kolme arvu summa
        arithmetic(x, y, op)

    :param int x: x sisestab kasutaja
    :param int y: y sisestab kasutaja
    :param str op: str sisestab kasutaja
    :rtype: int

    """
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if x == 0 or y == 0:
            print("jagamine nulliga ei ole võimalik")


#2
def is_year_leap(aasta: int)->bool:
    """Funktsioon otsustab kas aasta on liigasta või ei ole.
    Tagastad True kui aasta on liigaasta ja False kui aasta on tavaline aasta.

    param int aasta: Aasta sisestab kasutaja
    rtype: bool
    """
    if aasta%4==0 and aasta%100!=0:
        return True
    else:
        return False


#3
from math import *
def sqauer(külg:float)->any:
    """Ümber
    ruudu külk sisesta kasutaja
    Tagastab S,P,d

    """
    P=4*külg
    S=külg**2
    d=külg*sqrt(2)
    return S,P,d


#4
def season (a:int)->str:
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12, Sisesta veel kord number."))
            except:
                print("Viga andmetüübiga")
    if a==12 or a==1 or a==2:
        s="talv"
    elif a>2 and a<6:
        s="kevad"
    elif a in range(6,9,1):
        s="suvi"
    elif 9<=a<=11:
        s="sügis"
    return s



#5
def bank(a, years):
    total = a
    for _ in range(years):
        total += total * 0.10
    return total



#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

#7




#8











def inimeste_ja_palkage_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p

def andmed_veerudes(i:list,p:list)->any:
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param List i: Inimeste järjend
    :param List p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])

def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """
    nimi=input("Keda kustutada ära(nimi):")
    for j in range(len(i)):
        if nimi in i:
            i.remove
def kellel_on_suurim_palk(i:list,p:list)->any:
    """

    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed
def kellel_on_vaiksem_palk(i:list,p:list)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list

    """
    nimed=[]
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed
def sorteerimine(i:list,p:list):
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list

    """

    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m]>p[n]=p[n],p[m]
                i[m]>i[n]=i[n],i[m]
    return i,p



def vordsed_palgad(i:list,p:list)->list:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list

   """
   nimed={} #{key1:value,key2:value}, key1!=key2
   #for id_, palgad in enumerate(p):
   #    print(id_,palgad)
   for palk in p:
       n=p.cont(palk)
       ind=p.index(palk)
       if n>1:
           subnimed=[]
           for j in range(n):
               nimi=i[p.index(palk,ind)]
               subnimed.append(nimi)
               p.pop(ind)
               i.pop(ind)
               ind=+1
               nimed[palk]=subnimed
    print(nimed)


def otsi_palk_nime_jargi(i:list,p:list)->dict:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list

    """
    palgad={}
    nimi=input("Nimi: ")
    for nimi in i:
        n=i.count(nimi)
        ind=i.index(nimi)
        if n>1:
            subp=[]
            for j in range(n):
                palk=p[i.index(nimi,ind)]
                subp.append(palk)
                p.pop(ind)
                i.pop(ind)
                ind=+1
            palgad[nimi]=Subp 
    print(palgad)


def rohkem_vahem_kui(i:list,p:list):
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list

    """
    for i, palk in enumerate(palgad):
        if (rohkem and palk > summa) or (not rohkem and palk < summa):
            print(f"{inimesed[i]} teenib {'rohkem' if rohkem else 'vähem'} kui {summa}: {palk}")


def kõige_vaesemad_ja_rikkamad(i:list,p:list)->any:
