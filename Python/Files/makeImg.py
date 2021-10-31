from PIL import Image, ImageDraw, ImageFont
import os





lyricsFile = open('../../Lyrics/test.txt', 'r', encoding='UTF8')
curLine = lyricsFile.readline()
nextLine = lyricsFile.readline()

num = 999
while curLine:
    num += 1
    target_image = Image.open('../../Images/background.jfif')
    fontsFolder = '../../Fonts'
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'BMHANNA_11yrs_ttf.ttf'), 80)
    draw = ImageDraw.Draw(target_image)
    draw.text((100, 350), text=f"{curLine}", fill = "Black", font=selectedFont, align='center')
    draw.text((100, 800), text=f"{nextLine}", fill = "Gray", font=selectedFont, align='center')
    target_image.save(f"../../Images/{num}.jpg")
    curLine = nextLine
    nextLine = lyricsFile.readline()
        
lyricsFile.close()