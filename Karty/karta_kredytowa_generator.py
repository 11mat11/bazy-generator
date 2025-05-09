import random
import csv
from datetime import datetime, timedelta

bin_array = []

def wczytaj_biny():
    global bin_array
    if not bin_array:
        with open("Karty/bin.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                bin_array.append(row)

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(x) for x in str(n) if x.isdigit()]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        doubled = d * 2
        total += sum(digits_of(doubled))
    return total % 10

def generate_card_number():
    selected_bin = random.choice(bin_array)
    bin_code = selected_bin['BIN']
    scheme = selected_bin['Scheme']
    bank = selected_bin['Bank']
    card_type = selected_bin['Type']
    card_number = generate_luhn_number(bin_code, get_card_length(scheme))
    expiry = generate_expiry()
    cvv = generate_cvv(scheme)

    return {
        "numer_karty": card_number,
        "data_wazności": expiry,
        "cvv": cvv,
        "schemat": scheme,
        "bank": bank,
        "typ": card_type
    }
def generate_expiry():
    future_date = datetime.now() + timedelta(days=random.randint(365, 5 * 365))
    return future_date.strftime("%m/%y")

def generate_cvv(scheme):
    if scheme.lower() == "american express":
        return f"{random.randint(1000, 9999)}"
    return f"{random.randint(100, 999)}"

def get_card_length(scheme: str) -> int:
     match scheme.lower():
         case "visa":
             return random.choice([13, 16, 19])
         case "mastercard":
             return 16
         case "american express":
             return 15
         case "maestro":
             return random.choice([12, 13, 14, 15, 16, 17, 18, 19])
         case _:
             return 16

def generate_luhn_number(prefix, length=16):
    number = [int(x) for x in prefix]
    while len(number) < length - 1:
        number.append(random.randint(0, 9))
    check_digit = (10 - luhn_checksum(number + [0])) % 10
    number.append(check_digit)
    return ''.join(map(str, number))

