'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random

'''____________________ tworzymy okienko gry _____________________________'''
class our_GUI(): 
    def __init__(self):
        self.okienko = Tk()
        self.okienko.title("Wisielec")
        self.okienko.geometry("400x500")
    
    # kategorie haseł
        self.kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
        self.owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
        self.zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']
       
     def losuj_wyraz(lista_wyrazow):
        wyraz=random.choice(lista_wyrazow)
        lista_wyrazu=list(wyraz)
    return lista_wyrazu

    def akcja_przycisk(self):
        if wartosc.get() == 1:
            losuj_wyraz(self.kolory)
        
        elif wartosc.get() == 2:
            losuj_wyraz(self.owoce)
       
        elif wartosc.get() == 3:
            losuj_wyraz(self.zwierzeta)
        
        elif wartosc.get() == 4:
            lista = self.kolory[:] + self.owoce[:] + self.zwierzeta[:]
            losuj_wyraz(lista)
        
    
    
'''________________ tworzymy RadioButton z kategoriami _______________________'''
    def cathegory_button(self):
        
        przycisk = Button(self.okienko, text = "Wybor kategorii")
        przycisk.grid(row =0, column = 0)
        
        rprzycisk_1 = Radiobutton(self.okienko, text = "kolory", variable = wartosc, value = 1, command = akcja_przycisk)
        rprzycisk_1.grid(row =1, column = 0)
        rprzycisk_2 = Radiobutton(self.okienko, text = "owoce", variable = wartosc, value = 2, command= akcja_przycisk)
        rprzycisk_2.grid(row =1, column = 1)
        rprzycisk_3 = Radiobutton(self.okienko, text = "zwierzeta", variable = wartosc, value = 3, command = akcja_przycisk)
        rprzycisk_3.grid(row =1, column = 2)
        rprzycisk_4 = Radiobutton(self.okienko, text = "losowa", variable = wartosc, value = 4, command = akcja_przycisk)
        rprzycisk_4.grid(row =1, column = 3)

    
    def losuj_wyraz(lista_wyrazow):
        wyraz=random.choice(lista_wyrazow)
        lista_wyrazu=list(wyraz)
    return lista_wyrazu


    

'''_____________________ wszystkie funkcje _____________________________ '''


def autorzy():
    tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
    tekst.pack(side = TOP)
    
def instrukacja():
    tekst = Label(okienko, text = "Drogi graczu, /n witaj w grze wisielec! /n Aby rozpoczac grę wybierz kategorię, z której chcesz wylosować hasło. ")
    tekst.pack(side = TOP)

"""def jezyk_ang(lista_1,lista_2,lista_3):
    kat_1 = lista_1
    kat_2 = lista_2
    kat_3 = lista_3
    return kat_1, kat_2, kat_3
   
def jezyk_pl(lista_1,lista_2,lista_3):
    kat_1 = lista_1
    kat_2 = lista_2
    kat_3 = lista_3
    return kat_1, kat_2, kat_3"""
    
#def nowa_gra():

        
class Hangman():
    def __init__(self, okienko):        
        self.okienko = okienko
        self.miejsce_na_rysunek_hangmana = Label(self.okienko)
        self.miejsce_na_rysunek_hangmana.place(x=250,y=100)
        self.hangman_img=[]
        self.MAX_LICZBA_BLEDOW=10
        self.read()      

    def read(self):
        for i in range(self.MAX_LICZBA_BLEDOW):
            img=PhotoImage(file='hangman_'+str(i+1)+'.png')
            self.hangman_img.append(img)

    def draw(self, numer):
        obrazek = self.hangman_img[numer-1]
        self.miejsce_na_rysunek_hangmana.configure(image=obrazek)
        self.miejsce_na_rysunek_hangmana.image = obrazek

hangman=Hangman(okienko)
hangman.draw(5)
okienko.mainloop()

#hangman.draw(1)
#wczytanie grafiki z poszczególnymi etapami wisielca
#hangman1=PhotoImage(file='hangman_1.png')
#hangman1_zdj=Label(image=hangman1)
#przykładowe umiejscowienie:
#hangman1_zdj.place(x=250, y=100)

#hangman2=PhotoImage(file='hangman_2.png')
#hangman2_zdj=Label(image=hangman2)


#hangman3=PhotoImage(file='hangman_3.png')
#hangman3_zdj=Label(image=hangman3)

#hangman4=PhotoImage(file='hangman_4.png')
#hangman4_zdj=Label(image=hangman4)

#hangman5=PhotoImage(file='hangman_5.png')
#hangman5_zdj=Label(image=hangman5)

#hangman6=PhotoImage(file='hangman_6.png')
#hangman6_zdj=Label(image=hangman6)

#hangman7=PhotoImage(file='hangman_7.png')
#hangman7_zdj=Label(image=hangman7)

#hangman8=PhotoImage(file='hangman_8.png')
#hangman8_zdj=Label(image=hangman8)

#hangman9=PhotoImage(file='hangman_9.png')
#hangman9_zdj=Label(image=hangman9)

#hangman10=PhotoImage(file='hangman_10.png')
#hangman10_zdj=Label(image=hangman1)


#wczytanie list ze słowami
kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']

colours=['red', 'green', 'blue', 'purple', 'black']
fruits=['mango', 'pear', 'strawberry', 'banana', 'coconut']
animals=['cat', 'dog', 'zebra', 'fish', 'cow']

alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'o', 'r', 's', 't', 'u', 'w', 'y', 'z']

#funkcja losujaca wyraz i dzielaca go na litery
def losuj_wyraz(lista_wyrazow):
    wyraz=random.choice(lista_wyrazow)
    lista_wyrazu=list(wyraz)
    return lista_wyrazu








'''____________________ tworzymy menu gry _______________________________'''

moj_pasek_menu = Menu(okienko)

info_menu = Menu(moj_pasek_menu, tearoff = 0)
info_menu.add_command(label = "autorzy", command = autorzy)
info_menu.add_command(label = "instrukcja", command = instrukacja)
moj_pasek_menu.add_cascade(label = "informacje", menu = info_menu)

ustawienia_menu = Menu(moj_pasek_menu, tearoff = 0)
ustawienia_menu.add_command(label = "język", command = jezyk)
ustawienia_menu.add_command(label = "nowa gra", command = nowa_gra)
ustawienia_menu.add_command(label = "wyjście", command = okienko.quit)
moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)

"""jezyk_menu = Menu(moj_pasek_menu, tearoff = 0)
jezyk_menu.add_command(label = "English", command = jezyk_ang)
jezyk_menu.add_command(label = "Polski", command = jezyk_pl)
moj_pasek_menu.add_cascade(label = "język", menu = jezyk_menu)"""


