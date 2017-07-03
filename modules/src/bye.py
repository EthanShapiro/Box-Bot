from utilities import dataRetreiver as dR

SALUTATION_LOCATION = 'C:/Users/Ethan/Documents/GitHub/Box-Bot/data/salutations.json'


def process(user_input):
    salutation = dR.get_single_random(SALUTATION_LOCATION)
    return salutation
