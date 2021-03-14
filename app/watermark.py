import PIL
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

from pathlib import Path, PureWindowsPath


def watermark_text(in_img_path, out_img_path, text, pos, font_name, font_size, resolution):
    photo = Image.open(in_img_path)

    drawing = ImageDraw.Draw(photo)

    font_file = get_font_file(font_name)

    temp_font = ImageFont.truetype(str(Path(font_file)), font_size)

    temp_pos = get_position(pos, photo)

    font_color = (0,0,0)
    
    drawing.text(temp_pos, text, fill=font_color, font=temp_font)

    path = out_img_path

    #set test.png later
    photo.save(path + "/test.png", "PNG")

    resolution(resolution, out_img_path)

def watermark_img(
    in_img_path,
    out_img_path,
    img_to_watermark_path,
    pos,
    mark_base_ratio=0.10,
    size=None,
    resolution=None,
):
    base_image = Image.open(in_img_path)

    width, height = base_image.size

    watermark_image = Image.open(img_to_watermark_path)
    watermark_image = watermark_image.resize(
        (int(width * mark_base_ratio), int(height * mark_base_ratio)), Image.ANTIALIAS
    )
    base_image.paste(watermark_image, calc_cordinates(base_image, 0.50, 0.50))
    base_image.show()

    resolution(resolution, out_img_path)

    


def watermark_with_transparency(
    input_image_path, output_image_path, watermark_image_path, position
):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(
        watermark, calc_cordinates(base_image, 0.50, 0.50), mask=watermark
    )
    transparent.show()

    resolution(resolution, out_img_path)


# res is on a scale of 1-100 95 is optimal
def resolution(res, path):
    image = Image.open(path)

    split_path = os.path.splitext(path)

    if res >= 95:
        res = 95

    image.save(split_path[0] + "_new_res.jpg", quality=res)



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
    if pos == "top middle":
        return calc_cordinates(image, .10, .50)
    if pos == "top right":
        return calc_cordinates(image, .10, .75)
    if pos == "bottom left":
        return calc_cordinates(image, .75, .10)
    if pos == "bottom middle":
        return calc_cordinates(image, .75, .50)
    if pos == "bottom right":
        return calc_cordinates(image, .75, .75)
    if pos == "center left":
        return calc_cordinates(image, .50,.10)
    if pos == "center middle":
        return calc_cordinates(image, .50, .50)
    if pos == "center right":
        return calc_cordinates(image, .50, .75)
    else:
        return calc_cordinates(image, .10, .75)


if __name__ == "__main__":
    img = "static/ravberry.png"
    wm_text(img, "imageWaterMarked.png", text="hi there its mike lim", pos=(100, 100))

