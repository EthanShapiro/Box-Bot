from utilities import dataRetreiver as dR

SALUTATION_LOCATION = '/data/salutations.json'


def process(user_input):
    salutation = dR.get_single_random(SALUTATION_LOCATION)
    if not salutation:
        salutation = "I'm sorry, we don't have a goodbye for you."

    return salutation
