import ollama

# This is a list of questions to test the model
questions = [
    "What is the capital of South Africa?",
    "Explain Python in one sentence.",
    "What is 2 + 2?",
]

print("Starting the local AI test")

for q in questions:
    print(f"Question: {q}")

    try:
        # This sends the prompt to the local Ollama instance
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python tutor. Answer every question in no more than two sentences. Use simple language and avoid unnecessary details.",
                },
                {"role": "user", "content": q},
            ],
        )

        print(f"Answer: {response['message']['content']}\n")

    except Exception as e:
        print(f"Error: {e}\n")
