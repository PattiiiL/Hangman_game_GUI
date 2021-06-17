'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox

'''_____________________ wszystkie funkcje _____________________________ '''

def autorzy():
    tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
    tekst.pack(side = TOP)
    
def instrukacja():
    tekst = Label(okienko, text = "Witaj w grze wisielec! /n ")
    tekst.pack(side = TOP)

def jezyk():
    
def nowa_gra():

def wybierz_kat():

def kat_losowa():



'''____________________ tworzymy okienko gry _____________________________'''

okienko = Tk()
okienko.title("Wisielec")
okienko.geometry("400x500")
    
'''____________________ tworzymy menu gry _______________________________'''

moj_pasek_menu = Menu(okienko)

info_menu = Menu(pasekMenu, tearoff = 0)
info_menu.add_command(label = "autorzy", command = autorzy)
info_menu.add_command(label = "instrukcja", command = instrukacja)
moj_pasek_menu.add_cascade(label = "informacje ogolne", menu = info_menu)

ustawienia_menu = Menu(moj_pasek_menu, tearoff = 0)
ustawienia_menu.add_command(label = "jezyk", command = jezyk)
ustawienia_menu.add_command(label = "nowa_gra", command = wklej)
moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)

kat_menu = Menu(moj_pasek_menu, tearoff = 0)
kat_menu.add_command(label = "wybierz kategorie", command = wybierz_kat)
kat_menu.add_command(label = "kategoria losowa", command = kat_losowa)
moj_pasek_menu.add_cascade(label = "kategoria", menu = kat_menu)
okienko.config(menu = moj_pasek_menu)

okienko.mainloop()
