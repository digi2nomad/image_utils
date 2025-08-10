from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/Patrick_McGee.jpg"
OUTPUT = "image/book-review-chinese.png"

def create_thumbnail(
                     template=TEMPLATE,
                     output=OUTPUT,
                     ):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    draw = ImageDraw.Draw(image)

    draw.text((250, 15), "Sampan Review",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 75), fill="white") 
    draw.text((1035,100), "苹果在",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((1035,180), "中国的",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((1035,260), "现代版",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((1035,340), "马歇尔",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 
    draw.text((1035,420), "计划",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 65), fill="yellow") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    create_thumbnail()
