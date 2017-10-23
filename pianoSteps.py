'''
Piano Steps Python Script
Written by: John Buccieri
Property of: Drexel Theta Tau
'''

import serial
import pygame

pygame.mixer.pre_init(channels=1, buffer=1024)
pygame.mixer.init()

class PianoSteps():
    #Constructor
    def __init__(self):


        self.numPins = 1
        self.prevInputs = [False] * self.numPins

        self.ser = serial.Serial('/dev/tty.usbmodem14111', 9600)

        notes = ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]
        self.pianoNotes = [pygame.mixer.Sound("pianoNotes/"+note+".wav") for note in notes]

    # Play Method
    def playNote(self, i):
        self.pianoNotes[i].play()

    # Run Method
    def run(self):

        while True:
            line = self.ser.readline()
            line.strip()

            # Failsafe for improper hardware setup
            assert len(line) == self.numPins

            for i, pin in enumerate(list(line)):
                currentRun = pin is not '0'
                prevRun = self.prevInputs[i]
                if currentRun and not prevRun:
                    self.playNote(i)
                self.prevInputs[i] = currentRun


if __name__ == "__main__":
    pianoStairs = PianoSteps()
    pianoStairs.run()