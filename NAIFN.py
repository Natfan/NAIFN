#NAIFN
#Personal assistant/pseudo AI
#Takes a text input, outputs text & speech
#uses regex for language parsing??
import os
quit = False
commandList = {"help":"Here's what you can say to me: Hello, Goodbye, What's up? That's it for now.", "Hello":"Hi!", "Goodbye":"Goodbye!", "What's up?":"The sky, a few clouds. The usual."}
def setup():
	print("Hello! I am NAIFN, or Natural Artificial Intelligence For Netizens.")
	print("What is your name?")
	name = raw_input(">")
	print("Alright " + name + ", what OS do you use, OS X or Linux?")
	os.system("say Alright " + name + ", what operating system do you use? O S ten or linux?")
	OS = raw_input(">")
	if OS == "Linux":
		talk = "espeak "
	elif OS == "OS X":
		talk = "say "
	print("Awesome! Now I can talk to you!")
	os.system(talk + "Awesome! Now I can talk to you.")

#if firstTime == true:
#	setup()
#else:
#	continue

setup()
#Runtime!
while quit == False:
	userInput = raw_input(">")
	if userInput in commandList:
		answer = commandList[userInput]
	else:
		for word in userInput.split():
			if word in commandList:
				answer = commandList[word]
			else:
				answer = "Sorry! I dont understand that yet."
	print(answer)
	speech = talk + answer
	os.system(speech)