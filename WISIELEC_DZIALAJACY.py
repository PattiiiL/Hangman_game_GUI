'''_____________________ wszystkie imporciki _____________________________ '''

from tkinter import *
from tkinter import messagebox
import random

'''____________________ tworzymy okienko gry _____________________________'''

okienko = Tk()
okienko.title("Wisielec")
okienko.geometry("400x500")
    
'''_____________________ wszystkie funkcje _____________________________ '''


def autorzy():
    tekst = Label(okienko, text = "Autorzy: Kornelia Winiarska i Monika Patrycja Lelujko")
    #tekst.pack(side = TOP)
    
def instrukacja():
    tekst = Label(okienko, text = "Drogi graczu, /n witaj w grze wisielec! /n Aby rozpoczac grę wybierz kategorię, zktórej chcesz wylosować hasło. ")
    #tekst.pack(side = TOP)


kolory=['czerwony', 'zielony', 'niebieski', 'fioletowy', 'czarny']
owoce=['mango', 'gruszka', 'truskawka', 'banan', 'kokos']
zwierzeta=['kot', 'pies', 'zebra', 'ryba', 'krowa']

colours=['red', 'green', 'blue', 'purple', 'black']
fruits=['mango', 'pear', 'strawberry', 'banana', 'coconut']
animals=['cat', 'dog', 'zebra', 'fish', 'cow']

alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'o', 'r', 's', 't', 'u', 'w', 'y', 'z']
  
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
        self.wpisz_litere_okienko = Entry(self.okienko)
        self.przycisk_spr = Button(self.okienko, text = "Sprawdź", command = self.sprawdz_litere)
        self.przycisk_nowa_gra=Button(self.okienko, text="Nowa gra", command=self.uruchom_nowa_gre)
        
        self.txt_wybierz_kategorie.place(x=20, y=10)
        self.rprzycisk_1.place(x=25,y=30)
        self.rprzycisk_2.place(x=25,y=50)
        self.rprzycisk_3.place(x=25, y=70)
        self.rprzycisk_4.place(x=25, y=90)

        self.ukryte_haslo.place(x=310, y=260)
        self.wpisz_litere_info.place(x=25, y=240)
        self.wpisz_litere_okienko.place(x=25, y=260)
        self.przycisk_spr.place(x=125, y=260)
        self.przycisk_nowa_gra.place(x=170, y=470)

        ''' self.top_frame.pack()
        self.middle_frame.pack()           
        self.bottom_frame.pack()'''

        # Tworzymy menu gry

        self.moj_pasek_menu = Menu(self.okienko)

        info_menu = Menu(self.moj_pasek_menu, tearoff = 0)
        info_menu.add_command(label = "autorzy", command = autorzy)
        info_menu.add_command(label = "instrukcja", command = self.instrukcja)
        self.moj_pasek_menu.add_cascade(label = "informacje", menu = info_menu)

        ustawienia_menu = Menu(self.moj_pasek_menu, tearoff = 0)
        #ustawienia_menu.add_command(label = "język", command = self.jezyk)
        #ustawienia_menu.add_command(label = "nowa gra", command = self.nowa_gra)
        ustawienia_menu.add_command(label = "wyjście", command = self.okienko.quit)
        self.moj_pasek_menu.add_cascade(label = "ustawienia", menu = ustawienia_menu)

        self.uruchom_nowa_gre()

        mainloop()

    def instrukcja():
        tekst = Label(self.okienko, text = "Drogi graczu, /n witaj w grze wisielec! /n Aby rozpoczac grę wybierz kategorię, z której chcesz wylosować hasło. ")
        #tekst.pack(side = TOP)

    def losuj_kat(self):
        value=self.radio_button_wartosci.get()
        print(value)
        if value == 1:
            self.lista_wyrazow = self.kolory
        if value == 2:
            self.lista_wyrazow = self.owoce
        if value == 3:
            self.lista_wyrazow = self.zwierzeta
        if value == 4:
            self.lista_wyrazow = self.kolory + self.owoce + self.zwierzeta
        print(self.lista_wyrazow)
        self.losuj_wyraz()
        self.dezaktywuj_przyciski(True)
    
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
        print(self.lista_wyrazu)

    def zakryj_slowo(self):
        self.zakryte_slowo=[]
        print(self.lista_wyrazu)
        for i in list(self.lista_wyrazu):
           self.zakryte_slowo.append("_")
        self.ukryte_haslo.config(text=' '.join(self.zakryte_slowo))
        #messagebox.showinfo("Wylosowane słowo", print(self.zakryte_slowo))
        #slowo_kreski = print(self.zakryte_slowo)
        #return slowo_kreski
        

    def sprawdz_litere(self):
        sprawdzana = self.wpisz_litere_okienko.get()
        self.wpisz_litere_okienko.delete(0,END)
        print(sprawdzana)
        if sprawdzana in self.sprawdzane_litery:
            print('sprawdzales juz te litere')
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
            if self.bledne_litery==10:
                self.koniec_gry('przegrales!')
        self.ukryte_haslo.config(text=' '.join(self.zakryte_slowo))
        if '_' not in self.zakryte_slowo:
            self.koniec_gry('wygrales!')
        # do ogarniecia zeby litery dodawaly sie na odp msc
     
    def koniec_gry(self, status):
        print("koniec_gry", status)

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

    def read(self):
        for i in range(self.MAX_LICZBA_BLEDOW):
            img=PhotoImage(file='hangman_'+str(i+1)+'.png')
            self.hangman_img.append(img)

    def draw(self, numer):
        obrazek = self.hangman_img[numer-1]
        self.miejsce_na_rysunek_hangmana.configure(image=obrazek)
        self.miejsce_na_rysunek_hangmana.image = obrazek

    def uruchom_nowa_gre(self):
        self.dezaktywuj_przyciski(False)
        self.lista_wyrazow = []
        self.zgadywane_slowo = []
        self.sprawdzane_litery=[]
        self.bledne_litery = 0
        self.zakryte_slowo = []
        self.draw(1)
        self.ukryte_haslo.config(text='')

        

#https://stackoverflow.com/questions/2969870/removing-minimize-maximize-buttons-in-tkinter   
okienko.resizable(0,0)
hangman=Hangman(okienko)
hangman.draw(5)
okienko.mainloop()
