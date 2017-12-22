import serial
import PianoStepsError

class ArduinoSerial(Serial):
    __init__(self, port, baudRate = 9600, timeout = 0.1):
        super.__init__(baudRate, timeout)
        self.port = port
        self.baudRate = baudRate
        self.timeout = timeout
    
    def connect(self):
        try:
            self.open(self.port)
        except SerialError:
            raise new PianoStepsError('Serial', 1)
    
    def readSerialLine(self):
        try: 
            line = self.readLine()
        except: SerialTimeoutError:
            raise new PianoStepsError('Serial', 3)
        return line

    def readSerial(self, size):
        try: 
            line = self.read(size)
        except: SerialTimeoutError:
            raise new PianoStepsError('Serial', 3)
        return line

    def writeSerial(self, data, encoding):
        try:
            self.write(data)
        except SerialTimeoutError:
            raise new PianoStepsError('Serial', 3)


    def disconnect(): 
        self.close()

    
