from web_browser import youtube
from web_browser import google
from web_browser import monkey_type
from web_browser import chatgpt

from speak import speak
import requests


def check_open_or_not():
    r = requests.get("https://www.youtube.com", timeout=5)
    print("YouTube is reachable:", r.status_code)

driver = None

def browser(text):

    if "youtube" in text:
        youtube()

    elif "google" in text:
        google()

    elif "monkey type" in text:
        monkey_type()
        

    elif "chatgpt" in text:
        chatgpt()

    elif "github" in text:
        # TODO: Open GitHub with Selenium
        print("----Github opened----")
        speak("GitHub opened")

    elif "gemini" in text:
        # TODO: Open Gemini with Selenium
        print("----Gemini opened----")
        speak("Gemini opened")
