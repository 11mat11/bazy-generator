import csv
import random
import json
import tkinter as tk
from tkinter import messagebox, ttk

def generuj_telefon():
    # TODO: tu wstaw implementację numeru telefonu
    raise NotImplementedError("Phone number generation not implemented yet")

def generuj_pesel():
    # TODO: tu wstaw implementację PESEL
    raise NotImplementedError("PESEL generation not implemented yet")

def generuj_karta_kredytowa():
    # TODO: tu wstaw implementację karty kredytowej
    raise NotImplementedError("Credit card generation not implemented yet")

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

    # Przygotuj UI
    generate_button.config(state=tk.DISABLED)
    pb['maximum'] = ile
    pb['value'] = 0
    percent_label.config(text="0%")
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
        # TODO: Usuń False po dodaniu pola
        if False and var_telefon.get():
            osoba["telefon"] = generuj_telefon()
        if False and var_pesel.get():
            osoba["pesel"] = generuj_pesel()
        if False and var_karta.get():
            osoba["karta_kredytowa"] = generuj_karta_kredytowa()
        osoby.append(osoba)

        # ograniczona aktualizacja paska postępu
        if idx % step == 0 or idx == ile - 1:
            pb['value'] = idx + 1
            percent = int((idx + 1) / ile * 100)
            percent_label.config(text=f"{percent}%")
            root.update_idletasks()

    with open("osoby.json", "w", encoding="utf-8") as f:
        json.dump(osoby, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Sukces", f"Wygenerowano {ile} osób i zapisano do 'osoby.json'.")
    generate_button.config(state=tk.NORMAL)

# Tworzenie GUI
root = tk.Tk()
root.title("Generator osób")
root.resizable(False, False)
style = ttk.Style()
style.theme_use('clam')

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Liczba rekordów do wygenerowania
ttk.Label(mainframe, text="Ile osób:").grid(row=0, column=0, sticky=tk.W)
entry_ile = ttk.Entry(mainframe, width=10)
entry_ile.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
entry_ile.insert(0, "100")
entry_ile.focus()

# Opcje dla pól
var_imie = tk.BooleanVar(value=True)
var_nazwisko = tk.BooleanVar(value=True)
var_plec = tk.BooleanVar()
var_email = tk.BooleanVar()
# Dodatkowe zablokowane pola
var_telefon = tk.BooleanVar()
var_pesel = tk.BooleanVar()
var_karta = tk.BooleanVar()
options_frame = ttk.LabelFrame(mainframe, text="Pola do wygenerowania", padding="10 10 10 10")
options_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
ttk.Checkbutton(options_frame, text="Imię", variable=var_imie).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Nazwisko", variable=var_nazwisko).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Płeć", variable=var_plec).grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Email", variable=var_email).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
# TODO: Po zaimplementowaniu pola usuń "state=tk.DISABLED"
ttk.Checkbutton(options_frame, text="Telefon", variable=var_telefon, state=tk.DISABLED).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="PESEL", variable=var_pesel, state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Karta kredytowa", variable=var_karta, state=tk.DISABLED).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)

# Przycisk generowania
generate_button = ttk.Button(mainframe, text="Wygeneruj", command=wygeneruj)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Pasek postępu i etykieta procentowa
progress_frame = ttk.Frame(mainframe)
progress_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
pb = ttk.Progressbar(progress_frame, orient='horizontal', mode='determinate', length=200)
pb.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0,10))
percent_label = ttk.Label(progress_frame, text="0%", width=5)
percent_label.grid(row=0, column=1, sticky=tk.E, padx=(5,0))

# Powiąż klawisz Enter z generowaniem
root.bind('<Return>', lambda e: wygeneruj())

root.mainloop()
