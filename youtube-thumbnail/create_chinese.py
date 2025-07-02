from string import ascii_lowercase, digits
import sys

from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "image/thumbnail-template.png"
#FONTFILE = "font/SentyMovableType.ttf"
#FONTFILE = "font/HanyiSentyZhaoRegular.ttf"
FONTFILE = "font/HanyiSentyPagodaRegular.ttf"
#FONTFILE = "font/HanyiSentyMarshmallowChalk-B.ttf"
#FONTFILE = "font/HanyiSentyMarshmallowChalk-A.ttf"
#FONTFILE = "font/HanyiSentyGraffiti.ttf"
#FONTFILE = "font/GongfanmianfeitiRegular.ttf"
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

    for i, line in enumerate(text.split(SEPARATOR)):
        left, top = offset
        top += i * line_spacing
        new_offset = (left, top)
        draw.text(new_offset, line, font=font, fill=text_color)
    draw.text((100,150), "亚太每日",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 120), fill="yellow") 
    draw.text((100,300), "新闻焦点",  
              font=ImageFont.truetype("font/HanyiSentyPagodaRegular.ttf", 120), fill="yellow") 
    draw.text((30,550), "Sampan Podcast",  
              font=ImageFont.truetype("font/Bohme-Rounded.ttf", 65), fill="white") 

    draw.line((   0,   0,   0, 765), fill="yellow", width=10);
    draw.line((   0,   0,1410,   0), fill="yellow", width=10);
    draw.line((   0, 765,1410, 765), fill="yellow", width=10);
    draw.line((1410, 765,1410,   0), fill="yellow", width=20);

    out = Image.alpha_composite(base, image)

    out.save(output)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} 'title text seperated with bars' 'text font size(e.g.: 125)'")
        sys.exit(1)
    create_thumbnail(sys.argv[1], int(sys.argv[2]))
