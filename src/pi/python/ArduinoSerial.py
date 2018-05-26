from serial import Serial, SerialException, SerialTimeoutException
from threading import Thread

class ArduinoSerial:
    
    
    def __init__(self, port, baudrate=9600, timeout=0.1):
        self.port = port
        self.connection = Serial(baudrate, timeout)
    
    def open(self):
        self.connection.open()
    
    def close(self):
        self.connection.close()
    
    def listen(self, listener):
        
        # Won't return until finished litening
        def listen_sync():
            while True:
                line = self.connection.readline()
                if listener(line):
                    return
        
        Thread(target=listen_sync).start()
    
    def write(self, data):
        self.connection.write(data)
