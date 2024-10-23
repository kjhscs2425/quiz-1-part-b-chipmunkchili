from turtle import *

#This for loop draws the outer square, with side lengths of 100 pixels
for i in range(4):
    forward(100)
    right(90)

# This section repositions the turtle to draw the next square
forward(50)
right(45)

# This for loop draws the inner square, with side lengths of 71 pixels
for i in range (4):
    forward(71)
    right(90)

exitonclick()