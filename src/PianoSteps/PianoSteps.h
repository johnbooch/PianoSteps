/*=====================================
 *         Piano Steps Header
 *       Written by: John Buccieri
 *=====================================*/

#ifndef piano_h
#define piano_h

#include "ArduinoConstants.h"

/* Data Transfer Encodings */
#define START 0x00
#define ACK 0x01
#define STOP 0x02

/* Board Operation Encodings */
#define READY 0x03
#define INIT 0x04
#define EXEC 0x05
#define HALT 0x06

/* Signal Values */
#define SIGNAL 0x01
#define NO_SIGNAL 0x00

#define EXPAND_INFO_STR(INFO) INFO
#define EXPAND_WARN_STR(WARN) WARN
#define EXPAND_FATAL_STRING(FATAL) FATAL

/* Hardware values */
#define PIN_COUNT 0x08 // This value can be changed before compile time (See deploy script)
#define RECAL_FREQ 0x64

class PianoSteps
{

private:

  int recalCount = 0;
  int recalLimit = RECAL_FREQ;

  void sensorCalibration(void);
  void calculateAbsoluteThreshold(void);
  void calculateRecalLimit(void);
  void detectHardwareErrors(void);
  void sendErrorCode(uint8_t error);

public:
  /* Constructor*/
  PianoSteps(void);

  /* Destructor */
  ~PianoSteps(void);

  /*
   * Number of sensors connected to analog ports 
   */
  uint8_t pinCount;

  /*
   * Arduino Board ID
   */
  uint8_t boardId;

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
  uint8_t absoluteThreshold;

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
