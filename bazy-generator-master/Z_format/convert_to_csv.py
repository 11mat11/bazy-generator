import csv

def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def write_to_csv(data, filename='output.csv'):
    flat_data = [flatten_dict(record) for record in data]

    fieldnames = []
    for row in flat_data:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flat_data)