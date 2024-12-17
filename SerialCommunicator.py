import serial

class SerialCommunicator:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/cu.usbmodem21101', baudrate=9600)
        self.data = []
        self.start_mark = '<'
        self.end_mark = '>'

        self.receiving = False
    
    def readSerial(self):
        receivedChar = None

        while self.ser.in_waiting > 0:
            receivedChar = str(self.ser.read(), 'UTF-8')

            if self.receiving:
                if not receivedChar == self.end_mark:
                    self.data.append(receivedChar)
                else:
                    self.receiving = False
                    returnStr = "".join(self.data)
                    self.data = []
                    return returnStr
            else:
                if receivedChar == self.start_mark:
                    self.receiving = True