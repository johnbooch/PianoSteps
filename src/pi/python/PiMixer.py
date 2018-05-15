import pygame

VALID_SCALES = {
    'ChromaticScale': ["a", "b", "bb", "c", "cb", "d", "e", "eb", "g#", "f", "fb", "g", "gb"]
}

class PiMixer:
    __init__(self, NUM_CHANNELS, SCALE):
        self.SCALE = SCALE
        self.NUM_CHANNELS
        self.mixer = pygame.mixer
        self.initializeMixer()
        self.loadSoundChannels()
        self.loadSoundFiles()

    def initializeMixer(self):
        self.mixer.init()

    def loadSoundChannels(self):
        self.mixer.set_num_channels(self.NUM_CHANNELS)
        self.channels = [self.mixer.Channel(pin) for pin in range(0, self.NUM_CHANNELS)]

    def loadSoundFiles(self):
        if self.SCALE not in VALID_SCALES:
            raise Exceptions.Fatal('Invalid scale "{}"'.format(self.config['scale']))

        if self.NUM_CHANNELS is not len(VALID_SCALES(self.SCALE))
            raise Exceptions.Fatal('Channels Count: "{}" and Notes Count: "{}" do not match'.format(self.NUM_CHANNELS, len(VALID_SCALES(self.SCALE))))
        
        self.notes = [self.mixer.Sound(self.getNoteFile(self.SCALE, NOTE) for NOTE in VALID_SCALES[self.SCALE])]
    
    def getNoteFile(self, note):
            return 'resources/notes/{}/{}.wav'.format(scale, note)