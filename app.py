import ollama

# This is a list of questions to test the model
questions = [
    "What is the capital of South Africa?",
    "Explain Python in one sentence.",
    "What is 2 + 2?",
]

print("Starting the local AI test")

# Loop through each question string in the list
for q in questions:
    print(f"Question: {q}")  # Displays the current question

    try:
        # This sends the prompt to the local Ollama instance
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                # The "system" role provides instructions for the AI's behavior,
                # while the "user" role contains the question or message being sent to the AI.
                {
                    "role": "system",  # Sets rules/behavior before the user speaks
                    "content": "You are a Python tutor. Answer every question in no more than two sentences. Use simple language and avoid unnecessary details.",
                },
                {
                    "role": "user",  # Marks this message as coming from the user
                    "content": q,  # Inserts the current question from the loop
                },
            ],
        )

        print(f"Answer: {response['message']['content']}\n")

    except Exception as e:
        print(f"Error: {e}\n")
