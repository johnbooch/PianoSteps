/*===========================================
 *          Arduino Constants Header File
 *            Written by: John Buccieri
 *===========================================*/


#ifndef arduino_constants_h
#define arduino_constants_h

#include <Arduino.h>

/* Global Constants */
#define FALSE 0
#define TRUE  !FALSE

/* Supported Boards IDs */
#define UNO             0
#define MEGA            1 
#define NANO            2
#define MICRO           3
#define MINI            4
#define INVALID_ID      5 /* Keep this last */

/* Supported Boards Strings */
#define UNO             "UNO"
#define MEGA            "MEGA"
#define NANO            "NANO"
#define MICRO           "MICRO"
#define MINI            "MINI"
#define INVALID_ID      "INVALID"/* Keep this last */

#endif 
