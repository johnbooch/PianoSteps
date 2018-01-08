#!bin/bash

set -e 
set -a

PianoSteps_Path="$1"
PinCount="$2"
BoardType="$3"
SerialPort="$4"

DEPLOY_DIR="${PianoSteps_Path}/deploy/"
PYTHON_INIT="${PianoSteps_Path}/python/run.py"
PROPS_XML_FILE="${PianoSteps_Path}/META_INF/PianoSteps.xml"
PROPS_JSON_FILE="${PianoSteps_Path}/META_INF/PianoSteps.json"

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
	
	arduino --verify $PianoSteps_Path/src/PianoSteps.ino
	if [$? -ne 0]; then
		echo "[FATAL] Arduino sketch failed to verify. Exiting..."
		exit(1)

	arduino --upload $PianoSteps_Path/src/PianoSteps.ino --port $SerialPort

	if [$? -ne 0]; then
		echo "[FATAL] Arduinon sketch failed to upload. Exiting..."
		exit(1)
}

