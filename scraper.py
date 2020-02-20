import time
import csv
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#initial setup
driver = webdriver.Chrome(
    "/Users/benediktkuehn/Documents/Development/Python/chromedriver")

#login to WhatsApp web
driver.get("https://web.whatsapp.com/")

#scan QR code from phone
time.sleep(20)

print("The wait ist over!")

"""elem = driver.find_element_by_tag_name("_10V4p _1jxtm")"""

no_of_pagedowns = 3

while no_of_pagedowns:
            driver.find_element_by_css_selector('div.copyable-area > div').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(2)
            no_of_pagedowns -= 1