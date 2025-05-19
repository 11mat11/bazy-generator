CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    imie TEXT,
    nazwisko TEXT,
    pesel TEXT,
    plec TEXT,
    telefon TEXT
);

CREATE TABLE karta_kredytowa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    bank TEXT,
    cvv TEXT,
    data_wazności TEXT,
    numer_karty TEXT,
    schemat TEXT,
    typ TEXT
);

CREATE TABLE adres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    kod TEXT,
    miasto TEXT,
    numer TEXT,
    ulica TEXT,
    wojewodztwo TEXT
);

-- Inserts

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('annasłońska2002@hotmail.com', 'Anna', 'Słońska', '42031131245', 'K', '+48 696 972 035');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BANK ZACHODNI WBK, S.A.', '515', '03/29', '4127956106121', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '92-576', 'Lubin', '40/12', 'Miłosza', 'Lubuskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('hubert.stępień52@protonmail.com', 'Hubert', 'Stępień', '85111052991', 'M', '+48 608 878 067');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BANK POLSKA KASA OPIEKI S.A. (BANK PEKAO SA)', '753', '08/29', '4478390909194', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '74-832', 'Chorzów', '00', 'Ciasna', 'Dolnośląskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('klara.czarnecka9432@hotmail.com', 'Klara', 'Czarnecka', '92120994264', 'K', '+48 735 480 228');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'ALIOR BANK SPOLKA AKCYJNA', '631', '09/26', '5575475663580387', 'MASTERCARD', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '96-281', 'Zamość', '17', 'Żabia', 'Podlaskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('emilia.szpernalowska1905@aol.com', 'Emilia', 'Szpernalowska', '80061450185', 'K', '+48 452 354 092');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BNP PARIBAS BANK POLSKA, S.A.', '413', '10/27', '5359429394475351', 'MASTERCARD', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '23-141', 'Elbląg', '65/14', 'Leszczynowa', 'Podlaskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('wojciechkidawski8084@hotmail.com', 'Wojciech', 'Kidawski', '99142315831', 'M', '+48 738 291 161');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BNP PARIBAS BANK POLSKA, S.A.', '141', '08/27', '4107870686655', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '83-596', 'Biała Podlaska', '55/84', 'Północna', 'Podlaskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('antonina.derlikiewicz@verizon.net', 'Antonina', 'Derlikiewicz', '23132397602', 'K', '+48 691 611 804');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BANK ZACHODNI WBK, S.A.', '848', '04/28', '4466549783772028', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '19-795', 'Chorzów', '670', 'Gałczynskiego', 'Świętokrzyskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('oliwiawalkusz@gmail.com', 'Oliwia', 'Walkusz', '54062281082', 'K', '+48 726 894 747');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'ING BANK SLASKI, S.A.', '250', '12/28', '4277569155637780', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '42-443', 'Ostrów Wielkopolski', '12/38', 'Swierkowa', 'Wielkopolskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('jan.strzelczak78@verizon.net', 'Jan', 'Strzelczak', '19013019958', 'M', '+48 458 852 122');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'MBANK S.A.', '720', '02/30', '5478926065339861', 'MASTERCARD', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '93-014', 'Zduńska Wola', '56/87', 'Podleśna', 'Lubelskie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('julianbiałek4554@gmail.com', 'Julian', 'Białek', '06052471456', 'M', '+48 881 150 200');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BANK MILLENNIUM SPOLKA AKCYJNA', '412', '01/29', '4277027069772', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '14-184', 'Koszalin', '53/28', 'Nowa', 'Mazowieckie');

INSERT INTO person (email, imie, nazwisko, pesel, plec, telefon) VALUES ('leon.mes@hotmail.com', 'Leon', 'Mes', '69052176974', 'M', '+48 456 356 156');

INSERT INTO karta_kredytowa (person_id, bank, cvv, data_wazności, numer_karty, schemat, typ) VALUES (LAST_INSERT_ROWID(), 'BANK POLSKA KASA OPIEKI S.A. (BANK PEKAO SA)', '967', '02/30', '4063270568158863327', 'VISA', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '39-584', 'Toruń', '42/34', 'Sienkiewicza', 'Łódzkie');