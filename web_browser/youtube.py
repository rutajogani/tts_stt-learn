from listen import listen
from speak import speak
from hold import hold_web_page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


import requests
import time


def check_open_or_not():
    r = requests.get("https://www.youtube.com", timeout=5)
    print("YouTube is reachable:", r.status_code)

driver = None

def youtube():
    while True:
        global driver
        command = listen()
        
        # open youtube
        if "open" in command:
            driver = webdriver.Chrome()
            print("COMING HERE")
            hold_web_page("https://youtube.com")
            speak("youtube opened")
            
        # searching in youtube
        elif "search" in command:
            print("Is ther comeing here?")
            if driver is None:
                driver = webdriver.Chrome()
                hold_web_page("https://youtube.com")

            what_to_search = listen()
            time.sleep(3)

            if "youtube" in what_to_search:
                youtube()   

            search_box = driver.find_element(By.NAME, "search_query")
            search_box.send_keys(what_to_search)
            what_to_search = ""
            search_box.send_keys(Keys.RETURN)

            # try:

            #     if response.status_code == 200:
            #         search = driver.find_element(
            #          By.XPATH,
            #         "//input[@id='search']"
            #     )
            #         search.click(what_to_search)    
            #         speak("searching youtube")
                    
            #     else:
                    # driver = webdriver.Chrome()
                    # driver.get("https://youtube.com")
                    
                #     search = driver.find_element(
                #     By.XPATH,
                #     "//input[@id='search']"
                # )
                #     search.click(what_to_search)    
                #     speak("searching youtube")                            

            # except requests.RequestException:
            #     print("YouTube is not reachable → Do THAT")

        #close youtube 
        elif "close" in command:
            if driver:
                driver.quit()
                break
                
    driver = webdriver.Chrome()
    print("COMING HERE")
    driver.get("https://youtube.com")
    speak("youtube opened")
