/*=====================================
 *         Piano Steps Program
 *       Written by: John Buccieri
 *     Property of: Drexel Theta Tau
 *=====================================*/

#include "assert.h"
#include "PianoSteps.h"

PianoSteps ps;

void setup()
{
    assert(ps.init() == READY) ;
}

void loop()
{
    exit(ps.exec());
}
