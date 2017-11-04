from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse
from animelyrics import AnimeLyrics

app = Flask(__name__)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# extract video title from youtube link
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

# google and extract lyrics
@app.route("/google")
def google():
	keyword = request.args.get("key")
	resultArray = []
	al = AnimeLyrics(keyword)
	resultArray = al.lyrics("jp")

	return ", ".join(resultArray)

# get twitch chat messages
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