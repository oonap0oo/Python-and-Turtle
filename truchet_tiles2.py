# Truchet Tiles
import turtle as tl
import random


# parameters
tile_size = 50 # size of one side of square tile measured in pixels
window_width_tiles = 30 # window width measured in number of tiles
window_height_tiles = 18
color_bg = "#fffffa"
color_fg = "black"
line_width = 2
title = "Truchet Tiles using Python & Turtle"
time_delay_ms = 1500

#   tile numbers
#   ------------
#   Tile            number
#   up-left         1
#   up-right        2
#   down-right      3
#   down-left       4

# pattern definitions, which tile number goes where
pattern_D = (
    (1,4),
    (2,3))

pattern_E = (
    (1,2,3,4),
    (2,1,4,3),
    (3,4,1,2),
    (4,3,2,1))

pattern_L = (
    (3,4,3,4),
    (2,3,4,1),
    (3,2,1,4),
    (2,1,2,1))

pattern_N = (
    (1,4,3,2),
    (2,3,4,1),
    (3,2,1,4),
    (4,1,2,3))

pattern_V = (
    (2,4,3,4,2,4,1,4),
    (4,3,4,2,4,1,4,2),
    (3,4,2,4,1,4,2,4),
    (4,2,4,1,4,2,4,3),
    (2,4,1,4,2,4,3,4),
    (4,1,4,2,4,3,4,2),
    (1,4,2,4,3,4,2,4),
    (4,2,4,3,4,2,4,1)
    )

pattern_Y = (
    (1,3,4,2),
    (3,1,2,4),
    (2,4,3,1),
    (4,2,1,3)
    )

pattern_a = (
    (1,3,2,4),
    (3,1,4,2),
    (4,2,3,1),
    (2,4,1,3)
    )

pattern_X = (
    (2,4,3,4,4,2),
    (2,1,2,2,4,4),
    (3,4,4,2,2,4),
    (2,2,4,4,2,1),
    (4,2,2,4,3,4),
    (4,4,2,1,2,2)
    )

pattern_U = (
    (1,3,4,2),
    (3,4,2,1),
    (4,2,1,3),
    (2,1,3,4)
    )

pattern_1 = (
    (4,2,4,2,1,3,1,3),
    (1,3,1,3,4,2,4,2),
    (3,1,3,1,2,4,2,4),
    (1,3,1,3,4,2,4,2),
    (3,1,3,1,2,4,2,4),
    (2,4,2,4,3,1,3,1),
    (4,2,4,2,1,3,1,3),
    (2,4,2,4,3,1,3,1),
    )

pattern_2 = (
    (3,4,2,1,3,4),
    (4,2,4,3,1,3),
    (2,4,1,2,3,1),
    (3,1,4,3,2,4),
    (1,3,1,2,4,2),
    (2,1,3,4,2,1)
    )

pattern_3 = (
    (1,2,1,2,4,2,3,4,1,3),
    (3,4,3,4,2,4,2,1,3,1),
    (1,2,1,2,4,2,4,3,1,3),
    (4,1,2,3,1,3,1,2,4,2),
    (1,4,3,2,4,2,4,3,1,3),
    (4,3,4,3,1,3,1,2,4,2),
    (2,1,2,1,3,1,3,4,2,4),
    (4,3,4,3,1,3,2,1,4,2),
    (2,1,2,1,3,4,3,4,3,4),
    (3,4,3,4,2,1,2,1,2,1)
    )

pattern_G = (
    (4,2),
    (2,4)
    )

pattern_H = (
    (1,3,3),
    (3,1,3),
    (3,3,1)
    )

pattern_S = (
    (3,4,1,2),
    )

pattern_R = (
    (3,4),
    )

pattern_T = (
    (1,3,4,2),
    )

pattern_Z = (
    (1,2,4,3),
    (3,1,2,4)
    )
    
# patterns to draw
patterns = (pattern_D,
            pattern_E,
            pattern_L,
            pattern_N,
            pattern_V,
            pattern_Y,
            pattern_a,
            pattern_X,
            pattern_U,
            pattern_1,
            pattern_2,
            pattern_3,
            pattern_G,
            pattern_H,
            pattern_S,
            pattern_R,
            pattern_T,
            pattern_Z)

patterns = random.sample(patterns, len(patterns))

#patterns = (pattern_Z,) # to test 1 pattern

# set up turtle
def init():
    #   Mode:       Initial turtle heading:     positive angles:
    #   “standard”  to the right (east)         counterclockwise
    tl.mode("standard")
    #define window size
    screen = tl.Screen()
    screen.setup(width = window_width_tiles * tile_size , height = window_height_tiles * tile_size)
    # assign mouse click handler for terminating script
    screen.onclick(mouse_click_handler)
    # set speed
    tl.speed(0) # fastest drawing speed
    tl.tracer(0) # pauze screen updates untill tl.update() command is encountered, speeds up drawing
    # more settings
    tl.pensize(line_width)
    tl.hideturtle()
    tl.bgcolor(color_bg)
    tl.color(color_fg)
    tl.title(title)

# draw a single tile specified by number; x_top, y_top is the top left corner
def drawtile(tile_number, x_top, y_top):
    # three points depend on tile number
    match tile_number:
        case 1:
            x1, y1 = x_top, y_top
            x2, y2 = x_top + tile_size, y_top
            x3, y3 = x_top, y_top - tile_size
        case 2:
            x1, y1 = x_top + tile_size, y_top
            x2, y2 = x_top + tile_size, y_top - tile_size
            x3, y3 = x_top, y_top
        case 3:
            x1, y1 = x_top + tile_size, y_top - tile_size
            x2, y2 = x_top, y_top - tile_size
            x3, y3 = x_top + tile_size, y_top
        case 4:
            x1, y1 = x_top, y_top - tile_size
            x2, y2 = x_top, y_top
            x3, y3 = x_top + tile_size, y_top - tile_size
    # draw the triangular filled shape of specified tile
    tl.penup()
    tl.goto(x1,y1)
    tl.pendown()
    tl.begin_fill()
    tl.goto(x2,y2)
    tl.goto(x3,y3)
    tl.goto(x1,y1)
    tl.end_fill()
    # draw lines around border tile
    tl.penup()
    tl.goto(x_top,y_top)
    tl.pendown()
    for _ in range(4):
        tl.forward(tile_size)
        tl.right(90)
    
# draw a pattern of tiles; pattern is tuple of tuples containing the rows and columns of tile numbers
def draw_pattern(pattern, x_top, y_top):
   for row_number, row in enumerate(pattern):
       y = y_top - tile_size * row_number
       for column_number, tile in enumerate(row):
           x = x_top + tile_size * column_number
           drawtile(tile, x, y)

# draw a pattern several times as specified
def repeat_pattern(pattern, number_of_rows, number_of_columns):
    tl.clear() # clear screen
    x_top = -window_width_tiles * tile_size // 2
    y_top = window_height_tiles * tile_size // 2
    width_pattern = len(pattern[0])
    height_pattern = len(pattern)
    for row in range(number_of_rows):
        y_top_pattern = y_top - row * height_pattern * tile_size 
        for column in range(number_of_columns):
            x_top_pattern = x_top + column * width_pattern * tile_size
            draw_pattern(pattern, x_top_pattern, y_top_pattern)
    tl.update()

# mouse click in the window to stop the script
def mouse_click_handler(x,y):
    quit()

# loop through patterns; calls itself with timer function of turtle
def update():
    tl.ontimer(update, time_delay_ms) # set timer for next update
    global index
    pattern = patterns[index]
    if index < len(patterns) - 1:
        index += 1
    else:
        index = 0
    rows = window_height_tiles // len(pattern) + 1
    cols = window_width_tiles // len(pattern[0]) + 1
    repeat_pattern(pattern, rows, cols)
    
   

index = 0 # will keep track of which pattern has to be drawn
init()

update() # first time call update immediatly




     

