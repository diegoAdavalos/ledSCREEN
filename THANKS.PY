import time
import random
import board
import displayio
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.triangle import Triangle  # Import the missing Triangle class

# Constants
PUMPKIN_CENTER_X = 120
PUMPKIN_CENTER_Y = 100
PUMPKIN_RADIUS = 25
PUMPKIN_OFFSET = 7
STEM_OFFSET = 48
STEM_WIDTH = 12
STEM_HEIGHT = 24
MOON_X = 20
MOON_Y = 30
MOON_RADIUS = 10
CRESENT_OFFSET = 5
LIGHTNING = [(180, 0), (165, 40), (170, 40), (166, 60), (185, 30), (175, 30), (190, 0)]

# Colors
PUMPKIN = 0x964B00
BACKGROUND = 0Xffde4b
MOON = 0xCCCC00
STEM = 0xffffff
WHITE = 0x000000
WHITE1 = 0xFF0000

displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

dbus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(dbus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 3)
color_palette = displayio.Palette(6)
color_palette[0] = BACKGROUND
color_palette[1] = PUMPKIN
color_palette[2] = MOON
color_palette[3] = STEM
color_palette[4] = WHITE
color_palette[5] = WHITE1
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

display.root_group = main_group


pumpkin = []
rect = Rect(100, 80, width=50, height=75, fill=PUMPKIN, outline=WHITE)
pumpkin.append(rect)
for things in pumpkin:
    main_group.append(things)

stem = Rect(125, 90, width=8, height=25, fill=STEM)
main_group.append(stem)
stem1 = Rect(105, 90, width=8, height=25, fill=STEM)
main_group.append(stem1)
stem2 = Rect(125, 90, width=4, height=15, fill=WHITE)
main_group.append(stem2)
stem12 = Rect(105, 90, width=4, height=15, fill=WHITE)
main_group.append(stem12)


feathers = []
for i in range(5):
    val = random.randint(1, 4)
    if val == 2 or val == 3:
        cool = Rect(105 + (i * 9), 55, width=8, height=25, fill=STEM)
        feathers.append(cool)
    feather = Rect(105 + (i * 9), 55, width=8, height=25, fill=MOON)
    feathers.append(feather)
for x in feathers:
    main_group.append(x)

cresent = Circle(MOON_X, MOON_Y, MOON_RADIUS, fill=MOON)
main_group.append(cresent)
shadow = Circle(120, 120, MOON_RADIUS, fill=STEM)
main_group.append(shadow)
shadow1 = Circle(120, 120, MOON_RADIUS - 5, fill=WHITE1)
main_group.append(shadow1)




count = 0
direction = 1
while True:

    
    pumpkin_offset = 2 *  random.randint(0, 10) 
    for thing in pumpkin:
        thing.y = 80 + pumpkin_offset
 
    display.refresh()
    time.sleep(0.05)
    
    count += direction
    if count > 100 or count < 0:
        direction *= -1 

