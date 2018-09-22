from deploy_utils import copy_dir, clean_dir, RESOURCES_BUILD_DIR, RESOURCES_DIR, logger
from parsers import create_deploy_resources_parser

parser = create_deploy_resources_parser()
opts = parser.parse_args()

if opts.clean:
    logger.info('Cleaning pi build dir')
    clean_dir(RESOURCES_BUILD_DIR)
else:
    logger.info("Copying pi files into build directory")
    copy_dir(RESOURCES_DIR, RESOURCES_BUILD_DIR)