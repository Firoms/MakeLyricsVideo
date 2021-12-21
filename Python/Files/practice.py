import youtube_dl
import os

downloadList = []
youtubeURL = input("유튜브 링크를 입력해주세요 : ")
downloadList.append(youtubeURL)
output_dir = os.path.join(f"../../Musics/", f"test2.mp3")


ydlOpt = {
    "outtmpl": output_dir,
    "format": "bestaudio/best",
    "extractaudio": True,
    "audioformat": "mp3",
    "noplaylist": True,
    "nocheckcertificate": True,
    "addmetadata": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
        {"key": "FFmpegMetadata"},
    ],
}


with youtube_dl.YoutubeDL(ydlOpt) as ydl:
    ydl.download(downloadList)
