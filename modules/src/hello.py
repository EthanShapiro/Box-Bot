from utilities import dataRetreiver as dR

GREETINGS_LOCATION = 'C:/Users/Ethan/Documents/GitHub/Box-Bot/data/greetings.json'


def process(user_input):
    greeting = dR.get_single_random(GREETINGS_LOCATION)
    return greeting
