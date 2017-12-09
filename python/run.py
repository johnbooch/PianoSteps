import PianoStepsRunner
import PianoStepsErrorHandler

try:
	pianoStepsRunner = PianoStepsRunner()
	pianoStepsRunner.run()

except PianoStepsErrorHandler as PSE:
	