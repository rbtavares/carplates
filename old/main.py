# Imports
from PIL import Image, ImageDraw, ImageFont
from sys import argv

# Settings
base = "base/ls.png"
font_path = "fonts/fe-font.ttf"
font_size = 200
text_color = (0, 0, 0)
v_adj_offset = -20
h_adj_offset = 0
txt_wstart, txt_wend = 118, 1162 # Text Area Horizontal Limits (PIXELS)
txt_hstart, txt_hend = 11, 238   # Text Area Vertical Limits (PIXELS)

# Parsing
text = " ".join(argv[1:]).upper()

# Get Text Dimensions
def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3]
    return (text_width, text_height)

# Obtain Text Position

def get_text_start(text_string, font):
    dim = get_text_dimensions(text_string, font)
    print(dim)
    w_int = ((txt_wend - txt_wstart) - dim[0] + h_adj_offset) / 2
    h_int = ((txt_hend - txt_hstart) - dim[1] + v_adj_offset) / 2
    w = txt_wstart + w_int
    h = txt_hstart + h_int
    return (w, h)

# Load Base Image
img = Image.open(base) 

# Apply Text
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, font_size)
pos = get_text_start(text, font)
draw.text((pos[0], pos[1]), text, text_color, font=font)

# Show & Save Image
img.show()
#img.save('.\\plates\\' + text + '.png')