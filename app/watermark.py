import PIL
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

from pathlib import Path, PureWindowsPath


def watermark_text(in_img_path, out_img_path, text, pos, font_name, font_size, font_color):
    photo = Image.open(in_img_path)

    drawing = ImageDraw.Draw(photo)

    font_file = PureWindowsPath(
        os.path.join(
            if font_name == "Agilia"
                return os.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\AgiliaItalic.ttf"
            if font_name == "Times New Roman"
                return os.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\TimesNewRoman.ttf"
            if font_name == "Vonique 64"
                return os.path.abspath(os.getcwd()) + "\\app\\static\\fonts\\Vonique64.ttf"
        )
    )

    tfont = ImageFont.truetype(str(Path(filename)), font_size)

    drawing.text(pos, text, fill=font_color, font=temp_font)

    path = out_img_path
    photo.save(path + "/test.png", "PNG")


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


# res is on a scale of 1-100 95 is optimal
def resolution(res, path):
    image = Image.open(path)

    split_path = os.path.splitext(path)

    image.save(split_path[0] + "_new_res.jpg", quality=res)



# Returns the x and y pixel location depending on the x_ratio and y_ratio.
def calc_cordinates(image, x_ratio, y_ratio):
    out = image.size
    x = out[0] * x_ratio
    y = out[1] * y_ratio
    x = int(x)
    y = int(y)
    return [x, y]


if __name__ == "__main__":
    img = "static/ravberry.png"
    wm_text(img, "imageWaterMarked.png", text="hi there its mike lim", pos=(100, 100))
