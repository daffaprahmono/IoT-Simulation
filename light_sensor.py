import random

# light intensity generator
def lightGenerator():
    lightMax = 1620
    lightMin = 540
    light = 1080

    delta = random.uniform(-360, 360)
    light += delta
    light = max(lightMin, min(lightMax, light))
    return round(light, 0)