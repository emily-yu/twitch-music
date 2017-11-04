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

import threading
from threading import Thread, Lock, Event

from TwitchChat import TwitchChat
# from TwitchChat import MyThread

# # retrieve element messages from chat
# def findMesssages(html):
#     # looping
#     threading.Timer(5.0, findMesssages, [html])

#     # check for messages
#     soup = BeautifulSoup(html.get_attribute("innerHTML"), 'html.parser')
#     mydivs = soup.findAll("span", {
#         "class" : "message"
#     });
#     print(mydivs)
#     for divs in mydivs:
#         # print(divs)
#         print("CONTENT:")
#         print(divs.get_text().strip())

# # start up client
# def initBot():
#     channel = "shiphtur"
#     driver = webdriver.Chrome()
#     driver.get("https://www.twitch.tv/" + channel + "/chat")

#     wait = WebDriverWait(driver, 100)
#     h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body.ember-application")))
#     findMesssages(h3)

# initBot()

stop = Event()
tc = TwitchChat(stop, "shiphtur")
tc.start();
tc.stop()

# stopFlag = Event()
# thread = MyThread(stopFlag)
# thread.start()

# this will stop the timer
# stopFlag.set()