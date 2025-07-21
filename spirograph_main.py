from turtle import Turtle , Screen
import random

jimmy = Turtle() # give the name jimmy as a object
screen = Screen()

def random_color():
     # generating random color for turtle
    r = random.randint(0,1)
    g = random.randint(0,1)
    b = random.randint(0,1)

    tuple_color =  (r,g,b)
    return tuple_color


jimmy.speed("fastest")
# jimmy.width(3)  # can set the width of jimmy


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jimmy.color(random_color())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + size_of_gap)

draw_spirograph(3)
screen.exitonclick()
