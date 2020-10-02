import turtle

tur = turtle.Turtle()

tur.penup()
tur.goto(-50,-50)
tur.pendown()

n = 9
tur.left(45)
for i in range  (4):
    angle = 180 - 180 / n
for i in range(n):
        tur.forward(100)
        tur.right(angle)

tur.penup()
tur.goto(5,-30)
tur.left(45)
for i in range  (4):
    tur.pendown()

r =  50
tur.circle(r)

r = 15
n = 10
for i in range(1, n+1,1):
    tur.circle(r*i)

turtle.Screen().exitonclick()
