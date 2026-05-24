from listen import listen
from date_time import date_time
from web_browser import web_browser
from home_related_things import things
from password import password

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

text = listen()

date_time(text)
web_browser(text)
things(text)
