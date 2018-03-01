from os import path
import Runner

MAIN_DIR = path.dirname(path.abspath(__file__))
CONFIG_PATH = 'META-INF/PianoSteps.xml'

def main(args):
    config = path.join(MAIN_DIR, CONFIG_PATH)
    return Runner(config).run()

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))