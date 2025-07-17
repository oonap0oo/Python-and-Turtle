# define function to draw ellipse using Turtle graphics
# use this function to draw a python logo
import turtle as tl
from math import *

# turtle graphics does have circle but no ellipse
# this function draws ellipse
# a, b: size of ellipse
# direction: positive for counterclockwise, negative for clockwise
# keyword arguements:
# extent: part of ellipse to draw as angle in degrees
# npoints: number of steps to use
def ellipse(a, b , direction, **kwargs):
    def rotate(x, y, angle_deg): # rotate x,y point by angle
        angle_rad = radians(angle_deg)
        xr = dx * cos(angle_rad) - dy * sin(angle_rad)
        yr = dx * sin(angle_rad) + dy * cos(angle_rad)     
        return([xr, yr])
    # unpack keyword parameters if present
    extent = kwargs.get("extent", 360)
    npoints = kwargs.get("npoints", 100)
    # store current position and heading
    x_start, y_start = tl.pos()
    angle_start = tl.heading()
    # loop to draw ellipse
    for step in range(npoints):
        angle = step / npoints * extent
        dx = copysign(1, direction) * a * (cos(radians(angle)) - 1)
        dy = b * sin(radians(angle))
        dx, dy = rotate(dx, dy, angle_start - 90)
        tl.goto(x_start + dx, y_start + dy)
    # leave turtle at new correct heading after the ellipse drawing
    new_angle = angle_start + extent * copysign(1, direction)
    tl.setheading(new_angle)
    

# draw one half of python logo and a seperate circle for the eye
def draw_shape(color_shape, color_eye):
    # draw the shape
    tl.color(color_shape)
    tl.begin_fill()
    tl.pendown()
    tl.forward(100)
    tl.circle(50, extent = 90)
    tl.forward(185)
    ellipse(150 , 75, 1, extent=180)
    tl.forward(70)
    tl.left(90)
    tl.forward(125)
    tl.circle(-10, extent = 180)
    tl.forward(200)
    ellipse(150, 75, 1, extent=  180)
    tl.forward(80)
    tl.left(90)
    tl.forward(92)
    tl.circle(-60, extent = 90)
    tl.end_fill()
    # draw the eye
    x_current, y_current = tl.pos()
    angle_current = tl.heading()
    tl.setheading(90 + angle_current)
    tl.penup()
    tl.forward(255)
    tl.left(90)
    tl.forward(5)
    tl.pendown()
    tl.color(color_eye)
    tl.begin_fill()
    tl.circle(27)
    tl.end_fill()
    tl.penup()
    tl.goto(x_current, y_current)

def init():
    #define window size
    screen = tl.Screen()
    screen.setup(width = screen_width, height = screen_height)
    # set speed of turtle
    tl.speed(0)
    tl.tracer(n = 2)
    tl.title(title)


# parameters
color1 = "#3b77a8" # blue color
color2 = "#ffe05d" # yellow color
screen_width, screen_height = 1300, 800
background_color = "white"
title = "Python logo using Turtle graphics with ellipse function"

# set up turtle
init()

# draw the blue half
tl.penup()
tl.goto(-300,0)
tl.setheading(0)
draw_shape(color1, background_color)

# draw the yellow half
tl.penup()
tl.goto(tl.xcor()+110,tl.ycor()-18)
tl.pendown()
tl.setheading(180)
draw_shape(color2, background_color)

# draw text
tl.color(color1)
tl.penup()
tl.goto(100,80)
tl.write("python", align = "left", font = (None, 65, "normal"))
tl.color(color2)
tl.goto(110,0)
tl.write("using Turtle graphics", align = "left", font = (None, 20, "normal"))

