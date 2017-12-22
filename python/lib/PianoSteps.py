import pygame
import PianoStepsConfigurer
import PianoStepsError

class PianoStepsRunner(ArduinoSerial):

	scales = {'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]}


    def __init__(self, confFile):

    	configurations = PianoStepsConfigurer(confFile).getConfigurations()
		self.validateConfigurations(configurations)

        self.pinCount = configurations['PinCount']
        self.boardType = configurations['BoardType']
        self.scale = configurations['ScaleType']
		self.serialHistory = [False] * self.pinCount

		
		serialPort = configurations['SerialPort']
        baudRate = configurations['BaudRate']
        timeout = configurations['SerialTimeout']

		super.__init__(serialPort, baudRate, timeout)
			
	   
    def playNote(self, activePins):
        for pin in activePins: self.pianoNotes[pin].play()
		
	def processSerialLine(self, line):
		line = line.strip().split(' ')
		
		if (PianoStepsError.isErrorCode(*line):
			raise new PianoStepsError(*line) 
		
		line = list(map(bool, map(int, line[0])))
		line = [pin for pin, value in enumerate(line) if (value != False and value != self.serialHistory[pin])]
		return line
	
	def loadSoundFiles(self):
		if (!scales.has_key(self.scale)):
			raise new PianoStepsError('Sound', 2)
		
		self.pianoNotes = [pygame.mixer.Sound("pianoNotes/${self.scale}/"+note+".wav") for note in scales[self.scale]]
	
	def updateSerialHistory(self, activePins):
		updatedSerialHistory = [pin in activePins for pin, value in enumerate(self.serialHistory)]
		return updatedSerialHistory
		
    def run(self):
		while True:
			try:
				activePins = self.processSerialLine(self.ser.readline())
				
				self.playNotes(activePins)
				
				self.serialHistory = self.updateSerialHistory(activePins)

			except: PianoStepsError as PE:
				PianoStepsErrorHandler(PE)
				
				
				