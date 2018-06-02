import pygame
import json
import os

from ArduinoSerial import ArduinoSerial
from ErrorHandler import PSEHandler
from PiGPIO import PiGPIO


import Exceptions

# GLOBAL VALUES
SCALE = 'scale'
PIN_COUNT = 'pinCount'
BAUD_RATE = 'baudRate'
TIMEOUT = 'timeout'
GPIO_PINS = 'gpioPins' 
# Gpio pin list should be in the correct note order. The first gpio pin gives the
# pin number for the first note and so on.

CONFIG_PATH = 'resources/META-INF/PianoSteps.xml'
SOUND_PATH = 'resources/notes/'

# A list of required config values
REQUIRED_CONFIG_OPTS = [PIN_COUNT, SCALE, PIN_COUNT, GPIO_PINS]

# A dict mapping config options to their default values
DEFAULT_CONFIGS = {
    SCALE: 'ChromaticScale',
    BAUD_RATE: 9600,
    TIMEOUT: 0.1
}

class Runner:
    
    def __init__(self, MAIN_DIR):
        self.MAIN_DIR = MAIN_DIR
        self.configure(os.path.join(self.MAIN_DIR, CONFIG_PATH))
        self.serial = ArduinoSerial(self.config[SERIAL_PORT], self.config[BAUD_RATE], self.config[TIMEOUT]) # TODO determine serial port
        self.mixer = PiMixer(self.config[PIN_COUNT], self.config[SCALE])
        self.piGPIO= PiGPIO(self.mixer, self.config[GPIO_PINS])

    def configure(self, confFile):
            self.loadConfigurations(confFile)
            self.validateCo  nfigurations()

    def loadConfigurations(confFile):
        try:
            self.config = {**DEFAULT_CONFIGS, **json.load(open(confFile))}
        except FileNotFoundError as e:
            raise Exceptions.Fatal('Could not find config file "{}"'.format(confFile))
        except json.decoder.JSONDecodeError as e:
            raise Exceptions.Fatal('Syntax error in config file "{}"'.format(confFile))
    
    def validateConfigurations(): 
        for name in REQUIRED_CONFIG_OPTS:
            if name not in self.config or self.config[name] is None:
                raise Exceptions.Fatal('Missing configuration option "{}" in config file "{}"'.format(name, confFile))
        
        if self.config[PIN_COUNT] is not len(self.config[GPIO_PINS]):
                raise Exceptions.Fatal('Pin Count: "{}" and GPIO Pins: "{}" do not match"'.format(self.config[PIN_COUNT], len(self.config[GPIO_PINS]))

