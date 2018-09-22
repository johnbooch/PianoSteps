from argparse import ArgumentParser

def create_deploy_parser():
    parser = ArgumentParser(description='Piano Steps deploy script')

    parser.add_argument('-m', '--mode', type=str, default='Info', help='Run deployment in debug or info mode')
    parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean build directory')
    
    return parser

def create_deploy_arduino_parser():
    parser = ArgumentParser(description='Piano Steps environment script')

    parser.add_argument('-m', '--mode', type=str, default='Info', help='Run deployment in debug or info mode')
    parser.add_argument('-b', '--build', action='store_true', default=False, help='Build c source code')
    parser.add_argument('-u', '--upload', action='store_true', default=False, help='Upload compiled arduino source code')
    parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean arduino build directory')

    return parser

def create_deploy_pi_parser():
    parser = ArgumentParser(description='Piano Steps pi script')

    parser.add_argument('-m', '--mode', type=str, default='Info', help='Run deployment in debug or info mode')
    parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean env directory')

    return parser

def create_deploy_resources_parser():
    parser = ArgumentParser(description='Piano Steps resources script')

    parser.add_argument('-m', '--mode', type=str, default='Info', help='Run deployment in debug or info mode')
    parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean env directory')

    return parser

def create_env_parser():
    parser = ArgumentParser(description='Piano Steps environment script')

    parser.add_argument('-m', '--mode', type=str, default='Info', help='Run deployment in debug or info mode')
    parser.add_argument('-c', '--clean', action='store_true', default=False, help='Clean env directory')

    return parser
