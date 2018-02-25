/*=====================================
 *         Piano Steps Program
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "PianoSteps.h"


 ps = PianoSteps();

void setup()
{
    ps.init();
}

void loop()
{
    exit(ps.run());
}