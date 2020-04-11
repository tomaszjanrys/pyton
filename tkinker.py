import tkinter as tk
from tkinter import *
def okno(a):
    window = tk.Tk()
    window.title("tkinter - simple window -")
    window.geometry("1000x500")
    label = Label(window, text="""
    import tkinter as tk              <=======Ladowanie modulu tkinter========>
from tkinter import *                 <=======================================>
def okno(a):                          <=======================================>
    window = tk.Tk()                  <=======Tworzenie okna glownego========>
    window.title("Okienko")           <=======Ustawienie tytulu okna========>
    window.geometry("500x500")        <=======Ustawienie wielkosci okna========================================>
    label = Label(window, text = "Fajne okno w Pytonie" + a)   <=======LABEL kontrolka typu label -============>
    label.pack(side = tk.TOP)         <=======podpiecie kontrolki pod okno  SIDE - ulozenie na stronie ========>
    tk.mainloop()                     <=======Wywolanie petli ==================================================>
aa = 0                                <=======================================>
while aa < 1:                         <=======================================>
    aa = aa + 1                       <=======================================>
    okno(str(aa))                     <=======================================>

    """ + a)
    label.pack(side=tk.TOP)
    tk.mainloop()
aa = 0
while aa < 100000000:
    aa = aa + 1
    okno(str(aa))
