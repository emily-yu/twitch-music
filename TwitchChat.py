from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import threading
from threading import Thread, Lock, Event
import re

from Youtube import VideoStats

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
                                                        <p class = 'music-queuer-header' style = 'position: absolute;top: 15px;right: 20px;font-weight: bold'>MUSIC QUEUE</p>\
                                                    </div>")
        # self.addSong("test", twitchDriver)
        # self.addSong("test2", twitchDriver)
        # self.addSong("test3", twitchDriver)

    def addSong(self, text, twitchDriver):
        node2 = twitchDriver.find_elements_by_xpath("/html/body/div[@class='music-queuer']/p")
        if len(node2) > 1:
            topStyle = int(node2[1].value_of_css_property("top")[:-2]) + 35
        elif len(node2) == 1:
            topStyle = int(node2[0].value_of_css_property("top")[:-2]) + 65
        else: 
            topStyle = int(node2[0].value_of_css_property("top")[:-2]) + 35

        node = twitchDriver.find_element_by_xpath("/html/body/div/p[@class='music-queuer-header']")
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"

        ytv = VideoStats(text)

        twitchDriver.execute_script(script, node, "<h6 style = 'position: absolute; right: 20px; top: " + str(topStyle - 13) + "px'>" + ytv.title() + "</h6>\
                                                   <p style = 'position: absolute; top: " + str(topStyle) + "px; right: 20px'>" + text + "</p>")

    # retrieve element messages from chat
    def findMesssages(self, html, twitchDriver):
        soup = BeautifulSoup(html.get_attribute("innerHTML"), 'html.parser')
        mydivs = soup.findAll("span", {
            "class" : "message"
        });

        # adding and checking for songs to add to queue
        for divs in mydivs:
            print(divs.get_text().strip())
            if len((re.findall(r'(https?://[^\s]+)', divs.get_text().strip()))) != 0 and "youtube.com/watch?" in divs.get_text().strip():
                print("FOUND")
                print()
                try:
                    check = self.queue.index((re.findall(r'(https?://[^\s]+)', divs.get_text().strip())))
                    print(self.queue)
                except ValueError:
                    # "Do nothing"
                    print()
                    self.queue.append((re.findall(r'(https?://[^\s]+)', divs.get_text().strip())))
                    self.addSong(divs.get_text().strip(), twitchDriver)
                    print(self.queue)

    # start up client
    def start(self):
        twitchDriver = webdriver.Chrome()
        twitchDriver.get("https://www.twitch.tv/" + self.CHANNEL + "/chat")

        wait = WebDriverWait(twitchDriver, 100)
        h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body.ember-application")))

        youtubeDriver = webdriver.Chrome()
        youtubeDriver.get("https://www.youtube.com/")

        # start loop
        self.injectUI(twitchDriver)
        self.findMesssages(h3, twitchDriver)
        while not self.stopped.wait(5.0):
            self.findMesssages(h3, twitchDriver)

    # stop loop
    def stop(self):
        print("stopped?")
        self.stopped.set()


