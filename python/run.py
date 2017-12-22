import PianoStepsRunner
import PianoStepsErrorHandler

try:
	pianoStepsRunner = PianoStepsRunner()
	pianoStepsRunner.run()

except PianoStepsError as PSE:
	