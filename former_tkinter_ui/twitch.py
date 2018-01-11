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
# from test import app

# stop = Event()
# tc = TwitchChat(stop, "oxstormthunder")
# tc.start();
# tc.stop()

# app.addLabel("text")

from multiprocessing import Process
import sys

from tkinter import messagebox, Frame, Tk, Button, Scrollbar, Text, RIGHT, Y, LEFT, END, Label


rocket = 0

def func2():
	global rocket
	print('start func1')
	stop = Event()
	tc = TwitchChat(stop, "oxstormthunder")
	tc.start();
	tc.stop()
	while rocket < 234890328490283940923089480293489023804234983290849023849023890:
		rocket += 1
	print('end func1')

def func1():
	global rocket
	print('start func2')

	root = Tk()
	app = Application(master=root)
	app.mainloop()
	root.destroy()

	while rocket < 234890328490283940923089480293489023804234983290849023849023890:
		rocket += 1
	print('end func2')


p1 = Process(target=func1)
p1.start()
p2 = Process(target=func2)
p2.start()
p1.join()
p2.join()