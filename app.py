from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests

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

if __name__ == '__main__':
        app.run()