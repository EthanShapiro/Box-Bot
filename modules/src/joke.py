from utilities import dataRetreiver as dR

JOKE_LOCATION = '/data/jokes.json'


def process(user_input):
    joke = dR.get_single_random(JOKE_LOCATION)
    if not joke:
        joke = "I'm sorry, we don't currently have any jokes"

    return joke
