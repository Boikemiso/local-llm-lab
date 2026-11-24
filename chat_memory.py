import ollama
import json
import os

# --- PART 1: Load previous conversation ---
history_file = "chat_history.json"
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor. Keep answers concise.",
    }
]

if os.path.exists(history_file):
    with open(history_file, "r") as file:
        messages = json.load(file)

    print("Previous conversation loaded!")

else:
    print("Starting a new conversation!")

# --- PART 2: Chat with the local AI ---

print("\nLocal AI conversation started!")
print("Type 'exit' to end the conversation.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Conversation ended.")
        break
    if question.lower() == "/clear":
        messages = [
            {
                "role": "system",
                "content": "You are a helpful Python tutor. Keep answers concise.",
            }
        ]

        if os.path.exists(history_file):
            os.remove(history_file)

        print("Conversation history cleared!\n")
        continue

    messages.append({"role": "user", "content": question})

    response = ollama.chat(model="llama3.2:3b", messages=messages)

    answer = response["message"]["content"]

    print(f"AI: {answer}\n")

    messages.append({"role": "assistant", "content": answer})

    # --- PART 3: Save conversation ---
    # w mode creates the file if doesn't exist
    with open(history_file, "w") as file:
        json.dump(messages, file, indent=4)

    print("Conversation saved!")
