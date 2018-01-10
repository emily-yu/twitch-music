from TwitchChat import TwitchChat

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import threading
from threading import Thread, Lock, Event
import re
from test import app

stop = Event()
tc = TwitchChat(stop, "oxstormthunder")
tc.start();
tc.stop()

app.addLabel("text")