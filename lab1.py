import turtle 
import math

tur = turtle.Turtle() #name of turtle

tur.penup()  #pen is lifted 
tur.goto(0,0)
tur.pendown() #pen is on the "paper"

posX = 30 #initial position for x
posY = 30 #initial position for y
v0 = 30 #constant velocity
t = 50 #end time
theta = 25.0 #theta 
a = 9.81 #acceleration (gravity)
ti = 0 # initial time

def xCoord(xposx, xv0, xt, xtheta): #these parameters are local to this function only; no values yet just instructions. xt is the only parameter that changes  
  xRet = 0 #postion x will return to 0
  vx = xv0 * math.cos(math.radians(xtheta)) #vx= x velocity in that moment
  xRet = xposx + xv0 * xt #this calculates the x position

  return(xRet) # current x = return x

def yCoord(yposy, yv0, yt, ytheta, ya): #only instructions for y position and acceleration
  yRet = 0
  yv = yv0 * math.sin(math.radians(ytheta)) #formula to get velocity of y

  yRet = yposy + (yv * yt -  ((0.5 * ya) * (yt **2))) #formula calculate position of y

  return(yRet)

for tiempo in range(ti, t): #time starts with ti=0 and starts adding +1 until it gets to 't'

  currX = xCoord(posX, v0, tiempo, theta) 
  currY = yCoord(posY, v0, tiempo, theta, a)
  if(currY <0): 
    break    
  tur.goto(currX, currY) #turtle will move to the given positions

turtle.Screen().exitonclick()


