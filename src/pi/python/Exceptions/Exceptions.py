import logging

class PianoStepsNotice(object):
    def __init__(self, message, code):
        self.message = message
        self.code = code
    
    def getMessage(self):
        return self.message

    def getCode(self):
        return self.code
    
    def getLevel(self):
        raise NotImplementedError
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.message)

class PianoStepsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
    
    def getMessage(self):
        return self.message

    def getCode(self):
        return self.code

    def getLevel(self):
        raise NotImplementedError
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.message)

class Debug(PianoStepsNotice):

    def getLevel(self):
        return logging.DEBUG

    def __str__(self):
        return '[Debug {}'.format(self.message)

class Info(PianoStepsNotice):

    def getLevel(self):
        return logging.INFO

    def __str__(self):
        return '[Info] {}'.format(self.message)

class Warn(PianoStepsNotice):

    def getLevel(self):
        return logging.WARN

    def __str__(self):
        return '[Warning] {}'.format(self.message)
class Error(PianoStepsException):

    def getLevel(self):
        return logging.FATAL

    def __str__(self):
        return '[Error] {}'.format(self.message)

class Fatal(PianoStepsException):

    def getLevel(self):
        return logging.FATAL

    def __str__(self):
        return '[Fatal] {}'.format(self.message)

CODES = {
    "Debug": 1, # Typically used for DEBUG notices
    "General": 0, # Typically used for INFO notices
    "Serial": -1,
    "Sound": -2,
    "Laser": -3,
    "Calibration": -4,
    "Configuration": -5,
    "Invalid": -6 # Always last
}