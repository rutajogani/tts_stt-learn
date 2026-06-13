from listen import listen
from speak import speak

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time


def check_open_or_not():
    r = requests.get("https://www.google.com/", timeout=5)
    print("Google is reachable:", r.status_code)

driver = None

def google():
    while True:
        command = listen()

        if "open" in command:
            driver = webdriver.Chrome()
            print("COMING HERE")
            driver.get("https://www.google.com/")
            speak("Google opened")

        elif "search" in command:
            what_to_search = listen()
            time.sleep(3)
            # search_box = driver.find_element(By.NAME,  "search_query")
            # search_box = driver.find_element(By.NAME, "q")
            search_box = driver.find_element(By.NAME, "q") 
            # search_box.clear() 
            # search_box.send_keys(what_to_search) 
            # search_box.submit()
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
                print("🚀 ~ google ~ driver:", driver)
                break
                
    # driver = webdriver.Chrome()
    # print("COMING HERE")
    # driver.get("https://www.google.com/")
    # speak("Google opened")
