import argparse

parser = argparse.ArgumentParser(description='Piano Steps deploy script')

parser.add_argument('-a', help = 'Run deployment')
parser.add_argument('-d', '--debug', action='store_true', default=False, help = 'Run deployment in debug mode')
parser.add_argument('-v', '--verbose', action='store_true', default=False, help = 'Run deployment in verbose mode')

print(parser.parse_args())


def deploy(debug = False, verbose = False):
    pass