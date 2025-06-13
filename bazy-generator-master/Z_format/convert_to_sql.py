import json
from collections import defaultdict


def escape_sql(_val):
    if _val is None:
        return 'NULL'
    return "'" + str(_val).replace("'", "''") + "'"


def write_to_sql(data):
    # Identify fields dynamically
    root_fields = set()
    nested_fields = defaultdict(set)

    for record in data:
        for key, value in record.items():
            if key == '_address_mode':
                continue
            if isinstance(value, dict):
                # nested object
                for nk in value.keys():
                    nested_fields[key].add(nk)
            elif key == 'adres':
                # address may be JSON string
                try:
                    addr = json.loads(value)
                    for nk in addr.keys():
                        nested_fields['adres'].add(nk)
                except Exception:
                    root_fields.add(key)
            elif key in ['telefon', 'email', 'karta_kredytowa']:
                # Skip these fields from root as they'll have their own tables
                continue
            else:
                root_fields.add(key)

    # Generate SQL
    sql_statements = []

    # Main table
    main_table = 'person'
    cols = ['id INTEGER PRIMARY KEY AUTOINCREMENT']
    for f in sorted(root_fields):
        cols.append(f + ' TEXT')
    sql_statements.append(f"CREATE TABLE {main_table} (\n    " + ",\n    ".join(cols) + "\n);")

    # Contact information table
    sql_statements.append("""
CREATE TABLE contact_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    type TEXT NOT NULL,
    value TEXT NOT NULL
);""")

    # Credit cards table
    sql_statements.append("""
CREATE TABLE credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES person(id),
    card_number TEXT NOT NULL,
    expiry_date TEXT NOT NULL,
    cvv TEXT NOT NULL,
    scheme TEXT NOT NULL,
    bank TEXT NOT NULL,
    card_type TEXT NOT NULL
);""")

    # Nested tables (for address)
    for table, fields in nested_fields.items():
        tbl_name = table
        cols = ['id INTEGER PRIMARY KEY AUTOINCREMENT', f"person_id INTEGER REFERENCES {main_table}(id)"]
        for f in sorted(fields):
            cols.append(f + ' TEXT')
        sql_statements.append(f"CREATE TABLE {tbl_name} (\n    " + ",\n    ".join(cols) + "\n);")

    # Inserts
    sql_statements.append('-- Inserts')
    for record in data:
        # insert into person
        values = []
        for f in sorted(root_fields):
            val = record.get(f)
            if f == 'adres':
                # skip address string insertion in main
                values.append('NULL')
            else:
                values.append(escape_sql(val))
        sql_statements.append(
            f"INSERT INTO {main_table} (" + ", ".join(sorted(root_fields)) + ") VALUES (" + ", ".join(values) + ");"
        )

        # Insert contact information
        if 'telefon' in record and record['telefon']:
            for phone in record['telefon']:
                sql_statements.append(
                    f"INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'phone', {escape_sql(phone)});"
                )
        
        if 'email' in record and record['email']:
            for email in record['email']:
                sql_statements.append(
                    f"INSERT INTO contact_info (person_id, type, value) VALUES (LAST_INSERT_ROWID(), 'email', {escape_sql(email)});"
                )

        # Insert credit cards
        if 'karta_kredytowa' in record and record['karta_kredytowa']:
            for card in record['karta_kredytowa']:
                sql_statements.append(
                    f"INSERT INTO credit_cards (person_id, card_number, expiry_date, cvv, scheme, bank, card_type) VALUES ("
                    f"LAST_INSERT_ROWID(), "
                    f"{escape_sql(card['numer_karty'])}, "
                    f"{escape_sql(card['data_wazności'])}, "
                    f"{escape_sql(card['cvv'])}, "
                    f"{escape_sql(card['schemat'])}, "
                    f"{escape_sql(card['bank'])}, "
                    f"{escape_sql(card['typ'])});"
                )

        # Insert address
        for key in nested_fields.keys():
            tbl_name = key
            nested = record.get(key)
            if key == 'adres' and isinstance(nested, str):
                nested = json.loads(nested)
            if nested:
                cols = sorted(nested_fields[key])
                vals = []
                for f in cols:
                    v = nested.get(f)
                    vals.append(escape_sql(v))
                sql_statements.append(
                    f"INSERT INTO {tbl_name} (person_id, " + ", ".join(cols) + ") VALUES (LAST_INSERT_ROWID(), " + ", ".join(vals) + ");"
                )

    with open('output.sql', 'w', encoding='utf-8') as f:
        f.write("\n\n".join(sql_statements))
