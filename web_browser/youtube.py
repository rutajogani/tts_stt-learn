from listen import listen
from speak import speak

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time


def check_open_or_not():
    r = requests.get("https://www.youtube.com", timeout=5)
    print("YouTube is reachable:", r.status_code)

driver = None

def youtube(text):

    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT", "Gemini"]
    
    for web_page in list_of_web_page:

        if "youtube" in text:
            
            while True:

                command = listen()
                # open youtube
                if "open" in command:
                    driver = webdriver.Chrome()
                    print("COMING HERE")
                    response = driver.get("https://youtube.com")
                    speak("youtube opened")
                    
                # searching in youtube
                elif "search" in command:
                    what_to_search = listen()
                    time.sleep(3)

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
                elif "close youtube" in command:
                    if driver:
                        driver.quit()
                        break
                        
            driver = webdriver.Chrome()
            print("COMING HERE")
            driver.get("https://youtube.com")
            speak("youtube opened")
            break