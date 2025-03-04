try:
    import RPi.GPIO as GPIO  # Import the Raspberry Pi GPIO library
except ImportError:
    import Mock.GPIO as GPIO  # Use Mock.GPIO for testing on non-Raspberry Pi systems
    print("Using Mock.GPIO for simulation.")



import time

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
control_pin = 18        # PWM control pin
GPIO.setup(control_pin, GPIO.OUT)

# Initialize PWM on the control pin with 100 Hz frequency
pwm = GPIO.PWM(control_pin, 100)  # 100 Hz frequency
pwm.start(0)                      # Start with 0% duty cycle

# Target parameters
target_voltage = 2.0  # Target voltage in volts

# Function to adjust voltage
def adjust_voltage(target, current):
    """
    Adjust the PWM duty cycle to regulate the voltage.

    :param target: Target voltage
    :param current: Current voltage from the sensor
    """
    try:
        error = target - current  # Calculate error
        duty_cycle = min(max(error * 10, 0), 100)  # Scale error to a 0-100% duty cycle
        pwm.ChangeDutyCycle(duty_cycle)           # Update PWM duty cycle
        print(f"Target Voltage: {target:.2f} V, Current Voltage: {current:.2f} V")
        print(f"Adjusting duty cycle to: {duty_cycle:.2f}%")
    except Exception as e:
        print(f"Error in adjust_voltage: {e}")

try:
    while True:
        # Simulated current voltage (replace with actual sensor input in real use)
        try:
            current_voltage = float(input("Enter current voltage: "))  # Simulated sensor input
            adjust_voltage(target_voltage, current_voltage)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        time.sleep(1)  # Wait for 1 second between adjustments

except KeyboardInterrupt:
    # Cleanup on exit
    print("\nExiting program...")
    pwm.stop()
    GPIO.cleanup()
except Exception as e:
    print(f"Unexpected error: {e}")
    GPIO.cleanup()