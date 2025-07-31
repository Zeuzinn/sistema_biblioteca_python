import json
import os

DATA_DIR = 'data'

def save_to_json(data, filename):
    os.makedirs(DATA_DIR, exist_ok= True)   # cria pasta se não existir
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'w', encoding='UTF-8') as file_:
        json.dump(data, file_, indent=4, ensure_ascii= False)

def load_from_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file_:
        return json.load(file_)