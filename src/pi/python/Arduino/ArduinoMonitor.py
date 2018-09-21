import logging 

import Exceptions

class ArduinoMonitor:
    LOGGER = 'PianoStepsLogger'

    def __init__(self, logPath):
        self.logger = logging.getLogger(ArduinoMonitor.LOGGER)

    def evaluate(self, data):
        pass