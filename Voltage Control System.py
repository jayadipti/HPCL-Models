try:
    import RPi.GPIO as GPIO  
except ImportError:
    import Mock.GPIO as GPIO 
    print("Using Mock.GPIO for simulation.")



import time


GPIO.setmode(GPIO.BCM)  
control_pin = 18       
GPIO.setup(control_pin, GPIO.OUT)

pwm = GPIO.PWM(control_pin, 100)  
pwm.start(0)                     


target_voltage = 2.0  


def adjust_voltage(target, current):
    """
    Adjust the PWM duty cycle to regulate the voltage.

    :param target: Target voltage
    :param current: Current voltage from the sensor
    """
    try:
        error = target - current  
        duty_cycle = min(max(error * 10, 0), 100)  
        pwm.ChangeDutyCycle(duty_cycle)         
        print(f"Target Voltage: {target:.2f} V, Current Voltage: {current:.2f} V")
        print(f"Adjusting duty cycle to: {duty_cycle:.2f}%")
    except Exception as e:
        print(f"Error in adjust_voltage: {e}")

try:
    while True:
       
        try:
            current_voltage = float(input("Enter current voltage: "))  
            adjust_voltage(target_voltage, current_voltage)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        time.sleep(1) 

except KeyboardInterrupt:
 
    print("\nExiting program...")
    pwm.stop()
    GPIO.cleanup()
except Exception as e:
    print(f"Unexpected error: {e}")
    GPIO.cleanup()
