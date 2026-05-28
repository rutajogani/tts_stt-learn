from listen import listen
import webbrowser as web
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

driver = None

def web_browser(text): # web browser function

    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT", "Gemini"]
    
    for web_page in list_of_web_page:

        if "YouTube" in text:
            
            while True:
                
            command = listen()
            
            # open youtube
            if "open youtube" in command:
                driver = webdriver.Chrome()
                driver.get("https://youtube.com")

            # searching in youtube
            if "search" in text:
                print("Speak what you want to search: ")
                what_to_search = listen()
                searching = f"https://www.youtube.com/results?search_query={what_to_search}"
                web.open(searching)
                engine.runAndWait()

            #close youtube 
            elif "close youtube" in command:
                 if driver:
                    driver.quit()
                    driver = None
                    break
            

        web.open("https://www.youtube.com/")
        print("----Youtube opened----")
        engine.say("Youtube opened")
        engine.runAndWait()
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