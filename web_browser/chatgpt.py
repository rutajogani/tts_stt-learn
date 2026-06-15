from speak import speak
from selenium import webdriver

def chatgpt():

    driver = webdriver.Chrome()
    print("COMING HERE")
    driver.get("https://chatgpt.com/")
    speak("Chatgpt opened")