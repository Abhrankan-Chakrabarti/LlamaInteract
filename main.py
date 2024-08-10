from model_selector import *
from stream import *

# Ensure the model is available
if model not in [i['model'][:-7] for i in ollama.list()['models']]:
    # Create a new Llama object
    ollama.create(model=model, modelfile=f'FROM {file}')