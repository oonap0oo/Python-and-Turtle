# Randomly generated Truchet Tiles using Python & Turtle
# when key <s> is pressed save the pattern to a text file
# mouse click in the window to stop the script
import turtle as tl
import random

# parameters
tile_size = 50 # size of one side of square tile measured in pixels
window_width_tiles = 36 # window width measured in number of tiles
window_height_tiles = 18
pattern_half_number_of_rows = 3
pattern_half_number_of_columns = 3
color_bg = "#fffff8"
color_fg = "black"
line_width = 2
title = "Randomly generated Truchet Tiles using Python & Turtle"
time_delay_ms = 1500
patterns_output_file_name = "patterns.txt"

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
    # assign key <s> press event handler for saving pattern to file
    tl.onkey(key_save_pattern_handler, "s")
    # set speed
    tl.speed(0) # fastest drawing speed
    tl.tracer(0) # pauze screen updates untill tl.update() command is encountered, speeds up drawing
    # more settings
    tl.pensize(line_width)
    tl.hideturtle()
    tl.bgcolor(color_bg)
    tl.color(color_fg)
    tl.title(title)

#   tile numbers
#   ------------
#   Tile            number
#   up-left         1
#   up-right        2
#   down-right      3
#   down-left       4

# draw a single tile specified by number
# x_top, y_top is the top left corner
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
    
# draw a pattern of tiles; pattern is tuple of tuples
# containing the rows and columns of tile numbers
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
    
# tiles on lower half of pattern are complementary to those in upper half
complement_tiles_vert = {1:4, 4:1, 2:3, 3:2}

# tiles on right half of pattern are complementary to those in left half
complement_tiles_horz = {1:2, 2:1, 4:3, 3:4}

# random pattern using complementery tiles for pleasing result
def generate_random_pattern(half_number_of_rows, half_number_of_columns):
    pattern = []
    value = random.randint(1,4) # first tile used
    for row in range(half_number_of_rows):
        new_row = []
        for column in range(half_number_of_columns):
            new_row.append(value)
            value += random.choice([-3,-1,1,3]) # next tile based on previous either add or subtract 1 or 3
            value = (value - 1) % 4 + 1 # tile value wraps around if outside 1..4
        for column in range(half_number_of_columns - 1, -1, -1):
            first_tile = new_row[column]
            new_row.append(complement_tiles_horz[first_tile]) # right half is complementary to left
        pattern.extend([new_row])
    for row in range(half_number_of_rows - 1, -1, -1):
        new_row = []
        for column in range(half_number_of_columns * 2):   
            first_tile = pattern[row][column]
            new_row.append(complement_tiles_vert[first_tile]) # lower half is complementary to upper
        pattern.extend([ new_row ])
    return(pattern)

# mouse click in the window to stop the script
def mouse_click_handler(x,y):
    update()

# when key <s> is pressed save the pattern to a text file
def key_save_pattern_handler():
    global pattern
    print(*pattern, sep="\n") # print generated pattern to console
    print()
    with open(patterns_output_file_name, mode = "a") as file:
        file.write(str(pattern))
        file.write("\n")
    print("Pattern saved to", patterns_output_file_name),"\n\n"

# loop through random patterns
def update():
    global pattern
    pattern = generate_random_pattern(pattern_half_number_of_rows, pattern_half_number_of_columns)
    rows = window_height_tiles // len(pattern) + 1
    cols = window_width_tiles // len(pattern[0]) + 1
    repeat_pattern(pattern, rows, cols)
    tl.listen()
    
   
init()

print("""Randomly generated Truchet Tiles using Python & Turtle
when key <s> is pressed save the pattern to a text file
mouse click in the window to show next pattern""")

update() # first time call update immediatly

tl.done()


     

