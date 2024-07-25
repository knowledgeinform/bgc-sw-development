// Ethan Nguyen APL/AOS/QPT July 2023
// Used to take temperature readings using Adafruit_MAX31586 Universal TThermocouple Amplifier
// Run with Arduino IDE, install MAX31586 package, connected to an Arduino Metro Mini V2

#include <Adafruit_MAX31856.h>

// Use software SPI: CS, DI, DO, CLK
//Adafruit_MAX31856 maxthermo = Adafruit_MAX31856(10, 11, 12, 13);
// use hardware SPI, just pass in the CS pin
Adafruit_MAX31856 maxthermo = Adafruit_MAX31856(10);
int signalPin = 9;
float temperature = 0;
float chip = 0;
long int currentTime = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);
  Serial.println("FPD Ignition Board Test");
  //output Pin for relay to control ignition
  pinMode(signalPin, OUTPUT); //Pin for STEMMA Relay
  if (!maxthermo.begin()) {
    Serial.println("Could not initialize thermocouple.");
    while (1) delay(10);
  }
  //type K by default
  maxthermo.setThermocoupleType(MAX31856_TCTYPE_K);
  //determine thermocouple type
  Serial.print("Thermocouple type: ");
  switch (maxthermo.getThermocoupleType() ) {
    case MAX31856_TCTYPE_B: Serial.println("B Type"); break;
    case MAX31856_TCTYPE_E: Serial.println("E Type"); break;
    case MAX31856_TCTYPE_J: Serial.println("J Type"); break;
    case MAX31856_TCTYPE_K: Serial.println("K Type"); break;
    case MAX31856_TCTYPE_N: Serial.println("N Type"); break;
    case MAX31856_TCTYPE_R: Serial.println("R Type"); break;
    case MAX31856_TCTYPE_S: Serial.println("S Type"); break;
    case MAX31856_TCTYPE_T: Serial.println("T Type"); break;
    case MAX31856_VMODE_G8: Serial.println("Voltage x8 Gain mode"); break;
    case MAX31856_VMODE_G32: Serial.println("Voltage x8 Gain mode"); break;
    default: Serial.println("Unknown"); break;
  }
  maxthermo.setConversionMode(MAX31856_CONTINUOUS);
  Serial.println("Finished Setup");
  Serial.println("Flame Ignite on or off? (Y/N)");
  Serial.println("Enter 'Temp' to print Temperature");
  Serial.println("Enter 'Chip' to print Onboard Chip Temperature");
}

void loop() {
  String input = Serial.readString();
  //locates if found in string
  if (input.indexOf("Y") >= 0){
    digitalWrite(signalPin, HIGH);
    Serial.println("Ignition ON");
  }
  if (input.indexOf("N") >= 0){
    digitalWrite(signalPin, LOW);
    Serial.println("Ignition Off");
  }
  if (input.indexOf("Temp") >= 0){
    Serial.print("Thermocouple Temperature:");
    Serial.println(maxthermo.readThermocoupleTemperature());  
  }
  if (input.indexOf("Chip") >= 0){
    Serial.print("Cold Junction  Temperature:");
    Serial.println(maxthermo.readCJTemperature());
  }
  if (maxthermo.readThermocoupleTemperature() == 0){
    Serial.println("No Temp reading");
  }
  temperature = maxthermo.readThermocoupleTemperature();   
  chip = maxthermo.readCJTemperature();
  Serial.println(temperature);
}