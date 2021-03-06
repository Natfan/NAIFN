#NAIFN
#Personal assistant/pseudo AI
#Takes a text input, outputs text & speech
#uses regex for language parsing??
import os
import nltk
quit = False
ops = 'l'
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
def getWordTypes(text):
    if not text:
        print('ERROR, TEXT REQUIRED')
    text = nltk.word_tokenize(text)
    words = nltk.pos_tag(text)
    for item, index in words:
        if index == 'WRB' or index == '?':
            print(item, "is part of a word!")
            print(text);

#I think you can guess what this one does
#def main():
	#while quit = False:
		#speak(parse(input(userInput)))

#Setup
commandList = {"Hello":"Hi!", "Goodbye":"Goodbye!", "What's up?":"The sky, a few clouds. The usual."}
print("Hello! I am NAIFN, or Natural Artificial Intelligence For Netizens.")
if ops == 'm':
    os.system("say Hello! I am NAIFN, or Natural Artificial Intelligence For Netizens.")
print("What is your name?")
if ops == 'm':
    os.system("say What is your name?")
name = input(">")
print("Alright " + name + ", lets get started! Ask me anything.")
if ops == 'm':
    os.system("say Alright " + name + ", lets get started! Ask me anything.")
#Runtime!
while quit == False:
    userInput = input(">")
    if userInput in commandList:
        answer = commandList[userInput]
    else:
        for word in userInput.split():
            if word in commandList:
                answer = commandList[word]
            else:
                answer = "Sorry! I don't understand that yet."
        getWordTypes(userInput)
        print(answer)
        if ops == 'm':
            os.system("say " + answer)
