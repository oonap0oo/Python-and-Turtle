# Python-and-Turtle
Projects using CPython and Turtle graphics

## truchet_tiles2.py
![truchet_tiles.gif](truchet_tiles.gif)
This script shows a series of patterns of Truchet Tiles.

The tiles are drawn using the Turtle libary. All patters are made from 4 different tiles.

The patterns are defined as rows and columns of tile numbers, for this nested tuples are used:

    pattern_X = (
        (2,4,3,4,4,2),
        (2,1,2,2,4,4),
        (3,4,4,2,2,4),
        (2,2,4,4,2,1),
        (4,2,2,4,3,4),
        (4,4,2,1,2,2)
        )

## sierpinsky_turtle_cpython.py

![sierpinsky_turtle_cpython_screenshot.png](sierpinsky_turtle_cpython_screenshot.png)

This script draws a Sierpinsky triangle recursively using turtle. 

This one makes use extra functionality in CPython's turtle on the PC, such as drawing filled shapes. 

The code shows several triangles using  successively deeper recursion.
