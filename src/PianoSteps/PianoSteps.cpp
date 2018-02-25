/*=====================================
 *         Piano Steps CPP
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "Arduino.h"
#include "BasicProbe.h"
#include "PianoSteps.h"

PianoSteps::PianoSteps()
{

  /* Open serial connection */
  SerialRef.begin(9600);

  /* Wait for serial connection to be ready */
  while (!SerialRef);

  /* Send ready response to RSP3 */
  SerialRef.write(READY);

  /* Receive Stringyfied JSON object from RSP3 */
  while (SerialRef.read() != STOP)
  {
    if (!(Serial.available() < 0)) {
      //TODO
    }
  }

  ProbeRef = new Probe(boardId);
}

PianoSteps::~PianoSteps(void)
{
  SerialRef.end();
  free(sensorHistory);
  free(thresholds);
}

uint8_t PianoSteps::init(void)
{
  SerialRef.write(INIT);
  allocateThresholdMemory();
  lightSensorCalibration();
}

uint8_t PianoSteps::run(void)
{
  while (detectHardwareErrors() == RUN)
  {
    for (int i = 0; i < pinCount; i++)
    {
      if (ProbeRef->readAnalogPin(i) > thresholds[i] + absoluteThreshold)
        SerialRef.println(SIGNAL);
      else
        SerialRef.println(NO_SIGNAL);
    }
    if (recalCount == recalLimit)
      lightSensorRecalibration();
    recalCount++;
  }
  return HALT;
}

int PianoSteps::detectHardwareErrors(void) {

  return RUN;
}

int PianoSteps::lightSensorCalibration(void)
{
  calculateAbsoluteThreshold();
  calculateRecalLimit();
}

int PianoSteps::lightSensorRecalibration(void)
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
  return SUCCESS;
}

int PianoSteps::calculateAbsoluteThreshold(void) {
  //TODO
}

int PianoSteps::allocateThresholdMemory(void) {
  //TODO
}

int PianoSteps::calculateRecalLimit(void) {
  //TODO
}

