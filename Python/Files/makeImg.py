from PIL import Image, ImageDraw, ImageFont
import os
from alpGenerator import alpGenerator

lyricsFile = open('../../Lyrics/test.txt', 'r', encoding='UTF8')
titleLine = lyricsFile.readline()
title, singer = titleLine.split("-")
fontsFolder = '../../Fonts'
targetImage = Image.open('../../Images/background/background.jfif')
draw = ImageDraw.Draw(targetImage)
selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'GodoM.ttf'), 40)
draw.text((1240, 20), text=f"Lyrics WFS", fill = "#123152", font=selectedFont, align='center')
selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'GodoB.ttf'), 80)
draw.text((100, 350), text=f"{title}", fill = "Black", font=selectedFont, align='center')
selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'GodoM.ttf'), 60)
draw.text((1000, 550), text=f"{singer}", fill = "#575759", font=selectedFont, align='center')
targetImage.save(f"../../Images/aa.jpg")
blankLine = lyricsFile.readline()

curLine1 = lyricsFile.readline()
curLine2 = lyricsFile.readline()
nextLine = lyricsFile.readline()
alps = list(alpGenerator())

num = 0

while curLine1:    
    targetImage = Image.open('../../Images/background/background.jfif')
    draw = ImageDraw.Draw(targetImage)
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'GodoB.ttf'), 30)
    draw.text((20, 20), text=f"{titleLine}", fill = "#5d7530", font=selectedFont, align='center')
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'GodoM.ttf'), 40)
    draw.text((1240, 20), text=f"Lyrics WFS", fill = "#123152", font=selectedFont, align='center')
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'godoMaum.ttf'), 100)
    draw.text((100, 300), text=f"{curLine1}", fill = "Black", font=selectedFont, align='center')
    draw.text((100, 450), text=f"{curLine2}", fill = "Black", font=selectedFont, align='center')
    draw.text((100, 780), text=f"{nextLine}", fill = "#575759", font=selectedFont, align='center')
    targetImage.save(f"../../Images/{alps[num]}.jpg")
    curLine1 = nextLine
    curLine2 = lyricsFile.readline()
    nextLine = lyricsFile.readline()
    num += 1

targetImage = Image.open('../../Images/background/background.jfif')
draw = ImageDraw.Draw(targetImage)
targetImage.save(f"../../Images/{alps[num]}.jpg")

lyricsFile.close()