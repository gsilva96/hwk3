import random
import math
import turtle

def showMontePi (numNeedles):
    theta = 0 #angle at which needle falls 
    D = 0 # Distance from the center of the needle to the closest line
    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    length = 2
    wn.setworldcoordinates(-2, -2, 2, 2)
    x_center = 0
    y_center = 0
    gap = 1 #this is the gap that will have the two parallel lines
        
   # parallel lines,  x-axis is from (-1,1) & y-axis= (0,1)
    drawingT.up()
    drawingT.goto(-1, 0)
    drawingT.down()
    drawingT.forward(length)
    drawingT.penup()
    drawingT.forward(gap)
    drawingT.goto(-1, 1)
    drawingT.down()
    drawingT.forward(length)

    inParallel = 0
    

    for i in range (numNeedles):
        theta = random.randint (0, 180) #gives theta value of randomness  
        x_center = random.randint(-1, 1) # x center has a random value
        y_center = random.randint(0, 1)
        endPoint1x = 0.5*math.cos(theta) #calculates 1x 
        endPoint1y = 0.5*math.sin(theta) #calculates 1y
        theta = theta + 180
        #drawingT.up()
        #drawingT.left(90)
        #drawingT.down()
        drawingT.up()
        drawingT.goto(x_center, y_center)
        drawingT.down()
        drawingT.goto(endPoint1x, endPoint1y)
        drawingT.up()
        drawingT.goto(x_center, y_center)
        drawingT.down()
        drawingT.goto(endPoint2x, endPoint2y)
        endPoint2x = 0.5*math.cos(theta)
        endPoint2y = 0.5*math.sin(theta) 
        #drawingT.up()
        #drawingT.goto(x_center,y_center)
        #drawingT.down()
        #drawingT.goto(endPoint1x, endPoint1y)
        #drawingT.up()
        #drawingT.goto(x_center,y_center)
        #drawingT.down()
        #drawingT.goto(endPoint2x, endPoint2y)
        
        if D <= 0.5*math.sin(theta):
            inParallel = 2 
            drawingT.color("blue")
        else:
            drawingT.color("red")
        


                
    

    
    wn.exitonclick()
    

def main():
    showMontePi(2)
    return 0
   # Main ends here!

main()
