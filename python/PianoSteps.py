import serial
import pygame

import PianoStepsConfigurer
import PianStepsErrorHandler

class PianoStepsRunner():
    #Constructor
    def __init__(self):

        self.numPins = 1
        self.prevInputs = [False] * self.numPins
		self.serialPort = '/dev/tty.usbmodem14111'
		
		try {
			self.ser = serial.Serial(serialPort, 9600)
		}
		except Exception as e {
			raise PianStepsErrorHandler(errType, errID)
		}
        notes = ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]
        self.pianoNotes = [pygame.mixer.Sound("pianoNotes/"+note+".wav") for note in notes]

    # Play Method
    def playNote(self, i):
        self.pianoNotes[i].play()
	
	def errorThrower(self, errString){
		raise PianStepsErrorHandler(errString)
	}
    # Run Method
    def run(self):

        while True:
            line = self.ser.readline()
            line.strip()

            for i, pin in enumerate(list(line)):
                currentRun = pin is not '0'
                prevRun = self.prevInputs[i]
                if currentRun and not prevRun:
                    self.playNote(i)
                self.prevInputs[i] = currentRun