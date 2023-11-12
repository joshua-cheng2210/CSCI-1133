from turtle import *

def draw_square(x):
    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)

def draw_triangle(length):
    x = length
    forward(x)
    left(120)
    forward(x)
    left(120)
    forward(x)
    left(120)

length = int(input("Enter the side length: "))
shape_type = str(input("Enter shape type (S or s for square, T or t for triangle): "))

if (shape_type == "S") or (shape_type == "s"):
    draw_square(length)
elif (shape_type == "T") or (shape_type == "t"):
    draw_triangle(length)
else:
    print(f"Illegal shape type entered: {shape_type}")