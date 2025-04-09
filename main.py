import csv
import random
import json

# Wczytywanie imion z jednego pliku
imiona_meskie = []
imiona_zenskie = []

with open("imiona.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=',')
    reader.fieldnames = [n.strip() for n in reader.fieldnames]
    for row in reader:
        if row["PŁEĆ"] == "MĘŻCZYZNA":
            imiona_meskie.append(row["IMIĘ_PIERWSZE"].capitalize())
        elif row["PŁEĆ"] == "KOBIETA":
            imiona_zenskie.append(row["IMIĘ_PIERWSZE"].capitalize())

# Wczytywanie nazwisk męskich
nazwiska_meskie = []
with open("nazwiska_m.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        nazwiska_meskie.append(row["Nawisko"].capitalize())

# Wczytywanie nazwisk żeńskich
nazwiska_zenskie = []
with open("nazwiska_d.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        nazwiska_zenskie.append(row["Nawisko"].capitalize())

# Funkcja generująca jedną osobę
def generuj_osobe():
    plec = random.choice(["M", "K"])
    if plec == "M":
        return {
            "imie": random.choice(imiona_meskie),
            "nazwisko": random.choice(nazwiska_meskie),
            "plec": "M"
        }
    else:
        return {
            "imie": random.choice(imiona_zenskie),
            "nazwisko": random.choice(nazwiska_zenskie),
            "plec": "K"
        }

# Pytanie użytkownika
ile = int(input("Ile osób chcesz wygenerować? "))

# Generowanie i zapis
osoby = [generuj_osobe() for _ in range(ile)]

with open("osoby.json", "w", encoding="utf-8") as f:
    json.dump(osoby, f, indent=4, ensure_ascii=False)

print(f"Wygenerowano {ile} osób i zapisano do pliku 'osoby.json'.")
