import random
from string import punctuation

global begin_db
global responce_db

begin_db = ["hi", "hey"]
responce_db = {
				"hi": ["how are you", "hi"],
				"hey": ["how are you", "hey"],
			 	"how are you": ["good", "okay", "great",],
			 	"khjhaskjdhjkhenkajjhuy3jh42bjknuc": ["Sorry, i didnt catch that, could you say it again?"]
			 	}

DEBUGGING = False
VOICEINPUT = False
VOICEOUTPUT = False

BOTNAME = "Bot"

def rempunc(s):

	return ''.join(c for c in s if c not in punctuation).lower()

def SpeachRec():
	while 1:
		print("...") # This is the prompt. I probably should make this tts... (CAN BE CHANGED)
		uinput = input("")
		print("User: " + uinput)
		return uinput # This is just there so you can check to make sure that your speech was caught correctly.

def sinput():
	if VOICEINPUT:
		return SpeachRec()
	else:
		return rempunc(input("User: "))

def TextToSpeach(output):
	print(output)

def sout(reply):
	if VOICEOUTPUT:
		TextToSpeach(reply)
	print(BOTNAME + ": " + reply)

def debugging(dbstr):
	if DEBUGGING:
		print("DEBUGGING:")
		print(dbstr)

def main():

	# Variable used to exit the loop
	exitloop = False

	while exitloop != True:

		if random.choice([True, False]):
	
			res = random.choice(begin_db)
			wm = True
	
		else: 
	
			inp = sinput()
	
			if inp == 'exit':

				debugging("exit message seen")
				wm = False
				exitloop = True
	
			else:
	
				try:
					res = random.choice(responce_db[inp])
					debugging("Found responce")
					wm = True
	
				except:
					print("No responce data found, a new session will begin to gather more data...")
					debugging("No responce found")
					print("")
					begin_db.append(inp)
					wm = False
	
		while wm:
	
			sout(res)
	
			inp = sinput()
			if inp == 'exit':
				wm = False
				exitloop = True
	
			if wm:
	
				try:
					responce_db[res].append(inp)
					debugging("Added new responce '" + inp + "'' under old key '" + res + "'")
		
				except:
					responce_db[res] = [inp]
					debugging("Added new responce '" + inp + "'' under new key '" + res + "'")
		
				try:
					res = random.choice(responce_db[inp])
					debugging("Found responce")
		
				except:
					print("No responce data found, a new session will begin to gather more data...")
					debugging("No responce found")
					print("")
	
					wm = False


while 1:
	
	inp = input(">>> ")
	
	if inp == "save":
		vname = input("Name of file: ")
		file = open(vname + ".txt", "w")
		file.writelines(["begin_db = " + str(begin_db) + '\n', "responce_db = " + str(responce_db)])
		file.close()
		print("Save Complete")
	elif inp == "load":
		xname = input("Name of file: ")
		try:
			file = open(xname + ".txt", "r")
			for line in file.readlines():
				exec(line)
			file.close()
		except FileNotFoundError:
			print("Error, Load File Not Found")
		
		print("Load Comlpete")
	elif inp == "run":
		main()
	else:
		print("Error, Invalid Command")
		print("Avalible Commands are: 'save', 'load', 'run'")
