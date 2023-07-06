import openai

def set_api_key(api_key_file):
    with open(api_key_file, "r") as file:
        api_key = file.read().strip()
    openai.api_key = api_key

def ask_question(question):
    prompt = f"{question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].text.strip().split('\n')[0]
    return answer