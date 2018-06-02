import pigpio

LOOP = -1

class PiGPIO:
    __init__(self, mixer, GPIOS):
    """
    Constructor

    
    """
        self.gpio = pigpio.pi()
        self.map = {GPIO: PIN for (PIN, GPIO) in enumerate(GPIOS)}
        self.mixer = mixer
        self.registerGPIOcallbacks(self, GPIOS)
    
    def setPinModesInput(self, GPIOS):
        """
        Set GPIO pin modes to input

        Args:
            GPIOS: List of RP3 GPIO pins
        Returns:
            Nothing
        """
        for GPIO in GPIOS:
            self.gpio.set_mode(GPIO, pigpio.INPUT)

    def registerGPIOcallbacks(self, GPIOS):
        """
        Registers GPIO callbacks on each input GPIO pin

        Args:
            GPIOS: List of RP3 GPIO pins
        Returns:
            Nothing
        """
        for GPIO in GPIOS
            self.gpio.callback(GPIO, pigpio.EITHER_EDGE, self.gpioCallback)
            
    def gpioCallback(self, pin, level, tick):
        """
            Internal GPIO callback used for input GPIO Pins

            Args:
                pin: pin number callback was triggered on
                level: rising or falling edge of GPIO
                tick: timestamp of callback in milliseconds
            Returns:
                Nothing
        """
        if level == 1: # Rising Edge
            self.mixer.channels[self.map[pin]].play(self.mixer.notes[self.map[pin]], LOOP)
        elif level == 0: # Falling Edge
            self.mixer.channels[self.map[pin]].stop()
