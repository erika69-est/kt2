#Tkinter - Kodutöö nr 5
#Erika Laherand ITT20

from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#Aken ja selle seaded
aken = Tk()
aken.title("Palgakalkulaator")
aken.geometry("600x400")
aken.resizable(0,0)

#Muutujad
palk=0
tmaar=20
bruto=0
tmvaba=0
neto,tm,sots,tk,pens,tkk,kokku,maksustatav,nneto=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

def arvuta():#Arvutab kõik väljunread
    global palk,bruto,tmaar,sots,tmvaba,tk,tkk,maksustatav,nneto
    if rbValue.get()==1:
        brutost()
    else:
        netost()
    tmvaba=float(sisestustvaba.get())
    maksustatav=bruto-tk-pens
    maksuvaba()
    tm=round((maksustatav-tmvaba)*tmaar/100,2)
    neto=round(bruto-tm-tk-pens,2)
    sots=round(bruto*33/100,2)
    tkk=round(bruto*0.8/100,2)
    kokku=round(bruto+sots+tkk,2)
    brkast.config(text='{:.2f}'.format(bruto))
    tmkast.config(text='{:.2f}'.format(tm))#lisab tekstikastile uue sisu
    valjakast.config(text='{:.2f}'.format(neto))#lisab tekstikastile uue sisu
    sotskast.config(text='{:.2f}'.format(sots))
    tkkkast.config(text='{:.2f}'.format(tkk))
    tkkast.config(text='{:.2f}'.format(tk))
    penskast.config(text='{:.2f}'.format(pens))
    kokkukast.config(text='{:.2f}'.format(kokku))

def tootus():
    global tk
    if var.get()==1:
        tk=round(bruto*1.6/100,2)
    else:
        tk=0.0 

def sammas():
    global pens
    if varp.get()==1:
        pens=round(bruto*2/100,2)
    else:
        pens=0.0

def brutost():#Kontrollib, et sisestus ei oleks negatiivne arv
    global bruto
    bruto=float(sisestus.get())
    if bruto<0:
       bruto=0
       sisestus.delete(0,20)
       sisestus.insert(0,0.0)
       tkinter.messagebox.showerror("Viga!", "Negatiivseid arve ei saa sisestada")

def netost():#Väljastab info, et see valik veel ei tööta
    tkinter.messagebox.showerror("Kahju","Kasuta brutot, neto on veel välja mõtlemata")
            
def maksuvaba():#Kontrollib, et ei oleks sisestatud neg arv ning arvutab õige maksuvaba bruto suurusele
    global tmvaba,maksustatav,bruto
    if tmvaba<0:
        tmvaba=0
        tkinter.messagebox.showerror("Viga!", "Negatiivseid arve ei saa sisestada")
    if tmvaba>500:
        tmvaba=500
    if tmvaba>maksustatav:
        tmvaba=maksustatav
    if bruto>1200 and bruto<=2100:
        tmvaba=500-(bruto-1200)*((bruto-1200)/((bruto-1200)*1.8))
    sisestustvaba.delete(0,10)
    sisestustvaba.insert(0,round(tmvaba,2))

#Sisestusrida töötasu
tekstikast=Label(aken, text="Sisesta palk: ", width=30, font="Tahoma 12", anchor="w")
tekstikast.grid(row=0,column=0)
sisestus=Entry(aken, width=20, font="Tahoma 12")
sisestus.grid(row=0,column=1,sticky="e")

#Sisesturida tulumaksuvaba miinimun
tekstikast=Label(aken, text="Tulumaksuvaba miinimum: ", width=30, font="Tahoma 12", anchor="w")
tekstikast.grid(row=1,column=0)
sisestustvaba=Entry(aken, width=20, font="Tahoma 12")
sisestustvaba.grid(row=1,column=1,sticky="e")

#Töötuskindlustuse ja II pensionisamba valikud
var = IntVar()
tkvalikukast = Checkbutton(aken,text="Töötuskindlustus", variable=var, command=tootus)
tkvalikukast.grid(row=3)

varp = IntVar()
pvalikukast = Checkbutton(aken,text="II sammas", variable=varp, command=sammas)
pvalikukast.grid(row=3,column=1)

#Valikukoht, kas sisestus on bruto või neto
tekstikast=Label(aken, text="Bruto või neto: ", width=30, font="Tahoma 12", anchor="w")
tekstikast.grid(row=2,column=0,sticky="w")

rbValue=IntVar() #ühine muutuja väärtuste hoidmiseks
vk1=Radiobutton(aken, text="Brutotasu", value=1,variable=rbValue)
vk1.grid(row=2,column=1)
vk2=Radiobutton(aken, text="Netotasu", value=0,variable=rbValue)
vk2.grid(row=2,column=2)

#Joon
separator=ttk.Separator(aken,orient='horizontal')
separator.grid(row=4, column=0, columnspan=4, sticky="ew",padx=20)

#Väljundkastid
brkast=Label(aken, text="Brutotasu: ", font="Tahoma 12")
brkast.grid(row=5,column=0,sticky="w")
brkast=Label(aken, text="0.00", font="Tahoma 12")
brkast.grid(row=5,column=1,sticky="e")

tkkast=Label(aken, text="Isiku töötuskindlustus: ", font="Tahoma 12")
tkkast.grid(row=6,column=0,sticky="w")
tkkast=Label(aken, text="0.00", font="Tahoma 12")
tkkast.grid(row=6,column=1,sticky="e")

penskast=Label(aken, text="II sammas: ", font="Tahoma 12")
penskast.grid(row=7,column=0,sticky="w")
penskast=Label(aken, text="0.00", font="Tahoma 12")
penskast.grid(row=7,column=1,sticky="e")

tmkast=Label(aken, text="Tulumaks: ", font="Tahoma 12")
tmkast.grid(row=8,column=0,sticky="w")
tmkast=Label(aken, text="0.00", font="Tahoma 12")
tmkast.grid(row=8,column=1,sticky="e")
             
valjakast=Label(aken, text="Netotasu: ", font="Tahoma 12 bold",anchor="w")
valjakast.grid(row=9,column=0,sticky="w")
valjakast=Label(aken, text="0.00", font="Tahoma 12 bold",anchor="w")
valjakast.grid(row=9,column=1,sticky="e")

sotskast=Label(aken, text="Sotsiaalmaks: ", font="Tahoma 12",anchor="w")
sotskast.grid(row=10,column=0,sticky="w")
sotskast=Label(aken, text="0.00", font="Tahoma 12",anchor="w")
sotskast.grid(row=10,column=1,sticky="e")

tkkkast=Label(aken, text="Tööandja töötuskindlustus: ", font="Tahoma 12",anchor="w")
tkkkast.grid(row=11,column=0,sticky="w")
tkkkast=Label(aken, text="0.00", font="Tahoma 12",anchor="w")
tkkkast.grid(row=11,column=1,sticky="e")

kokkukast=Label(aken, text="Tööandja kulu kokku: ", font="Tahoma 12 bold",anchor="w")
kokkukast.grid(row=12,column=0,sticky="w")
kokkukast=Label(aken, text="0.00", font="Tahoma 12 bold",anchor="w")
kokkukast.grid(row=12,column=1,sticky="e")

#Arvutusnupp
Button(aken, text="Arvuta", width=10, font="Tahoma 12",command=arvuta).grid(row=0, column=2, padx=2, pady=2)
aken.mainloop()
