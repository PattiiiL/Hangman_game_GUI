'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random

'''____________________ tworzymy okienko gry _____________________________'''

okienko = Tk()
okienko.title("Wisielec")
okienko.geometry("400x500")
    

'''_____________________ wszystkie funkcje _____________________________ '''


#def autorzy():
 #   tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
  #  tekst.pack(side = TOP)
    
#def instrukacja():
 #   tekst = Label(okienko, text = "Witaj w grze wisielec! /n ")
  #  tekst.pack(side = TOP)

#def jezyk():
    
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








'''____________________ tworzymy menu gry _______________________________'''

#moj_pasek_menu = Menu(okienko)

#info_menu = Menu(moj_pasek_menu, tearoff = 0)
#info_menu.add_command(label = "autorzy", command = autorzy)
#info_menu.add_command(label = "instrukcja", command = instrukacja)
#moj_pasek_menu.add_cascade(label = "informacje", menu = info_menu)

#ustawienia_menu = Menu(moj_pasek_menu, tearoff = 0)
#ustawienia_menu.add_command(label = "język", command = jezyk)
#ustawienia_menu.add_command(label = "nowa gra", command = nowa_gra)
#ustawienia_menu.add_command(label = "wyjście", command = okienko.quit)
#moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)


