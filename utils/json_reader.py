import json
import os

def load_json(file_name):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", file_name)
    with open(file_path, "r") as file:
        return json.load(file)
