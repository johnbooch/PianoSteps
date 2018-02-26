/*=====================================
 *         Piano Steps CPP
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "PianoSteps.h"

PianoSteps::PianoSteps()
{
  /* Open serial connection */
  Serial.begin(9600);

  /* Wait for serial connection to be ready */
  while (!Serial);
}

PianoSteps::~PianoSteps(void)
{
  Serial.end();
}

uint8_t PianoSteps::init(void)
{
  Serial.write(process = INIT);
  sensorCalibration();

  return process; 
}

uint8_t PianoSteps::exec(void)
{
  Serial.write(process = EXEC);
  while (process == EXEC)
  {
    detectHardwareErrors();
    if (recalCount == RECAL_FREQ) {
      sensorCalibration();
    }
    sensorEvaluation();
  }
  return process;
}

void PianoSteps::detectHardwareErrors(void) {
  return;
}

void PianoSteps::sensorEvaluation(void) {
  for (int i = 0; i < pinCount; i++)
  {
      if (analogRead(i) > thresholds[i] + absoluteThreshold){
        Serial.write(SIGNAL);
      }
      else {
        Serial.write(NO_SIGNAL);
      }
  }
  recalCount++;
}

void PianoSteps::sensorCalibration(void)
{
  if (process == INIT); {
    calculateAbsoluteThreshold();
    calculateRecalLimit();  
  }
  calculateSensorThresholds();
}


void PianoSteps::calculateAbsoluteThreshold(void) {
  //TODO
}

void PianoSteps::calculateRecalLimit(void) {
  //TODO
}

void PianoSteps::calculateSensorThresholds(void)
{
  memset(thresholds, 0, pinCount * sizeof(int));

  for (int i = 0; i < HISTORY_SIZE; i++)
  {
    for (int pin = 0; pin < pinCount; pin++)
    {
      sensorHistory[i][pin] = analogRead(pin);
    }
  }
  for (int pin = 0; pin < pinCount; pin++)
  {
    for (int i = 0; i < HISTORY_SIZE; i++)
    {
      thresholds[pin] += sensorHistory[i][pin];
    }
    thresholds[pin] /= HISTORY_SIZE;
  }
}

void PianoSteps::allocateThresholdMemory(void) {
  //TODO
}

