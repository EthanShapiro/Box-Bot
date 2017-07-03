from utilities import dataRetreiver as dR

COMMANDS_LOCATION = 'C:/Users/Ethan/Documents/GitHub/Box-Bot/data/quotes.json'


def process(user_input):
    commands = dR.get_data(COMMANDS_LOCATION)
    return commands
