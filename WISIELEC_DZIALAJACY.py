'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random
    
'''_____________________ Tworzymy klasę Hangman _____________________________ '''
  
class Hangman():
    def __init__(self, okienko):   
        self.okienko = okienko
        self.miejsce_na_rysunek_hangmana = Label(self.okienko)
        self.miejsce_na_rysunek_hangmana.place(x=280,y=40)
        self.hangman_img=[]
        
        self.MAX_LICZBA_BLEDOW=10
        self.licznik_bledow=0
        self.read()  
        # kategorie haseł
        self.kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
        self.owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
        self.zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']    

        self.alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'o', 'r', 's', 't', 'u', 'w', 'y', 'z']
        self.zakryte_slowo=[]
        self.uzyte_bledne_litery = []
        # Tworzymy okienka w GUI z widgetami
        self.top_frame = Frame(self.okienko)
        self.middle_frame = Frame(self.okienko)
        self.bottom_frame = Frame(self.okienko)
        self.txt_wybierz_kategorie = Label(self.okienko, text = "Wybierz kategorię:")
        self.radio_button_wartosci = IntVar()
        self.radio_button_wartosci.set(1)

        # Tworzymy RadioButton z kategoriami       
                                            
        self.rprzycisk_1 = Radiobutton(self.okienko, text = "kolory", variable = self.radio_button_wartosci, value = 1, command = self.losuj_kat)                               
        self.rprzycisk_2 = Radiobutton(self.okienko, text = "owoce", variable = self.radio_button_wartosci, value = 2, command= self.losuj_kat)                               
        self.rprzycisk_3 = Radiobutton(self.okienko, text = "zwierzeta", variable = self.radio_button_wartosci, value = 3, command = self.losuj_kat)                              
        self.rprzycisk_4 = Radiobutton(self.okienko, text = "losowa", variable = self.radio_button_wartosci, value = 4, command = self.losuj_kat)


        self.wpisz_litere_info = Label(self.okienko, text = "Podaj dowolną literę - pomiń znaki polskie!")
        self.ukryte_haslo = Label(self.okienko, text = "info")
        self.instrukcja = Button(self.okienko, text = "Instrukcja", command = self.wyswietl_instrukcje)
        self.autorzy = Button(self.okienko, text = "Autorzy", command = self.wyswietl_autorow)
        self.wpisz_litere_okienko = Entry(self.okienko)
        self.przycisk_zle_litery = Button(self.okienko, text = "Sprawdź wykorzystane litery:", command = self.zle_litery)
        self.przycisk_spr = Button(self.okienko, text = "Sprawdź", command = self.sprawdz_litere)
        self.przycisk_nowa_gra=Button(self.okienko, text="Nowa gra", command=self.uruchom_nowa_gre)
       
        
        self.instrukcja.place(x=70, y=10)
        self.autorzy.place(x=10, y=20)
        self.txt_wybierz_kategorie.place(x=20, y=50)
        self.rprzycisk_1.place(x=20,y=50)
        self.rprzycisk_2.place(x=25,y=70)
        self.rprzycisk_3.place(x=25, y=90)
        self.rprzycisk_4.place(x=25, y=110)
        self.przycisk_zle_litery.place(x=25, y=130)
        self.ukryte_haslo.place(x=310, y=300)
        self.wpisz_litere_info.place(x=25, y=280)
        
        self.wpisz_litere_okienko.place(x=25, y=260)
        self.przycisk_spr.place(x=125, y=260)
        self.przycisk_nowa_gra.place(x=170, y=470)

        self.uruchom_nowa_gre()

        mainloop()

    '''_____________________ wszystkie funkcje _____________________________ '''
    
    def wyswietl_autorow():
        messagebox.showinfo("Autotzy","Kornelia Winiarska i Monika Patrycja Lelujko")
    
    def wyswietl_instrukcje():
        messagebox.showinfo("Instrukcja","Drogi graczu, /n witaj w grze wisielec! /n Aby rozpocząć grę wybierz kategorię, z której chcesz wylosować hasło, a następnie wpisz w określone pole dowolną literę alfabetu z pominięciem znaków języka polskiego. \n Aby sprawdzić czy dana litera znajduje się w wylosowanym przez Ciebie słowie naciśnij przycisk \"SPRAWDŹ\". Możesz pomylić się 10-krotnie zanim przegrasz. \n Aby ustalić jakie litery już sprawdziłeś naciśnij przycisk \"SPRAWDŹ WYKORZYSTANE LITERY\". \n Aby rozpocząć nową gre naciśnij przycisk \" NOWA GRA\" \nPowodzenia!")

    def losuj_kat(self):
        value=self.radio_button_wartosci.get()
        if value == 1:
            self.lista_wyrazow = self.kolory
        if value == 2:
            self.lista_wyrazow = self.owoce
        if value == 3:
            self.lista_wyrazow = self.zwierzeta
        if value == 4:
            self.lista_wyrazow = self.kolory + self.owoce + self.zwierzeta
        self.losuj_wyraz()
        self.dezaktywuj_przyciski(True)
    
    #funkcja utworzona na potrzeby funkcji uruchamiajacej nowa grę
    def dezaktywuj_przyciski(self, is_disabled):
        if is_disabled==True:
            self.rprzycisk_1.configure(state=DISABLED) 
            self.rprzycisk_2.configure(state=DISABLED)
            self.rprzycisk_3.configure(state=DISABLED)
            self.rprzycisk_4.configure(state=DISABLED)
        else:
            self.rprzycisk_1.configure(state=ACTIVE) 
            self.rprzycisk_2.configure(state=ACTIVE)
            self.rprzycisk_3.configure(state=ACTIVE)
            self.rprzycisk_4.configure(state=ACTIVE)
    
    #funkcja losujaca wyraz i dzielaca go na litery
    def losuj_wyraz(self):
        wyraz=random.choice(self.lista_wyrazow)
        self.lista_wyrazu=list(wyraz[:])
        self.zakryj_slowo()

    #funkcja zamieniająca litery w wylosowanym słowie na kreski
    def zakryj_slowo(self):
        self.zakryte_slowo=[]
        for i in list(self.lista_wyrazu):
           self.zakryte_slowo.append("_")
        self.ukryte_haslo.config(text=' '.join(self.zakryte_slowo))
        
    #funkcje: 
    #sprawdzająca czy dana litera znajduje się w wylosowanym słowie oraz czy dana litere była juz sprawdzana, 
    #wstawiająca prawidłową literę zamiast kreski w sprawdzanym słowie,
    #zliczjąca błedne próby podania litery
    #wyświetlająca użyte błędne litery
    #wyświetlająca komunikaty o przegranej bądź wygranej
    
    def sprawdz_litere(self):
        sprawdzana = self.wpisz_litere_okienko.get()
        self.wpisz_litere_okienko.delete(0,END)
        if sprawdzana in self.sprawdzane_litery:
            messagebox.showinfo(' ', 'Ta litera była już sprawdzana! Wybierz inną.')
            return 
        self.sprawdzane_litery.append(sprawdzana)
        i=0
        ok=False
        for litera in self.lista_wyrazu:
            if litera == sprawdzana:
                ok=True
                self.zakryte_slowo[i]=litera
            i+=1
        if ok==False:
            self.bledne_litery+=1
            self.draw(self.bledne_litery)
            self.uzyte_bledne_litery += sprawdzana
            if self.bledne_litery==10:
                self.koniec_gry('Przegrałeś!')
        self.ukryte_haslo.config(text=' '.join(self.zakryte_slowo))
        if '_' not in self.zakryte_slowo:
            self.koniec_gry('Wygrałeś!')
            
    def zle_litery(self):
        messagebox.showinfo(self.uzyte_bledne_litery)
    
    def koniec_gry(self, status):
        messagebox.showinfo("koniec_gry", status)

    def licz_bledy(self):
        lista_bledow=[]
        for l in lista_bledow:
            if l not in self.lista_wyrazu:
                lista_bledow.append(l)
                self.licznik_bledow+=1
    
    def wylacz_uzyte_litery(self, litera):
        uzyte_litery=[]
        for litera in alfabet:
            if litera in alfabet:
                uzyte_litery.append(litera)

#funkcja rysująca wisielca
    def read(self):
        for i in range(self.MAX_LICZBA_BLEDOW):
            img=PhotoImage(file='hangman_'+str(i+1)+'.png')
            self.hangman_img.append(img)

    def draw(self, numer):
        obrazek = self.hangman_img[numer-1]
        self.miejsce_na_rysunek_hangmana.configure(image=obrazek)
        self.miejsce_na_rysunek_hangmana.image = obrazek

#funkcja uruchamiajaca nowa grę po naciśnięciu odpowiedniego przycisku
    def uruchom_nowa_gre(self):
        self.dezaktywuj_przyciski(False)
        self.lista_wyrazow = []
        self.zgadywane_slowo = []
        self.sprawdzane_litery=[]
        self.bledne_litery = 0
        self.zakryte_slowo = []
        self.draw(0)
        self.ukryte_haslo.config(text='')

        

#https://stackoverflow.com/questions/2969870/removing-minimize-maximize-buttons-in-tkinter   
okienko.resizable(0,0)

#utworzenie obiektu klasy Hangman
hangman=Hangman()
hangman.draw(5)
