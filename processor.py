import time
from datetime import datetime
import temp_sensor
import light_sensor
import humidity_sensor

# temperature classification
def tempClassification(temp):
    if temp < 15:
        return 'Freezing'
    elif 15<=temp<20:
        return 'Cold'
    elif 20<=temp<25:
        return 'Ideal'
    elif 25<=temp<30:
        return 'Warm'
    elif temp>=30:
        return 'Hot'
    else:
        return 'Unknown'
    
# light intensity classification
def lightClassification(light):
    if 0<=light<540:
        return 'Dark'
    elif 540<=light<900:
        return 'Dim'
    elif 900<=light<1260:
        return 'Ideal'
    elif 1260<=light<1620:
        return 'Bright'
    elif light>=1620:
        return 'Overexposed'
    else:
        return 'Unknown'
    
# humidity level classification
def humidityClassification(humidity):
    if 0<=humidity<30:
        return 'Very Dry'
    elif 30<=humidity<40:
        return 'Dry'
    elif 40<=humidity<50:
        return 'Ideal'
    elif 50<=humidity<60:
        return 'Wet'
    elif humidity>=60:
        return 'Very Wet'
    else:
        return 'Unknown'

# processing function to read 30 seconds of sensor data and classify it
def processSensors():
    data = []
    start_time = time.time()
    while time.time() - start_time < 10:
        temp = temp_sensor.tempGenerator()
        light = light_sensor.lightGenerator()
        humidity = humidity_sensor.humidityGenerator()
        
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        data.append({
            'timestamp': timestamp,
            'temperature': temp,
            'light': light,
            'humidity': humidity,
            'temp_classification': tempClassification(temp),
            'light_classification': lightClassification(light),
            'humidity_classification': humidityClassification(humidity)
        })
        time.sleep(1)  # simulate 1 second delay for each reading
    return data

# plotting function to visualize the sensor data
def plotSensorData(data):
    import matplotlib.pyplot as plt
    import numpy as np

    timestamps = [entry['timestamp'] for entry in data]
    y_temp = [entry['temperature'] for entry in data]
    y_light = [entry['light'] for entry in data]
    y_humidity = [entry['humidity'] for entry in data]

    fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    # --- Temperature ---
    temp_ideal_min, temp_ideal_max = 20, 25
    axs[0].plot(timestamps, y_temp, color='black')
    axs[0].set_ylabel('Temperature (°C)')
    axs[0].set_title('Temperature Data')
    axs[0].axhline(temp_ideal_min, color='black', linestyle='-', linewidth=1)
    axs[0].axhline(temp_ideal_max, color='black', linestyle='-', linewidth=1)
    axs[0].fill_between(timestamps, min(y_temp + [temp_ideal_min]), temp_ideal_min, color='red', alpha=0.3)
    axs[0].fill_between(timestamps, temp_ideal_min, temp_ideal_max, color='green', alpha=0.3)
    axs[0].fill_between(timestamps, temp_ideal_max, max(y_temp + [temp_ideal_max]), color='red', alpha=0.3)

    # --- Light ---
    light_ideal_min, light_ideal_max = 900, 1260
    axs[1].plot(timestamps, y_light, color='black')
    axs[1].set_ylabel('Light (Lux)')
    axs[1].set_title('Light Data')
    axs[1].axhline(light_ideal_min, color='black', linestyle='-', linewidth=1)
    axs[1].axhline(light_ideal_max, color='black', linestyle='-', linewidth=1)
    axs[1].fill_between(timestamps, min(y_light + [light_ideal_min]), light_ideal_min, color='red', alpha=0.3)
    axs[1].fill_between(timestamps, light_ideal_min, light_ideal_max, color='green', alpha=0.3)
    axs[1].fill_between(timestamps, light_ideal_max, max(y_light + [light_ideal_max]), color='red', alpha=0.3)

    # --- humidity ---
    humidity_ideal_min, humidity_ideal_max = 40, 50
    axs[2].plot(timestamps, y_humidity, color='black')
    axs[2].set_ylabel('Humidity (%)')
    axs[2].set_title('Humidity Data')
    axs[2].set_xlabel('Timestamp')
    axs[2].axhline(humidity_ideal_min, color='black', linestyle='-', linewidth=1)
    axs[2].axhline(humidity_ideal_max, color='black', linestyle='-', linewidth=1)
    axs[2].fill_between(timestamps, min(y_humidity + [humidity_ideal_min]), humidity_ideal_min, color='red', alpha=0.3)
    axs[2].fill_between(timestamps, humidity_ideal_min, humidity_ideal_max, color='green', alpha=0.3)
    axs[2].fill_between(timestamps, humidity_ideal_max, max(y_humidity + [humidity_ideal_max]), color='red', alpha=0.3)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    sensor_data = processSensors()
    plotSensorData(sensor_data)

if __name__ == "__main__":
    main()