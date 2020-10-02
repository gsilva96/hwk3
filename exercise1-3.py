import turtle

tur = turtle.Turtle()
n = 9
angle = 180 - 180 / n
for i in range(n):
	tur.forward(100)
	tur.right(angle)

turtle.Screen().exitonclick()

