from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse

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
	# keyword = request.args.get("key")
	resultArray = []
	for url in search("catch the moment", tld='com.pk', lang='es', stop=20):
		if (urlparse(url).hostname == "www.animelyrics.com"):
			resultArray.append(url)
			print(url)

	url = resultArray[0]
	# url = "http://www.animelyrics.com/anime/sao/catchthemoment.htm"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html5lib')

	tdSearch = soup.findAll("td", {
		"class" : "translation"
		});
	# print(mydivs)
	count = 0
	for element in tdSearch:
		count = count + 1

	print(count)
	lyrics = []
	if count == 0:
		print("single table")
		# --------------------- TABLES WITH TRANSLATIONS ---------------------
		print("---------------------------------------------------------------")
		result = find_between(soup.text, "Lyrics from Animelyrics.com", "Transliterated")
		lyrics.append(result.replace("\xa0", " "))
		# --------------------------------------------------------------------

	else:
		print("double table")
		print("---------------------------------------------------------------")
		# --------------------- TABLES WITH TRANSLATIONS ---------------------
		for linebreak in soup.find_all('br'):
		    linebreak.extract()
		for line in soup.find_all('dt'):
		    line.extract()
		# print(soup.prettify())

		mydivs = soup.findAll("td", {
			"class" : "romaji"
			});
		# print("same")
		# print(mydivs)

		for x in mydivs:
			# print(x.text)
			lyrics.append(x.text.replace("\xa0", " "))
		# --------------------------------------------------------------------

	# lyrics for song
	print(lyrics)

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