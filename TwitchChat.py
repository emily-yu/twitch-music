from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import threading
from threading import Thread, Lock, Event
import re

class TwitchChat(Thread):

    def __init__(self, event, channel):
        self.CHANNEL = channel
        self.stopped = event
        self.queue = []

    # create queue
    def injectUI(self, twitchDriver):
        print("suddenly i wonder why i used python lmao")
        node = twitchDriver.find_element_by_xpath("/html/body")
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        twitchDriver.execute_script(script, node, "<div class = 'music-queuer'>\
                                                        <p class = 'music-queuer-header' style = 'position: absolute;top: 20px;right: 20px;'>Music Queue</p>\
                                                    </div>")
        self.addSong("test", twitchDriver)

    def addSong(self, text, twitchDriver):
        node = twitchDriver.find_element_by_xpath("/html/body/div/p[@class='music-queuer-header']")
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        twitchDriver.execute_script(script, node, "\
                                                        <p style = 'position: absolute; top: 40px; right: 20px'>Music Queuasdfadfe</p>\
                                                    ")

    # retrieve element messages from chat
    def findMesssages(self, html):
        soup = BeautifulSoup(html.get_attribute("innerHTML"), 'html.parser')
        mydivs = soup.findAll("span", {
            "class" : "message"
        });

        # adding and checking for songs to add to queue
        for divs in mydivs:
            print(divs.get_text().strip())
            if len((re.findall(r'(https?://[^\s]+)', divs.get_text().strip()))) != 0:
                print("FOUND")
                print()
                try:
                    check = self.queue.index((re.findall(r'(https?://[^\s]+)', divs.get_text().strip())))
                    print(self.queue)
                except ValueError:
                    # "Do nothing"
                    print()
                    self.queue.append((re.findall(r'(https?://[^\s]+)', divs.get_text().strip())))
                    print(self.queue)

    # start up client
    def start(self):
        twitchDriver = webdriver.Chrome()
        twitchDriver.get("https://www.twitch.tv/" + self.CHANNEL + "/chat")

        wait = WebDriverWait(twitchDriver, 100)
        h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body.ember-application")))

        # start loop
        self.findMesssages(h3)
        self.injectUI(twitchDriver)
        while not self.stopped.wait(5.0):
            self.findMesssages(h3)

    # stop loop
    def stop(self):
        print("stopped?")
        self.stopped.set()


