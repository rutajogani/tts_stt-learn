import speech_recognition as sr

#stt statement
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    text = r.recognize_google(audio)
    print("USER SPOKE: " + text)

    return text