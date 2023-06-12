import os
from pathlib import Path, PurePath

def zapis_pliku(nazwa: str, lista: list, sciezka = None):   #zwrot 0 - sukces, -1 - blad sciezki
    
   
    #dodawanie rozszerzenia, jesli go nie ma
    if '.' not in nazwa:
        nazwa = nazwa + ".txt"
    if sciezka is None:     #sprawdzanie, czy sciezka jest podana
        sciezka = ""
    else:
        sciezka = sciezka + "/"
        if '\\' in sciezka:     #zmiana \ na / aby nie dzialala funkcja Path
            for x in sciezka:
                if x == '\\':
                    x = '/'
    if not os.path.exists(Path(sciezka)):       #sprawdzanie, czy dana sciezka istnieje
        return -1
    f = open(Path(sciezka+nazwa), "a", encoding='utf-8')    #otwieranie pliku
    for x in lista:
        f.write(x + "\n")
    f.close()
    return 0


def odczyt_pliku(nazwa: str, sciezka = None) -> list:   #zwrot 0 - sukces, -1 - blad sciezki
    #dodawanie rozszerzenia, jesli go nie ma
    if '.' not in nazwa:
        nazwa = nazwa + ".txt"

    if sciezka is not None:
        sciezka = sciezka + "/"
        if '\\' in sciezka:     #zmiana \ na / aby nie dzialala funkcja Path
            for x in sciezka:
                if x == '\\':
                    x = '/'
    else:
        sciezka = ""
    if not os.path.exists(Path(sciezka+nazwa)):     #sprawdzenie, czy plik/sciezka istnieje
        return None
    f = open(Path(sciezka+nazwa), "r", encoding='utf-8')
    Zakupki = f.readlines()
    f.close()
    return Zakupki



#path = "E:/AppLista"
#zapis_pliku("wowow.txt",["pierwsze", "drugie"], path)
#print(odczyt_pliku("wowow", path))