from youtube import youtube


from listen import listen
from speak import speak
#import webbrowser as web
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time


def check_open_or_not():
    r = requests.get("https://www.youtube.com", timeout=5)
    print("YouTube is reachable:", r.status_code)

driver = None


def web_browser(text): # web browser function

    if "youtube" in text:
        youtube()
        
    elif "google" in text:

        if "search" in text:

            print("Speak what you want to search: ")
            what_to_search = listen()
            searching = f"http://www.google.com/search?q={what_to_search}"
            web.open(searching)
            engine.runAndWait()
            break

        web.open("https://www.google.com/")
        print("----Google opened----")
        engine.say("Google opened")
        engine.runAndWait()
        break

    elif "monkey type" in text:

        web.open("https://monkeytype.com/")
        print("----MonkeyType opened----")
        engine.say("MonkeyType opened")
        engine.runAndWait()
        break

    elif "chatgpt" in text:

        web.open("https://chatgpt.com/")
        print("----Chatgpt opened----")
        engine.say("Chatgpt opened")
        engine.runAndWait()
        break

    elif "github" in text:

        web.open("https://github.com/rutajogani")
        print("----Github opened----")
        engine.say("Github opened")
        engine.runAndWait()
        break

    elif "gemini" in text:

        web.open("https://gemini.google.com/app")
        print("----Gemini opened----")
        engine.say("Gemini opened")
        engine.runAndWait()
        break

    # elif "exit" in command:
    #     if driver:
    #         driver.quit()
    #         break