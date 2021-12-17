# vim: set fileencoding=utf8 :
# Näiteprogramm protsessoriaja planeerijate visualiseerimiseks
# algne autor Sten-Oliver Salumaa
# lõpetanud Annaliis Täheväli

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from algoritmid import *


def puhasta():
    tahvel.delete('all')

def color_picker(jarjend, nr):
    colors = ["green", "yellow", "orange", "red", "#8CD1F1", "#AFE88C", "#F8DAE3", "cyan", "#F1ED8C", "#C18FDE", "#B2A9F3", "#F955B3", "#9FA5A1"]
    color = ''
    
    if jarjend[nr][0] == ' ':
        color = colors[-1]
    else:
        color = colors[int(jarjend[nr][0].replace('P',''))]

    return color


# joonistab tahvlile protsesse kujutavad ristkülikud numbrite ja protsesside nimedega
def joonista(jarjend):
    print(jarjend)
    puhasta()
    eelmise_loppx = 20
    kaugus = 0
    for i in range(len(jarjend)):
        protsess = jarjend[i][0]
        kestus = jarjend[i][1]
        kujund = tahvel.create_rectangle(eelmise_loppx, 60, eelmise_loppx + kestus * 16,100, fill=color_picker(jarjend,i))
        keskpaik = eelmise_loppx+kestus * 8
        protsessi_id = tahvel.create_text(keskpaik, 80, text=protsess)
        m = tahvel.create_text(eelmise_loppx, 110, text=str(kaugus))
        kaugus += kestus
        eelmise_loppx += kestus*16
    m = tahvel.create_text(eelmise_loppx, 110, text=str(kaugus))

# teeb järjendist kahetasemelise listi, mida on mugavam töödelda
def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund

# otsustab, millist järjendit teha kahetasemeliseks massiiviks
def massiiviMeister():
    jarjend = []
    if var.get() == 1:
        return massiiviks(predef1)
    elif var.get() == 2:
        return massiiviks(predef2)
    elif var.get() == 3:
        return massiiviks(predef3)
    elif var.get() == 4:
        try:
            return massiiviks(kasutaja_jarjend.get())
        except:
            messagebox.showerror(title="Viga sisendis", message="Vigane kasutaja muster!")
            return massiiviks(predef1)
    else:
        return massiiviks(predef1)


# näitab programmis käimasolevat protsessijada
def massiiviTeavitaja(massiiv):
    text.delete(1.0, END)
    for jupp in massiiv:
        text.insert(INSERT, str(jupp) + "\n")

def kasuvalija(jarjend, algoritm):
    if algoritm == "FCFS":
        return FCFS(jarjend)
    elif algoritm == "SJF":
        return SJF(jarjend)
    elif algoritm == "RR3":
        return RR3(jarjend)
    elif algoritm == "FCFS2":
        return FCFS2(jarjend)

def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    massiiviTeavitaja(jarjend)
    (valjund, ooteaeg) = kasuvalija(jarjend, algoritm)
    joonista(valjund)
    keskm_oot = tahvel.create_text(80, 40, text="Keskmine ooteaeg:  " + str(ooteaeg))

predef1 = "0,7;1,5;2,3;3,1;4,2;5,1"
predef2 = "0,2;1,4;12,4;15,5;21,10"
predef3 = "0,4;1,5;2,2;3,1;4,6;6,3"


# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(False, False)
raam.geometry("830x400")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10,y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10,y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10,y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10,y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 1,10;4,2;12,3;13,2)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

silt_tahvel = ttk.Label(raam, text="Käsil olevad protsessid:")
silt_tahvel.place(x=450, y=10)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)

tahvel = Canvas(raam, width=830, height=180, background="white")
tahvel.place(x=0, y=220)

FCFS_nupp = ttk.Button(raam, text="FCFS", command = lambda : jooksuta_algoritmi("FCFS"))
FCFS_nupp.place(x=10, y=190,height=25, width=80)

SJF_nupp = ttk.Button(raam, text="SJF", command = lambda : jooksuta_algoritmi("SJF"))
SJF_nupp.place(x=100, y=190,height=25, width=80)

RR3_nupp = ttk.Button(raam, text="RR3", command = lambda : jooksuta_algoritmi("RR3"))
RR3_nupp.place(x=280, y=190,height=25, width=80)

FCFS2_nupp = ttk.Button(raam, text="FCFS 2x", command = lambda : jooksuta_algoritmi("FCFS2"))
FCFS2_nupp.place(x=190, y=190,height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command = lambda : puhasta() )
puhasta_nupp.place(x=500, y=190,height=25, width=130)

text = Text(raam, width=25, height=9)
text.place(x=450, y=30)

raam.mainloop()
