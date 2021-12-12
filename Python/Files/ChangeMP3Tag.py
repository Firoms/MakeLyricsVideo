import eyed3
import os
import requests
import youtube_dl
from bs4 import BeautifulSoup

class ChangeMP3Tag():
    """
    노래 MP3 파일을 유튜브로부터 다운로드 받고,
    mp3의 ID3 태그 값에 제목, 아티스트, 앨범, 가사 값을 집어넣어주는 클래스
    :param search: 제목과 아티스트
    """
    def __init__(self, search) -> None:
        self.search = search

    def downloadMusic(self) -> None:
        """
        MP3에 필요한 노래를 유튜브 링크로부터 다운로드 받는 메서드
        """
        downloadList = []
        self.youtubeURL = input("유튜브 링크를 입력해주세요 : ")
        downloadList.append(self.youtubeURL)
        output_dir = os.path.join(
            f"../../Musics/", f"{self.search}.mp3"
        )

        ydlOpt = {
            "outtmpl": output_dir,
            "format": "bestaudio/best",
        }

        with youtube_dl.YoutubeDL(ydlOpt) as ydl:
            ydl.download(downloadList)


    def getDatas(self) -> None:
        """
        MP3에 들어갈 제목, 아티스트, 앨범, 가사 값을 스크래핑 하는 메서드
        """
        fileCreate = open(
            f"../../Musics/Lyrics/{self.search}.txt", "w", encoding="cp949"
        )
        basicURL = "https://music.bugs.co.kr/search/integrated?q="
        searchURL = basicURL + self.search
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
        fileCreate.write(f"{self.search}\n#\n")
        for i in range(len(lyricsLines)):
            if i % 2 == 0:
                fileCreate.write(f"{lyricsLines[i]}\n")
            else:
                fileCreate.write(f"{lyricsLines[i]} #\n")
        fileCreate.write("#\n")
        fileCreate.close()


if __name__=="__main__":
    search = input("노래 제목 & 아티스트 입력\n> ")
    CMT = ChangeMP3Tag(search)
    CMT.downloadMusic()
    CMT.getLyrics()