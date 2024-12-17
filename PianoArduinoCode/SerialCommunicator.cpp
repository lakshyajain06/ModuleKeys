#include "SerialCommunicator.h"


/****************************************************
  Method: SerialCommunicator
  In: none
  Out: none
  Description: constructor class for encoder
*****************************************************/
SerialCommunicator::SerialCommunicator() {

}

/****************************************************
  Method: sendMessage
  In: message to be sent
  Out: none
  Description: prints encoded message ot serial
*****************************************************/
void SerialCommunicator::sendMessage(String message) {
  Serial.print("<");
  Serial.print(message);
  Serial.print(">");
}

/****************************************************
  Method: sendMessage
  In: message to be sent plus char to be sent
  Out: none
  Description: prints encoded message + char to serial
*****************************************************/
void SerialCommunicator::sendMessage(String message, char messageChar) {
  Serial.print("<");
  Serial.print(message);
  Serial.print(messageChar);
  Serial.print(">");
}

/****************************************************
  Method: sendMessage
  In: message to be sent plus integer to o be sent
  Out: none
  Description: prints encoded message + integer to serial
*****************************************************/
void SerialCommunicator::sendMessage(String message, int messageInt) {
  Serial.print("<");
  Serial.print(message);
  Serial.print(messageInt);
  Serial.print(">");
}

/****************************************************
  Method: sendMessage
  In: message to be sent plus float to o be sent
  Out: none
  Description: prints encoded message + float to serial
*****************************************************/
void SerialCommunicator::sendMessage(String message, float messageFloat) {
  Serial.print("<");
  Serial.print(message);
  Serial.print(messageFloat);
  Serial.print(">");
}

/****************************************************
  Method: sendMessage
  In: data to be sent
  Out: none
  Description: prints encoded data to serial
*****************************************************/
void SerialCommunicator::sendSensorData(float data) {
  Serial.print("<s:");
  Serial.print(data);
  Serial.print(">");
}