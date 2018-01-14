from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import threading
from threading import Thread, Lock, Event

import requests

class VideoStats:

	def __init__(self, link):
		self.RAW_LINK = link
		self.LINK_CONTENT = BeautifulSoup(requests.get(link).text, 'html.parser')

	def title(self):
		titleElements = self.LINK_CONTENT.findAll("span", {
			"class" : "watch-title"
		});
		for title in titleElements:
			return title.contents[0].strip();

	def duration(self):
		self.driver = webdriver.Chrome()
		self.driver.get(self.RAW_LINK)

		wait = WebDriverWait(self.driver, 100)
		h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.ytp-time-duration")))
		print(h3.get_attribute("innerHTML"))

		# lol screw hrs
		m, s = h3.get_attribute("innerHTML").split(':')
		# duration to keep tab open
		print((int(m) * 60 + int(s)) + 10)
		self.driver.quit()

		return (int(m) * 60) + int(s) + 10

		# driver.close()

	def open(self):
		self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
		self.driver.get(self.RAW_LINK)