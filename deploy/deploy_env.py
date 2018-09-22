import os
import logging
import subprocess
from deploy_utils import clean_dir, run_commands_seq, logger
from parsers import create_env_parser

# Parse options
parser = create_env_parser()
opts = parser.parse_args()

# Configure logger
logger.setLevel(getattr(logging, opts.mode.upper()))
logger.addHandler(logging.StreamHandler()) # Prints to stderr

# Path variables
ENV_PATH = os.path.join(os.getcwd(), 'env')
DEP_PATH = os.path.join(os.getcwd(), 'dependencies.txt')
 
logger.debug("Environment path: %s", ENV_PATH)
logger.debug("Dependencies path: %s", DEP_PATH)

VENV_COMMAND = "python -m virtualenv "+ENV_PATH
VENV_DEPENDENCIES = os.path.join(ENV_PATH, 'Scripts', 'pip')+" install -r "+DEP_PATH

# Create virtual environment 
if not os.path.exists(os.path.join(ENV_PATH, 'Scripts')):
    run_commands_seq(VENV_COMMAND)
    logger.info("Virtual envrironment created")

if opts.clean:
    clean_dir(ENV_PATH)

# Install dependencies 
logger.debug("Installing dependencies from %s", DEP_PATH)
run_commands_seq(VENV_DEPENDENCIES)
logger.info("Dependency installation completed")

logger.info("Virtual environment created successfully")
