
/* Arduino Generic Pin Probe Class
   Author: John Buccieri
   Last Date Updated: 07/18/17
*/

#ifndef probe_h
#define probe_h

#include "Arduino.h"
#include "constants.h"

/* Max Pin Macros */

#define UNO_MAX_ANALOG_PINS   6
#define MEGA_MAX_ANALOG_PINS 16
#define NANO_MAX_ANALOG_PINS  0
#define MICRO_MAX_ANALOG_PINS 0
#define MINI_MAX_ANALOG_PINS  0

#define UNO_MAX_DIGITAL_PINS  14
#define MEGA_MAX_DIGITAL_PINS 54
#define NANO_MAX_DIGITAL_PINS  0
#define MICRO_MAX_DIGITAL_PINS 0
#define MINI_MAX_DIGITAL_PINS  0



/* Supported Boards */
#define UNO             0
#define MEGA            1 
#define NANO            2
#define MICRO           3
#define MINI            4
#define INVALID_ID      5 /* Keep this last */

class Probe {

  private:
    /* Board Information */

    int boardId; /*Board ID */
    int maxAnalogPins; /* Max Number of onboard Analog Pins */
    int maxDigitalPins; /* Max Number of on board Digital Pins */
    int *activeAnalogPins; /* Active Analog Pin Reference */
    int *activeDigitalPins; /* Active Digital Pins Reference */
    int *analogPinVals;
    int *digitalPinVals;
    
  public:
    /* Constructor and Destructor*/
    Probe(int id);
    ~Probe(void);
    
    /* Probe Methods */
    int analogProbe(int pin_number);
    int digitalProbe(int pin_number);
    int analogDump(int values[], bool seriaPrint);
    int digitalDump(int values[], bool serialPrint);

    /* Get Methods */

    int getActiveAnalogPins(void);
    int getMaxAnalogPins(void);
    int getActiveDigitalPins(void);
    int getMaxDigitalPins(void);

};
#endif


