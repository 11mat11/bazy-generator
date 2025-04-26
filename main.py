import csv
import random
import json
import tkinter as tk
from tkinter import messagebox, ttk

# Bufory na dane – wczytywane tylko przy potrzebie
imiona_meskie = []
imiona_zenskie = []
nazwiska_meskie = []
nazwiska_zenskie = []
domeny = []
rozszerzenia = []
imiona_m_names = []
imiona_m_weights = []
imiona_z_names = []
imiona_z_weights = []
nazwiska_m_names = []
nazwiska_m_weights = []
nazwiska_z_names = []
nazwiska_z_weights = []

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

# Generowanie danych
def generuj_plec():
    return random.choice(["M", "K"])

def generuj_imie(plec):
    if plec == "M":
        return random.choices(imiona_m_names, weights=imiona_m_weights, k=1)[0]
    else:
        return random.choices(imiona_z_names, weights=imiona_z_weights, k=1)[0]

def generuj_nazwisko(plec):
    if plec == "M":
        return random.choices(nazwiska_m_names, weights=nazwiska_m_weights, k=1)[0]
    else:
        return random.choices(nazwiska_z_names, weights=nazwiska_z_weights, k=1)[0]

# Obsługa kliknięcia przycisku
def wygeneruj():
    try:
        ile = int(entry_ile.get())
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną liczbę osób.")
        return

    # wczytaj dane tylko raz
    wczytaj_imiona()
    wczytaj_nazwiska()
    wczytaj_domains()
    wczytaj_extensions()

    # ustawienie i wyzerowanie paska postępu
    pb['maximum'] = ile
    pb['value'] = 0
    root.update_idletasks()
    step = max(1, min(10, ile // 100))

    osoby = []
    for idx in range(ile):
        osoba = {}
        plec = generuj_plec()
        # przygotuj imię/nazwisko także dla e‑maila
        if var_plec.get():
            osoba["plec"] = plec
        if var_imie.get():
            imie = generuj_imie(plec)
            osoba["imie"] = imie
        else:
            imie = None
        if var_nazwisko.get():
            nazwisko = generuj_nazwisko(plec)
            osoba["nazwisko"] = nazwisko
        else:
            nazwisko = None
        if var_email.get():
            osoba["email"] = generuj_email(imie, nazwisko, plec)
        osoby.append(osoba)

        # ograniczona aktualizacja paska postępu
        if idx % step == 0 or idx == ile - 1:
            pb['value'] = idx + 1
            root.update_idletasks()

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
var_email = tk.BooleanVar()

check_imie = tk.Checkbutton(frame, text="Imię", variable=var_imie)
check_nazwisko = tk.Checkbutton(frame, text="Nazwisko", variable=var_nazwisko)
check_plec = tk.Checkbutton(frame, text="Płeć", variable=var_plec)
check_email = tk.Checkbutton(frame, text="Email", variable=var_email)

check_imie.pack(anchor='w')
check_nazwisko.pack(anchor='w')
check_plec.pack(anchor='w')
check_email.pack(anchor='w')

button = tk.Button(frame, text="Wygeneruj", command=wygeneruj)
button.pack(pady=10)

# progress bar pokazujący postęp
pb = ttk.Progressbar(frame, orient='horizontal', length=300, mode='determinate')
pb.pack(pady=(5, 0), fill='x')

root.mainloop()
