import openai

openai.api_key = "api-key"
model_engine = "text-davinci-003" 

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"},
    ])

message = response.choices[0]['message']
print("{}: {}".format(message['role'], message['content']))
