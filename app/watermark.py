import PIL
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

from pathlib import Path, PureWindowsPath

def watermark_text(in_img_path, out_img_path, text, pos):
    photo = Image.open(in_img_path)
    
    drawing = ImageDraw.Draw(photo)

    filename = Path(os.path.join(os.path.abspath(os.getcwd()) + "/app/static/fonts/AgiliaItalic.ttf"))

    temp_color = (0,0,0)

    temp_size = 40

    temp_font = ImageFont.truetype(str(Path(filename)), temp_size)

    drawing.text(pos, text, fill=temp_color, font=temp_font)

    path = out_img_path
    photo.save(path + "/test.png", "PNG")

    temp_res = 1

    temp_path = os.path.abspath(os.getcwd()) + "/app/static/uploads/test.png"

    resolution(temp_res, temp_path)

def watermark_img(in_img_path, out_img_path, img_to_watermark_path, pos, size, resolution):
    base_image = Image.open(in_img_path)
    watermark_image = Image.open(img_to_watermark_path)

    watermark_image = watermark_image.resize((basewidth,hsize), Image.ANTIALIAS)

    base_image.paste(watermark_image, pos)

    resolution(resolution, in_img_path)

    base_image.show()

    base_image.save(out_img_path)

# res is on a scale of 1-100 95 is optimal
def resolution(res, path):
    image = Image.open(path)

    split_path = os.path.splitext(path)

    image.save(split_path[0] + "_new_res.jpg", quality=res)


