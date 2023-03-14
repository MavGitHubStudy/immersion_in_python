import json
import os
from pathlib import Path


def get_form_user(file: Path) -> None:
    json_file = {}
    all_id = set()
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)
        all_id.update(
            *((value.keys()) for key, value in json_file.items()))

    while True:
        value, user_id, name = input(">>> ").split()
        if user_id in all_id:
            print("Такой id уже есть.")
            continue
        else:
            json_file[value].update({int(user_id): name})
            with open(file, 'w+', encoding='utf-8') as f:
                print(json_file)
                json.dump(json_file, f, indent=2)