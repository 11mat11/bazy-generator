import random
import csv


def wczytaj_prefiksy_komorkowe():
    """Wczytuje prefiksy operatorów komórkowych z pliku CSV"""
    prefiksy_komorkowe = []
    with open('prefiksy.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            prefiksy_komorkowe.append(row[0])
    return prefiksy_komorkowe

def generuj_numer_telefonu():
    """
    Generuje losowy, poprawny numer telefonu komórkowego dla Polski.
    Format: +48 XXX XXX XXX
    """
    # Wczytaj prefiksy komórkowe
    prefiksy_komorkowe = wczytaj_prefiksy_komorkowe()
    
    # Wybierz losowy prefiks operatora komórkowego
    prefiks = random.choice(prefiksy_komorkowe)
    # Wygeneruj pozostałe cyfry (9 - długość prefiksu)
    reszta = ''.join([str(random.randint(0, 9)) for _ in range(9 - len(prefiks))])
    numer = prefiks + reszta
    
    # Formatuj numer w standardowy sposób
    sformatowany_numer = f"+48 {numer[:3]} {numer[3:6]} {numer[6:]}"
    
    return sformatowany_numer
