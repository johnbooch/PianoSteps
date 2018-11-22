import os
from deploy_utils import copy_dir, clean_dir, PI_BUILD_DIR, PI_SRC_DIR, logger
from parsers import create_deploy_pi_parser

parser = create_deploy_pi_parser()
opts = parser.parse_args()

if opts.clean:
    logger.info('Cleaning pi build dir')
    clean_dir(PI_BUILD_DIR)
else:
    logger.info("Copying pi files into build directory")
    copy_dir(PI_SRC_DIR, PI_BUILD_DIR)