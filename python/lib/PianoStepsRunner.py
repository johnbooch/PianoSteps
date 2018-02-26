import pygame

from ArduinoSerial import ArduinoSerial
from PianoStepsErrorHandler import PSEHandler
from PianoStepsConfigurer import PianoStepsConfigurer

import PianoStepsExceptions as Exceptions

SCALES = {'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]}

class PianoStepsRunner:

    def __init__(self, confFile):
        self.loadConfigurations(confFile)
        self.serialHistory = [False] * self.pinCount
        self.serial = ArduinoSerial(self.serialPort, self.baudRate, self.timeout)

    def _playNotes(self, activePins):
        for pin in activePins:
            self.pianoNotes[pin].play()

    def _processSerialLine(self, line):
        line = line.strip().split(' ')
        if Exceptions.isValid(*line):
            raise Exceptions.deserialize(*line)
        
        line = list(map(bool, map(int, line[0])))
        line = [pin for pin, value in enumerate(line) if (value != False and value != self.serialHistory[pin])]
        return line

    def _loadSoundFiles(self):
        if self.scale not in SCALES:
            raise Exceptions.deserialize('Sound', 2)
        
        self.pianoNotes = []
        for note in SCALES[self.scale]:
            filename = 'pianoNotes/{}/{}.wav'.format(self.scale, note)
            self.pianoNotes.append(pygame.mixer.Sound(filename))
            
    def _loadConfigurations(confFile):
        for key, value in json.load(confFile):
            self[key] = value

    def _updateSerialHistory(self, activePins):
        updatedSerialHistory = [pin in activePins for pin, value in enumerate(self.serialHistory)]
        return updatedSerialHistory

    def run(self):
         while True:
            try:
                activePins = self._processSerialLine(self.readSerialLine())
                self._playNotes(activePins)
                self.serialHistory = self._updateSerialHistory(activePins)
                
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