class PianoStepsError(Exception):
	INFO = (0, 'INFO')
	WARN = (0, 'WARN')
	FATAL = (0, 'FATAL')

	errors = 
	{'Serial':
		[
			('Failed to conntect to serial port', FATAL), \
			('No serial port discovered', FATAL), 
			('Serial connection interrupted', FATAL)
		],
	'Configuration':
		[
			('Failed to parse XML conf file', FATAL), 
			('Failed to parse JSON conf file', FATAL)
		],
	'Sound':
		[
			('Missing sound file', FATAL), 
			('Invalid scale provided', FATAL)
		],
	'Arduino': 
		[
			('Calibration failure', FATAL), 
			('Failed laser', WARN), 
			('Failed sensor', WARN)
		]
	'Invalid Error':
    			[
					('Invalid error passed', INFO)
				]
	}
	
	def __init__(self, errID, errType):
		self.parseErrorCode(errType, errID):
		
	def __str__(self):
		return self.logErrorMessage

	def _setDefaultErrorMessage(self): 
		self.error = errors['Invalid Error'][0]

	def parseErrorCode(self, errID, errType):
		if(self.isErrorCode(errID, errType):
			self.error = errors[errType][errID]
		else:
			self._setDefaultErrorMessage()	
	
	@staticmethod	
	def isErrorCode(errID = None, errType = None):
			
		if (!all([errID, errType])):
			return False
		
		if(!errors.has_key(errType)):
			return False
		
		if(len(errors[errType]) > int(errID)):
			return False
		
		return True
