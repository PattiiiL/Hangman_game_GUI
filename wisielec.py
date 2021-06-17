'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random

'''_____________________ wszystkie funkcje _____________________________ '''

def autorzy():
    tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
    tekst.pack(side = TOP)
    
def instrukacja():
    tekst = Label(okienko, text = "Witaj w grze wisielec! /n ")
    tekst.pack(side = TOP)

def jezyk():
    
def nowa_gra():

kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']
colours=['red', 'green', 'blue', 'purple', 'black']
fruits=['mango', 'pear', 'strawberry', 'banana', 'coconut']
animals=['cat', 'dog', 'zebra', 'fish', 'cow']

alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'o', 'r', 's', 't', 'u', 'w', 'y', 'z']


'''____________________ tworzymy okienko gry _____________________________'''

okienko = Tk()
okienko.title("Wisielec")
okienko.geometry("400x500")
    
'''____________________ tworzymy menu gry _______________________________'''

moj_pasek_menu = Menu(okienko)

info_menu = Menu(pasekMenu, tearoff = 0)
info_menu.add_command(label = "autorzy", command = autorzy)
info_menu.add_command(label = "instrukcja", command = instrukacja)
moj_pasek_menu.add_cascade(label = "informacje", menu = info_menu)

ustawienia_menu = Menu(moj_pasek_menu, tearoff = 0)
ustawienia_menu.add_command(label = "język", command = jezyk)
ustawienia_menu.add_command(label = "nowa gra", command = nowa_gra)
ustawienia_menu.add_command(label = "wyjście", command = okienko.quit)
moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)

okienko.mainloop()
