import turtle,random
t = turtle.Turtle("classic")
t.speed(11000)
turtle.bgcolor("black")
color = ['red','blue','orange','white','yellow','pink','purple','green']
number = ['1','2','3','4','5','6']
for i in range(50,500):
    c=random.choice(color)
    t.forward(i+5)
    t.right(150)
    t.color(c)
n = random.choice(number)
t.clear()
for v in range(100,1000,100):
    t.penup()
    t.forward(v)
    t.pendown()
    t.color('white')
    t.write(n)
    t.right(90)
turtle.done()