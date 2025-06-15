from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/thumbnail-template.png"
FONTFILE = "font/Rockstar-ExtraBold.otf"
FONTSIZE = 175
OUTPUT = "image/thumbnail.png"
START_OFFSET_TEXT = (850, 125)
TEXTCOLOR = (255, 0, 0, 255)
LINE_SPACING = 140
SEPARATOR = "|"

def create_thumbnail(text,
                     template=TEMPLATE,
                     output=OUTPUT,
                     fontfile=FONTFILE,
                     font_size=FONTSIZE,
                     text_color=TEXTCOLOR,
                     start_offset=START_OFFSET_TEXT,
                     line_spacing=LINE_SPACING):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    font = ImageFont.truetype(fontfile, font_size)
    draw = ImageDraw.Draw(image)
    offset = start_offset

    for i, line in enumerate(text.split(SEPARATOR)):
        left, top = offset
        top += i * line_spacing
        new_offset = (left, top)
        draw.text(new_offset, line, font=font, fill=text_color)
    draw.text((100,200), "Asia Pacific",  
              font=ImageFont.truetype("font/Gendy.otf", 100), fill="yellow") 
    draw.text((100,300), "News",  
              font=ImageFont.truetype("font/Gendy.otf", 100), fill="yellow") 
    draw.text((100,400), "Daily Update",  
              font=ImageFont.truetype("font/Gendy.otf", 100), fill="yellow") 
    draw.text((30,600), "Sampan Podcast",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 65), fill="white") 

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} 'text on banner'")
        sys.exit(1)
    create_thumbnail(sys.argv[1])
