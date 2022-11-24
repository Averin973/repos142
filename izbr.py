from PIL import Image, ImageDraw, ImageFont
import os

def img():
    im = Image.new('RGB', (800,800), color=('#FAACAC'))
    font=ImageFont.truetype('C:/Windows/Fonts/Arial.TTF', size=1000)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (50,50),
        text,
        font=font,
        fill=('#000000'))
    im.show()

text=input('Введите текст: ')
img()
