from web_browser import youtube
from web_browser import google

import webbrowser as web
from listen import listen
from speak import speak
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests


def check_open_or_not():
    r = requests.get("https://www.youtube.com", timeout=5)
    print("YouTube is reachable:", r.status_code)

driver = None


def browser(text): # web browser function

    if "youtube" in text:
        youtube(text)

    elif "google" in text:
        google()


    elif "monkey type" in text:

        web.open("https://monkeytype.com/")
        print("----MonkeyType opened----")
        engine.say("MonkeyType opened")
        engine.runAndWait()
        

    elif "chatgpt" in text:

        web.open("https://chatgpt.com/")
        print("----Chatgpt opened----")
        engine.say("Chatgpt opened")
        engine.runAndWait()
        

    elif "github" in text:

        web.open("https://github.com/rutajogani")
        print("----Github opened----")
        engine.say("Github opened")
        engine.runAndWait()
        

    elif "gemini" in text:

        web.open("https://gemini.google.com/app")
        print("----Gemini opened----")
        engine.say("Gemini opened")
        engine.runAndWait()
        

    # elif "exit" in command:
    #     if driver:
    #         driver.quit()
    #         break