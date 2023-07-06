import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        r.adjust_for_ambient_noise(source)
    
    with microphone as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio, Capturing audio again")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))