/* =====================================
 *  Arduino Hardware Pin Probing Library
 *  Author: John Buccieri
 *  Last Date Updated: 07/18/17
 *====================================/

/*****************************************************************************************************
 * IMPORTANT NOTE: If you do not have unused analog pins tied to ground, active analog methods will not 
 * behave properly
 * 
 * Hardware Pin Probing
 * A library dedicated to dedicated to efficient continous probing of Arduino GPIOS, Analog, and Digital Pins
 * 
 ****************************************************************************************************/

#include "probe.h"
#include "Arduino.h"

/* Pin references for digital and analog pins on Arduino Uno */
const int uno_analog_pins[UNO_MAX_ANALOG_PINS] = {0, 1, 2, 3, 4, 5};
const int uno_digital_pins[UNO_MAX_DIGITAL_PINS] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

/* Pin references for digital and analog pins on Arduino Mega */
const int mega_analog_pins[MEGA_MAX_ANALOG_PINS] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
const int mega_digital_pins[MEGA_MAX_DIGITAL_PINS] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,45, 46, 47, 48, 49, 51, 52, 53};

const int analogPinNumber[] = {UNO_MAX_ANALOG_PINS,  MEGA_MAX_ANALOG_PINS, NANO_MAX_ANALOG_PINS, MICRO_MAX_ANALOG_PINS, MINI_MAX_ANALOG_PINS, INVALID_ID};
const int digitalPinNumber[] = {UNO_MAX_DIGITAL_PINS, MEGA_MAX_DIGITAL_PINS, NANO_MAX_DIGITAL_PINS, MICRO_MAX_DIGITAL_PINS, MINI_MAX_DIGITAL_PINS, INVALID_ID};


Probe::Probe(int id) {

  boardId = id;
  maxAnalogPins = analogPinNumber[id];
  maxDigitalPins = digitalPinNumber[id];

  analogPinVals = (int *) malloc(maxAnalogPins*sizeof(int));
  digitalPinVals = (int *) malloc(maxDigitalPins*sizeof(int));
}

Probe::~Probe(void) {

  free(analogPinVals);
  free(digitalPinVals);
}

int Probe::analogProbe(int pin){
  if (pin > maxAnalogPins) 
    return FAILURE;
    
  return analogRead(pin);
}

int Probe::digitalProbe(int pin){
  if (pin > maxDigitalPins) 
    return FAILURE;
    
  return digitalRead(pin);
}

int Probe::analogDump(int values[], bool serialPrint) {

  for (int i = 0; i < maxAnalogPins; i++){
    values[i] = analogRead(i);
    if (serialPrint) {
      Serial.print(values[i]);
      Serial.print("\t");
    }
  }
  Serial.println();
}

int Probe::digitalDump(int values[], bool serialPrint) {

  for (int i = 0; i < maxAnalogPins; i++){
    values[i] = analogRead(i);
    if (serialPrint) 
      Serial.println(values[i]);
  }
}
