from os import path

from Runner import Runner
import Exceptions

MAIN_DIR = path.dirname(path.abspath(__file__))

def main(args):
    runner = Runner()
    try:
        runner.configure(MAIN_DIR)
        runner.init()
    except Exceptions.PianoStepsException as e:
        runner.logger.log(e.getMessage(), e.getLevel())
        return e.getCode()
    else:
        return runner.run()

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))