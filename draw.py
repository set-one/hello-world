import turtle

painter = turtle.Turtle()

painter.pensize(10)
for i in range(101):
	painter.forward(100)
	painter.left(90)
	i+=1

turtle.done()