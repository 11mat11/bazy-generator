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

def generuj_telefon():
    return generuj_numer_telefonu()

def generuj_karta_kredytowa():
    return generate_card_number()

def generuj_pesel(plec=None):
    return generate_pesel(gender=plec)

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
        if var_telefon.get():
            osoba["telefon"] = generuj_telefon()
        if var_pesel.get():
            osoba["pesel"] = generuj_pesel(plec)
        if var_karta.get():
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
ttk.Checkbutton(options_frame, text="Telefon", variable=var_telefon).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="PESEL", variable=var_pesel).grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
ttk.Checkbutton(options_frame, text="Karta kredytowa", variable=var_karta).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)

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
