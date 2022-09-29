import turtle

painter = turtle.Turtle()

for i in range(100):
    painter.forward(i+100)
    painter.left(i+120)
    i+=2

turtle.done()
