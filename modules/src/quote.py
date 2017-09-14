from utilities import dataRetreiver as dR

QUOTES_LOCATION = '/data/quotes.json'


def process(user_input):
    quote = dR.get_single_random(QUOTES_LOCATION)
    if not quote:
        quote = "Sorry, no quotes today!"
    return quote
