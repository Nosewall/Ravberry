import PIL

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark_text(in_img_path, out_img_path, text, pos):
    photo = Image.open(in_img_path)
    
    drawing = ImageDraw.Draw(photo)

    temp_color = (0,0,0)

    temp_size = 40

    temp_font = ImageFont.truetype("static/fonts/AgiliaItalic.ttf", temp_size)

    drawing.text(pos, text, fill = temp_color, font = temp_font)

    path = out_img_path
    photo.save(path + "/test.png", "PNG")

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
    image = image.open(path)

    split_path = path.splitext(path)

    image.save(split_path[0] + "_new_res" + split_path[1], quality=res)

    
if __name__ == '__main__':
    img = 'static/ravberry.png'
    wm_text(img, 'imageWaterMarked.png', text='hi there its mike lim', pos=(100, 100))
