#Kodutöö nr 2
#Erika Laherand ITT20
#28.01.21

import random

#2.1 Bussid
inimesed=int(input("Sisesta inimeste arv: "))
buss=int(input("Sisesta bussi kohtade arv: "))
busse_vaja=(inimesed//buss)
viimane=inimesed%buss
print("Inimesite arv:",inimesed)
print("Bussis kohti:",buss)
if viimane!=0:
    busse_vaja+=1
    print("Busse vaja:",busse_vaja)
    print("Viimases bussis:",viimane)
else:
    print("Busse vaja:",busse_vaja)
    print("Viimases bussis:",buss)
print("")

#2.2 Äratus
kordi=int(input("Mitu korda on vaja äratada? "))
for i in range(kordi):
    print("Tõuse ja sära")
print("")
    
#2.3 Murelikud lapsevanemad    
ringe=int(input("Sisesta ringide arv: "))
loendur=0
porgand=0
while loendur<=ringe:
    if loendur%2==0:
        porgand=porgand+loendur
    else:
        porgand=porgand+0
    loendur+=1
print("Porgandite koguarv on: ",porgand)
print("")

#2.4 Täringud
tarv=int(input("Mitut täringut on vaja: "))
print(f"Täringute arv: {tarv}")
for i in range(1,tarv+1):
    vise=random.randrange(1,7)
    print(vise)

#2.5 Õunad
oun=0
ounad=0
poiss=int(input("Mitu pöialpoissi tahab õunu? "))
for i in range(poiss):
    oun=random.randrange(1,3)
    ounad=ounad+oun
    print(oun)
jaak=14-ounad
print("Lumivalgekesele jäi:",jaak)
