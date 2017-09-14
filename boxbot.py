from utilities import speak, dataRetreiver
from utilities import inputManager as input_manager
from modules import src
import pkgutil


commands_with_description = dataRetreiver.get_data('/data/commands.json')  # Get commands with descriptions

modules = []
for importer, modname, ispkg in pkgutil.iter_modules(src.__path__):
    m = importer.find_module(modname).load_module(modname)
    modules.append(m)

commands_modules = dict(zip(sorted(commands_with_description.keys()), modules))
print(commands_modules)

while True:
    response = input_manager.get_string_input()
    command, extras = input_manager.analyze_input(response, commands_with_description.keys())

    if not command:
        print("I'm sorry, I don't know that command.\n"
              "Type help to see the list of commands")
    else:
        text = commands_modules[command].process(extras)
        speak.say_text(text)
