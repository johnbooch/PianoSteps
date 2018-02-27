import pygame
import json

from ArduinoSerial import ArduinoSerial
from PianoStepsErrorHandler import PSEHandler
from PianoStepsConfigurer import PianoStepsConfigurer

import PianoStepsExceptions as Exceptions

# All config value names
SCALE = 'scale'
PIN_COUNT = 'pinCount'
BOARD_TYPE = 'boardType'
BAUD_RATE = 'baudRate'

# A list of required config values
REQUIRED_CONFIG_OPTS = [PIN_COUNT, BOARD_TYPE, BAUD_RATE]

# A dict mapping config options to their default values
DEFAULT_CONFIG_OPTS = {
    SCALE: 'ChromaticScale'
}

NOTE_SCALES = {
    'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]
}

def getNoteFile(scale, note):
    return 'pianoNotes/{}/{}.wav'.format(scale, note)

class PianoStepsRunner:
    
    def __init__(self, confFile):
        self.loadConfigurations(confFile)
        self.loadSoundFiles()
        
        self.timeout = 0.1
        self.pinHistory = [False] * self.config[PIN_COUNT]
        # TODO determine serial port
        self.serial = ArduinoSerial(self.serialPort, self.config[BAUD_RATE], self.timeout)
    
    def playNotes(self, activePins):
        for pin in activePins:
            if 0 <= pin < len(self.pianoNotes):
                self.pianoNotes[pin].play()
    
    def isValidPinState(state):
        return len(state) == self.pinCount and all([c in '01' for c in state])
    
    def readSerialLine():
        pass # TODO
    
    def processException(line):
        raise Exceptions.deserialize(line[0], line[1])
    
    def processNotes(line):
        vals = [x == '1' for x in line[0]]
        pins = [pin for pin, value in enumerate(vals) if (value and value != self.pinHistory[pin])]
        self.playNotes(pins)
        self.updatePinHistory(vals)
    
    def processSerialLine(self, line):
        line = line.strip().split(' ')
        
        # check if line represents an Arduino error
        if len(line) == 2 and Exceptions.isErrorCode(*line):
            self.processException(line)
        
        # check if line represents a valid pin state
        elif len(line) == 1 and isValidPinState(*line)
            self.processNotes(line)
        
        else:
            # TODO print as a warning rather than raising an exception
            raise Exceptions.fatal('Invalid line read from serial port')
    
    def loadSoundFiles(self):
        if self.config['scale'] not in NOTE_SCALES:
            raise Exceptions.Fatal('Invalid scale "{}"'.format(self.config['scale']))
        
        self.pianoNotes = []
        for note in NOTE_SCALES[self.scale]:
            filename = getNoteFile(self.scale, note)
            self.pianoNotes.append(pygame.mixer.Sound(filename))
            
    def loadConfigurations(confFile):
        try:
            self.config = json.load(open(confFile))
        except FileNotFoundError as e:
            raise Exceptions.Fatal('Could not find config file "{}"'.format(confFile))
        except json.decoder.JSONDecodeError as e:
            raise Exceptions.Fatal('Syntax error in config file "{}"'.format(confFile))
        
        # check for config options which have default values
        for name in DEFAULT_CONFIG_OPTS:
            if name not in self.config or self.config[name] is None:
                self.config[name] = DEFAULT_CONFIG_OPTS[name]
        
        # check for config options which are required
        for name in REQUIRED_CONFIG_OPTS:
            if name not in self.config or self.config[name] is None:
                raise Exceptions.Fatal('Missing configuration option "{}" in config file "{}"'.format(name, confFile))

    def updatePinHistory(self, pinValues):
        self.pinHistory = pinValues
    
    def run(self):
         while True:
            try:
                self.processSerialLine(self.readSerialLine())
                
            except Exceptions.PSInformation as exc:
                print(exc)
                
            except Exceptions.PSWarning as exc:
                print(exc)
                
            except Exceptions.PSError as exc:
                print(exc)
                print('Exiting...')
                return 1
                
            except Exception as exc:
                print(exc)
                print('Exiting...')
                return 1