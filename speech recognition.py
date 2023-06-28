import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Set the microphone as the audio source
microphone = sr.Microphone()

# Adjust the microphone for normal noise levels
with microphone as source:
    r.adjust_for_ambient_noise(source)

# Continuously listen for audio and perform speech recognition
print("Listening...")

flag = True

while flag:
    # Start the microphone input
    with microphone as source:
        # Use the recognizer to listen for speech
        audio = r.listen(source)

    try:
        # Perform speech recognition on the captured audio
        text = r.recognize_google(audio)
        print("Recognized speech:", text)

        # Ask the user to confirm if the recognized speech is correct
        print("Was the above text correct? (Yes/No)")

        while True:
            with microphone as source:

                # Listen for the user's response
                response_audio = r.listen(source)
                response_text = r.recognize_google(response_audio)

                if any(word in response_text for word in ["yes", "yeah"]):
                    print("User:", response_text) 
                    flag = False
                    break
                elif any(word in response_text for word in ["no", "nope"]):
                    print("User:", response_text)
                    print("Capturing audio again...")
                    break
                else:
                    print("User:", response_text)
                    print("Invalid Answer, Capturing audio again...")
                    break
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio, Capturing audio again")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))