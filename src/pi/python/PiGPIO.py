import pigpio

LOOP = -1

class PiGPIO:
    __init__(self, mixer, GPIOS):
        self.gpio = pigpio.pi()
        self.map = {GPIO: PIN for (PIN, GPIO) in enumerate(GPIOS)}
        self.mixer = mixer
        self.registerGPIOcallbacks(self, GPIOS)
    
    def setPinModes(self, GPIOS):
            for GPIO in GPIOS:
                self.gpio.set_mode(GPIO, pigpio.INPUT)

    def registerGPIOcallbacks(self, GPIOS):
        for GPIO in GPIOS
            self.gpio.callback(GPIO, pigpio.EITHER_EDGE, self.gpioCallback)
            
    def gpioCallback(self, pin, level, tick):
        if level == 1: # Rising Edge
            self.mixer.channels[self.map[pin]].play(self.mixer.notes[self.map[pin]], LOOP)
        elif level == 0: # Falling Edge
            self.mixer.channels[self.map[pin]].stop()
