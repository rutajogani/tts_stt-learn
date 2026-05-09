import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def date_time():  # date and time function

    now_date = datetime.now()
    date_now = now_date.strftime("%d-%m-%Y")
    now_time = datetime.now()
    time_now = now_time.strftime("%H:%M:%S")

    date_time = ["date","time"]

    if "date" in text:
        print(date_now)
        engine.say(date_now)
        engine.say("date is here:")
        print("----Here is your Date----")

    elif "time" in text:
        print(time_now)
        engine.say("time is here:")
        print("----Here is your Time----")

engine.runAndWait()
