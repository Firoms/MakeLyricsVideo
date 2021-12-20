import youtube_dl
import os

downloadList = []
youtubeURL = input("유튜브 링크를 입력해주세요 : ")
downloadList.append(youtubeURL)
output_dir = os.path.join(f"../../Musics/", f"test.mp3")


ydlOpt = {
    "outtmpl": output_dir,
    "format": "bestaudio/best",
}

with youtube_dl.YoutubeDL(ydlOpt) as ydl:
    ydl.download(downloadList)
