from utilities import dataRetreiver as dR

GREETINGS_LOCATION = '/data/greetings.json'

def process(user_input):
    greeting = dR.get_single_random(GREETINGS_LOCATION)
    if not greeting:
        greeting = "I'm sorry, not greetings currently"

    return greeting
