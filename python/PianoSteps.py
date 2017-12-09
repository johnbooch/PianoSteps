import serial
import pygame
import PianoStepsConfigurer
import PianStepsErrorHandler

class PianoStepsRunner():

	scales = {'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"],}


    def __init__(self, confFile):
    
    	configurations = PianoStepsConfigurer(confFile).getConfigurations()
        self.pinCount = configurations['PinCount']
        self.boardType = configurations['BoardType']
        self.serialPort = configurations['SerialPort']
        self.baudRate = configurations['BaudRate']
        self.scaleType = configurations['ScaleType']
        
        
        self.serialHistory = [False] * self.pinCount
        self.pianoNotes = [pygame.mixer.Sound("pianoNotes/"+note+".wav") for note in notes]
        self.ser = serial.Serial(self.serialPort, self.baudRate)
        
       
    def playNote(self, i):
        self.pianoNotes[i].play()
	
	def errorThrower(errID, errType){
		raise PianStepsErrorHandler(errID, errType)
	}
	
    def run(self):

        while True:
            line = self.ser.readline()
            line.strip()

            for _ , pin in enumerate(list(line)):
            	playNote = pin != '0' && pin != self.serialHistory[pin]
                if playNote:
                    self.playNote(pin)
                self.serialHistory[pin] = pin != '0'