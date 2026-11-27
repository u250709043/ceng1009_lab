import turtle

def draw_square(t, size, filled):
    if filled:
        t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)

    if filled:
        t.end_fill()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
size = 40

for row in range(6):
    for col in range(6):
        t.penup()
        t.goto(-120 + col * size, -120 + row * size)
        t.pendown()
        draw_square(t, size, (row + col)%2==0)


wn.exitonclick()