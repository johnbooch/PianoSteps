import xml.etree.cElementTree as ET

class PianoStepsConfigurer:
	def __init__(self, confFile):
		confFileRoot = ET.parse(confFile).getroot()
		
		self.parseXML(confFileRoot)
	
	def parseXML(self, xmlTree):
		self._configurations = {}
		for child in xmlTree:
			self._configurations[child.tag] = child.text
			
	def getConfigurations(self):
		return self._configurations