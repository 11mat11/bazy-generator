import json
from faker import Faker
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut
import random

fake = Faker("pl_PL")
geolocator = Nominatim(user_agent="adres-generator")

WOJEWODZTWA = [
    "Dolnośląskie", "Kujawsko-Pomorskie", "Lubelskie", "Lubuskie",
    "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie",
    "Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie", "Warmińsko-Mazurskie",
    "Wielkopolskie", "Zachodniopomorskie"
]

def losuj_wspolrzedne():
    lat = random.uniform(49.0, 54.9)
    lon = random.uniform(14.1, 24.2)
    return lat, lon

def sformatuj_wojewodztwo(nazwa):
    if nazwa.lower().startswith("województwo "):
        return nazwa[12:].capitalize()
    return nazwa.capitalize()

def pobierz_adres_z_api(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True, language="pl", addressdetails=True)
        if not location or not location.raw.get("address"):
            return None

        dane = location.raw["address"]
        if dane.get("country_code", "") != "pl":
            return None  # Adres spoza Polski

        return {
            "wojewodztwo": sformatuj_wojewodztwo(dane.get("state", "")),
            "miasto": dane.get("city", dane.get("town", dane.get("village", ""))),
            "ulica": dane.get("road", ""),
            "numer": dane.get("house_number", ""),
            "kod": dane.get("postcode", "")
        }
    except (GeocoderUnavailable, GeocoderTimedOut):
        return None

def uzupelnij_adres(adres):
    zrodla = {}

    if not adres.get("wojewodztwo"):
        adres["wojewodztwo"] = random.choice(WOJEWODZTWA)
        zrodla["wojewodztwo"] = "F"
    else:
        zrodla["wojewodztwo"] = ""

    if not adres.get("miasto"):
        adres["miasto"] = fake.city()
        zrodla["miasto"] = "F"
    else:
        zrodla["miasto"] = ""

    if not adres.get("ulica"):
        adres["ulica"] = fake.street_name()
        zrodla["ulica"] = "F"
    else:
        zrodla["ulica"] = ""

    if not adres.get("numer"):
        adres["numer"] = fake.building_number()
        zrodla["numer"] = "F"
    else:
        zrodla["numer"] = ""

    if not adres.get("kod"):
        adres["kod"] = fake.postcode()
        zrodla["kod"] = "F"
    else:
        zrodla["kod"] = ""

    return adres, zrodla

def generuj_adres(wybierz_elementy=None, z_f=False):
    # Zbiór dostępnych danych
    lat, lon = losuj_wspolrzedne()
    adres = pobierz_adres_z_api(lat, lon)

    if adres is None:
        adres = {}
    adres, zrodla = uzupelnij_adres(adres)

    # Filtracja na podstawie elementów do wyboru
    if wybierz_elementy:
        # Jeśli lista wyboru jest pusta, zwróci cały adres
        adres = {key: value for key, value in adres.items() if key in wybierz_elementy}
        zrodla = {key: value for key, value in zrodla.items() if key in wybierz_elementy}

    def oznacz(wartosc, zrodlo):
        return f"{wartosc} (F)" if zrodlo == "F" and z_f else wartosc

    # Przygotowanie JSON-a
    adres_json = {}
    for key, value in adres.items():
        if value:
            adres_json[key] = oznacz(value, zrodla.get(key, ""))

    return json.dumps(adres_json, ensure_ascii=False, indent=4)

# Przykład użycia:
# 1. Jeśli użytkownik chce generować tylko ulice i miasto:
print(generuj_adres(wybierz_elementy=["ulica", "miasto","wojewodztwo","numer", "kod"]))

# 3. Z opcją dodania literki (F) do danych wygenerowanych przez Faker:
print(generuj_adres(z_f=True))

