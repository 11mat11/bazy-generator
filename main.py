import json
import tkinter as tk
from tkinter import messagebox, ttk
from Pesel.pesel_generator import generate_pesel
from Imiona.imie_generator import wczytaj_imiona, generuj_imie
from Nazwiska.nazwisko_generator import wczytaj_nazwiska, generuj_nazwisko
from Email.email_generator import wczytaj_domain_extensions, generuj_email
from Plec.plec_generator import generuj_plec
from Telefon.telefon_generator import generuj_numer_telefonu
from Karty.karta_kredytowa_generator import wczytaj_biny, generate_card_number
from Adres.generator_adresu import generuj_adres
from Z_format.convert_to_csv import write_to_csv
from Z_format.convert_to_json import write_to_json
from Z_format.convert_to_sql import write_to_sql
import random


def generuj_telefon():
    return generuj_numer_telefonu()

def generuj_karta_kredytowa():
    return generate_card_number()

def generuj_pesel(plec=None):
    return generate_pesel(gender=plec)

def generuj_osobe():
    osoba = {}
    # Płeć
    plec = generuj_plec()
    if var_plec.get():
        osoba["plec"] = plec

    # Imię
    imie = generuj_imie(plec) if var_imie.get() else None
    if imie is not None:
        osoba["imie"] = imie

    # Nazwisko
    nazwisko = generuj_nazwisko(plec) if var_nazwisko.get() else None
    if nazwisko is not None:
        osoba["nazwisko"] = nazwisko

    # Generowanie wielu numerów telefonów
    if var_telefon.get():
        max_telefonow = int(entry_max_telefonow.get())
        liczba_telefonow = random.randint(1, max_telefonow)
        osoba["telefon"] = [generuj_telefon() for _ in range(liczba_telefonow)]

    # Generowanie wielu kart kredytowych
    if var_karta.get():
        max_kart = int(entry_max_kart.get())
        liczba_kart = random.randint(1, max_kart)
        osoba["karta_kredytowa"] = [generuj_karta_kredytowa() for _ in range(liczba_kart)]

    # Generowanie wielu adresów email
    if var_email.get():
        max_emaili = int(entry_max_emaili.get())
        liczba_emaili = random.randint(1, max_emaili)
        osoba["email"] = [generuj_email(imie, nazwisko, plec) for _ in range(liczba_emaili)]

    # PESEL (pozostaje pojedynczy)
    if var_pesel.get():
        osoba["pesel"] = generuj_pesel(plec)

    # Adres składający się z opcjonalnych części
    if var_adres.get():
        options = [
            (var_adres_wojewodztwo, "wojewodztwo"),
            (var_adres_miasto, "miasto"),
            (var_adres_ulica, "ulica"),
            (var_adres_numer, "numer"),
            (var_adres_kod, "kod"),
        ]
        elems = [name for flag, name in options if flag.get()]
        mode = var_address_mode.get()
        if elems:
            osoba["adres"] = generuj_adres(wybierz_elementy=elems, mode=mode)
        else:
            osoba["adres"] = generuj_adres(mode=mode)
    return osoba

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
    wczytaj_domain_extensions()
    wczytaj_biny()

    # Przygotuj UI
    generate_button.config(state=tk.DISABLED)
    pb['maximum'] = ile
    pb['value'] = 0
    percent_label.config(text="0%")
    root.update_idletasks()
    step = max(1, min(10, ile // 100))

    osoby = []
    for idx in range(ile):
        osoba = generuj_osobe()
        osoba['_address_mode'] = var_address_mode.get()
        osoby.append(osoba)

        # ograniczona aktualizacja paska postępu
        if idx % step == 0 or idx == ile - 1:
            pb['value'] = idx + 1
            percent = int((idx + 1) / ile * 100)
            percent_label.config(text=f"{percent}%")
            root.update_idletasks()

    if var_csv.get():
        write_to_csv(osoby)
    if var_sql.get():
        write_to_sql(osoby)
    if var_json.get():
        write_to_json(osoby)

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
var_adres = tk.BooleanVar()
# Części adresu
var_adres_wojewodztwo = tk.BooleanVar(value=True)
var_adres_miasto = tk.BooleanVar(value=True)
var_adres_ulica = tk.BooleanVar(value=True)
var_adres_numer = tk.BooleanVar(value=True)
var_adres_kod = tk.BooleanVar(value=True)
options_frame = ttk.LabelFrame(mainframe, text="Pola do wygenerowania", padding="10 10 10 10")
options_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
ttk.Checkbutton(options_frame, text="Imię", variable=var_imie).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Nazwisko", variable=var_nazwisko).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Płeć", variable=var_plec).grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Email", variable=var_email).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Telefon", variable=var_telefon).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="PESEL", variable=var_pesel).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Karta kredytowa", variable=var_karta).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Adres", variable=var_adres).grid(row=3, column=1, sticky=tk.W, padx=5, pady=2)
# Ramka na cześci adresu
address_options_frame = ttk.LabelFrame(options_frame, text="Elementy adresu", padding="10 10 10 10")
address_options_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
# Checkboxy dla części adresu
ttk.Checkbutton(address_options_frame, text="Województwo", variable=var_adres_wojewodztwo).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(address_options_frame, text="Miasto", variable=var_adres_miasto).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(address_options_frame, text="Ulica", variable=var_adres_ulica).grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(address_options_frame, text="Numer", variable=var_adres_numer).grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(address_options_frame, text="Kod", variable=var_adres_kod).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
# Domyślnie schowaj te opcje
address_options_frame.grid_remove()
# Dodaj opcje trybu generowania adresu
var_address_mode = tk.StringVar(value="most_real")
address_mode_frame = ttk.LabelFrame(options_frame, text="Tryb generowania adresu", padding="10 10 10 10")
address_mode_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
ttk.Radiobutton(address_mode_frame, text="Celnie", variable=var_address_mode, value="most_real").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Radiobutton(address_mode_frame, text="Zbalansowanie", variable=var_address_mode, value="mixed").grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Radiobutton(address_mode_frame, text="Szybko", variable=var_address_mode, value="fastest").grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
# Ukryj tryby na start
address_mode_frame.grid_remove()
# Odkryj opcje, gdy adres jest zaznaczony
def _toggle_address_options(*args):
    if var_adres.get():
        address_options_frame.grid()
        address_mode_frame.grid()
    else:
        address_options_frame.grid_remove()
        address_mode_frame.grid_remove()
var_adres.trace_add('write', _toggle_address_options)

#Wybór formatu
var_json = tk.BooleanVar(value=True)
var_csv = tk.BooleanVar(value=False)
var_sql = tk.BooleanVar(value=False)

format_frame = ttk.LabelFrame(mainframe, text="Format", padding="10 10 10 10")
format_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
ttk.Checkbutton(format_frame, text="JSON", variable=var_json).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(format_frame, text="CSV", variable=var_csv).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(format_frame, text="SQL", variable=var_sql).grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
def update_button_state(*args):
    if var_json.get() or var_csv.get() or var_sql.get():
        generate_button.config(state=tk.NORMAL)
    else:
        generate_button.config(state=tk.DISABLED)
var_json.trace_add('write', update_button_state)
var_csv.trace_add('write', update_button_state)
var_sql.trace_add('write', update_button_state)

# Dodajemy nowe pola dla maksymalnej liczby elementów
max_counts_frame = ttk.LabelFrame(mainframe, text="Maksymalna liczba elementów", padding="10 10 10 10")
max_counts_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

# Telefony
ttk.Label(max_counts_frame, text="Maks. liczba telefonów:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
entry_max_telefonow = ttk.Entry(max_counts_frame, width=10)
entry_max_telefonow.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
entry_max_telefonow.insert(0, "1")

# Karty kredytowe
ttk.Label(max_counts_frame, text="Maks. liczba kart:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
entry_max_kart = ttk.Entry(max_counts_frame, width=10)
entry_max_kart.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
entry_max_kart.insert(0, "1")

# Emails
ttk.Label(max_counts_frame, text="Maks. liczba emaili:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
entry_max_emaili = ttk.Entry(max_counts_frame, width=10)
entry_max_emaili.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
entry_max_emaili.insert(0, "1")

# Ukryj ramkę z maksymalnymi liczbami na start
max_counts_frame.grid_remove()

# Funkcja do pokazywania/ukrywania ramki z maksymalnymi liczbami
def toggle_max_counts(*args):
    if var_telefon.get() or var_karta.get() or var_email.get():
        max_counts_frame.grid()
    else:
        max_counts_frame.grid_remove()

var_telefon.trace_add('write', toggle_max_counts)
var_karta.trace_add('write', toggle_max_counts)
var_email.trace_add('write', toggle_max_counts)

# Przycisk generowania
generate_button = ttk.Button(mainframe, text="Wygeneruj", command=wygeneruj)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Pasek postępu i etykieta procentowa
progress_frame = ttk.Frame(mainframe)
progress_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
pb = ttk.Progressbar(progress_frame, orient='horizontal', mode='determinate', length=200)
pb.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0,10))
percent_label = ttk.Label(progress_frame, text="0%", width=5)
percent_label.grid(row=0, column=1, sticky=tk.E, padx=(5,0))

# Powiąż klawisz Enter z generowaniem
root.bind('<Return>', lambda e: wygeneruj())

root.mainloop()
