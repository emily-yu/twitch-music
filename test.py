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
from Youtube import VideoStats
from animelyrics import AnimeLyrics

from itertools import product
import itertools

from tkinter import *

# stop = Event()
# tc = TwitchChat(stop, "oxstormthunder")
# tc.start();
# tc.stop()

# def google(keyword):
# 	# keyword = request.args.get("key")
# 	resultArray = []
# 	al = AnimeLyrics(keyword)
# 	resultArray = al.lyrics("jp")

# 	return (resultArray)

# def isEnglish(s):
#     try:
#         s.encode(encoding='utf-8').decode('ascii')
#     except UnicodeDecodeError:
#         return False
#     else:
#         return True

# ytv = VideoStats("https://www.youtube.com/watch?v=4GPKYLabHv0")
# print(ytv.title())
# print(google("black bullet lyrics"))
# print(google(ytv.title() + "lyrics"))
# permutation = ytv.title().split()
# print(permutation)
# for word in permutation:
# 	if (isEnglish(word) == False):
# 		permutation.remove(word)

# keywords = [''.join(i) for i in itertools.product(permutation, repeat = 3)]

# for key in keywords:
# 	print(key)
# 	try: 
# 		print(google(key + "lyrics"))
# 	except AttributeError:
# 		print("none")
# 	else:
# 		# break;
# 		print("same")


# print(ytv.duration())
# ytv.open()




# gui
class Application(Frame):
    def next(self, master = None):
        print("TODO: generate preview of thing")
        Frame.__init__(self, master)
        self.pack()
        self.addLabel("same")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "PAUSE",
        self.hi_there["command"] = self.next

        self.hi_there.pack({"side": "left"})

    def addLabel(self, text):
        self.label = Label(self)
        self.label["text"] = text
        self.label["fg"]   = "red"
        self.label.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()