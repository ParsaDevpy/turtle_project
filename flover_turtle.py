import math
import turtle

def first(x):
    return 12 * math.cos(x) ** 3

def second(x):
    return 12 * math.cos(x) - 5 * math.cos(2 * x) - 2 * math.cos(3 * x) - math.cos(4 * x)

turtle.speed(9000000000)
turtle.bgcolor("blue")
# win = turtle.Turtle.screen()
# win.setup(width = 400,heigh=400)
for i in range(360):
    x = first(math.radians(i)) * 4
    y = second(math.radians(i)) * 4
    turtle.goto(x,y)
    turtle.color("#F52375")
    turtle.goto(0,0)

turtle.done()