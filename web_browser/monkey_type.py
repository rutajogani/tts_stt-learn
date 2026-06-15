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
