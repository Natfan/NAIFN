#NAIFN
#Personal assistant/pseudo AI
#Takes a text input, outputs text & speech
#uses regex for language parsing??
import os
quit = False
#ALL CODE TEMPORARILY COMMENTED OUT TO AVOID THE HEADACHE THAT IS FUNCTIONS.
#THANK YOU, AND APOLOGIES FOR THE INCONVENINCE
#function that cocatonates text output with say command
#def speak(answer):
	#spokenAnswer = ("say " + answer)
	#os.system(spokenAnswer)
	#print(answer)

#Input parser. Figures out appropiate response to input using regex
#def parse():
	#commandList = ["test1", "test2", "testCommand"]
	#if any(command in userInput for command in commandList):
    	#answer = "Command Found."
    #else
    	#answer = "Command Not Found."

#Takes input from user, tidies it up for parsing (fixing typos, etc)
#def input():
	#userInput = input("> ")
	#compare each word of input to a dictionary
	#auto-correct typos (need auto-correct module)
	#If question includes 'does/why/where/when/what/how/who' append a question mark

#I think you can guess what this one does
#def main():
	#while quit = False:
		#speak(parse(input(userInput)))

#Setup
commandList = ["test1", "test2", "testCommand"]
print("Hello! I am NAIFN, or Natural Artificial Intelligence For Netizens.")
os.system("say Hello! I am NAIFN, or Natural Artificial Intelligence For Netizens.")
os.system("say What is your name?")
name = raw_input("What is your name? ")
print("Alright " + name + ", lets get started! Ask me anything.")
os.system("say Alright " + name + ", lets get started! Ask me anything.")
#Runtime! Command parsing is not working yet, dunno why.
while quit == False:
	userInput = raw_input(">")
	for word in userInput:
		if word in commandList:
			answer = "Command Found."
		else:
			answer = "Command Not Found."
	print(answer)
	os.system("say " + answer)