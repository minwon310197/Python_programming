import speech_recognition

robot_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
# /* same as_but line5 will let mic_off when done // mic = speech_recognition.Microphone */
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

print("You: " + you)