from console_explorer import *

file = browse_for_file(extensions_list=('gguf',))

import llama_cpp

# Create a new Llama object
llama_obj = llama_cpp.Llama(model_path=file, verbose=False, n_ctx=2048)

# REPL loop
while True:
    # Read user input
    user_input = input(">> ")

    # Check for exit command
    if user_input.lower() == "exit":
        break

    try:
        # Evaluate the input using the llama_obj
        tokens = llama_obj.tokenize(user_input.encode())
        for token in llama_obj.generate(tokens, top_k=40, top_p=0.95, temp=0.7, repeat_penalty=1.1):
            print(llama_obj.detokenize([token]).decode(), end="", flush=True)
        print()
    except BaseException as e:
        print("\n" + repr(e).split("(")[0] + (":" if str(e) else ""), e)