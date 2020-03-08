import time
import csv
import re
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#Chrome driver
driver = webdriver.Chrome(
    "/Users/Benediktkuehn/Documents/Development/Python/chromedriver")

#Login to WhatsApp web
driver.get("https://web.whatsapp.com/")

#Scan QR-code with your phone
time.sleep(15)

print("The wait ist over! I hope you have logged in and selected a chat.")

no_of_pagedowns = 800
while no_of_pagedowns:
    driver.find_element_by_css_selector('div.copyable-area > div').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    no_of_pagedowns -= 1

html = BeautifulSoup(driver.page_source, 'html.parser')
sentMessages = html.select('div.message-out')

#print(sentMessages)

messageTXT = []

for message in sentMessages:
    text = message.select('span.selectable-text')
    rawtext = BeautifulSoup(str(text), "html.parser").text
    #print(rawtext)
    cleantext = rawtext.replace("[", "")
    cleantext = cleantext.replace("]", "")
    print(cleantext)
    messageTXT.append(cleantext)

with open("Sentences.txt","w") as f: 
    for message in messageTXT:
        f.write("%s\n" % message)