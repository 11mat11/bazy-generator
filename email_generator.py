import csv
import random
from plec_generator import generuj_plec
from imie_generator import generuj_imie
from nazwisko_generator import generuj_nazwisko

# Bufory na dane – wczytywane tylko przy potrzebie
domeny = []
rozszerzenia = []

def wczytaj_domains():
    global domeny
    if not domeny:
        with open("domains.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    domeny.append(row[0].strip())

def wczytaj_extensions():
    global rozszerzenia
    if not rozszerzenia:
        with open("extensions.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    rozszerzenia.append(row[0].strip())

def generuj_email(imie, nazwisko, plec):
    # Jeśli brak imienia lub nazwiska, wygeneruj tymczasowo
    if not imie or not nazwisko or not plec:
        plec = generuj_plec()
    if not imie:
        imie = generuj_imie(plec)
    if not nazwisko:
        nazwisko = generuj_nazwisko(plec)
    local = imie.lower()

    # Czy wstawić kropkę między imieniem i nazwiskiem
    if random.choice([True, False]):
        local += "."
    local += nazwisko.lower()

    # Jaką liczbę wstawić po nazwisku
    if random.random() < 0.7:
        scheme = random.choice([1, 2, 3])
        if scheme == 1: # Typowa liczba
            num = str(random.randint(1, 99))
        elif scheme == 2: # Rok
            num = str(random.randint(1900, 2030))
        else: # Dowolna liczba
            num = str(random.randint(1, 9999))
        local += num

    domain = random.choice(domeny)
    ext = random.choice(rozszerzenia)
    return f"{local}@{domain}.{ext}"
