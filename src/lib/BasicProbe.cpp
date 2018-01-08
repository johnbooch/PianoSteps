/* =====================================
 *  Arduino Hardware Pin Probing Library
 *  Author: John Buccieri
 *  Last Date Updated: 07/18/17
 *====================================*/

/*****************************************************************************************************
 * 
 * Hardware Pin Probing
 * A library dedicated to efficient continuous probing of Arduino GPIOS, Analog, and Digital Pins
 * 
 ****************************************************************************************************/

#include "Arduino.h"
#include "include/BasicProbe.h"


/*
 * Constructor
 *
 *
 */

BasicProbe::BasicProbe(int boardId) {
  boardId = boardId;
  maxAnalogPins = EXPAND_MAX_ANALOG_PINS(boardId);
  maxDigitalPins = EXPAND_MAX_DIGITAL_PINS(boardId);

  analogPinVals = (int *) malloc(maxAnalogPins*sizeof(int));
  analogPinModes = (int *) malloc(maxAnalogPins*sizeof(int));
  digitalPinVals = (int *) malloc(maxAnalogPins*sizeof(int));
  digitalPinModes = (int *) malloc(maxDigitalPins*sizeof(int));
}

/* 
 * Destructor 
 * 
 * 
 * 
 * */
 
BasicProbe::~BasicProbe(void) {
  free(analogPinVals);
  free(digitalPinVals);
}

int Probe::isAnalogPin(int pin) {
  if (pin > maxAnalogPins){
    return INVALID_ANALOG_PIN_FAILURE;
  }
  return SUCCESS;
}

int Probe::isDigitalPin(int pin) {
  if (pin > maxDigitalPins) {
    return INVALID_DIGITAL_PIN_FAILURE; 
  }
  return SUCCESS;
}

int Probe::readAnalogPin(int pin){
  if (isAnalogPin(pin)) {
      return ANALOG_READ_FAILURE;
  }
  return analogPinVals[pin] = analogRead(pin);
}

int Probe::readDigitalPin(int pin){
  if (isDigitalin(pin)) {
    return DIGITAL_READ_FAILURE;    
  }
  return digitalPinVals[pin] = digitalRead(pin);
}

int Probe::writeDigitalPWMPin(int pin, int value) {
  if (isDigitalPin(pin) && !isPWMPin(pin)) {
    return DIGITAL_PWM_WRITE_FAILURE;
  }
  analogWrite(pin, value);  
  return SUCCESS; 
}

int Probe::writeDigitalPin(int pin, int value){
  if (isDigitalPin(pin)) {
    return DIGITAL_WRITE_FAILURE;    
  }
  digitalWrite(pin, value);
  return SUCCESS;
}

/*
 * Utility Functions
 *
 *
 *
 */

int Probe::analogDump(int values[], bool serialPrint) {

}

int Probe::digitalDump(int values[], bool serialPrint) {

}

int Probe::highAnalogPinsDump(bool values[], bool serialPrint) {

}

int Probe::highDigitalPinsDump(bool values[], bool serialPrint) {
  
}

int Probe::isAnalogPinHigh(int pin){
	bool isActive = readAnalogPin(pin) != 0 ? TRUE : FALSE;
	return isActive
}

bool Probe::isDigitalPinHigh(int pin){
	bool isActive = readDigitalPin(pin) != 0 ? TRUE : FALSE;
	return isActive
}
