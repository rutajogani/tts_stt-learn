from listen import listen
from speak import speak
from date_time import date_time
from browser import browser
from home_related_things import things
from password import password

text = listen()
speak(text)

if "data" or "time" in text:
    date_time(text)

browser(text)
# things(text)
