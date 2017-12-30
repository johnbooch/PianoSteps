import pygame

from ArduinoSerial import ArduinoSerial
from PianoStepsErrorHandler import PSEHandler
from PianoStepsConfigurer import PianoStepsConfigurer

import PianoStepsExceptions as Exceptions


class PianoStepsRunner(ArduinoSerial):

    scales = {'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]}

    def __init__(self, confFile):
        configurations = PianoStepsConfigurer(confFile).getConfigurations()
        self._validateConfigurations(configurations)

        self.pinCount = configurations['PinCount']
        self.boardType = configurations['BoardType']
        self.scale = configurations['ScaleType']
        self.serialHistory = [False] * self.pinCount

        serialPort = configurations['SerialPort']
        baudRate = configurations['BaudRate']
        timeout = configurations['SerialTimeout']

        ArduinoSerial.__init__(serialPort, baudRate, timeout)

    def _validateConfigurations(self, confs):
        pass

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
        if not PianoStepsRunner.scales.has_key(self.scale):
            raise Exceptions.deserialize('Sound', 2)

        self.pianoNotes = [pygame.mixer.Sound("pianoNotes/${self.scale}/" + note + ".wav") for note in
                           PianoStepsRunner.scales[self.scale]]

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
