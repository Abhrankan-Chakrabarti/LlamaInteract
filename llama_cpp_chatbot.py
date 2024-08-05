from model_selector import *
from stream import *

if model not in [i['model'][:-7] for i in ollama.list()['models']]:
    # Create a new Llama object
    ollama.create(model=model, modelfile=f'FROM {file}')

def mode_selector():
    console = Console(width=59, height=30)
    while True:
    	text = (
    	    'Select a mode'
    	)

    	options = {1: 'Terminal mode', 2: 'Web App mode'}
    	starting_menu = Menu(text, options, console)
    	starting_menu.print_menu()
    	starting_menu.print_options()
    	a = starting_menu.choice()

    	if a == 1:
    		import terminal
    		return terminal
    	elif a == 2:
    		import app
    		return app

selected_mode = mode_selector()
selected_mode.main(model=model, stream=stream)