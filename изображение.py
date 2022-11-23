from PIL import Image, ImageDraw, ImageFont

img()
def img():
    im = Image.new('RGB', (300,300), color=('#FAACAC'))
    font=ImageFont.truetype('C:/Windows/Fonts/Arial.TTF', size=15)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (0,0),
        '— Скажи-ка, дядя, ведь недаром\nМосква, спаленная пожаром,\nФранцузу отдана?\nВедь были ж схватки боевые,\nДа, говорят, еще какие!\nНедаром помнит вся Россия\nПро день Бородина!',
        font=font,
        fill=('#000000'))
    im.show()


