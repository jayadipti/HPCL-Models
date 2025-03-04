const int tempPin = A0;     
const int pressurePin = A1; 
const int flowPin = A2;     


const float TEMP_SCALE = 100.0;     
const float PRESSURE_SCALE = 10.0;  
const float FLOW_SCALE = 50.0;      

void setup() {

  Serial.begin(9600);

  pinMode(tempPin, INPUT);
  pinMode(pressurePin, INPUT);
  pinMode(flowPin, INPUT);


  Serial.println("Sensor Readings:");
  Serial.println("==============================");
}

void loop() {

  float temperature = analogRead(tempPin) * (5.0 / 1023.0) * TEMP_SCALE;
  float pressure = analogRead(pressurePin) * (5.0 / 1023.0) * PRESSURE_SCALE; 
  float flowRate = analogRead(flowPin) * (5.0 / 1023.0) * FLOW_SCALE;

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C, Pressure: ");
  Serial.print(pressure);
  Serial.print(" bar, Flow Rate: ");
  Serial.print(flowRate);
  Serial.println(" L/min");

  // Wait for 1 second before updating
  delay(1000);
}
