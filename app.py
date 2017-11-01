from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/videoTitle")
def getVideoTitle():
	# get url
	# url = "https://www.youtube.com/watch?v=Icpi7-whh3Q"
	url = request.args.get("url")
	r = requests.get(url)

	# title of video to search
	print("VIDEO TITLE")
	videoTitle = ""
	soup = BeautifulSoup(r.text, 'html.parser')
	mydivs = soup.findAll("span", {
		"class" : "watch-title"
		});
	for divs in mydivs:
		videoTitle = divs.contents[0].strip()

	print(videoTitle)
	return videoTitle

@app.route("/google")
def google():
	# keyword = request.args.get("key")
	resultArray = []
	for url in search("caste room", tld='com.pk', lang='es', stop=20):
		if (urlparse(url).hostname == "www.animelyrics.com"):
			resultArray.append(url)
			print(url)

	url = resultArray[0]
	# url = "http://www.animelyrics.com/anime/sao/catchthemoment.htm"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html5lib')

	# ---------------------------------------------------- TABLES WITH TRANSLATIONS----------------------------------------------------
	# remove br and dt tags
	for linebreak in soup.find_all('br'):
	    linebreak.extract()
	for line in soup.find_all('dt'):
	    line.extract()
	print(soup.prettify())

	# only use this for double table lines
	mydivs = soup.findAll("td", {
		"class" : "romaji"
		});
	print("same")
	print(mydivs)
	# ---------------------------------------------------------------------------------------------------------------------------------

	lyrics = []
	for x in mydivs:
	    print("-------------------------------------------------------------------------------------------------------------")
	    print(x.text)
	    lyrics.append(x.text.replace("\xa0", " "))

	# lyrics for song
	print(lyrics)

	return ", ".join(resultArray)

@app.route("/getMessages")
def get():
	# channelName = request.args.get("channelName")
	channelName = "shiphtur"
	r = requests.get("https://www.twitch.tv/" + channelName)
	soup = BeautifulSoup(r.text, 'html.parser')
	print(soup.prettify())
	mydivs = soup.findAll("span", {
		"class" : "message"
		});
	print(mydivs)
	for divs in mydivs:
		print(divs)
	return "Sae,"

if __name__ == '__main__':
        app.run()