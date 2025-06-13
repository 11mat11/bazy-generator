CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    pesel TEXT,
    plec TEXT
);


CREATE TABLE contact_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    type TEXT NOT NULL,
    value TEXT NOT NULL
);


CREATE TABLE credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    card_number TEXT NOT NULL,
    expiry_date TEXT NOT NULL,
    cvv TEXT NOT NULL,
    scheme TEXT NOT NULL,
    bank TEXT NOT NULL,
    card_type TEXT NOT NULL
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

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Ignacy', 'Nowak', '09081707297', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 796 887 390');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 737 863 809');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 889 203 243');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'ignacynowak28@gmail.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'ignacynowak2025@aol.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'ignacynowak@aol.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5456022697959882', '07/28', '489', 'MASTERCARD', 'BANK MILLENNIUM, S.A.', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '76-124', 'Gwiazdowo', '84 (F)', 'Urocza (F)', 'Zachodniopomorskie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Dawid', 'Gürbüz', '16131731555', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 883 509 441');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'dawid.gürbüz@hotmail.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5577005883590664', '01/29', '299', 'MASTERCARD', 'ERZSEBET UTALVANYFORGALMAZO ZRT. (EUF)', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5294740660083028', '02/29', '147', 'MASTERCARD', 'SANTANDER CONSUMER BANK, S.A.', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5472808660920806', '08/27', '115', 'MASTERCARD', 'CREDIT AGRICOLE BANK POLSKA SPOLKA AKCYJNA', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '52-292 (F)', 'Radomsko (F)', '08 (F)', 'Makowa (F)', 'Dolnośląskie (F)');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Tymon', 'Leszkoven', '10120818476', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 668 666 447');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'tymonleszkoven83@protonmail.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'tymon.leszkoven1917@msn.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4550659323957562', '11/29', '820', 'VISA', 'ING BANK SLASKI, S.A.', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5477017275652680', '09/29', '408', 'MASTERCARD', 'BANK OCHRONY SRODOWISKA S.A. (BOS S.A.)', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '43-394', 'Rudzica', '528 (F)', 'Mała Rudzica', 'Śląskie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Jan', 'Wiśniewski', '42121665276', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 602 501 318');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 667 514 824');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'jan.wiśniewski@msn.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'jan.wiśniewski@gmail.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'janwiśniewski1993@outlook.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4107878946733691', '11/28', '929', 'VISA', 'BNP PARIBAS BANK POLSKA, S.A.', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '64-111 (F)', 'Piła (F)', '938 (F)', 'Gołębia (F)', 'Podlaskie (F)');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Tymoteusz', 'Andrysewicz', '75102036752', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 723 621 564');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 796 382 412');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 518 504 456');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'tymoteusz.andrysewicz@aol.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'tymoteusz.andrysewicz1915@msn.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'tymoteusz.andrysewicz1983@gmail.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '676485058414047505', '02/27', '394', 'MAESTRO', 'BANK BPH SPOLKA AKCYJNA', 'DEBIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4063282012131', '10/28', '358', 'VISA', 'BANK POLSKA KASA OPIEKI S.A. (BANK PEKAO SA)', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '32-733', 'Ujazd', '89', 'Wodna (F)', 'Małopolskie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Stanisław', 'Rządca', '95100256875', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 574 814 780');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 530 194 547');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 603 230 560');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'stanisławrządca@aol.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'stanisław.rządca61@hotmail.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'stanisławrządca@live.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4168565658760568', '04/30', '410', 'VISA', 'BANK MILLENNIUM SPOLKA AKCYJNA', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4478411378285433568', '08/26', '870', 'VISA', 'BANK POLSKA KASA OPIEKI S.A. (BANK PEKAO SA)', 'DEBIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '11-001', 'Barkweda', '58 (F)', 'Sokola (F)', 'Warmińsko-mazurskie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Antonina', 'Tartak', '98082611344', 'K');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 608 779 904');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 579 744 688');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'antoninatartak2028@mail.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'antoninatartak@protonmail.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5481970159953125', '03/29', '432', 'MASTERCARD', 'BANK POLSKA KASA OPIEKI S.A. - (BANK PEKAO S.A.)', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '08-111', 'Izdebki-Kośmidry', '94 (F)', 'Porzeczkowa (F)', 'Mazowieckie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Bartłomiej', 'Kaliszuk', '42062481977', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 786 860 767');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 733 799 728');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'bartłomiej.kaliszuk1913@mail.ru');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5530849135086633', '08/29', '851', 'MASTERCARD', 'BANK MILLENNIUM S.A.', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '76-021', 'Jadwiżyn', '073 (F)', 'Lwowska (F)', 'Zachodniopomorskie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Jadwiga', 'Frynia', '75133009284', 'K');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 691 889 155');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 790 878 826');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 739 437 756');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'jadwiga.frynia66@hotmail.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4466555921943355', '11/26', '793', 'VISA', 'BANK ZACHODNI WBK, S.A.', 'DEBIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5471061073825763', '02/30', '338', 'MASTERCARD', 'BANK DNB NORD POLSKA SA', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '08-330', 'Buczyn Dworski', '07/35 (F)', 'Kolejowa (F)', 'Mazowieckie');

INSERT INTO person (imie, nazwisko, pesel, plec) VALUES ('Franciszek', 'Al-mashhadani', '30030467515', 'M');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 721 837 934');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', '+48 504 280 316');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'franciszek.al-mashhadani2330@aol.com');

INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', 'franciszek.al-mashhadani57@live.com');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '4787396328745365606', '03/29', '242', 'VISA', 'BANK MILLENNIUM SPOLKA AKCYJNA', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5578951069345994', '02/27', '461', 'MASTERCARD', 'MBANK, S.A.', 'CREDIT');

INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES (LAST_INSERT_ROWID(), '5521856896320102', '06/26', '762', 'MASTERCARD', 'BANK BPH SPOLKA AKCYJNA', 'CREDIT');

INSERT INTO adres (person_id, kod, miasto, numer, ulica, wojewodztwo) VALUES (LAST_INSERT_ROWID(), '19-400', 'Plewki', '38', 'Cyprysowa (F)', 'Warmińsko-mazurskie');