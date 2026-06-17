from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def hold_web_page(url):
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    return driver
