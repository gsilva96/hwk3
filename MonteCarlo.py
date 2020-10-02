import random
import math

def montePi (numDarts) :

    inCircle = 0  #accumulator

    for i in range((numDarts)) : 
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    
    pi = inCircle / numDarts * 4
    return pi

var = montePi(100000)

print (str(var))
 
