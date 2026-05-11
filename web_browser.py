import webbrowser as web
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def web_browser(): # web browser function

    list_of_web_page = ["YouTube", "Google", "monkey type", "chat GPT", "Gemini"]
    
    for web_page in list_of_web_page:

        if "YouTube" in text:

            if "search" in text:

                print("Speak what you want to search: ")
                what_to_search = listen()
                searching = f"https://www.youtube.com/results?search_query={what_to_search}"
                web.open(searching)
                break

            web.open("https://www.youtube.com/")
            print("----Youtube opened----")
            engine.say("Youtube opened")
            break

        elif "Google" in text:

            if "search" in text:

                print("Speak what you want to search: ")
                what_to_search = listen()
                searching = f"http://www.google.com/search?q={what_to_search}"
                web.open(searching)
                break

            web.open("https://www.google.com/")
            print("----Google opened----")
            engine.say("Google opened")
            break

        elif "monkey type" in text:

            web.open("https://monkeytype.com/")
            print("----MonkeyType opened----")
            engine.say("MonkeyType opened")
            break

        elif "chat GPT" in text:

            web.open("https://chatgpt.com/")
            print("----Chatgpt opened----")
            engine.say("Chatgpt opened")
            break

        elif "GitHub" in text:

            web.open("https://github.com/rutajogani")
            print("----Github opened----")
            engine.say("Github opened")
            break

        elif "Gemini" in text:

            web.open("https://gemini.google.com/app")
            print("----Gemini opened----")
            engine.say("Gemini opened")
            break

engine.runAndWait()