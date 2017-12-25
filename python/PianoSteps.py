import os

from lib.PianoStepsRunner import PianoStepsRunner

PianoStepsConfPath = os.path.dirname(os.path.abspath(__file__))
PianoSteps = PianoStepsRunner('${PianoSteps_Path}/META-INF/PianoSteps.xml')
PianoSteps.run()