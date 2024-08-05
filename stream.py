import ollama

def stream(input, model):
    """Evaluate the input using the llama model"""
    completion = ollama.chat(
    model=model,
    messages=[{'role': 'user', 'content': input}],
    stream=True,
    )
    for chunk in completion:
        yield chunk['message']['content']