#ifndef serialcommunicator_h
#define serialcommunicator_h

#include "Arduino.h"
#include <Wire.h>
#include <AS5600.h>

class SerialCommunicator { 
    public:
        SerialCommunicator();
        void readSerial();
        void sendMessage(String message);
        void sendMessage(String message, char messageChar);
        void sendMessage(String message, int messageInt);
        void sendMessage(String message, float messageFloat);
        void sendSensorData(float data);

        bool isDataProcessed();


    private:
        bool dataProcessed;
        bool receiving = false;
        byte i = 0;
        const char startMark = '<';
        const char endMark = '>';
        char receivedChar;
};

#endif