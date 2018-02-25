/*=====================================
 *         Piano Steps Header
 *       Written by: John Buccieri
 *=====================================*/

#ifndef piano_h
#define piano_h

#include "Arduino.h"
#include "SoftwareSerial.h"
#include "BasicProbe.h"

/* Data Transfer Encodings */
#define START 0x00
#define ACK 0x01
#define STOP 0x02

/* Board Operation Encodings */
#define READY 0x03
#define INIT 0x04
#define RUN 0x05
#define HALT 0x06

/* Signal Values */
#define SIGNAL 0x01
#define NO_SIGNAL 0x00

#define EXPAND_INFO_STR(INFO) INFO
#define EXPAND_WARN_STR(WARN) WARN
#define EXPAND_FATAL_STRING(FATAL) FATAL

#define HISTORY_SIZE 0x0A

class PianoSteps
{

private:
  int recalCount = 0;
  int recalLimit;
  int allocateThresholdMemory(void);
  int lightSensorCalibration(void);
  int lightSensorRecalibration(void);
  int calculateAbsoluteThreshold(void);
  int calculateRecalLimit(void);
  int detectHardwareErrors(void);

public:
  /* Constructor*/
  PianoSteps(void);

  /* Destructor */
  ~PianoSteps(void);

  /*
   * Serial Monitor refernence to the built in Arduino Serial Monitor
   */
  HardwareSerial SerialRef = Serial;

  /*
   * Basic Probe reference for use in reading pin values
   */
  Probe *ProbeRef;

  /*
   * Number of sensors connected to analog ports 
   */
  uint8_t pinCount;

  /*
   * Arduino Board ID
   */
  uint8_t boardId;

  /*
   *  Dynamic Threshold Array for real time sensor calibration 
   *  Pin 0 | Pin 1 | Pin 2 | Pin 3 | ... Pin N |
   * Thresh1|Thresh2|Thresh3|Thresh4|    Thresh N |
   */
  uint16_t *thresholds;

  /*
   * Dynamic Sensor History for real time calculation of sensor thresholds
   *         Pin 0 | Pin 1 | Pin 2 |... Pin N |
   * Hist 0  Val00 | Val10 | Val20
   * Hist 1  Val01 | Val11 | Val21
   * Hist 2  Val02 | Val12 | Val22
   *  ...
   * Hist M
   */
  uint16_t *sensorHistory[HISTORY_SIZE];

  /*
	 * Measurement of minimum voltage drop to be considered a signal
	 * Calculated during initial calibration of Piano Steps Environment
	 */
  uint8_t absoluteThreshold;

  /* 
   *
   * 
   */
  uint8_t init(void);

  /* 
   *
   * 
   */
  uint8_t run(void);
};
#endif
