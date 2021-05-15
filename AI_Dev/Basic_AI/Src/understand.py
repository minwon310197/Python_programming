you = "hello"

if you == ""
	robot_brain = "i can't hear you, please try again."
elif you == "hello":
	robot_brain = "Hell MinWon."
elif you == "today":
	robot_brain = "today is Sunday."
else:
	robot_brain = "Sorry i don't know how to answer this question."
print(robot_brain)