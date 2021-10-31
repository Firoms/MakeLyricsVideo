from PIL import Image, ImageDraw, ImageFont
import os
from alpGenerator import alpGenerator





lyricsFile = open('../../Lyrics/test.txt', 'r', encoding='UTF8')
curLine1 = lyricsFile.readline()
curLine2 = lyricsFile.readline()
nextLine = lyricsFile.readline()
alps = list(alpGenerator())


num = 0
while curLine1:
    target_image = Image.open('../../Images/background/background.jfif')
    fontsFolder = '../../Fonts'
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'BMHANNA_11yrs_ttf.ttf'), 80)
    draw = ImageDraw.Draw(target_image)
    draw.text((100, 350), text=f"{curLine1}", fill = "Black", font=selectedFont, align='center')
    draw.text((100, 500), text=f"{curLine2}", fill = "Black", font=selectedFont, align='center')
    draw.text((100, 800), text=f"{nextLine}", fill = "Gray", font=selectedFont, align='center')
    target_image.save(f"../../Images/{alps[num]}.jpg")
    curLine1 = nextLine
    curLine2 = lyricsFile.readline()
    nextLine = lyricsFile.readline()
    num += 1

target_image = Image.open('../../Images/background/background.jfif')
draw = ImageDraw.Draw(target_image)
target_image.save(f"../../Images/{alps[num]}.jpg")

lyricsFile.close()