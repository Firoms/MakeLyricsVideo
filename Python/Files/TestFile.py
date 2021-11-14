import requests
from bs4 import BeautifulSoup

basicURL = 'https://music.bugs.co.kr/search/integrated?q='
song = input("노래 제목 - 가수 입력\n> ")
searchURL = basicURL + song
searchHtml = requests.get(searchURL).text
searchSoup = BeautifulSoup(searchHtml, "html.parser")
lyricsBtnTag = searchSoup.find("a", {"class": "trackInfo"})
lyricsURL = lyricsBtnTag["href"]

lyricsHtml = requests.get(lyricsURL).text
lyricsSoup = BeautifulSoup(lyricsHtml, "html.parser")
lyricsTag = lyricsSoup.find("xmp")
lyrics = lyricsTag.text


lyricsLines = list(lyrics.split("\r\n"))
print(lyricsLines)