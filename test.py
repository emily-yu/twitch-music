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

from tkinter import messagebox, Frame, Tk, Button, Scrollbar, Text, RIGHT, Y, LEFT, END

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
	def newRequest(self, master = None):
		print("TODO: generate preview of thing")
		self.addLabel("same")

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit

		self.QUIT.pack({"side": "left"})

		self.hi_there = Button(self)
		self.hi_there["text"] = "PAUSE",
		self.hi_there["command"] = self.newRequest

		self.hi_there.pack({"side": "left"})

	def addLabel(self, text, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.label = Label(self)
		self.label["text"] = text
		self.label["fg"]   = "red"
		self.label.pack({"side": "left"})

	def scrollText(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		S=Scrollbar(self)
		T=Text(self, height=20, width=50)
		S.pack(side=RIGHT, fill=Y)
		T.pack(side=LEFT, fill=Y)
		S.config(command=T.yview)
		T.config(yscrollcommand=S.set)
		quote = """
sotto  hakidasu  tameiki wo suikonda  koukai wa nigai aji nokoshite 
itsumo  nande?  kanjin na koto ienai mama  tsugi no asahi ga kao dashiteru

iya ni natta unmei wo  NAIFU de kirikizande 
mou ichido yarinaoshitara  kimi ni deaenai kamo

boku no koe ga hibiita toki ni hajimaru  inochi no RIMITTO  shinzou ga KAUNTO shiteru 
kanaete mo kanaete mo  owaranai negai 
ase wo kaite hashitta  sekai no byoushin wa  itsuka tomatta boku wo oite yuku 
ato nankai kimi to waraeru no? 
tameshiterunda  boku wo  Catch the Moment

ikko shiawase wo kazoeru tabi ni  kawatteiku mirai ni obiete shimau kedo

aijou no tane wo taisetsu ni sodateyou 
buatsui kumo mo  yagate tsukiyaburu kana

kimi no koe ga hibiita  boku no zenshin wo kayotte  shinzou no DOA wo NOKKU shiteru 
"Okubyou" demo akechaunda yo  shinjitai kara 
nan ni mo to omotta hazu no ashimoto ni  itsuka fukaku tashika na ne wo hayasu 
arashi no yoru ga kita to shite mo  yuraidari wa shinai

nando demo 
oitsuitari  oikoshitari  kimi ga fui ni wakannaku natte 
iki wo shita TAIMINGU ga au dake de  ureshiku nattari shite 
atsumeta ichibyou wo  eien ni shite ikeru kana

boku no koe ga hibiita toki ni hajimaru  inochi no RIMITTO  shinzou ga KAUNTO shiteru 
kanaete mo kanaete mo  owaranai negai 
ase wo kaite hashitta  sekai no byoushin ga  itsuka tomatta boku wo oite yuku 
ato nankai kimi to waraeru no? 
tameshiterunda  boku wo  Catch the Moment

nogasanai yo  boku wa 
kono toki wo tsukame  Catch the Moment
		"""
		T.insert(END, quote)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		self.scrollText()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

stop = Event()
tc = TwitchChat(stop, "oxstormthunder")
tc.start();
tc.stop()