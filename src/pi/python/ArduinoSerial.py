from serial import Serial, SerialException, SerialTimeoutException

class ArduinoSerial(Serial):

    def __init__(self, port, baudrate=9600, timeout=0.1):
        Serial.__init__(baudrate, timeout)
        self.port = port
    
    def connect(self):
        self.open()

    def readSerialLine(self):
        data = self.readline()
        return data

    def readSerial(self, size):
        data = self.read(size)
        return data

    def writeSerial(self, data):
        self.write(data)

    def disconnect(self):
        self.close()