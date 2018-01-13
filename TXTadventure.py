import random
import os


# variables for menu
statsroll = True
one = False
two = False
menu_on = False
exit = False
mode = "2p"
incorrect = "Please enter a proper option."
swb = False
pldn = False
kgt = False
bbn = False
drd = False
ncm = False
thrt = False
x_i = False
mt_rcr = False
rgr = False
trpr = False
shdw = False
asasn = False
alkmst = False
njnr = False
blasa = False

def menu(one,two):
	menu_on = True
	while menu_on == True:
		exit = False
		print("{INSERT NAME OF GAME}!")
		print("START\nCAMPAIGN\nMISSIONS\nMODES\nCREDITS\nEXIT")
		m_select = input("Please enter one of the above: ")
		if m_select.lower() == "start":
			menu_on = False
			create()
		elif m_select.lower() == "campaign":
			menu_on = False
			create()
		elif m_select.lower() == "missions":
			while exit == False:
				print("Year 1 - Active")
				print("Year 2 - Locked\nBACK")
				tab = input("")
				if tab.lower() == "back":
					exit = True
				else:
					print(incorrect)
		elif m_select.lower() == "modes":
			print("MULTIPLAYER\nLAN MULTIPLAYER")
			mode_select = input("Please enter the mode you wish to play in: ")
			if mode_select.lower() == "multiplayer" or mode_select.lower() == "lan multiplayer":
				mode = mode_select.lower()
			else:
				print("Please enter a proper option.")

		elif m_select.lower() == "credits":
			while exit == False:
				print("--------------------------------------------------------------------------------\nCreator = Griffin Dugan\n--------------------------------------------------------------------------------\nBACK")
				credit_tab = input("")
				if credit_tab.lower() == "back":
					exit = True
				else:
					print(incorrect)


		elif m_select.lower() == "exit":
			menu_on = False
			exit()
		else:
			print("Please enter a proper option.")

def create():
	swb = False
	pldn = False
	kgt = False
	bbn = False
	drd = False
	ncm = False
	thrt = False
	x_i = False
	mt_rcr = False
	rgr = False
	trpr = False
	shdw = False
	asasn = False
	alkmst = False
	njnr = False
	blasa = False
	statsroll = True
	classchoosing = True
	while classchoosing == True:
		print("\n\n\n\n\n\n\n\n\n\nPlease choose a class.")
		print("Swashbuckler\nPaladin\nKnight\nBarbarian\nDruid\nNecromancer\nTheurgist\nCross-eye\nMounted Archer\nRanger\nTrapper\nShadow\nAssassin\nEngineer\nAlchemist\nBellasucia")
		uclass = input("")
		luclass = uclass.lower()
		if luclass == "swashbuckler":
			print("A fighter who tends toward light or no armor and prefers agility, cunning, daring, and technical skill to sheer force.")
			swb = True
		elif luclass == "paladin":
			print("The Paladin is a Fighter with the power of Light and healing magic as well as defensive buffs for their allies. Their devotion to their god or deity gives them various prayers, healing abilities, and light-based spells to protect themselves and others. Naturally, they are a type of Magic Knight.")
			pldn = True
		elif luclass == "knight":
			kgt = True
			print("They typically wear bigger, heavier armor and weaponry, sacrificing speed for defense and power. They gain support abilities to aid their allies in battle (such as the ability to shield the group from enemy attacks and/or the ability to make powerful Counter Attacks against enemies who ignore them).")
		elif luclass == "barbarian":
			bbn = True
			print("The Barbarian is a breed of Fighter focused more on damage than defense. Barbarians are damaged strongly by magic. They wear less armor, and are less civilized. They have an ability to be able to fly into a berserker rage that increases damage output and if they are below ¼ hp, they do double the damage.")
		elif luclass == "druid":
			drd = True
			print("A jack of all trades nature magician. They often have a mix of elemental offense, healing, and the ability to morph into animals or elemental spirits to become melee fighters.")
		elif luclass == "necromancer":
			ncm = True
			print("A magic-user who wields power over the dead, blood, and 'death energy'. Often they employ a Undead Rush - creating hordes of weak undead and sending them after a problem till it dies. Any other abilities are curses that weaken or sap away strength.")
		elif luclass == "theurgist":
			thrt = True
			print("The character makes a pact with a higher spirit, who supplies the him/her with magical powers. The entity normally gives them the power to harm or destroy. The pact may turn out to be with demons. Thus, this type of magic is usually heavily offensive and nasty.")
		elif luclass == "cross-eye":
			x_i = True
			print("A cross-eye is totally reliant on archery, but usually does higher damage because of it. If the character hits the enemy’s head, it does extra damage. Keeps to the back of a battle.")
		elif luclass == "mounted rcher":
			mt_rcr = True
			print("The Mounted Archers act as skirmishers and rely on agility and speed. They often specialize in Hit-and-Run Tactics, especially with archers who can spur their horse, turn around and shoot backwards as their enemies pursue.")
		elif luclass == "ranger":
			rgr = True
			print("A version of the archer that can handle bladed weapons as well, allowing them to defend themselves against approaching enemies or close in for the kill.")
		elif luclass == "trapper":
			trpr = True
			print("The Trapper is a character who can lay down various traps in an area that the enemy can walk into, making them vulnerable to ambushes or follow-up attacks.")
		elif luclass == "shadow":
			shdw = True
			print("The Shadows specialize in magic or powers that augment their stealth, and when they do, those powers generally feature darkness, shadows or the occult as themes.")
		elif luclass == "assassin":
			asasn = True
			print("A more offensive rogue, who sacrifices technical expertise for better stealth and killing abilities. Often have a variety of weakening and poisoning abilities and are able to cripple a foe to leave him open for allies or to let him die from damage over time.")
		elif luclass == "alchemist":
			alkmst = True
			print("An Alchemist combines items, magic or otherwise, to create potions or bombs to use in battle, often mixing them together during battle.")
		elif luclass == "engineer":
			njnr = True
			print("This is a character class that relies on technology to achieve ranged controlling effects similar to a wizard. They most likely have guns and bombs as primary weapons, and employ stationary and/or mobile machines on the battlefield. They can also build blockades.")
		elif luclass == "bellasucia":
			blasa = True
			voice = None
			print("Can deafen enemies with singing, usually sits at the back of a battle field or in high ground.")
		else:
			print(incorrect)

		fclass = input("Do you wish to choose this class?(y/n)")
		if fclass == "y":
			print("Okay. You chose the " + uclass + " class.")
			classchoosing = False
		elif fclass == "n":
			pass
		else:
			print(incorrect)

	print("Now, your stats will be randomly generated.")
	while statsroll == True:
		attack = random.choice([1, 2, 3, 4, 5, 6])
		defence = random.choice([1, 2, 3, 4, 5, 6])
		agility = random.choice([1, 2, 3, 4, 5, 6])
		intelligence = random.choice([1, 2, 3])
		perception = random.choice([1, 2, 3])
		hp = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) * 50
		strength = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) * 5
		print("Your stats have been generated. Now the perks of your class will be added to the stats.")
		if swb == True:
			agility = agility + 2
			attack = attack + 1
			strength = strength + 1
		elif pldn == True:
			defence = defence + 1
			attack = attack + 1
			hp = hp + 30
		elif kgt == True:
			defence = defence + 3
			hp = hp + 15
		elif bbn == True:
			attack = attack + 2
			agility = agility + 1
			strength = strength + 2
		elif drd == True:
			agility = agility + 1
		elif thrt == True:
			attack = attack + 2
			strength = strength + 1
		elif x_i == True:
			attack = attack + 2
			perception = perception + 1
			strength = strength + 5
		elif mt_rcr == True:
			agility = agility + 1
		elif rgr == True:
			agility = agility + 2
		elif trpr == True:
			intelligence = intelligence + 1
		elif shdw == True:
			agility = agility + 3
		elif asasn == True:
			attack = attack + 3
			strength = strength + 4
		elif alkmst == True:
			intelligence = intelligence + 3
		elif njnr == True:
			intelligence = intelligence + 4
		elif blasa == True:
			voice = 5000000

		if blasa == True:
			print("Voice: " + str(voice))

		print("Attack: " + str(attack))
		print("Defence: " + str(defence))
		print("Agility: " + str(agility))
		print("Intelligence: " + str(intelligence))
		print("Perception: " + str(perception))
		print("HP: " + str(hp))
		print("Strength" + str(strength))

		reroll = input("Do you wish to reroll your stats? (y/n): ")
		if reroll == "y":
			pass
		elif reroll == "n":
			statsroll = False
			tutorial()
			
			
		else:
			print(incorrect)




def tutorial():
	print("Entering the tutorial...")
	time.sleep(6)
	print("Welcome to the tutorial! My name is Minerva and I will be your guide throughout this tutorial.\nLet's start with the basic movement. ")


























menu(one,two)