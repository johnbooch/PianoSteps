#!bin/bash

set -e 
set -a

PIANOSTEPS_PATH="$1"

DEPLOY_DIR="${PIANOSTEPS_PATH}/deploy/"
PYTHON_INIT="${PIANOSTEPS_PATH}/python/run.py"
PROPS_FILE="${PIANOSTEPS_PATH}/META_INF/PianoSteps.xml"

CompileSrc() {

}

InitPython() {

	bash $PYTHON_INIT

}



if [ -f "$PROPS_FILE" ]; then	
	lines="cat $PROPS_FILE"
	for line in $lines; do
		echo $line
    do	
else
   echo "No hardware configuration file found"
   exit 1
fi

