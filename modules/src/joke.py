from utilities import dataRetreiver as dR

JOKE_LOCATION = 'C:/Users/Ethan/Documents/GitHub/Box-Bot/data/jokes.json'


def process(user_input):
    joke = dR.get_single_random(JOKE_LOCATION)
    return joke
