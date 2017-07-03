import json
from random import sample, choice


def get_data(f_location):
    with open(f_location, 'r') as file:
        return json.load(file)


def save_data(f_location, data):
    data = json.dumps(data, indent=0, separators=(',', ':'))
    with open(f_location, 'w') as file:
        file.writelines(data)


def get_single_random(f_location):
    with open(f_location, 'r') as file:
        data = json.load(file)
        if type(data) == dict:
            return sample(data.items(), 1)
        elif type(data) == list:
            return choice(data)
