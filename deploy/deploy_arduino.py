import os
from deploy_utils import copy_dir, clean_dir, ARDUINO_BUILD_DIR, ARDUINO_SRC_DIR, logger
from parsers import create_deploy_arduino_parser

parser = create_deploy_arduino_parser()
opts = parser.parse_args()

if opts.clean:
    logger.info('Cleaning arduino build dir')
    clean_dir(ARDUINO_BUILD_DIR)
else:
    logger.info("Copying arduino files into build directory")
    copy_dir(ARDUINO_SRC_DIR, ARDUINO_BUILD_DIR)

if opts.build:
    pass

if opts.upload:
    pass
