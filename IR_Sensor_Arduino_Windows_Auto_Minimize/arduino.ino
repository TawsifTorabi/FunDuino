const int irSensorPin = 7;  // Define the pin for the IR sensor
const int serialOutputPin = 9600;  // Define the baud rate for serial communication

void setup() {
  pinMode(irSensorPin, INPUT);  // Set IR sensor pin as input
  Serial.begin(serialOutputPin);  // Start serial communication
}

void loop() {
  if (digitalRead(irSensorPin) == HIGH) {  // Check if IR sensor pin is HIGH
    Serial.println("done");  // Send "done" through serial
    delay(100); // Optional delay to prevent multiple rapid readings
  } else {
    //Serial.println("none");  // Send "none" through serial
    delay(100); // Optional delay to prevent multiple rapid readings
  }
}
