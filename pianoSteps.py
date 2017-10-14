#=====================================#
#       Piano Steps Python Script
#       Written by: John Buccieri
#     Property of: Drexel Theta Tau
#=====================================#

import serial
import pygames

onpi = True #True ==  Rasp Pi 3

pygame.mixer.pre_init(channels=13, buffer=1024)
pygame.mixer.init()

class PianoStairs ():
        
        def __init__(self):

                self.num_pins = 13
                self.prev_inputs = [False] * self.num_pins

                if onpi == True:
                        self.ser = serial.Serial('/dev/ttyACM0', 9600)

                notes =  ["c","c#","d", "d#", "e","f", "f#", "g", "g#", "a","a#","b","c"]
                self.piano_notes = [pygame.mixer.Sound("piano_notes/"+note+".wav") for note in notes]

        

        def play_piano_note(self, i):
                self.piano_notes[i].play();*

        def run(self):

                # time.sleep(3);

                while True:
                        print("DEBUG")
                        if onpi:
                                line = self.ser.readline()
                        else:
                                line = raw_input()

                        if len(line) < self.num_pins:
                                continue

                        for i in range(self.num_pins):
                                current_run = line[i] != '0'
                                prev_run = self.prev_inputs[i]
                                if current_run and not prev_run:
                                        self.play_piano_piano(i);
                                self.prev_inputs[i] = current_run

if __name__ == "__main__":
    pianoStairs = PianoStairs()
    pianoStairs.run()