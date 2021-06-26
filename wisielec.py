'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random

'''____________________ tworzymy okienko gry _____________________________'''

class Hangman_GUI(): 
    def __init__(self):
        # kategorie haseł
        self.kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
        self.owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
        self.zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']

        self.lista_wyrazow = []

        self.zgadywane_slowo = []
        self.bledne_litery = []
        self.zakryte_slowo = []

        self.alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'o', 'r', 's', 't', 'u', 'w', 'y', 'z']
        
        # Tworzymy okienka w GUI z widgetami
        self.okienko = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.okienko)
        self.middle_frame = tkinter.Frame(self.okienko
        self.bottom_frame = tkinter.Frame(self.okienko)
        self.okienko = tkinter.Tk()
        self.etykietka_1 = tkinter.Label(self.top_frame, text = "Gra wisielec")
        self.radio_button_wartosci = tkinter.IntVar()

        # Tworzymy RadioButton z kategoriami
        
        self.radio_button_wartosci.set(4)
                                          
        self.rprzycisk_1 = Radiobutton(self.middle_frame, text = "kolory", variable = self.radio_button_wartosci, value = 1, command = losuj_kat)                               
        self.rprzycisk_2 = Radiobutton(self.middle_frame, text = "owoce", variable = self.radio_button_wartosci, value = 2, command= losuj_kat)                               
        self.rprzycisk_3 = Radiobutton(self.middle_frame, text = "zwierzeta", variable = self.radio_button_wartosci, value = 3, command = losuj_kat)                              
        self.rprzycisk_4 = Radiobutton(self.middle_frame, text = "losowa", variable = self.radio_button_wartosci, value = 4, command = losuj_kat)


        self.przycisk = tkinter.Button(self.okienko, text = "Wyświetl wylosowane słowo", command = self.zakryte_slowo)
        self.wpisz_litere_info = tkinter.Label(self.bottom_frame, text = "Podaj dowolną literę - pomiń znaki polskie!")       
        self.wpisz_litere_okienko = tkinter.Entry(self.bottom_frame, width = 10)
        self.przycisk_spr = tkinter.Button(self.okienko, text = "Sprawdź", command = self.sprawdz_litere)

        self.rprzycisk_1.pack()
        self.rprzycisk_2.pack()
        self.rprzycisk_3.pack()
        self.rprzycisk_4.pack()

        self.etykietka_1.pack(side = "top")

        self.przycisk.pack()
        self.wpisz_litere_info.pack(side = "left")
        self.wpisz_litere_okienko(side = "left")

        self.top_frame.pack()
        self.middle_frame.pack()           
        self.bottom_frame.pack()

        # Tworzymy menu gry

        self.moj_pasek_menu = Menu(self.okienko)

        info_menu = Menu(self.moj_pasek_menu, tearoff = 0)
        info_menu.add_command(label = "autorzy", command = autorzy)
        info_menu.add_command(label = "instrukcja", command = instrukacja)
        moj_pasek_menu.add_cascade(label = "informacje", menu = info_menu)

        ustawienia_menu = Menu(self.moj_pasek_menu, tearoff = 0)
        ustawienia_menu.add_command(label = "język", command = jezyk)
        ustawienia_menu.add_command(label = "nowa gra", command = nowa_gra)
        ustawienia_menu.add_command(label = "wyjście", command = self.okienko.quit)
        moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)

        tkinter.mainloop()

'''_____________________ wszystkie funkcje _____________________________ '''

    def losuj_kat(self):
        if value == 1:
            self.lista_wyrazow = self.kolory
        if value == 2:
            self.lista_wyrazow = self.owoce
        if value == 3:
            self.lista_wyrazow = self.zwierzeta
        if value == 4:
            self.lista_wyrazow = self.kolory + self.owoce + self.zwierzeta
            
    return lista_wyrazow
        
    def losuj_wyraz(lista_wyrazow,losuj_kat):
        wyraz=random.choice(lista_wyrazow)
        lista_wyrazu=list(wyraz)
    return lista_wyrazu

    def zakryte_slowo(self):
        for i in range(len(lista_wyrazu[:])):
            self.zakryte_slowo += "_"
        tkinter.messagebox.showinfo("Wylosowane słowo", print(zakreskowane))
        slowo_kreski = print(zakryte_slowo)
    return slowo_kreski
        

    def sprawdz_litere(self,losuj_wyraz):
        sprawdzana = self.wpisz_litere_okienko.get()
        for i in range(len(lista_wyrazu[:])):
            if i == sprawdzana:
                 self.zgadywane_slowo += i
        # do ogarniecia zeby litery dodawaly sie na odp msc
            else:
                self.bledne_litery += i

    def autorzy():
        tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
        tekst.pack(side = TOP)
    
    def instrukacja():
        tekst = Label(okienko, text = "Drogi graczu, /n witaj w grze wisielec! /n Aby rozpoczac grę wybierz kategorię, z której chcesz wylosować hasło. ")
        tekst.pack(side = TOP)


    
#def nowa_gra():

# utworzenie egzemplarza klasy Hangman_GUI

wisielec = Hangman_GUI()

        




