from utilities import dataRetreiver as dR

QUOTES_LOCATION = 'C:/Users/Ethan/Documents/GitHub/Box-Bot/data/quotes.json'


def process(user_input):
    quote = dR.get_single_random(QUOTES_LOCATION)
    return quote
