import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser as web

#stt statement
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print("USER SPOKE: " + text)

# tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def web_browser(): # web browser function
    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT"]
    
    for web_page in list_of_web_page:
        if "YouTube" in text:
            web.open("https://www.youtube.com/")
            print("----Youtube opened----")
            engine.say("Youtube opened")
            break
        elif "Google" in text:
            web.open("https://www.google.com/")
            print("----Google opened----")
            engine.say("Google opened")
            break
        elif "monkey type" in text:
            web.open("https://monkeytype.com/")
            print("----MonkeyType opened----")
            engine.say("MonkeyType opened")
            break
        elif "chat GPT" in text:
            web.open("https://chatgpt.com/")
            print("----Chatgpt opened----")
            engine.say("Chatgpt opened")
            break

def date_time():  #date and time function

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

# things = {
#     "phone": "Here is your phone",
#     "tv": "Turning on the TV",
#     "bag": "Here is your bag"
# }

# for thing in things:
#     if thing in text:
#         print("FOUND IT")
#         engine.say(things[thing])
    
# else: 
#         print("Not Found")

engine.runAndWait()

web_browser()
date_time()
