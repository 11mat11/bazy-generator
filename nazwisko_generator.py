import csv
import random

# Bufory na dane – wczytywane tylko przy potrzebie
nazwiska_meskie = []
nazwiska_zenskie = []
nazwiska_m_names = []
nazwiska_m_weights = []
nazwiska_z_names = []
nazwiska_z_weights = []

def wczytaj_nazwiska():
    global nazwiska_meskie, nazwiska_zenskie, nazwiska_m_names, nazwiska_m_weights, nazwiska_z_names, nazwiska_z_weights
    if not nazwiska_meskie:
        with open("nazwiska_m.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                nazwisko = row["Nawisko"].capitalize()
                liczba = int(row["Liczba"])
                nazwiska_meskie.append((nazwisko, liczba))
    if not nazwiska_zenskie:
        with open("nazwiska_d.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                nazwisko = row["Nawisko"].capitalize()
                liczba = int(row["Liczba"])
                nazwiska_zenskie.append((nazwisko, liczba))
    # wstępne obliczenie rozkładu nazwisk
    if nazwiska_meskie and not nazwiska_m_names:
        names, weights = zip(*nazwiska_meskie)
        nazwiska_m_names = list(names)
        nazwiska_m_weights = list(weights)
    if nazwiska_zenskie and not nazwiska_z_names:
        names, weights = zip(*nazwiska_zenskie)
        nazwiska_z_names = list(names)
        nazwiska_z_weights = list(weights)

def generuj_nazwisko(plec):
    if plec == "M":
        return random.choices(nazwiska_m_names, weights=nazwiska_m_weights, k=1)[0]
    else:
        return random.choices(nazwiska_z_names, weights=nazwiska_z_weights, k=1)[0]
