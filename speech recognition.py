import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Set the microphone as the audio source
microphone = sr.Microphone()

# Adjust the microphone for normal noise levels
with microphone as source:
    r.adjust_for_ambient_noise(source)


print("Listening...")

# Start the microphone input
with microphone as source:
    # Use the recognizer to listen for speech
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Recognized speech:", text)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from speech recognition service; {0}".format(e))