import json
from random import sample, choice
from os import path

base_path = path.dirname(path.dirname(__file__)).replace('\\', '/')


def get_data(f_location):
    full_file_path = base_path + f_location
    with open(full_file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            return None
        else:
            return data


def save_data(f_location, data):
    full_file_path = base_path + f_location
    data = json.dumps(data, indent=0, separators=(',', ':'))
    with open(full_file_path, 'w') as file:
        file.writelines(data)


def get_single_random(f_location):
        data = get_data(f_location)
        if type(data) == dict:
            return sample(data.items(), 1)
        elif type(data) == list:
            return choice(data)


