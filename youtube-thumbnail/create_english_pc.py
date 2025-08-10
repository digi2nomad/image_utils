from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/thumbnail-podcast.png"
OUTPUT = "image/thumbnail-pc-english.png"

def create_thumbnail(
                     template=TEMPLATE,
                     output=OUTPUT,
                     ):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    draw = ImageDraw.Draw(image)

    draw.text((45,100), "Asia Pacific Deep Dive",  
              font=ImageFont.truetype("font/Gendy.otf", 70), fill="yellow") 
    draw.text((200,280), "in-depth",  
              font=ImageFont.truetype("font/Gendy.otf", 115), fill="red") 
    draw.text((200,420), "analysis",  
              font=ImageFont.truetype("font/Gendy.otf", 115), fill="red") 
    draw.text((20,600), "Sampan Podcast",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 65), fill="white") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    create_thumbnail()
