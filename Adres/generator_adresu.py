import random
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def losuj_wspolrzedne():
    lat = round(random.uniform(49.0, 54.9), 6)
    lon = round(random.uniform(14.1, 24.2), 6)
    return lat, lon

def reverse_geocode(lat, lon):
    geolocator = Nominatim(user_agent="polish_address_generator")
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True, language='pl', addressdetails=True)
        if not location or not location.raw.get("address"):
            return "Nie znaleziono adresu"

        addr = location.raw["address"]
        ulica = addr.get("road", "brak ulicy")
        numer = addr.get("house_number", "brak numeru")

        return f"ul. {ulica} {numer}"

    except GeocoderTimedOut:
        return "Błąd geokodowania (timeout)"

# Przykład użycia
lat, lon = losuj_wspolrzedne()
adres = reverse_geocode(lat, lon)

print(f"Współrzędne: {lat}, {lon}")
print(f"Najbliższy adres: {adres}")
