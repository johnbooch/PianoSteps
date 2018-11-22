import os
from deploy_utils import clean_build_scaffold, mk_build_scaffold, run_commands_seq, BUILD_PATH, ENV_PATH, logger
from parsers import create_deploy_parser

parser = create_deploy_parser()
opts = parser.parse_args()

if not os.path.exists(BUILD_PATH):
    logger.info('Creating build directory scaffold')
    mk_build_scaffold(BUILD_PATH)

if opts.clean:
    clean_build_scaffold(BUILD_PATH)

assert(os.path.exists(ENV_PATH)) # Check to make sure python environment exists

COMMANDS = ["python deploy_arduino.py --upload", "python deploy_pi.py", "python "+os.path.join(BUILD_PATH, 'pi', 'run.py')]

run_commands_seq(COMMANDS)