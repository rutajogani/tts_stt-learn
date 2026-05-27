from listen import listen
from speak import speak
from date_time import date_time
from web_browser import web_browser
from home_related_things import things
from password import password
from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium
driver = webdriver.Chrome()
driver.quit()

if "youtube" in text.lower():
    driver.get("https://youtube.com")
    engine.say("Opening YouTube")
    engine.runAndWait()

# engine = pyttsx3.init()
# engine.setProperty('rate', 120) 
# text = listen()
# speak(text)

# password()
# date_time(text)
# web_browser(text)
# things(text)
