# Polygon
# -------
# drawing n rotated polygons with n corners using Turtle Graphics
# n: number of points Polygon
# dalpha: angle over which the turtle has to turn to draw next side 
# dalpha = 360° / n
# D: length of one side of polygon
# R: radius or distance corner point to center
# D/2 = R * tan(360° / n / 2)
# => D = 2 * R * tan(360° / n / 2)
# => D = 2 * R * tan(dalpha / 2)
# summary, needed formulas:
# angle over which the turtle has to turn to draw next side
# dalpha = 360° / n
# length of side turtle has to draw
# D = 2 * R * tan(dalpha / 2)

import turtle as tl
from math import *

# settings for turtle graphics
def init_turtle():
    tl.Screen().setup(900,900) # size of image in pixels
    tl.speed(0) # max speed
    tl.tracer(0) # wait to update image untill turtle.update() is called: big speed increase
    tl.hideturtle() # hide the turtle icon
    tl.pensize(2) # thickness of lines
    tl.bgcolor("black") # background color of image

# draw one polygon, given number of corner points, side length and angle between sides
def draw_polygon(n_points, side_polygon, delta_angle):
    for n in range(n_points):
        c = abs(int(n - n_points / 2 + 0.5)) # color to use for current polygon side
        col = colors[c % number_colors] # use one color out of list
        tl.color(col)
        tl.forward(side_polygon) # draw next side
        tl.right(delta_angle) # turn right amount for next side

# draw set of rotated polygons, uses draw_polygon()
# number of polygons, radius and number of corner points of 1 polygon are given
def draw_set_rotated_polygons(number_polygons, radius_polygon, n_points_polygon):
    tl.title(f"{number_polygons:<3} polygons with {n_points_polygon:<3} corner points")
    # angle_between_polygons: angle between 2 successive polygons in the set
    angle_between_polygons = 360 / number_polygons 
    # angle_between_sides: angle over which the turtle has to turn to draw next side of polygon
    angle_between_sides = 360 / n_points_polygon
    # side_polygon: length of one side of polygon 
    side_polygon = 2 * radius_polygon * tan(radians(angle_between_sides / 2))
    for p in range(number_polygons):
        tl.right(angle_between_polygons) # turn right amount for next polygon
        draw_polygon(n_points_polygon, side_polygon, angle_between_sides)
    tl.update() # update the image here to show new set of polygons

# this function draws next image and
# calls itself with a timer delay using turtle.ontimer()
# uses draw_set_rotated_polygons()
def update():
    global number_polygons, delta_number_polygons # this function has to modify some global variables
    tl.clear() # delete previous image
    draw_set_rotated_polygons(number_polygons, 180, number_polygons)
    # number_polygons counts up and down between two values
    if number_polygons >= 30: 
        delta_number_polygons = -2
    elif number_polygons <= 6:
        delta_number_polygons = +2
    number_polygons += delta_number_polygons
    tl.ontimer(update, 100) # call this function again after timer delay
    

# generate set of colors to use, using list comprehension
# creates a list of strings with format "#RRGGBB"
# the three R,G,B color components are hexadecimal 2 digit numbers, 00 to FF
colors = [f"#{(c):02x}{(abs(c-127)*2):02x}{(255-c):02x}" for c in range(0,256,18)]
number_colors = len(colors)

# starting value for number of polygons
# also used for number of corner points for 1 polygon
number_polygons = 6
# starting value for step to increase or decrease number_polygons
delta_number_polygons = +2

# turtle settings
init_turtle()

# first time call update() here, after this the function calls itself with timer delay
update()

tl.exitonclick()

    
