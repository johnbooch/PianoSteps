/*=====================================
 *         Piano Steps Header
 *       Written by: John Buccieri
 *=====================================*/

#ifndef piano_h
#define piano_h

#include "ArduinoConstants.h"

/* Board Operation Encodings */
#define INIT 0x03
#define CALIBRATED 0x04
#define READY 0x05
#define EXEC 0x06
#define HALT 0x07

/* Signal Values */
#define SIGNAL 0x01
#define NO_SIGNAL 0x00

#define EXPAND_INFO_STR(INFO) INFO
#define EXPAND_WARN_STR(WARN) WARN
#define EXPAND_FATAL_STRING(FATAL) FATAL

/* Hardware values */
#define PIN_COUNT 0x08 // This value can be changed before compile time (See deploy script)
#define RECAL_FREQ 0x64
#define CALIBRATION_DELAY 0x100
#define CALIBRATION_BLINKS 0xA
#define MOFSET_PIN 0x1

class PianoSteps
{

private:

  int recalCount = 0;
  int recalLimit = RECAL_FREQ;

  uint8_t sensorCalibration(void);
  uint8_t calculateAbsoluteThreshold(void);
  void calculateSensorThresholds(void);
  void getLowValue(uint16_t lows[PIN_COUNT][CALIBRATION_BLINKS], uint8_t pos);
  void getHighValue(uint16_t lows[PIN_COUNT][CALIBRATION_BLINKS], uint8_t pos);
  void calcAvgDiffArray(uint16_t lows[PIN_COUNT][CALIBRATION_BLINKS], uint16_t highs[PIN_COUNT][CALIBRATION_BLINKS]);
  uint8_t detectHardwareErrors(void);
  void sensorEvaluation(void);
  void sendErrorCode(uint8_t error);

public:
  /* Constructor*/
  PianoSteps(void);

  /* Destructor */
  ~PianoSteps(void);

  /*
   * Current Process
   */
  uint8_t process;

  /*
   *  Dynamic Threshold Array for real time sensor calibration 
   *  Pin 0 | Pin 1 | Pin 2 | Pin 3 | ... Pin N |
   * Thresh1|Thresh2|Thresh3|Thresh4|    Thresh N |
   */
  uint16_t thresholds[PIN_COUNT];

  /*
   * Dynamic Sensor History for real time calculation of sensor thresholds
   *         Pin 0 | Pin 1 | Pin 2 |... Pin N |
   * Hist 0  Val00 | Val10 | Val20
   * Hist 1  Val01 | Val11 | Val21
   * Hist 2  Val02 | Val12 | Val22
   *  ...
   * Hist M
   */
  uint16_t sensorHistory[PIN_COUNT][RECAL_FREQ];

  /*
	 * Measurement of minimum voltage drop to be considered a signal
	 * Calculated during initial calibration of Piano Steps Environment
	 */
  uint8_t absoluteThresholds[PIN_COUNT];

  /* 
   * Initialization process
   */
  uint8_t init(void);

  /* 
   * Execution process
   */
  uint8_t exec(void);
};
#endif
