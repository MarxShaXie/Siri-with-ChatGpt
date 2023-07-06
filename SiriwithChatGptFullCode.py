from ChatGptAPI import set_api_key, ask_question
from TextToSpeech import text_to_speech
from SpeechRecognition import recognize_speech

# Set up the API key
api_key_file = "C:/api_key.txt"
set_api_key(api_key_file)

# Listen for user input
text_to_speech("Listening...")
text = recognize_speech()

# Confirm the recognized text
flag = True
while flag:
    text_to_speech("Recognized speech:")
    text_to_speech(text)
    text_to_speech("Was the above text correct?")
    response_text = recognize_speech()
    
    if any(word in response_text for word in ["yes", "yeah"]): 
        flag = False
        break
    elif any(word in response_text for word in ["no", "nope"]):
        text_to_speech("Capturing audio again...")
        text = recognize_speech()
        break
    else:
        text_to_speech("Invalid answer. Please answer again.")
        continue

# Ask the question to ChatGPT API and get the answer
answer = ask_question(text)

# Output the answer
text_to_speech("Here's what ChatGpt says:")
text_to_speech(answer)