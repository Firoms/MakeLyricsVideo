import cv2
import datetime
import glob
import moviepy.editor as mp
import os
import sqlite3
import youtube_dl
from alpGenerator import alpGenerator
from PIL import Image, ImageDraw, ImageFont


class makeLyricsVideo:
    '''
    노래 가사 영상을 최대한 간편하게 제작할 수 있도록 도와주는 클래스
    :param Name: 영상 이름
    '''

    def __init__(self, name: str) -> None:
        self.videoName = name
        self.makeDir()

    def makeDir(self) -> None:
        """
        영상 제작에 필요한 파일들을 저장하는 디렉토리 생성 함수
        """
        try:
            os.chdir('../../Lyrics')
            os.mkdir(self.videoName)
            os.chdir('../Musics')
            os.mkdir(self.videoName)
            os.chdir('../Images')
            os.mkdir(self.videoName)
            os.chdir('../Videos')
            os.mkdir(self.videoName)
        except:
            print("이미 같은 제목의 영상이 있습니다.")
        os.chdir('../Python/Files')

    def getLyrics(self) -> None:
        '''
        영상에 들어갈 제목, 가수, 가사를 입력받는 함수
        '''
        fileCreate = open(f'../../Lyrics/{self.videoName}/lyrics.txt', 'w')
        fileCreate.close()
        print(f"Lyrics/{self.videoName} 폴더 안에 생성된 lyrics.txt 파일에 가사를 입력해주세요.")
        print('첫번째 줄은 "제목 - 가수" 형식이어야 하며, 두번째 줄은 공백, 세번째 줄부터는 가사를 넣어주세요.')
        lyricsInput = input("저장 이후 파일을 닫고 엔터를 눌러주시면 진행됩니다.")
        self.lyricsFile = open(
            f'../../Lyrics/{self.videoName}/lyrics.txt', 'r', encoding='UTF8')

    def makeTitleImg(self) -> None:
        '''
        영상에 들어갈 제목 사진을 만드는 함수
        '''
        self.titleLine = self.lyricsFile.readline()
        title, singer = self.titleLine.split("-")
        fontsFolder = '../../Fonts'
        targetImage = Image.open('../../Images/background/background.jfif')
        draw = ImageDraw.Draw(targetImage)
        selectedFont = ImageFont.truetype(
            os.path.join(fontsFolder, 'GodoM.ttf'), 40)
        draw.text((1240, 20), text=f"Lyrics WFS", fill="#123152",
                  font=selectedFont, align='center')
        selectedFont = ImageFont.truetype(
            os.path.join(fontsFolder, 'GodoB.ttf'), 80)
        draw.text((100, 350), text=f"{title}",
                  fill="Black", font=selectedFont, align='center')
        selectedFont = ImageFont.truetype(
            os.path.join(fontsFolder, 'GodoM.ttf'), 60)
        draw.text((1000, 550), text=f"{singer}",
                  fill="#575759", font=selectedFont, align='center')
        targetImage.save(f"../../Images/{self.videoName}/aa.jpg")
        blankLine = self.lyricsFile.readline()

    def makeImg(self) -> None:
        '''
        영상에 들어갈 가사가 적힌 사진을 만드는 함수
        '''
        curLine1 = self.lyricsFile.readline()
        curLine2 = self.lyricsFile.readline()
        nextLine = self.lyricsFile.readline()
        alps = list(alpGenerator())
        fontsFolder = '../../Fonts'
        idx = 0
        while curLine1:
            targetImage = Image.open('../../Images/background/background.jfif')
            draw = ImageDraw.Draw(targetImage)
            selectedFont = ImageFont.truetype(
                os.path.join(fontsFolder, 'GodoB.ttf'), 30)
            draw.text(
                (20, 20), text=f"{self.titleLine}", fill="#5d7530", font=selectedFont, align='center')
            selectedFont = ImageFont.truetype(
                os.path.join(fontsFolder, 'GodoM.ttf'), 40)
            draw.text((1240, 20), text=f"Lyrics WFS", fill="#123152",
                      font=selectedFont, align='center')
            selectedFont = ImageFont.truetype(
                os.path.join(fontsFolder, 'godoMaum.ttf'), 100)
            draw.text(
                (100, 300), text=f"{curLine1}", fill="Black", font=selectedFont, align='center')
            draw.text(
                (100, 450), text=f"{curLine2}", fill="Black", font=selectedFont, align='center')
            draw.text(
                (100, 780), text=f"{nextLine}", fill="#575759", font=selectedFont, align='center')
            targetImage.save(f"../../Images/{self.videoName}/{alps[idx]}.jpg")
            curLine1 = nextLine
            curLine2 = self.lyricsFile.readline()
            nextLine = self.lyricsFile.readline()
            idx += 1

        targetImage = Image.open('../../Images/background/background.jfif')
        draw = ImageDraw.Draw(targetImage)
        targetImage.save(f"../../Images/{self.videoName}/{alps[idx]}.jpg")
        self.lyricsFile.close()

    def getChangeTime(self) -> None:
        '''
        가사를 넘겨줄 타이밍을 입력받는 함수
        '''
        timeList = [0]
        print("가사를 넘길 시간을 입력해주세요\n")
        while True:
            time = input()
            try:
                timeList.append(int(time[0])*60 + int(time[1:3]))
            except:
                break

        self.frameList = []
        for i in range(len(timeList)):
            if i == 0:
                continue
            self.frameList.append(timeList[i]-timeList[i-1])

    def makeVideo(self) -> None:
        '''
        가사가 적힌 사진을 모아 영상으로 제작하는 함수
        '''
        frameSize = (1470, 980)
        out = cv2.VideoWriter(f'../../Videos/{self.videoName}/{self.videoName}-nosound.avi',
                              cv2.VideoWriter_fourcc(*'DIVX'), 1, frameSize)
        idx = 0
        for filename in glob.glob(f'../../Images/{self.videoName}/*.jpg'):
            for i in range(self.frameList[idx]):
                img = cv2.imread(filename)
                out.write(img)
            idx += 1
        out.release()

    def downloadMusic(self) -> None:
        '''
        영상에 필요한 노래를 유튜브 링크로부터 다운로드 받는 함수
        '''
        downloadList = []
        youtubeURL = input("유튜브 링크를 입력해주세요 : ")
        downloadList.append(youtubeURL)
        output_dir = os.path.join(
            f'../../Musics/{self.videoName}/', f'{self.videoName}.mp3')

        ydlOpt = {
            'outtmpl': output_dir,
            'format': 'bestaudio/best',
        }

        with youtube_dl.YoutubeDL(ydlOpt) as ydl:
            ydl.download(downloadList)

    def putMusicInVideo(self) -> None:
        '''
        영상에 다운로드 받은 음악을 합쳐 완성하는 함수
        '''
        audio = mp.AudioFileClip(
            f"../../Musics/{self.videoName}/{self.videoName}.mp3")
        video1 = mp.VideoFileClip(
            f"../../Videos/{self.videoName}/{self.videoName}-nosound.avi")
        final = video1.set_audio(audio)
        final.write_videofile(
            f"../../Videos/{self.videoName}/{self.videoName}.mp4", codec='mpeg4', audio_codec='libvorbis')

    def saveDatabase(self) -> None:
        db = sqlite3.connect(
            "../../Database/Datas.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM VideoDatas")
        count = cursor.fetchone()[0]
        insert_query = f"INSERT INTO VideoDatas VALUES('{count+1}','{self.videoName}','{self.frameList}','{datetime.datetime.now()}')"
        cursor.execute(insert_query)
        db.commit()

if __name__ == '__main__':
    name = input("영상 제목을 영어로 입력해주세요 : ")
    video = makeLyricsVideo(name)
    video.getLyrics()
    video.makeTitleImg()
    video.makeImg()
    video.getChangeTime()
    video.makeVideo()
    video.downloadMusic()
    video.putMusicInVideo()
    video.saveDatabase()

    