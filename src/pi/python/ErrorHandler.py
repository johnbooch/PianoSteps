import os

class ErrorHandler:
    def __init__(self, logPath):
        self.logFile = open(logPath, 'a+')

    def evaluateError(self, PSE):
        self.logError(PSE.logErrorMessage)
        self.evaluateErrorSeverity(PSE.error['severity'])

    def evaluateErrorSeverity(self, error):
        if error[0] == 0:
            pass ## TODO

        if error[0] == 1:
            pass ## TODO

        if error[0] == 2:
            pass ## TODO

    def logError(self, message):
        self.logFile.write(message + '\n')

    def __del__(self):
        self.logFile.close()

LogPath = os.path.dirname(os.path.abspath(__file__))
PSEHandler = ErrorHandler(LogPath + 'logs/PianoSteps.log')