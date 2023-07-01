import speech_recognition as sr
import pyttsx3
import openai

# Set up your OpenAI API credentials
openai.api_key = 'api key'

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

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Create a recognizer instance
r = sr.Recognizer()

# Set the microphone as the audio source
microphone = sr.Microphone()

# Adjust the microphone for normal noise levels
with microphone as source:
    r.adjust_for_ambient_noise(source)

# Continuously listen for audio and perform speech recognition
text_to_speech("Listening...")

flag = True

while flag:
    # Start the microphone input
    with microphone as source:
        # Use the recognizer to listen for speech
        audio = r.listen(source)

    try:
        # Perform speech recognition on the captured audio
        text = r.recognize_google(audio)
        text_to_speech("Recognized speech:")
        text_to_speech(text)

        while True:
            with microphone as source:

                # Ask the user to confirm if the recognized speech is correct
                text_to_speech("Was the above text correct?")

                # Listen for the user's response
                response_audio = r.listen(source)
                response_text = r.recognize_google(response_audio)

                if any(word in response_text for word in ["yes", "yeah"]): 
                    flag = False
                    break
                elif any(word in response_text for word in ["no", "nope"]):
                    text_to_speech("Capturing audio again...")
                    break
                else:
                    text_to_speech("Invalid Answer, Please answer again")
                    continue
    except sr.UnknownValueError:
        text_to_speech("Speech recognition could not understand audio, Capturing audio again")
    except sr.RequestError as e:
        text_to_speech("Could not request results from speech recognition service; {0}".format(e))

answer=ask_question(text)

text_to_speech("Here's what ChatGpt says:")
text_to_speech(answer)