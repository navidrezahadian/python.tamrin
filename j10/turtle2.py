import turtle
circle = turtle.Turtle()
circle.speed(0)
turtle.bgcolor("black")
for i in range (15) :
    for colours in ("red", "magenta", "blue", "cyan", "green", "yellow", "white") :
        circle.color(colours)
        circle.pensize(3)
        circle.left(4)
        circle.forward(200)
        circle.left(90)
        circle.forward(200)
        circle.left(90)
        circle.forward(200)
        circle.left(90)
        circle.forward(200)
        circle.left(90)
turtle.done()