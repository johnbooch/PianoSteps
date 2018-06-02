from serial import Serial, SerialException, SerialTimeoutException
from threading import Thread

class ArduinoSerial:
    """
    Wrapper class for Arduino serial connection
    """
    
    def __init__(self, port, baudrate=9600, timeout=0.1):
        self.port = port
        self.connection = Serial(baudrate, timeout)
    
    def open(self):
        """
        Opens serial connection

        Raises: 
            SerialException

        Returns:
            Nothing
        """
        self.connection.open()
    
    def close(self):
        """
        Closes serial connection

        Returns:
            Nothing
        """
        self.connection.close()
 
    def registerErrorListener(self, listener):
        """
        Registers error listener on new thread

        Args:
            listener: User defined error listener function
        Returns:
            Nothing
        """
        def errorListener():
            while True:
                line = self.connection.readline()
                if listener(line):
                    return
        
        Thread(target=errorListener).start()
    
    def write(self, data):
        """
        Write data byte string to serial connection
        Args:
            data: Byte string of data to be written
        Returns:
            Nothing
        """
        self.connection.write(data)
