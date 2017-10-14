/*=====================================
 *         Piano Steps Program
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "probe.h"
#include "pianoSteps.h"

Probe PianoStepsProbe(MEGA);
PianoSteps PianoSteps(1);

int absoluteThreshold = 10;

void setup() {
  Serial.begin(9600);
  
  PianoSteps.lightSensorCalibration();
}

void loop() {
  static int recal = 0;
  
  for (int pin = 0; pin < PianoSteps.getStepCount(); pin++) {
   
    if(PianoStepsProbe.analogProbe(pin) > PianoSteps.thresholds[pin] + absoluteThreshold){
      Serial.print(1);
    }
    else {
      Serial.print(0);
    }    
    recal++;
    if (recal > 15) {
      PianoSteps.lightSensorCalibration(); 
      recal = 0;
    }
  }
  delay(100);
}
