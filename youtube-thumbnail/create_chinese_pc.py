from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/thumbnail-podcast.png"
OUTPUT = "image/thumbnail-pc-chinese.png"

def create_thumbnail(
                     template=TEMPLATE,
                     output=OUTPUT,
                     ):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    draw = ImageDraw.Draw(image)

    draw.text((100,100), "亚太深入焦点",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 85), fill="yellow") 
    draw.text((100,350), "深度的分析视角",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 75), fill="red") 
    draw.text((20,600), "Sampan Podcast",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 65), fill="white") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    create_thumbnail()
