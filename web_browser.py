from listen import listen
from speak import speak
#import webbrowser as web
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def check_open_or_not():
        r = requests.get("https://www.youtube.com", timeout=5)
        print("YouTube is reachable:", r.status_code)

driver = None


def web_browser(text): # web browser function

    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT", "Gemini"]
    
    for web_page in list_of_web_page:

        if "YouTube" in text:
            
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

                    search = driver.find_element(
                    By.XPATH,
                    "//input[@id='search_query']"
                    )
                    search.click(what_to_search)    
                    speak("searching youtube")                            
                
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
                        driver = None
                        break
                        
            driver = webdriver.Chrome()
            print("COMING HERE")
            driver.get("https://youtube.com")
            speak("youtube opened")
            break

        elif "Google" in text:

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

        elif "chat GPT" in text:

            web.open("https://chatgpt.com/")
            print("----Chatgpt opened----")
            engine.say("Chatgpt opened")
            engine.runAndWait()
            break

        elif "GitHub" in text:

            web.open("https://github.com/rutajogani")
            print("----Github opened----")
            engine.say("Github opened")
            engine.runAndWait()
            break

        elif "Gemini" in text:

            web.open("https://gemini.google.com/app")
            print("----Gemini opened----")
            engine.say("Gemini opened")
            engine.runAndWait()
            break

            # elif "exit" in command:
            #     if driver:
            #     driver.quit()
            #     break