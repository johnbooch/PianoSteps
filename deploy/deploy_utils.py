import logging
import os

logger = logging.getLogger('Deploy_Logger')

BUILD_PATH = os.path.join(os.getcwd(), 'build')
ENV_PATH = os.path.join(os.getcwd(), 'env')
DEP_PATH = os.path.join(os.getcwd(), 'dependencies.txt')
ARDUINO_SRC_DIR = os.path.join(os.getcwd(), 'src', 'arduino')
ARDUINO_BUILD_DIR =  os.path.join(os.getcwd(), 'build', 'arduino')
PI_SRC_DIR = os.path.join(os.getcwd(), 'src', 'pi')
PI_BUILD_DIR =  os.path.join(os.getcwd(), 'build', 'pi')
RESOURCES_DIR = os.path.join(os.getcwd(), 'resources')
RESOURCES_BUILD_DIR = os.path.join(os.getcwd(), 'build', 'resources')

def mk_build_scaffold():
    os.makedirs(BUILD_PATH, exist_ok=True)
    os.makedirs(ARDUINO_BUILD_DIR, exist_ok=True)
    os.makedirs(PI_BUILD_DIR, exist_ok=True)

def clean_build_scaffold(BUILD_PATH):
    import shutil
    shutil.rmtree(ARDUINO_BUILD_DIR)
    shutil.rmtree(PI_BUILD_DIR)

def copy_dir(src, dst):
    import shutil
    shutil.copytree(src, dst)

def clean_dir(dir):
    import shutil
    shutil.rmtree(dir)

def run_commands_seq(*cmds):
    import subprocess
    for cmd in cmds:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            o = p.stdout.readline().decode('utf-8')
            if o == '' and p.poll() is not None:
                break
            if o:
                logger.info(o.strip())