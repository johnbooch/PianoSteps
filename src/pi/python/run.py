import Runner

MAIN_DIR = path.dirname(path.abspath(__file__))

def main(args):
    return Runner(MAIN_DIR).run()

if __name__ == '__main__':
    import sys
    exit(main(sys.argv[1:]))