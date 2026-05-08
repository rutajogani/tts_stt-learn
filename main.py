import speech_recognition as sr
import pyttsx3
import webbrowser as web

#stt statement
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print("USER SPOKE: " + text)
    return text

text = listen()

# tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def web_browser(): # web browser function

    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT", "Gemini"]
    
    for web_page in list_of_web_page:
        if "YouTube" in text:
            if "search" in text:
                print("Speak what you search: ")
                what_to_search = listen()
                searching = f"https://www.youtube.com/results?search_query={what_to_search}"
                web.open(searching)
                break

            web.open("https://www.youtube.com/")
            print("----Youtube opened----")
            engine.say("Youtube opened")
            break

        elif "Google" in text:
            if "search" in text:
                print("Speak what you search: ")
                what_to_search = listen()
                searching = f"http://www.google.com/search?q={what_to_search}"
                web.open(searching)
                break

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

        elif "GitHub" in text:
            web.open("https://github.com/rutajogani")
            print("----Github opened----")
            engine.say("Github opened")
            break

        elif "Gemini" in text:
            web.open("https://gemini.google.com/app")
            print("----Gemini opened----")
            engine.say("Gemini opened")
            break


def things(): # Home related things 

    things = {
        "phone": "Here is your phone",
        "TV": "Turning on the TV",
        "bag": "Here is your bag",
        "fan": "Turn on your fan"
    }

    found = 0

    for thing in things:
        if thing in text:
            print("FOUND IT")
            print(things[thing])
            engine.say(things[thing])
            found = 1
            break

    if found == 0:
        print("NOT FOUND")


web_browser()
date_time()
things()

engine.runAndWait()
