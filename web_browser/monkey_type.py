from listen import listen
from speak import speak

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def monkey_type():

    driver = webdriver.Chrome()
    print("COMING HERE")
    driver.get("https://monkeytype.com/")
    speak("Monkey type opened")