import turtle
import math
import time

t = turtle.Turtle()
turtle.title("Animated Heart")
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()

t.color("red")
t.width(2)

def heart_x(t):
    return 16 * (math.sin(t) ** 3)

def heart_y(t):
    return (13 * math.cos(t)
            - 5 * math.cos(2*t)
            - 2 * math.cos(3*t)
            - math.cos(4*t))


def draw_heart(scale):
    t.clear()
    t.penup()

    for i in range(360):
        ang = math.radians(i)
        x = heart_x(ang) * scale
        y = heart_y(ang) * scale

        t.goto(x, y)
        t.pendown()

scale = 10
grow = True

while True:
    draw_heart(scale)


    if grow:
        scale += 0.3
        if scale >= 13:
            grow = False
    else:
        scale -= 0.3
        if scale <= 10:
            grow = True

    time.sleep(0.02)

turtle.done()
