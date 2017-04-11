#NAIFN
#Personal assistant/pseudo AI
#Takes a text input, outputs text & speech
#uses regex for language parsing
import os

#function that cocatonates text output with say command
def speak(answer):
	print(answer)
	spokenAnswer = ("say " + answer)
	os.system(spokenAnswer)

#Input parser. Figures out appropiate response to input using regex
def parse():
	#compare each word to a list of known words
	#Choose the output that best corresponds
	#For example, if input includes 'say' && 'funny':
	#	output = [say something funny command]
	#if input includes 'tell' && 'joke':
	#	output = [tell joke command]
	#if input includes 'weather':
	#	output = [weather command]
	#and so on and so forth.

#Takes input from user, tidies it up for parsing (fixing typos, etc)
def input():
	#compare each word of input to a dictionary
	#auto-correct typos (need auto-correct module)
	#If question inludes 'does/why/where/when/how/who' append a question mark

#I think you can guess what this one does
def main():
	#In progress
