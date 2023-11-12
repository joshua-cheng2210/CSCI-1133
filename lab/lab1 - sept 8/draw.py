from turtle import *

showturtle()
speed(0)
pensize(1)

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)

# def square(x, y):
#     i = 1
#     while(i <= 2):
#         forward(x)
#         left(90)
#         forward(y)
#         left (90)
#         i = i + 1

# square(10, 100)

def random_circle():
	num_circle = int(input("number circle do u wanna draw: "))
	radius = int(input("input radius: "))
	angle = float(360 / num_circle)
	i = 1
	while(i <= num_circle):
		circle(radius)
		left(angle)
		i = i + 1

random_circle()

# more about turtle from the website ont he next line
# https://realpython.com/beginners-guide-python-turtle/#:~:text=turtle%20is%20a%20pre%2Dinstalled,gives%20the%20library%20its%20name.