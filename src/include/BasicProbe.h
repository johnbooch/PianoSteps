/* Arduino Generic Pin Probe Class
   Author: John Buccieri
   Last Date Updated: 07/18/17
*/

#ifndef basic_probe_h
#define basic_probe_h

#include "Arduino.h"
#include "include/ArduinoConstants.h"

/* Error Types */
#define SUCCESS                    (0)
#define ANALOG_READ_FAILURE        (-1)
#define DIGITAL_READ_FAILURE       (-2)
#define DIGITAL_PWM_WRITE_FAILURE  (-3)
#define DIGITAL_WRITE_FAILURE      (-4)

/* Arduino Board Pin Constants*/
#define UNO_MAX_ANALOG_PINS    (6)
#define MEGA_MAX_ANALOG_PINS   (16)
#define NANO_MAX_ANALOG_PINS   (8)
#define MICRO_MAX_ANALOG_PINS  (12)
#define MINI_MAX_ANALOG_PINS   (8)

#define UNO_MAX_DIGITAL_PINS   (14)
#define MEGA_MAX_DIGITAL_PINS  (54)
#define NANO_MAX_DIGITAL_PINS  (14)
#define MICRO_MAX_DIGITAL_PINS (20)
#define MINI_MAX_DIGITAL_PINS  (14)

/* Arduino Macro Functions*/
#define EXPAND_MAX_ANALOG_PINS(BOARD)  (BOARD##MAX_ANALOG_PINS)
#define EXPAND_MAX_DIGITAL_PINS(BOARD) (BOARD##MAX_DIGITAL_PINS)

class BasicProbe {

  private:
    /*
     * Private Members
     */

    /* Board Information */
    int boardId; /* Board ID */
    int maxAnalogPins; /* Max Number of on board Analog Pins */
    int maxDigitalPins; /* Max Number of on board Digital Pins */

    /* Reference and Resolution Values */
    int analogReference; 

    /* Pin value arrays */
    int *analogPinVals; /* Analog Pin Values */
    int *digitalPinVals; /* Digital Pin Values */
    bool *highAnalogPins; /* Active Analog Pin Reference */
    bool *highDigitalPins; /* Active Digital Pins Reference. 1st row is pin number */

    /*
     * Private Methods
     */

    int validateAnalogPin(int pin)
    int validateDigitalPin(int pin);
    
  public:
    /* Constructor and Destructor*/
    Probe(int boardId, char[] boardIdString);
    ~Probe(void);

    /* Probe Methods */
    int readAnalogPin(int pin);
    int readDigitalPin(int pin);
    int writeDigitalPWMPin(int pin, int value);
    int writeDigitalPin(int pin, int value, bool isAnalogPin);

	  /* Dump Methods */
    int * analogDump(bool seriaPrint);
    int * digitalDump(bool serialPrint);
    int * highAnalogPinsDump(bool serialPrint);
    int * highDigitalPinsDump(bool serialPrint);

    /* Utility Methods */
    bool isPWMPin(int pin);
    bool isHighAnalogPin(int pin);
    bool isHighDigitalPin(int pin);

    /* Set Methods */
    int setAnalogReference(int ref);
    int setAnalogPinMode(int pin, bool isOuput);
    int setDigitalPinMode(int pin, bool isOuput);

    /* Get Methods */
    int getMaxAnalogPins(void);
    int getMaxDigitalPins(void);
    int getAnalogPinMode(int pin);
    int getDigitalPinMode(int pin);
};
#endif