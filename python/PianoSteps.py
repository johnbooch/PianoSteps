from os import path as path
from lib.PianoStepsRunner import PianoStepsRunner

def main():
    PianoStepsConfPath = path.dirname(path.abspath(__file__))
    PianoSteps = PianoStepsRunner('${PianoSteps_Path}/META-INF/PianoSteps.xml')
    return PianoSteps.run()

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))