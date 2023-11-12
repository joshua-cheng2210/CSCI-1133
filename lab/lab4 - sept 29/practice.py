import turtle, random


def spiro(num, side):
    for i in range(num):
        turtle.speed(0)
        turtle.delay(0)

        r = random.random()
        g = random.random()
        b = random.random()
        turtle.color(r,g,b)

        turtle.begin_fill()
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)
        turtle.end_fill()
        turtle.left(360 / num)

spiro(15, 200)
turtle.exitonclick()



# import turtle, random

# turtle.speed(0)
# turtle.delay(0)

# def one_square():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.color(r,g,b)

#     turtle.begin_fill()
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#     turtle.end_fill()

# def spiro(num, side)
# turtle.exitonclick()