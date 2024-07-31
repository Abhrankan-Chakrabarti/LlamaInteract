from console_explorer import *

file = browse_for_file(extensions_list=('gguf',))
model = file.split(sep)

import ollama

# Create a new Llama object
ollama.create(model=model, modelfile=f'FROM {file}')

# REPL loop
while True:
    # Read user input
    user_input = input(">> ")

    # Check for exit command
    if user_input.lower() == "exit":
        break

    try:
        # Evaluate the input using the llama model
        stream = ollama.chat(
    model=model,
    messages=[{'role': 'user', 'content': user_input}],
    stream=True,
)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        print()
    except BaseException as e:
        print("\n" + repr(e).split("(")[0] + (":" if str(e) else ""), e)