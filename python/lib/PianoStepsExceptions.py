### Exception Classes ###

class PSException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.message)

class Info(PSException):
    def __str__(self):
        return '[Info] {}'.format(self.message)

class Warn(PSException):
    def __str__(self):
        return '[Warning] {}'.format(self.message)

class Fatal(PSException):
    def __str__(self):
        return '[Error] {}'.format(self.message)



### Arduino Exceptions List ###

# When supplied with a string, each of these returns a template for creating
# PSException objects containing that string
INFO = lambda message: lambda: Info(message)
WARN = lambda message: lambda: Warn(message)
FATAL = lambda message: lambda: Fatal(message)

ERRORS = {
    'Serial':
        [
            FATAL('Failed to conntect to serial port'),
            FATAL('No serial port discovered'),
            FATAL('Serial connection interrupted')
        ],
    'Configuration':
        [
            FATAL('Failed to parse XML conf file'),
            FATAL('Failed to parse JSON conf file')
        ],
    'Sound':
        [
            FATAL('Missing sound file'),
            FATAL('Invalid scale provided')
        ],
    'Arduino':
        [
            FATAL('Calibration failure'),
            WARN('Failed laser'),
            WARN('Failed sensor')
        ],
    'Invalid Error':
        [
            INFO('Invalid error passed')
        ]
}

def isErrorCode(errType=None, errID=None):
    '''Returns True if the serialized exception is valid. False otherwise'''
    
    if errID is None or errType is None:
        return False
        
    elif not ERRORS.has_key(errType):
        return False
        
    elif int(errID) >= len(ERRORS[errType]):
        return False
        
    else:
        return True

def deserialize(errType, errID):
    '''Deserializes and returns an exception object'''
    
    if isErrorCode(errType, errID):
        return ERRORS[errType][errID]()
    else:
        return ERRORS['Invalid Error'][0]()
