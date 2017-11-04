from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse
from Naked.toolshed.shell import execute_js, muterun_js

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

# browser = webdriver.Firefox()
# browser.get("https://www.twitch.tv/shiphtur/chat")
# delay = 3 # seconds
driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS, "message"))
    )
finally:
    driver.quit()

# # remove br and dt tags
# for linebreak in soup.find_all('br'):
#     linebreak.extract()
# for line in soup.find_all('dt'):
#     line.extract()
# print(soup.prettify())

# mydivs = soup.findAll("td", {
# 	"class" : "romaji"
# 	});
# print("same")
# print(mydivs)

# lyrics = []
# for x in mydivs:
#     print("-------------------------------------------------------------------------------------------------------------")
#     print(x.text)
#     lyrics.append(x.text.replace("\xa0", " "))

# print(paragraphs)