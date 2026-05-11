from date_time import date_time
from web_browser import web_browser
from home_related_things import things

import speech_recognition as sr
import pyttsx3

#tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120)

#stt statement
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    text = r.recognize_google(audio)
    print("USER SPOKE: " + text)

    return text

text = listen()

date_time(text)
web_browser(text, listen)
things(text)

engine.runAndWait()
