from utilities import dataRetreiver as dR

COMMANDS_LOCATION = '/data/commands.json'


def process(user_input):
    commands = dR.get_data(COMMANDS_LOCATION)
    if not commands:
        commands = "Sorry, no commands implemented"

    return commands
