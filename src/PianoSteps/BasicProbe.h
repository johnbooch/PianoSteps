/* Arduino Generic Pin Probe Class
   Author: John Buccieri
   Last Date Updated: 07/18/17
*/

#ifndef basic_probe_h
#define basic_probe_h

#include "Arduino.h"
#include "ArduinoConstants.h"

/* Error Types */
#define SUCCESS (0)
#define ANALOG_READ_FAILURE (-1)
#define DIGITAL_READ_FAILURE (-2)
#define DIGITAL_PWM_WRITE_FAILURE (-3)
#define DIGITAL_WRITE_FAILURE (-4)

class Probe
{

private:
  /*
     * Private Members
     */

  /* Board Information */
  int boardId;        /* Board ID */
  int numAnalogPins;  /* Max Number of on board Analog Pins */
  int numDigitalPins; /* Max Number of on board Digital Pins */

  /* Pin value arrays */
  int *analogPinVals;    /* Analog Pin Values */
  int *digitalPinVals;   /* Digital Pin Values */
  int *analogPinModes;   /* Analog Pin Modes */
  int *digitalPinModes;  /* Digital Pin Modes */
  bool *highAnalogPins;  /* Active Analog Pin Reference */
  bool *highDigitalPins; /* Active Digital Pins Reference. 1st row is pin number */

public:
  /* Constructor and Destructor*/
  Probe(int boardId);
  ~Probe(void);

  /* Probe Methods */
  int readAnalogPin(int pin);
  int readDigitalPin(int pin);

  /* Utility Methods */
  bool isHighAnalogPin(int pin);
  bool isHighDigitalPin(int pin);

  /* Get Methods */
  int *getAnalogPinVals(bool seriaPrint);
  int *getDigitalPinVals(bool serialPrint);
  int *getNumAnalogPins();
  int *getNumDigitalPins();
  bool *getHighAnalogPins(bool serialPrint);
  bool *getHighDigitalPins(bool serialPrint);
};
#endif
