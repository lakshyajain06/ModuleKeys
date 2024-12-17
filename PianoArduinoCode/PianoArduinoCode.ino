#include "SerialCommunicator.h"

//digital pins
const int key1 = 2;
const int led = 7;
const int key3 = 4;

SerialCommunicator serialCom;

bool on = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(key1, INPUT);
  pinMode(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:


  if (digitalRead(key1) != on) {
    on = digitalRead(key1);
    if (on){
      serialCom.sendMessage("pa1");
      digitalWrite(led, HIGH);
    }
    else {
      serialCom.sendMessage("ra1");
      digitalWrite(led, LOW);
    }
  }
  
}
