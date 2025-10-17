# Groq AI Agent

A simple AI agent powered by Groq's LLaMA models using LangChain and LanGraph. This project provides an interactive command-line interface to chat with an AI assistant.

## Features

- Interactive chat interface
- Powered by Groq's fast LLaMA 3 model (llama3-70b-8192)
- Built with LangChain and LanGraph frameworks
- Simple and lightweight design

## Prerequisites

- Python 3.8 or higher
- A Groq API key (get one at https://console.groq.com)

## Installation

1. Clone or download this project
2. Install the required dependencies:

```bash
pip install langchain-core langchain-groq langgraph python-dotenv
```

## Setup

1. Create a `.env` file in the project root directory:

```
GROQ_API_KEY=your_actual_api_key_here
```

2. Replace `your_actual_api_key_here` with your actual Groq API key

## Usage

Run the agent:

```bash
python main.py
```

Once started, you can:
- Type any message to chat with the assistant
- Ask questions or request help
- Type `exit` to quit the program

Example interaction:
```
You: What is 2 + 2?
Assistant: 2 + 2 = 4

You: Tell me a joke
Assistant: Why did the scarecrow win an award? Because he was outstanding in his field!

You: exit
```

## Configuration

You can modify the following in the code:

- **Model**: Change `model="llama3-70b-8192"` to use different Groq models:
  - `llama3-8b-8192` (faster, less capable)
  - `mixtral-8x7b-32768` (alternative option)
  
- **Temperature**: Adjust `temperature=0` for response randomness (0 = deterministic, 1 = creative)

## Project Structure

- `main.py` - Main agent script with the chat loop
- `.env` - Environment variables (create this file with your API key)

## Dependencies

- **langchain-core** - Core LangChain functionality
- **langchain-groq** - Groq integration for LangChain
- **langgraph** - Graph-based agentic orchestration
- **python-dotenv** - Environment variable management

## Troubleshooting

**Rate limiting errors**
- Groq may rate limit requests. Wait a moment before trying again

## Future Enhancements

Possible improvements:
- Add tool integrations for web search, calculations, etc.
- Implement conversation memory/history
- Add streaming response support
- Support for multiple conversation threads

## License

This is a simple project for learning purposes.
