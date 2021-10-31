import youtube_dl
import os

output_dir = os.path.join('../../Musics/', 'test.mp3')

download_list = [
    'https://www.youtube.com/watch?v=JbV-yAKIXgs',
    ]

ydl_opt = {
    'outtmpl': output_dir,
    'format': 'bestaudio/best',
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(download_list)
