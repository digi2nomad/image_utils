from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/Wang_gungwu.png"
OUTPUT = "image/thumbnail-chinese.png"

def create_thumbnail(
                     template=TEMPLATE,
                     output=OUTPUT,
                     ):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    draw = ImageDraw.Draw(image)

    draw.text((750,10), "Book Review:",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1150,25), "Ep0",  
              font=ImageFont.truetype("font/Gendy.otf", 45), fill="white") 
    draw.text((785,90), "王赓武教授生平和他的书:",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((950,170), "海外华人社群的历史",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((30, 800), "Sampan Review",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 75), fill="white") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    create_thumbnail()
