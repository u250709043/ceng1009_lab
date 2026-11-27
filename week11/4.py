import turtle


def draw_square(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.pensize(2)


for i in range(12):
    draw_square(t, 80)
    t.left(30)