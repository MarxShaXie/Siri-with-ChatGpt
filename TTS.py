import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

text_to_speech("Hello, how are you?")

# Prompt user for text input and convert to speech
while True:
    text = input("Enter text (or 'q' to quit): ")
    if text.lower() == 'q':
        break
    text_to_speech(text)

# Cleanup the engine
engine.stop()
engine.runAndWait()