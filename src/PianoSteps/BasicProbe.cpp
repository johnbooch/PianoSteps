/* =====================================
 *  Arduino Hardware Pin Probing Library
 *  Author: John Buccieri
 *  Last Date Updated: 07/18/17
 *====================================*/

/*****************************************************************************************************
 * 
 * Hardware Pin Probing
 * A library dedicated to efficient control and probing of Arduino Analog, and Digital Pins
 * 
 ****************************************************************************************************/

#include "Arduino.h"
#include "BasicProbe.h"

/*
 * Constructor
 *
 *
 */

Probe::Probe(int _boardId)
{
  boardId = _boardId;
  numAnalogPins = NUM_ANALOG_INPUTS;
  numDigitalPins = NUM_DIGITAL_PINS;

  analogPinVals = (int *) malloc(numAnalogPins * sizeof(int));
  analogPinModes = (int *) malloc(numAnalogPins * sizeof(int));
  digitalPinVals = (int *) malloc(numDigitalPins * sizeof(int));
  digitalPinModes = (int *) malloc(numDigitalPins * sizeof(int));
}

/* 
 * Destructor 
 * 
 * */

Probe::~Probe(void)
{
  free(analogPinVals);
  free(digitalPinVals);
}

int Probe::readAnalogPin(int pin)
{
  return analogPinVals[pin] = analogRead(pin);
}

int Probe::readDigitalPin(int pin)
{
  return digitalPinVals[pin] = digitalRead(pin);
}

/*
 * Utility Functions
 */

int * Probe::getAnalogPinVals(bool serialPrint)
{
  for (int pin = 0; pin < numAnalogPins; pin++)
  {
    analogPinVals[pin] = readAnalogPin(pin);
    if (serialPrint){
      Serial.println();
    }
  }
  return analogPinVals;
}

int * Probe::getDigitalPinVals(bool serialPrint)
{
  for (int pin = 0; pin < numDigitalPins; pin++)
  {
    digitalPinVals[pin] = readDigitalPin(pin);
  }
  return digitalPinVals;
}

bool * Probe::getHighAnalogPins(bool serialPrint)
{
  return highAnalogPins;
}

bool * Probe::getHighDigitalPins(bool serialPrint)
{
  return highDigitalPins;
}

bool Probe::isHighAnalogPin(int pin)
{
  bool isActive = readAnalogPin(pin) != 0 ? TRUE : FALSE;
  return isActive;
}

bool Probe::isHighDigitalPin(int pin)
{
  bool isActive = readDigitalPin(pin) != 0 ? TRUE : FALSE;
  return isActive;
}
