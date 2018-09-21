import argparse
import subprocess

parser = argparse.ArgumentParser(description='Piano Steps deploy script')

parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean build directory')
parser.add_argument('-b', '--build', action='store_true', default=False, help='Build c source code')
parser.add_argument('-d', '--debug', action='store_true', default=False, help = 'Run deployment in debug mode')
parser.add_argument('-v', '--verbose', action='store_true', default=False, help = 'Run deployment in verbose mode')