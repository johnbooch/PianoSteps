class PianoStepsError(Exception):
    INFO = (0, 'INFO')
    WARN = (1, 'WARN')
    FATAL = (2, 'FATAL')

    errors = {
        'Serial':
            [
                {'message': 'Failed to conntect to serial port', 'severity': FATAL},
                {'message': 'No serial port discovered', 'severity': FATAL},
                {'message': 'Serial connection interrupted', 'severity': FATAL}
            ],
        'Configuration':
            [
                {'message': 'Failed to parse XML conf file', 'severity': FATAL},
                {'message': 'Failed to parse JSON conf file', 'severity': FATAL}
            ],
        'Sound':
            [
                {'message': 'Missing sound file', 'severity': FATAL},
                {'message': 'Invalid scale provided', 'severity': FATAL}
            ],
        'Arduino':
            [
                {'message': 'Calibration failure', 'severity': FATAL},
                {'message': 'Failed laser', 'severity': WARN},
                {'message': 'Failed sensor', 'severity': WARN}
            ],
        'Invalid Error':
            [
                {'message': 'Invalid error passed', 'severity': INFO}
            ]
    }

    def __init__(self, errID, errType):
        self.parseErrorCode(errType, errID)

    def __str__(self):
        return self.logErrorMessage

    def _setDefaultErrorMessage(self):
        self.error = PianoStepsError.errors['Invalid Error'][0]

    def parseErrorCode(self, errID, errType):
        if (self.isErrorCode(errID, errType)):
            self.error = PianoStepsError.errors[errType][errID]
            self.logErrorMessage = '[%s] %s' % (self.error['severity'][1], self.error['message'])
        else:
            self._setDefaultErrorMessage()

    @staticmethod
    def isErrorCode(errID=None, errType=None):

        if not all([errID, errType]):
            return False

        if not PianoStepsError.errors.has_key(errType):
            return False

        if not PianoStepsError.errors[errType] > int(errID):
            return False

        return True
