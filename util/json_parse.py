import json

def get_data(path):
    with open(path) as f:
        return json.load(f)