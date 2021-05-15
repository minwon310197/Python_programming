import speech_recognition
import pyttsx3
from datetime import date

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
today = date.today()


with speech_recognition.Microphone() as mic:
# /* same as_but line5 will let mic_off when done // mic = speech_recognition.Microphone */
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

print("You: " + you)



if you == "":
	robot_brain = "i can't hear you, please try again."
elif you == "hello":
	robot_brain = "Hello MinWon."
elif you == "today":
	robot_brain = "Today is: " + today.strftime("%B %d, %Y")
else:
	robot_brain = "Sorry i don't know how to answer this question."

print(robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()