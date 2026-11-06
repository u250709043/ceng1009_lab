import turtle


def draw_bar(t, height):
    """Get turtle t to draw one bar of the given height."""
    t.begin_fill()  # Start filling the bar
    t.left(90)
    t.forward(height)  # Draw the up-stroke
    t.write("  " + str(height))  # Optional: label the height on top
    t.right(90)
    t.forward(40)  # Width of the bar
    t.right(90)
    t.forward(height)  # Draw the down-stroke
    t.left(90)
    t.end_fill()  # Complete the fill
    t.forward(10)  # Space/gap after the bar


# Setup the turtle window and turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)

# Sample data list of values
data = [48, 117, 200, 240, 160, 99, 222, 75]

# Move turtle to starting position
t.penup()
t.goto(-200, -150)
t.pendown()
t.speed(0)

for value in data:
    # Determine the fill color based on the value
    if value >= 200:
        t.color("red")
    elif value >= 100:
        t.color("yellow")
    else:
        t.color("green")

    draw_bar(t, value)

turtle.done()