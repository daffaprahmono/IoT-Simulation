import random

# moisture generator
def moistureGenerator():
    moistMax=60
    moistMin=30
    moist=45

    delta = random.uniform(-10, 10)
    moist += delta
    moist = max(moistMin, min(moistMax, moist))
    return round(moist, 0)