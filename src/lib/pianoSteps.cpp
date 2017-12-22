/*=====================================
 *         Piano Steps CPP
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "Arduino.h"
#include "pianoSteps.h"

PianoSteps::PianoSteps(int steps, int boardId) {

  stepCount = steps;

  /* Dynamic Memory Allocation for a 2D array */
  sensorHistory = (int **) malloc(HISTORY_LENGTH * sizeof(int *));
  for (int i = 0; i < HISTORY_LENGTH; i++) {
    sensorHistory[i] = (int *) malloc(stepCount * sizeof(int));
    if (sensorHistory[i] == NULL) // Check for memory overflow
      abort();
  }

  thresholds = (int *) malloc(stepCount * sizeof(int));
  memset(thresholds, 0, stepCount * sizeof(int));
}

PianoSteps::~PianoSteps(void){
  free(sensorHistory);
  free(thresholds);  
}

int PianoSteps::lightSensorCalibration(void) {

}

int PianoSteps::lightSensorRecalibration(void) {
  memset(thresholds, 0, stepCount * sizeof(int));
  
  for (int i = 0; i < HISTORY_LENGTH; i++) {
    for (int pin = 0; pin < stepCount; pin++) {
      sensorHistory[i][pin] = analogRead(pin);
    }
  }
  for (int pin = 0; pin < stepCount; pin++) {
    for (int i = 0; i < HISTORY_LENGTH; i++) {
       thresholds[pin] += sensorHistory[i][pin];
    }
    thresholds[pin] /= HISTORY_LENGTH;
  }
  return SUCCESS;
}

/* Gets and Dump Methods */
int PianoSteps::getStepCount(void) {
  return stepCount;
}

int PianoSteps::thresholdDump(void) {
  for (int pin = 0; pin < stepCount; pin++) {
    Serial.print(thresholds[pin]);
    Serial.print("\t");
  }
  Serial.println();
  return SUCCESS;
}

int PianoSteps::sensorHistoryDump(void) {
  for (int i = 0; i < HISTORY_LENGTH; i++) {
      for (int pin = 0; pin < stepCount; pin++) {
        Serial.print(sensorHistory[i][pin]);
        Serial.print("\t");
      }
      Serial.println();
    }
}

