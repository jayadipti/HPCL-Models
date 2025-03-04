import time
import random

# Simulate analog input readings (replace with actual sensor readings)
def read_analog(pin):
    return random.uniform(0, 1023)  # Simulating a value between 0 and 1023

def setup():
    # Initialize pins for sensors
    # In Raspberry Pi, we use GPIO pins or ADC pins if sensors are connected
    pass

def loop():
    while True:
        # Simulate sensor data reading
        temp_pin_value = read_analog(0)  # Temperature sensor
        pressure_pin_value = read_analog(1)  # Pressure sensor
        flow_pin_value = read_analog(2)  # Flow sensor

        # Convert to actual units
        temperature = (temp_pin_value * (5.0 / 1023.0)) * 100  # Convert to Celsius
        pressure = (pressure_pin_value * (5.0 / 1023.0)) * 10  # Convert to bar
        flow_rate = (flow_pin_value * (5.0 / 1023.0)) * 50  # Convert to L/min

        # Display data
        print(f"Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} bar, Flow Rate: {flow_rate:.2f} L/min")

        time.sleep(1)  # Update every second

if _name_ == "_main_":
    setup()
    loop()