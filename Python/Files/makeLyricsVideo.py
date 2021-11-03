import os
from alpGenerator import alpGenerator
from PIL import Image, ImageDraw, ImageFont


class makeLyricsVideo:
    '''
    노래 가사 영상을 최대한 간편하게 제작할 수 있도록 도와주는 클래스
    :param Name: 영상 이름
    '''

    def __init__(self, Name: str) -> None:
        self.videoName = Name
        self.makeImg()

    def makeDir(self, dirName) -> None:
        pass

    def getLyrics(self) -> None::
        '''
        영상에 들어갈 제목, 가수, 가사를 입력받는 함수
        '''
        os.chdir('../../Lyrics')
        os.mkdir(self.videoName)
        print(f"Lyrics/{self.videoName} 폴더 안에 생성된 lyrics.txt 파일에 가사를 입력해주세요.")
        print('첫번째 줄은 "제목 - 가수" 형식이어야 하며, 두번째 줄은 공백, 세번째 줄부터는 가사를 넣어주세요.')
        lyricsInput = input("저장 이후 파일을 닫고 엔터를 눌러주시면 진행됩니다.")

    def makeTitleImg(self) -> None::
        lyricsFile = open(
            f'../../Lyrics/{self.videoName}/lyrics.txt', 'r', encoding='UTF8')
        titleLine = lyricsFile.readline()
        title, singer = titleLine.split("-")
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
        blankLine = lyricsFile.readline()

        curLine1 = lyricsFile.readline()
        curLine2 = lyricsFile.readline()
        nextLine = lyricsFile.readline()
        alps = list(alpGenerator())


    def makeImg(self) -> None:
        '''
        영상에 들어갈 가사가 적힌 사진을 만드는 함수
        '''
        lyricsFile = open(
            f'../../Lyrics/{self.videoName}/lyrics.txt', 'r', encoding='UTF8')
        titleLine = lyricsFile.readline()
        title, singer = titleLine.split("-")
        fontsFolder = '../../Fonts'
        idx = 0
        while curLine1:
            targetImage = Image.open('../../Images/background/background.jfif')
            draw = ImageDraw.Draw(targetImage)
            selectedFont = ImageFont.truetype(
                os.path.join(fontsFolder, 'GodoB.ttf'), 30)
            draw.text(
                (20, 20), text=f"{titleLine}", fill="#5d7530", font=selectedFont, align='center')
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
            curLine2 = lyricsFile.readline()
            nextLine = lyricsFile.readline()
            idx += 1

        targetImage = Image.open('../../Images/background/background.jfif')
        draw = ImageDraw.Draw(targetImage)
        targetImage.save(f"../../Images/{self.videoName}/{alps[idx]}.jpg")

        lyricsFile.close()

    def makeVideo(self) -> None:
        '''
        가사가 적힌 사진을 모아 영상으로 제작하는 함수
        '''

    def downloadMusic(self) -> None:
        '''
        영상에 필요한 노래를 유튜브 링크로부터 다운로드 받는 함수
        '''

    def putMusicInVideo(self) -> None:
        '''
        영상에 다운로드 받은 음악을 합쳐 완성하는 함수
        '''


if __name__ == '__main__':
    Name = input()
    Video = makeLyricsVideo(Name)
