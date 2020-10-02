import turtle
import time

tur = turtle.Turtle()

def exercise1_2():
    for i in range(5): # turtle will move only 5 times
        tur.forward(155) #turtle will move 255 units forward
        tur.right(144) # after it moves 140 units, it will turn to the right 144 degrees
def exercise1_1():
    for i in range(4):
        tur.forward(150)
        tur.left(90)

    tur.left(35)

    for i in range(4):
        tur.forward(150)
        tur.left(90)
    tur.left(45)
    for i in range(4):
        tur.forward(150)
        tur.left(90)

    tur.left(55)
    for i in range(4):
        tur.forward(150)
        tur.left(90)

    tur.left(65)
    for i in range(4):
        tur.forward(150)
        tur.left(90)



def exercise1_3():
    n = 7
    angle = 180 - 180 / n
    for i in range(n):
        tur.forward(100)
        tur.right(angle)

def exercise1_4():
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
    for i in range(4):
     tur.pendown()
    
    r =  50
    tur.circle(r)

    r = 15
    n = 10
    for i in range(1, n+1,1):
        tur.circle(r*i)

def main():
    tur.penup()
    tur.goto(0,0)
    tur.clear()
    tur.pendown()

    exercise1_2()
    time.sleep(100)

    tur.penup()
    tur.goto(0,0)
    tur.clear()
    tur.pendown()

    exercise1_1()
    time.sleep(100)

    tur.penup()
    tur.goto(0,0)
    tur.clear()
    tur.pendown()

    exercise1_3()
    time.sleep(100)
    tur.penup()
    tur.goto(0,0)
    tur.clear()
    tur.pendown()

    exercise1_4()
    time.sleep(100)

    tur.penup()
    tur.goto(0,0)
    tur.clear()
    tu.rpendow
    
