from tkinter import *
import random
t = Tk()
t.title("Wybierz swoje przeznaczenie")
t.geometry("350x400")

def wstaw_przyciski():
    ile_przycisków = 8
    global przyciski
    przyciski = []
    dobry = random.randint(0,ile_przycisków-1)
    for i in range (ile_przycisków):
        if i == dobry:
            przyciski.append(Button(t,text = "Ssspróbuj szczęścia",command=trafiony))
        else:
            przyciski.append(Button(t,text="Spróbuj szczęścia",command=pudlo))
    for i in przyciski:
        i.pack(fill=BOTH,expand=YES)

def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t,text = "Trafiony!!!")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(5000,restart)
def restart():
    etykieta.destroy()
    wstaw_przyciski()
def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t,text = "Pudlo!!!")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(5000,restart)

wstaw_przyciski()
