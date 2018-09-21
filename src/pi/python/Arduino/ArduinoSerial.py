from serial import Serial, SerialException, SerialTimeoutException
from threading import Thread

class ArduinoSerial:
    """
    Wrapper class for Arduino serial connection
    """
    
    def __init__(self, port, baudrate=9600, timeout=0.1):
        self.port = port
        self.connection = Serial(baudate=baudrate, timeout=timeout)
    
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
            
    def write(self, data):
        """
        Write data byte string to serial connection
        Args:
            data: Byte string of data to be written
        Returns:
            Nothing
        """
        self.connection.write(data)

    def read(self, size=1):
        """
        Write data byte string to serial connection
        Args:
            size: Number of bytes to read
        Returns:
            Byte of data read
        """
        return self.connection.read(size)