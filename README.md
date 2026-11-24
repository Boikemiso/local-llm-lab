# Local LLM Chatbot

A simple Python chatbot powered by a locally running LLM using Ollama and the Llama 3.2 3B model.

## Features

- Connects Python to a local AI model using Ollama.
- Uses a system prompt to control the AI's personality.
- Maintains conversation context during chats.
- Saves conversation history to a JSON file.
- Loads previous conversations when restarted.
- Includes a `/clear` command to reset conversation history.

## Requirements

- Python
- Ollama
- Llama 3.2 3B model
- Python `ollama` package

## Setup

1. Install [Ollama](https://ollama.com/).
2. Download the model:

   ```bash
   ollama pull llama3.2:3b
   ```

3. Install the Python dependency:

   ```bash
   pip install ollama
   ```

4. Run the chatbot:

   ```bash
   python chat_memory.py
   ```

## Commands

- `/clear` — Clear saved conversation history.
- `exit` — End the conversation.

## Technologies

- Python
- Ollama
- Llama 3.2
- JSON

## Purpose

This project was built as a practical introduction to local LLM integration, prompt engineering, conversation memory, and persistent data storage.