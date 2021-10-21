from PIL import Image,ImageDraw,ImageFont
import os
 
for i in range(1000):
    target_image = Image.open('../../Images/background.jfif')
    fontsFolder = '../../Fonts'
    selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'BMHANNA_11yrs_ttf.ttf'), 150)
    draw = ImageDraw.Draw(target_image)
    draw.text((200, 400), text=f"{i}", fill = "Black", font=selectedFont, align='center')
    target_image.save(f"../../Images/{i}.jpg")