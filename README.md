# LlamaInteract

**LlamaInteract** is a versatile, AI-powered platform developed by *The Vanguards*, offering both terminal and web-based interfaces for dynamic, real-time AI interactions. This project is designed for flexibility, enabling users to easily switch between different language models and experience immediate response streaming.

## Features

- **Dual Interface Flexibility**: Interact via Terminal Interface or through a user-friendly Web Application.
- **Real-Time Streaming**: Immediate feedback and interaction using Server-Sent Events (SSE).
- **Dynamic Model Integration**: Easily switch between models without extensive reconfiguration.
- **Modular Design**: Structured for easy maintenance and future enhancements.

## Technology Stack

- **Python**: Core programming language.
- **Flask**: Framework for the web application.
- **Ollama**: Library for model interactions and streaming.
- **HTML/CSS/JavaScript**: For building and styling the web interface.
- **Server-Sent Events (SSE)**: For real-time communication between server and client.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Abhrankan-Chakrabarti/LlamaInteract.git
    cd LlamaInteract
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Web Application**:
    ```bash
    python app.py
    ```
    Visit `http://127.0.0.1:5000` in your browser.

4. **Run the Terminal Interface**:
    ```bash
    python terminal.py
    ```

## Usage

- **Terminal Mode**:
  - Run `terminal.py` and follow the prompts to interact with the AI model directly through the terminal.
  - Type `exit` to quit the terminal mode.

- **Web App Mode**:
  - Start the web server using `app.py` and interact through the browser interface.
  - Input your queries and receive real-time responses directly on the webpage.

## Contributing

We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request with your improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Abhrankan Chakrabarti**
- **The Vanguards** Team