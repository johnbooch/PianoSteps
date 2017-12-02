import xml.etree.cElementTreet as ET

class PianoStepsConfigurer
	def __init__(self, confFile):
		confFileRoot = Et.parse(confFile).getRoot()
		
		self._parseXML(confFileRoot)
	
	def parseXML(xmlTree):
		self.configurations = {}
		for child in xmlTree:
			self.configuration[child.tag] = child.attrib
			
	def getConfigurations():
		return self.configurations
		
	