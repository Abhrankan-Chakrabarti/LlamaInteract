def terminal(model, stream):
    # Read user input
    user_input = input(">> ")

    # Validate the input
    if not user_input:
        return

    # Check for exit command
    if user_input.lower() == "exit":
        return True

    try:
        response = stream(input=user_input, model=model)
        for res in response:
            print(res, end='', flush=True)
        print()
    except BaseException as e:
        print("\n" + repr(e).split("(")[0] + (":" if str(e) else ""), e)

def main(model, stream):
    """REPL loop"""
    exit_cmd = None
    while not exit_cmd:
        exit_cmd = terminal(model, stream)

if __name__ == '__main__':
    from main import *
    main(model=model, stream=stream)