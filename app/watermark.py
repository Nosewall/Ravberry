from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def wm_text(in_im_path, out_im_path, text, pos):
    photo = Image.open(in_im_path)

    drawing = ImageDraw.Draw(photo)

    color = 15

    font = ImageFont.truetype("fonts/AgiliaItalic.ttf", 40)

    drawing.text(pos, text, fill=color, font=font)

    photo.show()

if __name__ == '__main__':
    img = 'static/ravberry.png'
    wm_text(img, 'imageWaterMarked.png', text='hi there its mike lim', pos=(100, 100))