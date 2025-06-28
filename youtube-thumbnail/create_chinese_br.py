from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/Website_Jin_book_talk.jpeg"
FONTFILE = "font/Rockstar-ExtraBold.otf"
OUTPUT = "image/thumbnail-chinese.png"
START_OFFSET_TEXT = (850, 125)
TEXTCOLOR = (255, 0, 0, 255)
LINE_SPACING = 140
SEPARATOR = "|"

def create_thumbnail(text,
                     font_size,
                     template=TEMPLATE,
                     output=OUTPUT,
                     fontfile=FONTFILE,
                     text_color=TEXTCOLOR,
                     start_offset=START_OFFSET_TEXT,
                     line_spacing=LINE_SPACING):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    font = ImageFont.truetype(fontfile, font_size)
    draw = ImageDraw.Draw(image)
    offset = start_offset

    #for i, line in enumerate(text.split(SEPARATOR)):
    #    left, top = offset
    #    top += i * line_spacing
    #    new_offset = (left, top)
    draw.text((100,1050), "Book Review:",  
              font=ImageFont.truetype("font/Gendy.otf", 175), fill="yellow") 
    draw.text((100,1250), "金刻羽: 官二代精英",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 185), fill="yellow") 
    draw.text((100,1520), "为中国模式辩护",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 185), fill="yellow") 
    draw.text((30, 1800), "Sampan Review",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 165), fill="white") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} 'title text seperated with bars' 'text font size(e.g.: 165)'")
        sys.exit(1)
    create_thumbnail(sys.argv[1], int(sys.argv[2]))
