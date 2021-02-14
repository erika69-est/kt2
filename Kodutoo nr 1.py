#Erika Laherand ITT-20
#17.01.2021
#Kodutöö nr 

#Tervitus
print("Tere, maailm!")
print("")

#Aasta liblikas
aasta=2020
liblikas="teelehemosaiikliblikas"
lause_keskosa=". aasta liblikas on "
lause=str(aasta)+lause_keskosa+liblikas
print(lause)
print("")

#Astendamine
alus=int(input("Sisesta astme alus: "))
astendaja=int(input("Sisesta astendaja: "))
aste=pow(alus,astendaja)
print(f"{alus} astmes {astendaja} on {aste}")
print("")

#Trahv
nimi=input("Sisesta nimi: ")
lubatud_k=int(input("Sisesta lubatud sõidukiirus: "))
tegelik_k=int(input("Sisesta tegelik kiirus: "))
maksimum=190
if tegelik_k>=lubatud_k:
    tegelik=(tegelik_k-lubatud_k)*3
    if tegelik>=maksimum:
        tegelik=maksimum
    print(f"{nimi.capitalize()}, kiiruse ületamise eest on teie trahv {tegelik} eurot")
else:
    print(f"Kodanik {nimi.capitalize()}, võite jätkata teekonda, aga ärge takistage liiklust!")



        
