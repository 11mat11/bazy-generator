import csv
import random
import json
import tkinter as tk
from tkinter import messagebox

# Bufory na dane – wczytywane tylko przy potrzebie
imiona_meskie = []
imiona_zenskie = []
nazwiska_meskie = []
nazwiska_zenskie = []

# Wczytywanie danych – tylko gdy potrzebne
def wczytaj_imiona():
    global imiona_meskie, imiona_zenskie
    if not imiona_meskie and not imiona_zenskie:
        with open("imiona.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            reader.fieldnames = [n.strip() for n in reader.fieldnames]
            for row in reader:
                if row["PŁEĆ"] == "MĘŻCZYZNA":
                    imiona_meskie.append(row["IMIĘ_PIERWSZE"].capitalize())
                elif row["PŁEĆ"] == "KOBIETA":
                    imiona_zenskie.append(row["IMIĘ_PIERWSZE"].capitalize())

def wczytaj_nazwiska():
    global nazwiska_meskie, nazwiska_zenskie
    if not nazwiska_meskie:
        with open("nazwiska_m.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                nazwiska_meskie.append(row["Nawisko"].capitalize())
    if not nazwiska_zenskie:
        with open("nazwiska_d.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                nazwiska_zenskie.append(row["Nawisko"].capitalize())

# Generowanie danych
def generuj_plec():
    return random.choice(["M", "K"])

def generuj_imie(plec):
    wczytaj_imiona()
    if plec == "M":
        return random.choice(imiona_meskie)
    else:
        return random.choice(imiona_zenskie)

def generuj_nazwisko(plec):
    wczytaj_nazwiska()
    if plec == "M":
        return random.choice(nazwiska_meskie)
    else:
        return random.choice(nazwiska_zenskie)

# Obsługa kliknięcia przycisku
def wygeneruj():
    try:
        ile = int(entry_ile.get())
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną liczbę osób.")
        return

    osoby = []
    for _ in range(ile):
        osoba = {}
        plec = generuj_plec()

        if var_plec.get():
            osoba["plec"] = plec
        if var_imie.get():
            osoba["imie"] = generuj_imie(plec)
        if var_nazwisko.get():
            osoba["nazwisko"] = generuj_nazwisko(plec)

        osoby.append(osoba)

    with open("osoby.json", "w", encoding="utf-8") as f:
        json.dump(osoby, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Sukces", f"Wygenerowano {ile} osób i zapisano do 'osoby.json'.")

# Tworzenie GUI
root = tk.Tk()
root.title("Generator osób")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Ile osób wygenerować?")
label.pack()
entry_ile = tk.Entry(frame)
entry_ile.pack()

var_imie = tk.BooleanVar()
var_nazwisko = tk.BooleanVar()
var_plec = tk.BooleanVar()

check_imie = tk.Checkbutton(frame, text="Imię", variable=var_imie)
check_nazwisko = tk.Checkbutton(frame, text="Nazwisko", variable=var_nazwisko)
check_plec = tk.Checkbutton(frame, text="Płeć", variable=var_plec)

check_imie.pack(anchor='w')
check_nazwisko.pack(anchor='w')
check_plec.pack(anchor='w')

button = tk.Button(frame, text="Wygeneruj", command=wygeneruj)
button.pack(pady=10)

root.mainloop()
