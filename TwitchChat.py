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
import time

from Youtube import VideoStats

class TwitchChat(Thread):

    def __init__(self, event, event2, channel):
        self.CHANNEL = channel
        self.stopped = event
        self.musicStopped = event2
        self.queue = []

    # create queue
    def injectUI(self, twitchDriver):
        print("suddenly i wonder why i used python lmao")
        node = twitchDriver.find_element_by_xpath("/html/body")
        script = "arguments[0].insertAdjacentHTML('afterEnd', arguments[1])"
        twitchDriver.execute_script(script, node, "<div class = 'music-queuer'>\
                                                        <p class = 'music-queuer-header' style = 'position: absolute;top: 15px;right: 20px;font-weight: bold'>MUSIC QUEUE</p>\
                                                    </div>")

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

    def startMusic(self, driver, link):
        driver.get(link)

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
        # while not self.stopped.wait(5.0):

        queue_index = 0
        song_timer = 0
        while not self.musicStopped.wait(1.0):
            self.findMesssages(h3, twitchDriver)
            print(len(self.queue))
            print(song_timer)
            if len(self.queue) > 0 and song_timer < 1:
                print("start new song: length of queue is more than 0 AND song_timer is not positive")
                link = VideoStats(self.queue[queue_index][0])
                youtubeDriver.get(self.queue[queue_index][0])
                song_timer = link.duration()
                queue_index = queue_index + 1
            elif len(self.queue) == 0 and song_timer < 1:
                print("none in queue: length of queue is 0")
            else:
                print("song_timer is positive?")
                song_timer = song_timer - 1
                print(song_timer)

    # stop loop
    def stop(self):
        print("stopped?")
        self.stopped.set()


