# Phyllotaxis vogel formula
# φ = n * 137,5°
# r = c * √n

import turtle as tl
from math import *
import random

# constants
golden_angle_deg = 137.5

# parameters
time_delay_ms = 1700
c = 30
symbol_colors_1 = ("yellow", "orange","red","brown")
symbol_colors_2 = ("#D0D0FF", "#AAAAE0", "#5555A0","#000060")
symbol_colors_3 = ("#D0FFD0", "#AAE0AA", "#55A055","#006000")
symbol_colors_4 = ("#FFD0D0", "#E0AAAA", "#A05555","#600000")
symbol_colors_5 = ("#D0FFFF", "#AAE0E0", "#55A0D0","#006060")
symbol_colors_6 = ("#FFFFD0", "#E0E0AA", "#A0A055","#606000")
symbol_colors_7 = ("#FFD0FF", "#E0AAE0", "#A055A0","#600060")
colors = [symbol_colors_1, symbol_colors_2, symbol_colors_3, symbol_colors_4, symbol_colors_5, symbol_colors_6, symbol_colors_7]
title = "Phyllotaxis, vogel formula"

# draw one triangle shape at current turtle position7
# size is dependant on distance between symbol and origin (0,0) 
def draw_symbol_triangle(distance_from_origin):
    tl.tracer(n = 3)
    size = 48 + distance_from_origin / 50
    tl.begin_fill()
    tl.left(30)
    tl.forward(size)
    tl.right(120)
    tl.forward(size)
    tl.right(120)
    tl.forward(size)
    tl.end_fill()

# draw one circle shape at current turtle position7
# size is dependant on distance between symbol and origin (0,0) 
def draw_symbol_circle(distance_from_origin):
    tl.tracer(n = 14)
    size = 35 + distance_from_origin / 50
    tl.begin_fill()
    tl.circle(size / 2)
    tl.end_fill()
    
# draw one diamong shape at current turtle position7
# size is dependant on distance between symbol and origin (0,0) 
def draw_symbol_diamond(distance_from_origin):
    tl.tracer(n = 4)
    size = 30 + distance_from_origin / 48
    tl.begin_fill()
    tl.left(45)
    tl.forward(size)
    tl.right(90)
    tl.forward(size)
    tl.right(90)
    tl.forward(size)
    tl.end_fill()

# list of symbol drawing functions 
symbols = [draw_symbol_triangle, draw_symbol_circle, draw_symbol_diamond]

# draw symbols according to vogel formula of given shape and color
def draw_figure(symbol, number_symbols, colors_to_use):
    for number_symbol in range(number_symbols):
        angle = number_symbol * golden_angle_deg
        radius = c * sqrt(number_symbol)
        color_index = int(radius / 100) % len(colors_to_use)
        tl.color(colors_to_use[color_index])
        tl.penup()
        tl.goto(0,0)
        tl.setheading(angle)
        tl.forward(radius)
        tl.pendown()
        symbol(radius)

# set up turtle
def init_turtle():
    #define window size
    screen = tl.Screen()
    screen.setup(width=0.8, height=0.9)
    tl.bgcolor("black")
    tl.title(title)
    # speed up turtle
    tl.speed(0)
    # more settings
    tl.pensize(1)
    tl.hideturtle()
    # assign mouse click handler for terminating script
    screen.onclick(mouse_click_handler)


# mouse click in the window to stop the script
def mouse_click_handler(x,y):
    quit()

# draw next figure, this function calls itself with timer
def update():
    global index_color, index_symbol
    
    symbol_to_use = symbols[index_symbol]
    colors_to_use = colors[index_color]
    if index_color < len(colors) - 1:
        index_color += 1
    else:
        index_color = 0    
    if index_symbol < len(symbols) - 1:
        index_symbol += 1
    else:
        index_symbol = 0
    tl.reset()
    draw_figure(symbol_to_use, 270, colors_to_use)   
    tl.ontimer(update, time_delay_ms) # set timer for next update

# set uo turtle
init_turtle()

# intial value of indexes
index_color = 0; index_symbol = 0

# first tile call update, , this function then calls itself with timer
update()

tl.done()
