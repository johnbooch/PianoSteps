
/* Arduino Generic Pin Probe Class
   Author: John Buccieri
   Last Date Updated: 07/18/17
*/

#ifndef probe_h
#define probe_h

#include "Arduino.h"
#include "constants.h"

class BasicProbe {

  private:
    /* Board Information */

    int boardId; /*Board ID */
    int maxAnalogPins; /* Max Number of onboard Analog Pins */
    int maxDigitalPins; /* Max Number of on board Digital Pins */
    
  public:
    /* Constructor and Destructor*/
    Probe(int id);
    ~Probe(void);

	/* Pin value arrays */	
	int **highAnalogPins; /* Active Analog Pin Reference. 1st row is pin number, 2nd row is value */
    int *highDigitalPins; /* Active Digital Pins Reference. 1st row is pin number */
    int *analogPinVals; /* Analog Pin Values */
    int *digitalPinVals; /* Digital Pin Values */
    
    /* Probe Methods */
    int analogProbe(int pin_number);
    int digitalProbe(int pin_number);   
	
	/* Utility Methods */	
    int analogDump(int values[], bool seriaPrint);
    int digitalDump(int values[], bool serialPrint);

    /* Get Methods */
    int getMaxAnalogPins(void);
    int getMaxDigitalPins(void);
	
  private:
	bool isActiveAnalogPin(int pin);
	bool isActiveDigitalPin(int pin);
};
#endif