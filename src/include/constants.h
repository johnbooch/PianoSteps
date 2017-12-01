/*=====================================
 *          Constants Header File
 *       Written by: John Buccieri
 *=====================================*/


#ifndef constants_h
#define constants_h

#include <Arduino.h>

/* Generic Constants */
#define FALSE 0
#define TRUE !FALSE
#define SUCCESS 1
#define FAILURE 0

/* Arduino Hardware Constants*/

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
 
/* Piano Step Hardware Setup Constants */
#define NUMPINS 8 
#define INSTALLED_BOARD MEGA
#define MAX_STEPS 13 
#define HISTORY_LENGTH 13

#endif 
