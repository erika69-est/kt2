#Iseseisev töö nr 3
#Erika Laherand ITT20
#14.02.2021

#3.1 Ülikooli vastuvõetud
print("***************Ülikooli vastuvõetud******************")
fail=open("rebased.txt",encoding="UTF-8")
vastuvoetud=[]
vastus="J"
for rida in fail:
    vastuvoetud.append(int(rida))
fail.close()

def valjasta():
    aasta=int(input("Millise aasta vastuvõetute andmeid vajate: "))
    if aasta>=2011 and aasta<=2019:
        print(f"Aastal {aasta}. a vastuvõetuid {vastuvoetud[aasta-2011]}")
    else:
        print(f"{aasta}. a vastuvõetute andmed puuduvad")
    
while vastus=="J":
    valjasta()
    vastus=input("Kas soovite veel andmeid (J/E): ")
    vastus=vastus.upper()
print("")

#3.2 Jänesevanemate mure ver. 3    
print("**********Jänesevanemad ver 3************")
def ringid(ringe):
    porgand=0
    for loendur in range(ringe+1):
        if loendur%2==0:
            porgand=porgand+loendur
        else:
            porgand=porgand+0
    print("Porgandite koguarv on: ",porgand)
vastus="J"    
while vastus=="J":
    ringe=int(input("Sisesta ringide arv: "))
    if ringe>=0:
        ringid(ringe)
    else:  
        print("Ringide arv peab olema positiivne täisarv")
    vastus=input("Kas soovid veel proovida (J/E): ")
    vastus=vastus.upper()
print("")

#3.3 Sissetulekud
print("************Konto sissetulekud*************")
failk=open("konto.txt",encoding="UTF-8")
tehingud=[]
for rida in failk:  
    tehingud.append(float(rida))
failk.close()
print("Konto sissetulekud on: ")
for i in range(len(tehingud)):
    if tehingud[i]>0:
         print(tehingud[i])
print("")

#3.4 Jukebox
print("***********Jukebox************")
muusika=["jukebox.txt","80ndad.txt","eesti_muusika.txt","edm.txt"]

def jukebox(plaat):
    palad=[]
    failp=open(plaat,encoding="UTF-8")
    for pala in failp:
        palad.append(pala)
    failp.close()
    for i in range(len(palad)):
        print(i+1," ",palad[i])
    nr=int(input("Millist lugu soovid: "))
    print(f"Valitud lugu on {palad[nr-1]}")

jvastus="J"
while jvastus=="J":
    print("Meie muusikavalik on selline: ")
    for m in range(len(muusika)):
        print(muusika[m])
    plaat=input("Sisesta oma valik: ")
    jukebox(plaat)
    jvastus=input("Kas soovid veel lugusid kuulata (J/E): ")
    jvastus=jvastus.upper()
print("")

#3.5 Tahvli juurde
print("************Tahvli juurde*************")
from datetime import *
kuup=datetime.now().day
loend=[]
failinimi=input("Sisesta õpilaste nimekirja failinimi: ")
with open(failinimi,'r',encoding="UTF-8") as minu_fail:
   loend=minu_fail.readlines()
   if kuup<=len(loend):
        print("Vastama tuleb ",loend[kuup-1])
   else:
       kuup=kuup%len(loend)
       print("Alustame nimekirja algust, vastama tuleb",loend[kuup-1])
