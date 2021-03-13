from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(in_img_path, out_img_path, text, pos, size, color, font_name, resolution):
    photo = Image.open(in_img_path)

    drawing = ImageDraw.Draw(photo)

    font = ImageFont.truetype(font_name, size)

    drawing.text(pos, text, fill=color, font=font)

    photo.show()

    photo.save(out_img_path)


def watermark_img(in_img_path, out_img_path, img_to_watermark_path, pos, size, resolution)
    base_image = Image.open(in_img_path)
    watermark_image = Image.open(img_to_watermark_path)

    watermark_image = watermark_image.resize((basewidth,hsize), Image.ANTIALIAS)

    base_image.paste(watermark_image, pos)

    base image = resolution(resolution, base_image)

    base_image.show()

    base_image.save(out_img_path)

def resolution(res, photo)
    


if __name__ == '__main__':
    img = 'static/ravberry.png'
    wm_text(img, 'imageWaterMarked.png', text='hi there its mike lim', pos=(100, 100))