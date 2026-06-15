from speak import speak
from selenium import webdriver

def monkey_type():

    driver = webdriver.Chrome()
    print("COMING HERE")
    driver.get("https://monkeytype.com/")
    speak("Monkey type opened")