/*=====================================
 *         Piano Steps CPP
 *       Written by: John Buccieri and Curtis Bechtel
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "PianoSteps.h"

PianoSteps::PianoSteps()
{
  /* Turn on laser array */
  digitalWrite(MOFSET_PIN, HIGH);

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
  while(Serial.read() != INIT);
  Serial.write(process = INIT);
  Serial.write(process = sensorCalibration());
  return process; 
}

uint8_t PianoSteps::exec(void)
{
  while (Serial.read() != EXEC);
  Serial.write(process = EXEC);
  while (process == EXEC)
  {
    if (recalCount == RECAL_FREQ) {
      sensorCalibration();
    }
    sensorEvaluation();
    process = detectHardwareErrors();    
  }
  return process;
}

uint8_t PianoSteps::detectHardwareErrors(void) {
  return EXEC;
}

 void PianoSteps::sensorEvaluation(void) {
  for (int i = 0; i < PIN_COUNT; i++)
  {
      if (analogRead(i) > thresholds[i] + absoluteThresholds[i]){
        Serial.write(SIGNAL);
      }
      else {
        Serial.write(NO_SIGNAL);
      }
  }
  recalCount++;
}

uint8_t PianoSteps::sensorCalibration(void)
{
  recalCount = 0;
  if (process == INIT); {
    if (calculateAbsoluteThreshold() != CALIBRATED) {
     return HALT; 
    }
  }
  calculateSensorThresholds();
  return process;
}

uint8_t PianoSteps::calculateAbsoluteThreshold(void) {
  uint16_t lowVals[PIN_COUNT][CALIBRATION_BLINKS];
  uint16_t highVals[PIN_COUNT][CALIBRATION_BLINKS];
  for (int i = 0; i < CALIBRATION_BLINKS; i++) {
    getLowValue(lowVals, i);
    getHighValue(highVals, i);
  }

  calcAvgDiffArray(lowVals, highVals);
  return CALIBRATED;
}

void PianoSteps::getLowValue(uint16_t lows[PIN_COUNT][CALIBRATION_BLINKS], uint8_t blink) {
  digitalWrite(MOFSET_PIN, LOW);
  delay(CALIBRATION_DELAY);  
  for (int i = 0; i < PIN_COUNT; i++) {
    lows[i][blink] = analogRead(i);
  }
}

void PianoSteps::getHighValue(uint16_t highs[PIN_COUNT][CALIBRATION_BLINKS],  uint8_t blink) {
  digitalWrite(MOFSET_PIN, HIGH);
  delay(CALIBRATION_DELAY);
  for (int i = 0; i < PIN_COUNT; i++) {
    highs[i][blink] = analogRead(i);
  }
}

void PianoSteps::calcAvgDiffArray(uint16_t lows[PIN_COUNT][CALIBRATION_BLINKS], uint16_t highs[PIN_COUNT][CALIBRATION_BLINKS]) {
  for (int i = 0; i < PIN_COUNT; i++) {
    for(int j = 0; j < CALIBRATION_BLINKS; j++) {
      absoluteThresholds[i] += highs[i][j] - lows[i][j];
    }
    absoluteThresholds[i] /= CALIBRATION_BLINKS;
  }
}

void PianoSteps::calculateSensorThresholds(void)
{
  memset(thresholds, 0, PIN_COUNT * sizeof(int));

  for (int i = 0; i < RECAL_FREQ; i++)
  {
    for (int pin = 0; pin < PIN_COUNT; pin++)
    {
      sensorHistory[i][pin] = analogRead(pin);
    }
  }
  for (int pin = 0; pin < PIN_COUNT; pin++)
  {
    for (int i = 0; i < RECAL_FREQ; i++)
    {
      thresholds[pin] += sensorHistory[i][pin];
    }
    thresholds[pin] /= RECAL_FREQ;
  }
}