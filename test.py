from flask import Flask, request
from bs4 import BeautifulSoup
import urllib.request
import requests
from google import search
from urllib.parse import urlparse
from Naked.toolshed.shell import execute_js, muterun_js

url = "http://www.animelyrics.com/anime/sao/catchthemoment.htm"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html5lib')

# remove br and dt tags
for linebreak in soup.find_all('br'):
    linebreak.extract()
for line in soup.find_all('dt'):
    line.extract()
print(soup.prettify())

mydivs = soup.findAll("td", {
	"class" : "romaji"
	});
print("same")
print(mydivs)

lyrics = []
for x in mydivs:
    print("-------------------------------------------------------------------------------------------------------------")
    print(x.text)
    lyrics.append(x.text.replace("\xa0", " "))

print(lyrics)