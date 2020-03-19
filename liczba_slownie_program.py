from funkcje import *

import tkinter
from tkinter import messagebox
import os

path = os.path.dirname(__file__)
os.chdir(path)


def akcja():
    global poleTekstowe, koncowy_wynik
    full_number = poleTekstowe.get()
    try:
        if full_number == '0':
            koncowy_wynik.configure(text='zero złotych')
        elif full_number != '0' and int(full_number):
            lista = liczba_slownie(full_number)
            lista.reverse()
            lista = podzial(lista)
            lista.reverse()
            lista_slownie = zmien_na_slownie(lista, setki, liczby, cyfry, tysiace, miliony, biliony, tryliony)
            if full_number[0] == '-':
                lista_slownie.insert(0, 'minus')
            if 'złotych' not in lista_slownie and 'złote' not in lista_slownie and 'złoty' not in lista_slownie:
                lista_slownie.append('złotych')

            wynik = ''
            licznik = 1
            while lista_slownie:
                for element in lista_slownie:
                    if licznik % 6 != 0:
                        wynik += element + ' '
                        licznik += 1
                    else:
                        wynik += element + '\n'
                        licznik += 1
                        continue
                    lista_slownie = lista_slownie[5:]

            koncowy_wynik.configure(text=wynik)
    except ValueError:
        tkinter.messagebox.showinfo('Uwaga!', 'Podano błędne dane. Wprowadź liczbę całkowitą.')


def main():
    global poleTekstowe, koncowy_wynik
    root = tkinter.Tk()
    root.title('Liczba słownie')
    root.configure(background='grey')
    app = tkinter.Frame(root)
    app.configure(background='white')
    app.grid()

    '''opcja = tkinter.Radiobutton(master=app, text='PL', font=('Gill sans MT', 18), anchor='e', command=polish_version)
    opcja.grid(column=0, row=0)
    opcja2 = tkinter.Radiobutton(master=app, text='ENG', font=('Gill sans MT', 18), anchor='e', command=english_version)
    opcja2.grid(column=0, row=1)'''
    myphoto = tkinter.PhotoImage(file='logo2.png')
    label11 = tkinter.Label(master=app, image=myphoto)
    label11.grid(column=0, row=0)

    label2 = tkinter.Label(master=app, text='Podaj liczbę: ', bg='white', fg='#996699',
                           font=('Gill sans MT', 20, 'bold'))
    label2.grid(columnspan=2, row=1)
    poleTekstowe = tkinter.Entry(app, font=('Consolas', 20), bg='white')
    poleTekstowe.grid(columnspan=2, row=2)

    button1 = tkinter.Button(master=app, text="Konwertuj", bg='#CC99FF', fg='black', font=('Gill sans MT', 16, 'bold'),
                             command=akcja)
    button1.grid(columnspan=2, row=3)
    koncowy_wynik = tkinter.Label(master=app, text='', bg='white',
                                  fg='black', font=('Gill sans MT', 16))
    koncowy_wynik.grid(columnspan=2, rowspan=3)

    root.mainloop()


if __name__ == '__main__':
    main()
