/*=====================================
 *         Piano Steps Header
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#ifndef piano_h
#define piano_h

#include "Arduino.h"
#include "probe.h"

class PianoSteps: public BasicProbe {

    private:
      int stepCount;
      
    public:
      /* Constructor and Destructor */
      PianoSteps(int steps);
      ~PianoSteps(void);

      /*************************************************************
       *  Dynamic Threshold Array for real time sensor calibration 
       *  Pin 0 | Pin 1 | Pin 2 | Pin 3 | ... Pin N |
       * Thresh1|Thresh2|Thresh3|Thresh4|    Thresh N |
       *************************************************************/
      int *thresholds;
	  
      /************************************************************************ 
       * Dynamic Sensor History for real time calculation of sensor thresholds
       *         Pin 0 | Pin 1 | Pin 2 |... Pin N |
       * Hist 0  Val00 | Val10 | Val20
       * Hist 1  Val01 | Val11 | Val21
       * Hist 2  Val02 | Val12 | Val22
       *  ...
       * Hist M
       ************************************************************************/
      int **sensorHistory;
	  
	  /*********************************************************
	  * Measurement of minimum voltage drop to be considered a signal
	  * Calculated during initial calibration of Piano Steps Environment
	  ***********************************************************/
	  int absoluteThreshold;
     
      /* Calibration Methods */
      int lightSensorCalibration(void);
      int lightSensorRecalibration(void);

      /* Get Methods */
      int getStepCount(void);
      int thresholdDump(void);
      int sensorHistoryDump(void);
};
#endif 
