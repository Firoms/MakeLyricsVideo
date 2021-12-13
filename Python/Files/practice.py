
import os
import requests
from bs4 import BeautifulSoup




search = input()

fileCreate = open(
    f"../../Musics/Lyrics/{search}.txt", "w", encoding="cp949"
)
basicURL = "https://music.bugs.co.kr/search/integrated?q="
searchURL = basicURL + search
searchHtml = requests.get(searchURL).text
searchSoup = BeautifulSoup(searchHtml, "html.parser")
lyricsBtnTag = searchSoup.find("a", {"class": "trackInfo"})
lyricsURL = lyricsBtnTag["href"]
lyricsHtml = requests.get(lyricsURL).text
lyricsSoup = BeautifulSoup(lyricsHtml, "html.parser")
lyricsTag = lyricsSoup.find("xmp")
lyrics = lyricsTag.text
lyricsLines = list(lyrics.split("\r\n"))
enter = lyricsLines.count("")
for _ in range(enter):
    lyricsLines.remove("")
fileCreate.write(f"{search}\n#\n")
for i in range(len(lyricsLines)):
    if i % 2 == 0:
        fileCreate.write(f"{lyricsLines[i]}\n")
    else:
        fileCreate.write(f"{lyricsLines[i]} #\n")
fileCreate.write("#\n")
fileCreate.close()

TitleTag = lyricsSoup.find("header", {"class":"sectionPadding pgTitle noneLNB"})
Title = TitleTag.find("h1").text.strip())

InfoTag = lyricsSoup.find("table", {"class":"info"})
Artist = InfoTag.find_all("td")[0].text.strip()
Album = print(InfoTag.find_all("td")[2].text.strip()