/*
This code uses an Arduino to take 6x inputs and trigger off of their edges to generate 12 outputs
Each output is 2 seconds long
For use with Adafruit Metro Mini V2 in Arduino IDE
Ethan Nguyen AOS-QPT 2023
Use Command line to read which relays/edge is being triggered
*/
//Input Pins
const int input1 = 14;
const int input2 = 15;
const int input3 = 16;
const int input4 = 17;
const int input5 = 18;
const int input6 = 19;
int inputs[] = {-1, 14, 15, 16, 17, 18, 19};

//Relay Output Pins
const int Relay1 = 13;
const int Relay2 = 12;
const int Relay3 = 11;
const int Relay4 = 10;
const int Relay5 = 9;
const int Relay6 = 8;
const int Relay7 = 7;
const int Relay8 = 6;
const int Relay9 = 5;
const int Relay10 = 4;
const int Relay11 = 3;
const int Relay12 = 2;
int outputs[] = {-1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2};

//Allows processing of multiple relays, stores edge detection
const long period = 2000;
long int currentTime = 0;
//Last Time relay turned on
long int prevMillis[] = {-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
//Current Time
long int currMillis[] = {-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

//Stores states, PULL-UP so starts with Voltage HIGH(1), if not start with LOW(0)
int currState[] = {-1, 0, 0, 0, 0, 0, 0};
int prevState[] = {-1, 1, 1, 1, 1, 1, 1};

int userInput = -1;
int userRelay = -1;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  while(!Serial) delay(10);
  Serial.println("Valve Control Relay Test");
  // 6x Inputs, matched with pins across the board starting top to bottom
  //USE INPUT_PULLUP if not connected to definite voltage (Input pins default to HIGH)
  pinMode(input1, INPUT_PULLUP);
  pinMode(input2, INPUT_PULLUP);
  pinMode(input3, INPUT_PULLUP);
  pinMode(input4, INPUT_PULLUP);
  pinMode(input5, INPUT_PULLUP);
  pinMode(input6, INPUT_PULLUP);
  //12 Outputs, odd is rising edge, even is falling edge
  pinMode(Relay1, OUTPUT);  //input1
  pinMode(Relay2, OUTPUT);  //input1
  pinMode(Relay3, OUTPUT);  //input2
  pinMode(Relay4, OUTPUT);  //input2
  pinMode(Relay5, OUTPUT);  //input3
  pinMode(Relay6, OUTPUT);  //input3
  pinMode(Relay7, OUTPUT);  //input4
  pinMode(Relay8, OUTPUT);  //input4
  pinMode(Relay9, OUTPUT);  //input5
  pinMode(Relay10, OUTPUT); //input5
  pinMode(Relay11, OUTPUT); //input6
  pinMode(Relay12, OUTPUT); //input6
  // Set maximum milliseconds to wait for serialdata
  Serial.setTimeout(10);
  Serial.println("Finished Setup");
}

void loop() {
  currentTime = millis();

  //turn on a relay manually
  if (Serial.available() > 0){
    userInput = Serial.parseInt();
    if (userInput != -1 && userInput != 0){
      Serial.println(millis());
      Serial.print("User Turning on Relay ");
      Serial.println(userInput);
      Serial.println(millis());
      //Turn on desired relay
      digitalWrite(outputs[userInput], HIGH);
      //start count, will turn off in 2 seconds
      prevMillis[userInput] = currMillis[userInput];
      //not an edge so doesn't update previous state
      userInput = -1;
    }
  }
  //for each of the 6 inputs
  for (int i=1; i<7; i++){
    // update times and states
    currMillis[i*2] = currentTime;
    currMillis[(i*2)-1] = currentTime;
    currState[i]=digitalRead(inputs[i]);
    //edge detection and turning on relay
    if (currState[i] != prevState[i]){
      //rising edge
      if (currState[i] == HIGH){
        Serial.println("Rising Edge Detected");
        //Turn on odd numbered relay
        digitalWrite(outputs[(i*2)-1], HIGH);
        //start count, only updates if edge detected
        prevMillis[(i*2)-1] = currMillis[(i*2)-1];
        prevState[i] = currState[i];
      }
      //falling edge
      else if (currState[i] == LOW){
        Serial.println("Falling Edge Detected");
        //Turn on even numbered relay
        digitalWrite(outputs[(i*2)], HIGH);
        //start count, only updates if edge detected
        prevMillis[(i*2)] = currMillis[(i*2)];
        prevState[i] = currState[i];
      }
    }
    //decide if any of the 12 outputs need to be turend off
    if(digitalRead(outputs[(i*2)-1]) == HIGH){
      if (currMillis[(i*2)-1] - prevMillis[(i*2)-1] >= period){
        //Turn off
        // Serial.print("Time elapsed: ");
        // Serial.println(currMillis[(i*2)-1] - prevMillis[(i*2)-1]);
        digitalWrite(outputs[(i*2)-1], LOW);
      }
    }
    if(digitalRead(outputs[(i*2)]) == HIGH){
      if (currMillis[(i*2)] - prevMillis[(i*2)] >= period){
        //Turn off
        // Serial.print("Time elapsed: ");
        // Serial.println(currMillis[(i*2)] - prevMillis[(i*2)]);
        digitalWrite(outputs[(i*2)], LOW);
      }
    }
  }
}
