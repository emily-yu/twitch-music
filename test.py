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

# stop = Event()
# tc = TwitchChat(stop, "oxstormthunder")
# tc.start();
# tc.stop()
def google(keyword):
	# keyword = request.args.get("key")
	resultArray = []
	al = AnimeLyrics(keyword)
	resultArray = al.lyrics("jp")

	return (resultArray)

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

ytv = VideoStats("https://www.youtube.com/watch?v=4GPKYLabHv0")
print(ytv.title())
permutation = ytv.title().split()
print(permutation)
for word in permutation:
	if (isEnglish(word) == False):
		permutation.remove(word)

keywords = [''.join(i) for i in itertools.product(permutation, repeat = 3)]

for key in keywords:
	print(key)
	try: 
		print(google(key + "lyrics"))
	except AttributeError:
		print("none")
	else:
		# break;
		print("same")


# print(ytv.duration())
# ytv.open()