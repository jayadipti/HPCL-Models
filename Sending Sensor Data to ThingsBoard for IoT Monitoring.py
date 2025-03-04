import requests
import json

# ThingsBoard setup
THINGSBOARD_URL = "http://demo.thingsboard.io/api/v1/YOUR_ACCESS_TOKEN/telemetry"  # Replace with your access token

def send_data_to_thingsboard(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(THINGSBOARD_URL, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Data sent successfully:", data)
    else:
        print("Failed to send data. Status code:", response.status_code)

# Simulated sensor data
sensor_data = {
    "temperature": 25.5,
    "pressure": 1.2,
    "flow_rate": 5.0,
    "output_efficiency": 80.0
}

# Send data to ThingsBoard
send_data_to_thingsboard(sensor_data)