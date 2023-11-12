from turtle import *
from random import *
speed(0)

def target_board(size):
    penup()
    forward(size)
    left(90)
    pendown()
    for xxxx in range(4):
        forward(size)
        left(90)
        forward(size)
        for x in range(2):
            right(90)
            forward(size / 2)
            right(90)
    color('red')
    circle(size)
    color('black')

def shoot(bullet, size):
    for ammo in range(bullet):
        penup()
        setpos(randint(-size, size), randint(-size, size))
        pendown()
        dot(5, color(random(), random(), random()))

target_board(220)
shoot(100, 220)

exitonclick()

'''
dot(size, 'color')

'''