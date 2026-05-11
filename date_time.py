import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def date_time():  # date and time function

    now_time, now_date = datetime.now()
    
    date_now = now_date.strftime("%d-%m-%Y")
    time_now = now_time.strftime("%H:%M:%S")

    date_time = ["date","time"]

    if "date" in text:
        print(date_now)
        engine.say("Today's date is")
        engine.say(date_now)
        engine.runAndWait()
        print("----Here is your Date----")

    elif "time" in text:
        print(time_now)
        engine.say("Current time is")
        engine.say(time_now)
        engine.runAndWait()
        print("----Here is your Time----")


