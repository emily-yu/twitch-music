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

# stop = Event()
# tc = TwitchChat(stop, "oxstormthunder")
# tc.start();
# tc.stop()

ytv = VideoStats("https://www.youtube.com/watch?v=m8MfJg68oCs")
print(ytv.title())
print(ytv.duration())
ytv.open()