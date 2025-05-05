import csv
import random
from plec_generator import generuj_plec
from imie_generator import generuj_imie
from nazwisko_generator import generuj_nazwisko

# Bufor na dane – wczytywane tylko przy potrzebie
kombinacje = []
weights = []  # weights for weighted random choice based on priority list

# Wczytaj faktyczne kombinacje z pliku CSV
def wczytaj_domain_extensions():
    global kombinacje, weights
    if not kombinacje:
        with open("domain_extensions.csv", encoding="utf-8") as f:
            kombinacje = [row[0].strip() for row in csv.reader(f) if row]
        # Assign higher weight to earlier (more popular) items
        total = len(kombinacje)
        weights = [total - i for i in range(total)]

def generuj_email(imie, nazwisko, plec):
    # Upewnij się, że kombinacje są wczytane
    wczytaj_domain_extensions()
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

    # Wybór domeny z wagami zgodnie z priorytetami
    domain_extension = random.choices(kombinacje, weights=weights, k=1)[0]
    return f"{local}@{domain_extension}"
