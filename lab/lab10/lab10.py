def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# print(fibonacci(3))
# print(fibonacci(20))

def flat_square(lst):
    if lst == []:
        return []
    elif type(lst[0]) == list:
        return flat_square(lst[0]) + flat_square(lst[1:])
    else:
        return [lst[0] ** 2] + flat_square(lst[1:])

# print(flat_square([[-1, [2], [3], [[[-4,5]]], [], []]]))

def deep_square(lst):
    if lst == []:
        return []
    elif type(lst[0]) == list:
        return [deep_square(lst[0])] + deep_square(lst[1:])
    else:
        return [lst[0] ** 2] + deep_square(lst[1:])

# print(deep_square([[-1, [2], [3], [[[-4,5]]], [], []]]))
# print([[1, [4], [9], [[[16, 25]]], [], []]])

import turtle

turtle.speed(0)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def sierpinski(n, size):
    if n == 0:
        square(size)
    elif n == 1:
        for i in range(3):
            square(size / 3)  
            turtle.forward(size / 3) 
        turtle.left(90)
        turtle.forward(size / 3)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(180)
        square(size / 3)
        turtle.forward(size / 3 * 2)
        square(size / 3)
        turtle.left(180)
        turtle.forward(size / 3 * 2)
        turtle.right(90)
        turtle.forward(size / 3)
        turtle.right(90)
        for i in range(3):
            square(size / 3)  
            turtle.forward(size / 3)
        turtle.right(90)
        turtle.forward(size / 3 * 2)
        turtle.left(90)
    else:
        for i in range(3):
            sierpinski(n - 1, size / 3)
        turtle.left(90)
        turtle.forward(size / 3)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(180)
        sierpinski(n - 1, size / 3)
        turtle.forward(size / 3)
        sierpinski(n - 1, size / 3)
        turtle.left(90)
        turtle.forward(size / 3)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(180)
        for i in range(3):
            sierpinski(n - 1, size / 3)
        turtle.right(90)
        turtle.forward(size / 3 * 2)
        turtle.left(90)

# sierpinski(3, 100)
# turtle.exitonclick()

import turtle

def rec_tree(t, trunk_length):
    t.forward(trunk_length)
    t.left(30)
    if trunk_length > 15:
        rec_tree(t, trunk_length - 15)
    t.backward(trunk_length-15)
    t.right(60)
    if trunk_length > 15:
        rec_tree(t, trunk_length - 15)
    t.backward(trunk_length-15)
    t.left(30)

# turtle.hideturtle()
# tree_turtle = turtle.Turtle()
# # tree_turtle.hideturtle()
# tree_turtle.speed(0)
# tree_turtle.left(90)
# rec_tree(tree_turtle, 135)
# turtle.exitonclick()

import random

def random_rec_tree(t, trunk_length):
    t.forward(trunk_length)

    left_turn = random.randrange(15, 45)
    t.left(left_turn)
    if trunk_length > 15:
        random_rec_tree(t, trunk_length - 15)
    t.backward(trunk_length-15)

    right_turn = left_turn + random.randrange(15, 45)
    t.right(right_turn)
    if trunk_length > 15:
        random_rec_tree(t, trunk_length - 15)
    t.backward(trunk_length-15)
    t.left(right_turn - left_turn)

turtle.hideturtle()
tree_turtle = turtle.Turtle()
# tree_turtle.hideturtle()
tree_turtle.speed(0)
tree_turtle.right(90)
tree_turtle.penup()
tree_turtle.forward(300)
tree_turtle.left(180)
tree_turtle.pendown()
random_rec_tree(tree_turtle, 135)
turtle.exitonclick()