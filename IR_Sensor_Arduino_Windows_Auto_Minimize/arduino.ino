//Attach IR Sensor Input at pin 7 on Arduino, I've used arduino Mega.
//Use 9600 baud, you can use any but define the baud rate in the python script too. They should match.
//Get the COM port ID using the Arduino IDE as Arduino IDE can detect Development boards and COM ports.

const int irSensorPin = 7;  // Define the pin for the IR sensor
const int serialOutputPin = 9600;  // Define the baud rate for serial communication

void setup() {
  pinMode(irSensorPin, INPUT);  // Set IR sensor pin as input
  Serial.begin(serialOutputPin);  // Start serial communication
}

void loop() {
  // Check if IR sensor pin is HIGH (For Sensors with Active Low state, check if your sensor works. 
  //If doesn't, change the HIGH to LOW)
  if (digitalRead(irSensorPin) == HIGH) {  
    Serial.println("done");  // Send "done" through serial
    delay(100); // Optional delay to prevent multiple rapid readings
  } else {
    //Serial.println("none");  // Send "none" through serial
    delay(100); // Optional delay to prevent multiple rapid readings
  }
}
