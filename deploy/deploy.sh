#!bin/bash

set -e 
set -a

PIANOSTEPS_PATH="$1"

DEPLOY_DIR="${PIANOSTEPS_PATH}/deploy/"
PYTHON_INIT="${PIANOSTEPS_PATH}/python/run.py"
PROPS_FILE="${PIANOSTEPS_PATH}/META_INF/PianoSteps.xml"

DiscoverSerialPort() {
	echo "Discovering Serial Ports"

}

SetConfigurations() {
	xml ed -u "PianoSteps/PinCount" -v $PinCount $PROPS_FILE
	xml ed -u "PianoSteps/BoardType" -v $BoardType $PROPS_FILE
	xml ed -u "PianoSteps/SerialPort" -v $SerialPort $PROPS_FILE
}

InitPython() {
	echo "Initializing Python scripts"

	bash $PYTHON_INIT

	if [$? -ne 0]; then 
		echo "[FATAL] Failed to initialize python scripts"
		exit(1)
}

UploadArduinoSrc() {
	echo "Compiling and uploading source to Arduino"
	
	arduino --verify $PIANOSTEPS_PATH/src/PianoSteps.ino
	if [$? -ne 0]; then
		echo "[FATAL] Arduino sketch failed to verify. Exiting..."
		exit(1)

	arduino --upload $PIANOSTEPS_PATH/src/PianoSteps.ino --port $SerialPort

	if [$? -ne 0]; then
		echo "[FATAL] Arduinon sketch failed to upload. Exiting..."
		exit(1)
}

