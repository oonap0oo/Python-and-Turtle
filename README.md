# Python-and-Turtle
Projects using CPython and Turtle graphics

## truchet_tiles2.py
![truchet_tiles.gif](truchet_tiles.gif)

code:
![https://github.com/oonap0oo/Python-and-Turtle/blob/main/truchet_tiles2.py](https://github.com/oonap0oo/Python-and-Turtle/blob/main/truchet_tiles2.py)

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

## truchet_tiles2_random.py

![truchet_tiles2_random.gif](truchet_tiles2_random.gif)

Randomly generated Truchet Tiles using complementery tiles for pleasing result.

code of version which loops automatically through random patterns, mouse click stops script:
![truchet_tiles2_random.py](truchet_tiles2_random.py)

code of version which saves pattern to text file when <a> key is pressed, loops to next random patterns with mouse click:
![truchet_tiles2_random_with_save.py](truchet_tiles2_random_with_save.py)

## turtle_python_logo.py

![turtle_python_logo_screenshot.png](turtle_python_logo_screenshot.png)

This script defines a fucntion to draw an ellipse using Turtle graphics.

Turtle graphics does have a circle function but no ellipse.

The ellipse function is then used to draw a python logo suing Turtle graphics.

## sierpinsky_turtle_cpython.py

![sierpinsky_turtle_cpython_screenshot.png](sierpinsky_turtle_cpython_screenshot.png)

code:
![https://github.com/oonap0oo/Python-and-Turtle/blob/main/sierpinsky_turtle_cpython.py](https://github.com/oonap0oo/Python-and-Turtle/blob/main/sierpinsky_turtle_cpython.py)

This script draws a Sierpinsky triangle recursively using turtle. 

This one makes use extra functionality in CPython's turtle on the PC, such as drawing filled shapes. 

The code shows several triangles using  successively deeper recursion.
