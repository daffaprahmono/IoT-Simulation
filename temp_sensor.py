import random

# temp generator
def tempGenerator():
    tempMin=15.0
    tempMax=30.0
    temp=22.5
    
    delta= random.uniform(-5, 5)
    temp += delta
    temp = max(tempMin, min(tempMax, temp))
    return round(temp, 1)