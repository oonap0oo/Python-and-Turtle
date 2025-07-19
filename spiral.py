import turtle as tl
from math import *

def init():
    #define window size
    screen = tl.Screen()
    screen.setup(width = screen_width, height = screen_height)
    # set speed of turtle
    tl.speed(0)
    tl.tracer(0)
    tl.title(title)
    tl.pensize(line_width)
    tl.bgcolor(color_bg)
    tl.hideturtle()
    # assign mouse click handler for terminating script
    screen.onclick(mouse_click_handler)

# draw one spiral
def spiral(frequency):
    tl.clear()
    angle = number_rotations * 360
    for step in range(number_steps_per_rotation * number_rotations):
        length = 0.05 * angle * sin(frequency * radians(angle))
        distance = angle ** 1.2 / 15
        col = colors[int( (1 + copysign(1,length)) / 2 )]
        tl.penup()
        tl.setheading(angle)
        tl.goto(0,0)
        tl.forward(distance - length / 2)
        tl.pendown()
        tl.color(col)
        tl.forward(length)
        angle -= delta_angle_deg
    tl.update()

# mouse click in the window to stop the script
def mouse_click_handler(x,y):
    quit()

# draw new psiral and update frequency
def update(frequency, delta_frequency):
    spiral(frequency)
    if frequency >= freq_upper:
        delta_frequency = -3
    elif frequency <= freq_lower:
        delta_frequency = 3
    frequency += delta_frequency
    tl.ontimer(update(frequency, delta_frequency), time_delay_ms) # set timer for next update

# parameters
colors = ("#3b77a8", # blue color
         "#ffe05d") # yellow color
screen_width, screen_height = 1300, 800
number_rotations = 9
number_steps_per_rotation = 120
delta_angle_deg = 360 / number_steps_per_rotation
line_width = 4
color_bg = "black"
title = "Spiral"
time_delay_ms = 30
freq_upper = 11
freq_lower = -11


init()
  
update(freq_upper, -3) # first time call update immediatly

tl.done()
