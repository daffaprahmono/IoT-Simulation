import random

# humidity generator
def humidityGenerator():
    humidityMax=60
    humidityMin=30
    humidity=45

    delta = random.uniform(-10, 10)
    humidity += delta
    humidity = max(humidityMin, min(humidityMax, humidity))
    return round(humidity, 0)