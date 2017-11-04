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

class TwitchChat(Thread):

    def __init__(self, event, channel):
        self.CHANNEL = channel
        self.stopped = event

    # retrieve element messages from chat
    def findMesssages(self, html):
        soup = BeautifulSoup(html.get_attribute("innerHTML"), 'html.parser')
        mydivs = soup.findAll("span", {
            "class" : "message"
        });
        print(mydivs)
        for divs in mydivs:
            print("CONTENT:")
            print(divs.get_text().strip())

    # start up client
    def start(self):
        driver = webdriver.Chrome()
        driver.get("https://www.twitch.tv/" + self.CHANNEL + "/chat")

        wait = WebDriverWait(driver, 100)
        h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body.ember-application")))

        # start loop
        self.findMesssages(h3)
        while not self.stopped.wait(5.0):
            self.findMesssages(h3)

    # stop loop
    def stop(self):
        print("stopped?")
        self.stopped.set()
