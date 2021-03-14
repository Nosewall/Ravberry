import PIL
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

from pathlib import Path, PureWindowsPath

def watermark_text(in_img_path, out_img_path, text, pos, font_name, font_size, resolution):
    base_image = Image.open(in_img_path)

    drawing = ImageDraw.Draw(base_image)

    font_file = get_font_file(font_name)

    temp_font = ImageFont.truetype(str(Path(font_file)), font_size)

    temp_pos = get_position(pos, base_image)

    font_color = (0,0,0)
    
    drawing.text(temp_pos, text, fill=font_color, font=temp_font)

    path = out_img_path

    #set test.png later
    base_image.save(path + "/test.png", "PNG")

    resolution(res, out_img_path)

def watermark_img(
    in_img_path,
    out_img_path,
    img_to_watermark_path,
    pos,  
    resolution,
    mark_base_ratio=0.10,
):
    base_image = Image.open(in_img_path)

    width, height = base_image.size

    watermark_image = Image.open(img_to_watermark_path)
    watermark_image = watermark_image.resize(
        (int(width * mark_base_ratio), int(height * mark_base_ratio)), Image.ANTIALIAS
    )
    base_image.paste(watermark_image, get_position(pos, base_image))

    path = out_img_path

    base_image.save(path + "/test.png", "PNG")

    base_image.show()

    resolution(res, out_img_path)

    


def watermark_with_transparency(
    in_img_path, out_img_path, img_to_watermark_path, pos, res
):
    base_image = Image.open(in_img_path)
    watermark = Image.open(img_to_watermark_path)
    width, height = base_image.size
    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(
        watermark, get_position(pos, base_image), mask=watermark
    )

    path = out_img_path

    base_image.save(path + "/test.png", "PNG")

    transparent.show()

    resolution(res, out_img_path + "\\test.png")


# res is on a scale of 1-100 95 is optimal
def resolution(res, path):
    image = Image.open(path)

    split_path = os.path.splitext(path)

    if res >= 95:
        res = 95

    image.save(split_path[0] + "_new_res.png", quality=res)



# Returns the x and y pixel location depending on the x_ratio and y_ratio.
def calc_cordinates(image, x_ratio, y_ratio):
    out = image.size
    x = out[0] * x_ratio
    y = out[1] * y_ratio
    x = int(x)
    y = int(y)
    return (x, y)


def get_font_file(font_name):
    if font_name == "Agilia":
        return PureWindowsPath(os.path.join(s.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\AgiliaItalic.ttf"))
    if font_name == "Times New Roman":
        return PureWindowsPath(os.path.join(s.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\TimesNewRoman.ttf"))
    if font_name == "Vonique":
        return PureWindowsPath(os.path.join(s.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\Vonique64.ttf"))
    if font_name == "Comic Sans":
        return PureWindowsPath(os.path.join(s.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\Comic.ttf"))

def get_position(pos, image):
    if pos == "top left":
        return calc_cordinates(image, .10, .10)
    elif pos == "top middle":
        return calc_cordinates(image, .10, .50)
    elif pos == "top right":
        return calc_cordinates(image, .10, .75)
    elif pos == "bottom left":
        return calc_cordinates(image, .75, .10)
    elif pos == "bottom middle":
        return calc_cordinates(image, .75, .50)
    elif pos == "bottom right":
        return calc_cordinates(image, .75, .75)
    elif pos == "center left":
        return calc_cordinates(image, .50,.10)
    elif pos == "center middle":
        return calc_cordinates(image, .50, .50)
    elif pos == "center right":
        return calc_cordinates(image, .50, .75)
    else:
        return calc_cordinates(image, .10, .75)



