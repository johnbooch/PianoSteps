class PianoStepsErrorHandler(Exception):

	errorIDs = {'Serial': ['Failed to conntect to serial port', 'No serial port discovered', 'Serial connection interrupted'],
				'Configuration': ['Failed to parse XML Conf File'],
				''}


	def __init__(self, errID, errType, severity):
		
		
