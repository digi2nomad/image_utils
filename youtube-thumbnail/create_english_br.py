from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/Patrick_McGee.jpg"
OUTPUT = "image/book-review-english.png"

def create_thumbnail(
                     template=TEMPLATE,
                     output=OUTPUT,
                     ):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    draw = ImageDraw.Draw(image)

    draw.text((250, 15), "Sampan Review",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 75), fill="white") 
    draw.text((1035,100), "Apple's",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1035,180), "modern",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1035,260), "day",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1035,340), "Marshall",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1035,420), "plan",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 
    draw.text((1035,500), "in China",  
              font=ImageFont.truetype("font/Gendy.otf", 65), fill="yellow") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    create_thumbnail()
