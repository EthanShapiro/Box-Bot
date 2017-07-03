def get_string_input():
    response = input('(type help to hear a list of the commands)\nPlease enter a command: ')
    return response

def analyze_input(response, commands):
    """
    take a response and commands and check to see whether the response
    contains any of the commands
    :param response:
    :param commands:
    :return command, extras:
    """

    def words_are_similar(word1, word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1) == sorted(word2)

    response = response.split()
    command = None
    extras = None   # Anything after the command that is needed for the module to process
    for i, word in enumerate(response):
        if word in commands.keys():
            command = word
            extras = response[i+1:]
        else:
            for c in commands.keys():
                if words_are_similar(c, word):  # The user may have mistyped, check for similar words
                    command = c
                    extras = response[i+1:]

    return command, extras
