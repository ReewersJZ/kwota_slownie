from slownik_liczb import *

def liczba_slownie(full_number):
    list = []
    for element in full_number:
        list += element
    if list[0] == '-':
        list = list[1:]

    return list

def koncowki(trojka, wielkosc):
    if trojka == '2' or trojka == '3' or trojka == '4':
        a = wielkosc[1]
    elif trojka == '5' or trojka == '1' or trojka == '6' or trojka == '7' or trojka == '8' or trojka == '9' or trojka == '0':
        a = wielkosc[2]

    return a

def polish_version():
    pass

def english_version():
    pass


def podzial(lista):  # Funkcja dzielaca podana liczbe na listy 3-cyfrowe. Tutaj jako argument musi trafic ogolna lista (odwrocona kolejnosc cyfr)
    lista2 = []
    while lista:
        if len(lista) >= 3:
            lista_trojkowa = lista[0:3]
            lista2.append(lista_trojkowa)
            lista = lista[3:]
        if len(lista) == 2:
            lista_trojkowa = ['korek']
            lista_trojkowa = lista_trojkowa + lista
            lista2.append(lista_trojkowa)
            lista = []
        if len(lista) == 1:
            lista_trojkowa = ['korek', 'korek']
            lista_trojkowa.append(lista[0])
            lista2.append(lista_trojkowa)
            lista = []

    return lista2

def wielkosc_def(trojka, wielkosc):
    a = ''
    if trojka[1] =='korek' or trojka[0] == 'korek':
        if trojka[2] == '1' and trojka[1] == 'korek' and trojka[0] == 'korek':
            a = wielkosc[0]
        elif trojka[2] != '1' and trojka[1] == 'korek' and trojka[0] == 'korek':
            a = koncowki(trojka[2], wielkosc)
        elif trojka[1] != 'korek' and trojka[0] == 'korek':
            if trojka[2] == '1':
                a = wielkosc[2]
            elif trojka[2] != '1':
                a = koncowki(trojka[1], wielkosc)
    elif trojka[1] !='korek' and trojka[0] != 'korek':
        if trojka[2] == '0' and trojka[1] == '0' and trojka[0] == '0':
            a = wielkosc[3]
            print('na pewno jestem tu')
        elif trojka[2] != '0':
            if trojka[1] == '1':
                a = wielkosc[2]
            elif trojka[1] != '1':
                a = koncowki(trojka[0], wielkosc)
        elif trojka[0] == '1' and trojka[1] == '0' and trojka[2] == '0':
            a = wielkosc[0]
        elif trojka[0] != '1' and trojka[1] == '0' and trojka[0] == '0':
            a = koncowki(trojka[0], wielkosc)
        elif trojka[1] == '1' and trojka[2] == '0':
            a = wielkosc[2]
        elif trojka[1] != '1' and trojka[2] == '0':
            a = koncowki(trojka[0], wielkosc)

    return a


def cyfry_def(lista_slownie, trojka, cyfry):
    for klucz in cyfry:
        if trojka == klucz:
            lista_slownie.append(cyfry[klucz])

    return lista_slownie

def liczby_def(lista_slownie, trojka, liczby):
    for klucz in liczby:
        if trojka == klucz:
            lista_slownie.append(liczby[klucz])

    return lista_slownie


def zmien_na_slownie(lista, setki, liczby, cyfry, tysiace, miliony, biliony, tryliony):
    przejscie_petli = 1
    lista_slownie = []
    for trojka in lista:
        if trojka[1] != 'korek' and trojka[0] != 'korek':
            if trojka[2] == '0':
                if trojka[1] != '0' and trojka[1] != '1':
                    for klucz in dziesiatki:
                        if trojka[1] == klucz:
                            lista_slownie.append(dziesiatki[klucz])
                            lista_slownie = cyfry_def(lista_slownie, trojka[0], cyfry)
                elif trojka[1] == '1':
                    lista_slownie = liczby_def(lista_slownie, trojka[0], liczby)
                elif trojka[1] == '0':
                    if trojka[0] == '0':
                        przejscie_petli += 1
                        continue
                    elif trojka[0] != '0':
                        lista_slownie = cyfry_def(lista_slownie, trojka[0], cyfry)
            elif trojka[2] != '0':
                for klucz in setki:
                    if trojka[2] == klucz:
                        lista_slownie.append(setki[klucz])
                        if trojka[1] != '0' and trojka[1] != '1':
                            for klucz in dziesiatki:
                                if trojka[1] == klucz:
                                    lista_slownie.append(dziesiatki[klucz])
                                    lista_slownie = cyfry_def(lista_slownie, trojka[0], cyfry)
                        elif trojka[1] == '1':
                            lista_slownie = liczby_def(lista_slownie, trojka[0], liczby)
                        elif trojka[1] == '0':
                            lista_slownie = cyfry_def(lista_slownie, trojka[0], cyfry)
        elif trojka[1] == 'korek':
            lista_slownie = cyfry_def(lista_slownie, trojka[2], cyfry)
        elif trojka[0] == 'korek':
            if trojka[2] != '1':
                for klucz in dziesiatki:
                    if trojka[2] == klucz:
                        lista_slownie.append(dziesiatki[klucz])
                        lista_slownie = cyfry_def(lista_slownie, trojka[1], cyfry)
            elif trojka[2] == '1':
                lista_slownie = liczby_def(lista_slownie, trojka[1], liczby)

        if len(lista) - przejscie_petli == 0: # tutaj docelowo podana będzie waluta
            a = wielkosc_def(trojka, slownie)
            lista_slownie.append(a)
        if len(lista) - przejscie_petli == 1:
            a = wielkosc_def(trojka, tysiace)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 2:
            a = wielkosc_def(trojka, miliony)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 3:
            a = wielkosc_def(trojka, miliardy)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 4:
            a = wielkosc_def(trojka, biliony)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 5:
            a = wielkosc_def(trojka, biliardy)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 6:
            a = wielkosc_def(trojka, tryliony)
            lista_slownie.append(a)
        elif len(lista) - przejscie_petli == 7:
            a = wielkosc_def(trojka, tryliardy)
            lista_slownie.append(a)

        przejscie_petli += 1

    return lista_slownie

