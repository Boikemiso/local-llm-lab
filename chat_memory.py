import ollama
import json
import os

# --- PART 1: Load previous conversation ---
history_file = "chat_history.json"
# Default system rules for a fresh conversation
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor. Keep answers concise.",
    }
]

# If the history file exists, load saved messages, otherwise start fresh
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        # loads saved messages
        messages = json.load(file)

    print("Previous conversation loaded!")

else:
    print("Starting a new conversation!")

# --- PART 2: Chat with the local AI ---

print("\nLocal AI conversation started!")
print("Type 'exit' to end the conversation.\n")

while True:
    question = input("You: ")  # Reads what the user types

    if question.lower() == "exit":  # Case insensitive check to stop the loop
        print("Conversation ended.")
        break
    if (
        question.lower() == "/clear"
    ):  # Resets chatbot's saved conversation history and delete saved file, then keep looping
        messages = [
            {
                "role": "system",
                "content": "You are a helpful Python tutor. Keep answers concise.",
            }
        ]

        if os.path.exists(history_file):
            os.remove(history_file)

        print("Conversation history cleared!\n")
        continue  # Skip to the next loop cycle

    messages.append(
        {"role": "user", "content": question}
    )  # Add user message to list in memory

    response = ollama.chat(
        model="llama3.2:3b", messages=messages
    )  # Send full chat history to model

    answer = response["message"]["content"]  # Pull out just the reply text

    print(f"AI: {answer}\n")

    messages.append(
        {"role": "assistant", "content": answer}
    )  # Saves model reply in memory for next turn

    # --- PART 3: Save conversation ---
    # Write the updated list to disk ("w" creates the file or overwrites old contents)
    with open(history_file, "w") as file:
        json.dump(messages, file, indent=4)

    print("Conversation saved!")

# Common open() modes:

# "r" — read mode (default; raises FileNotFoundError if missing).

# "w" — write mode (creates or overwrites).

# "a" — append mode (creates or adds to the end without erasing existing text).
