import csv 
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
    