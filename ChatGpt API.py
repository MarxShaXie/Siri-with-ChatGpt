import openai

# Set up your OpenAI API credentials
openai.api_key = 'api-key'

def ask_question(question):
    # Define the prompt with the user's question
    prompt = f"{question}\nAnswer:"

    # Generate the response using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Extract the answer from the API response
    answer = response.choices[0].text.strip().split('\n')[0]

    return answer

# Main loop to keep asking questions until the user enters 'quit'
while True:
    user_question = input("Enter your question (or 'quit' to exit): ")
    
    if user_question.lower() == 'quit':
        break

    answer = ask_question(user_question)
    print("Answer:", answer)