import time
import random


def read_analog(pin):
    return random.uniform(0, 1023)  

def setup():

    pass

def loop():
    while True:
       
        temp_pin_value = read_analog(0)  
        pressure_pin_value = read_analog(1)  
        flow_pin_value = read_analog(2) 

        temperature = (temp_pin_value * (5.0 / 1023.0)) * 100  
        pressure = (pressure_pin_value * (5.0 / 1023.0)) * 10  
        flow_rate = (flow_pin_value * (5.0 / 1023.0)) * 50 

        print(f"Temperature: {temperature:.2f} °C, Pressure: {pressure:.2f} bar, Flow Rate: {flow_rate:.2f} L/min")

        time.sleep(1)  

if _name_ == "_main_":
    setup()
    loop()
