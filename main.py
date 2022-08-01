#python3

#> Imports
from PIL import Image, ImageDraw, ImageFont
from imgutils import *
import sys

#> Plate Settings

corner_radius = 50
rounded = True
border = False

plate_size   = (520*5, 120*5)
plate_color  = (255, 255, 255)

lstrip_width  = 275
lstrip_color  = (0, 0, 175)

letter_cc    = "P"
letter_font  = ImageFont.truetype(r'fonts/din1451alt.ttf', 150)

emblem = True
emblem_path = r"emblem/eu.png"
emblem_margin = 50

text = " ".join(sys.argv[1:])
text_font = ImageFont.truetype(r'fonts/din1451alt.ttf', 625)
#text_font = ImageFont.truetype(r'fonts/fe-font.ttf', 525)

#> Build Plate
plate = Image.new(
    mode='RGBA',
    size=plate_size,
    color=plate_color
)

#> Build LStrip
lstrip = Image.new(
    mode='RGBA',
    size=(lstrip_width, plate_size[1]),
    color=lstrip_color
)

# Add CC Letter
letter = Image.new(mode='RGBA', size=lstrip.size, color=(0,0,0,0))
ImageDraw.Draw(letter).text((0, 0), letter_cc, fill="white", font=letter_font)
letter = trim(letter)
lstrip = center_paste(lstrip, letter, (0, round(lstrip.size[1]/2), lstrip.size[0], lstrip.size[1]))

# Add Emblem
if emblem:
    emblem = Image.open(emblem_path)
    emblem = trim(emblem)

    if emblem.size[0] > lstrip.size[0] + emblem_margin:
        diff = emblem.size[0] / (lstrip.size[0] - emblem_margin)
        emblem = emblem.resize((round(emblem.size[0]/diff), round(emblem.size[1]/diff)))

    if emblem.size[1] > round(lstrip.size[1]/2) + emblem_margin:
        diff = emblem.size[1] / (round(lstrip.size[1]/2) - emblem_margin)
        emblem = emblem.resize((round(emblem.size[0]/diff), round(emblem.size[1]/diff)))

    lstrip = center_paste(lstrip, emblem, (0, 0, lstrip.size[0], round(lstrip.size[1]/2)))

#> Build Main Text
txt = Image.new(mode='RGBA', size=(round(plate.size[0]*1.5), round(plate.size[1]*1.5)), color=(0,0,0,0))
ImageDraw.Draw(txt).text((0, 0), text.upper(), fill="black", font=text_font)
txt = trim(txt)
if txt.size[0] > plate.size[0] - lstrip.size[0]:
    print('too big')
    exit()
plate = center_paste(plate, txt, (lstrip.size[0], 0, plate.size[0], plate.size[1]))

#> Mount Plate
plate.paste(lstrip, (0, 0))

#> Finalize Layout
if rounded:
    if border:
        ImageDraw.Draw(plate).rounded_rectangle((0, 0, plate.size[0], plate.size[1]), outline="black", width=10, radius=corner_radius)
    plate = add_corners(plate, corner_radius)

print(f'Created plate \"{text}\"')
plate.show()
plate.save(text + '.png')
