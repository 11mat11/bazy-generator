import csv
import random

# Bufory na dane – wczytywane tylko przy potrzebie
imiona_meskie = []
imiona_zenskie = []
imiona_m_names = []
imiona_m_weights = []
imiona_z_names = []
imiona_z_weights = []

# Wczytywanie danych – tylko gdy potrzebne
def wczytaj_imiona():
    global imiona_meskie, imiona_zenskie, imiona_m_names, imiona_m_weights, imiona_z_names, imiona_z_weights
    if not imiona_meskie and not imiona_zenskie:
        with open("imiona.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            reader.fieldnames = [n.strip() for n in reader.fieldnames]
            for row in reader:
                imie = row["IMIĘ_PIERWSZE"].capitalize()
                liczba = int(row["LICZBA_WYSTĄPIEŃ"])
                if row["PŁEĆ"] == "MĘŻCZYZNA":
                    imiona_meskie.append((imie, liczba))
                elif row["PŁEĆ"] == "KOBIETA":
                    imiona_zenskie.append((imie, liczba))
    # wstępne obliczenie rozkładu imion
    if imiona_meskie and not imiona_m_names:
        names, weights = zip(*imiona_meskie)
        imiona_m_names = list(names)
        imiona_m_weights = list(weights)
    if imiona_zenskie and not imiona_z_names:
        names, weights = zip(*imiona_zenskie)
        imiona_z_names = list(names)
        imiona_z_weights = list(weights)

def generuj_imie(plec):
    if plec == "M":
        return random.choices(imiona_m_names, weights=imiona_m_weights, k=1)[0]
    else:
        return random.choices(imiona_z_names, weights=imiona_z_weights, k=1)[0]
