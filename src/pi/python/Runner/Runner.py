import json
import logging
import os
import pygame

from Arduino.ArduinoSerial import ArduinoSerial
from Pi.PiMixer import PiMixer
from Pi.PiGPIO import PiGPIO

from Exceptions import Exceptions

# GLOBAL VALUES
SCALE = 'scale'
PIN_COUNT = 'pinCount'
BAUD_RATE = 'baudRate'
TIMEOUT = 'timeout'
GPIO_PINS = 'gpioPins' 
SERIAL_PORT = 'serialPort' 

class Runner(object):

    CONFIG_PATH = 'resources/META-INF/PianoSteps.json'

    REQUIRED_CONFIG_OPTS = [GPIO_PINS, PIN_COUNT, SCALE, SERIAL_PORT]

    DEFAULT_CONFIGS = {
        SCALE: 'ChromaticScale',
        BAUD_RATE: 9600,
        TIMEOUT: 0.1
    }

    LOGGER = 'PianoStepsLogger'

    INIT = 3
    EXEC = 6
    HALT = 7

    def __init__(self):
        self.logger = logging.getLogger(Runner.LOGGER)

    def configure(self, path):
        self.__loadConfigurations(os.path.join(path, Runner.CONFIG_PATH))
        self.__validateConfigurations()

    def init(self):

        # Set logger level
        self.logger.setLevel(getattr(logging, self.config.logLevel))

        # Get Mixer Ready
        self.mixer = PiMixer(self.config[PIN_COUNT], self.config[SCALE])
        self.mixer.init()

        # Get PI GPIO interface ready
        self.piGPIO= PiGPIO(self.mixer, self.config[GPIO_PINS])

        # Establish connection with arduino serial port
        self.serial = ArduinoSerial(self.config[SERIAL_PORT], self.config[BAUD_RATE], self.config[TIMEOUT]) # TODO determine serial port
        self.serial.open()

        self.state = Runner.INIT
        self.serial.write(self.state)

        while (self.serial.read() != Runner.INIT): pass
    
    def run(self):
        self.state = Runner.EXEC
        self.serial.write(self.state)
        while (self.serial.read() != Runner.EXEC): pass

        while (self.state != Runner.HALT): 
            self.state = self.serial.read()
        
        return 0

    def __loadConfigurations(self, confFile):
        try:
            self.config = {**Runner.DEFAULT_CONFIGS, **json.load(open(confFile))}
        except FileNotFoundError:
            raise Exceptions.Fatal('Could not find config file "{}"'.format(confFile), Exceptions.CODES['Configuration'])
        except json.decoder.JSONDecodeError:
            raise Exceptions.Fatal('Syntax error in config file "{}"'.format(confFile), Exceptions.CODES['Configuration'])
    
    def __validateConfigurations(self): 
        for name in Runner.REQUIRED_CONFIG_OPTS:
            if name not in self.config or self.config[name] is None:
                raise Exceptions.Fatal('Missing configuration option "{}" in config file'.format(name), Exceptions.CODES['Configuration]'])
        
        if self.config[PIN_COUNT] is len(self.config[GPIO_PINS]):
                raise Exceptions.Fatal('Pin Count: "{}" and GPIO Pins: "{}" do not match"'.format(self.config[PIN_COUNT], len(self.config[GPIO_PINS])), Exceptions.CODES['Configuration]'])