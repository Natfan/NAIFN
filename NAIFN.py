#NAIFN
#Personal assistant/pseudo AI
#Takes a text input, outputs text & speech
#uses regex for language parsing
import os

#function that cocatonates text output with say command
def speak(answer):
	spokenAnswer = ("say " + answer)
	os.system(spokenAnswer)
	print(answer)

#Input parser. Figures out appropiate response to input using regex
def parse():
	if any(command in userInput for command in commandList):
    	answer = "Command Found."
    else:
    	answer = "No command Found."

#Takes input from user, tidies it up for parsing (fixing typos, etc)
def input():
	userInput = input("> ")
	#compare each word of input to a dictionary
	#auto-correct typos (need auto-correct module)
	#If question includes 'does/why/where/when/what/how/who' append a question mark

#I think you can guess what this one does
def main():
	while quit = False:
		speak(parse(input(userInput)))

main()
