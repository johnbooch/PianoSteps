import PianoStepsRunner

try:
	pianoStepsRunner = PianoStepsRunner()
	pianoStepsRunner.run()

except PianoStepsErrorHandler as e:
	pass
