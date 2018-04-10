import random

#
#
# Bah bah black sheep
# have you any wool
# yessir yessir tree bags full
#
#

code = {
	"a" : "•",
	"b" : "¢",
	"c" : "¡",
	"d" : "¬",
	"e" : "√",
	"f" : "˚",
	"q" : "º",
	"w" : "ﬂ",
	"r" : "›",
	"t" : "°",
	"y" : "ª",
	"u" : "Ô",
	"i" : "Í",
	"o" : "ı",
	"p" : "Ÿ",
	"s" : "∫",
	"g" : "∑",
	"h" : "„",
	"j" : "Œ",
	"k" : "Æ",
	"l" : "¿",
	"z" : "˘",
	"x" : "¯",
	"v" : "»",
	"n" : "’",
	"m" : "±",
	" " : "‡",
	"Q" : "‹",
	"W" : "«",
	"E" : "…",
	"R" : "≥",
	"T" : "≤",
	"Y" : "˜",
	"U" : "⁄",
	"I" : "◊",
	"O" : "—",
	"P" : "”",
	"A" : "⨚",
	"S" : "∴",
	"D" : "∷",
	"F" : "≐",
	"G" : "≕",
	"H" : "⊜",
	"J" : "⊠",
	"K" : "⊪",
	"L" : "⊤",
	"Z" : "⋣",
	"X" : "⋮",
	"C" : "⋲",
	"V" : "⨀",
	"B" : "⨡",
	"N" : "⟓",
	"M" : "⧉",
	"." : "⦺",
	"," : "⧮",
	";" : "⟡",
	":" : "⫷",
	"?" : "⫡",
	"!" : "⫍",
	"&" : "⪤",
	"'" : "⨊"
}

codeREV = {
	"•" : "a",
	"¢" : "b",
	"¡" : "c",
	"¬" : "d",
	"√" : "e",
	"˚" : "f",
	"º" : "q",
	"ﬂ" : "w",
	"›" : "r",
	"°" : "t",
	"ª" : "y",
	"Ô" : "u",
	"Í" : "i",
	"ı" : "o",
	"Ÿ" : "p",
	"∫" : "s",
	"∑" : "g",
	"„" : "h",
	"Œ" : "j",
	"Æ" : "k",
	"¿" : "l",
	"˘" : "z",
	"¯" : "x",
	"»" : "v",
	"’" : "n",
	"±" : "m",
	"‡" : " ",
	"‹" : "Q",
	"«" : "W",
	"…" : "E",
	"≥" : "R",
	"≤" : "T",
	"˜" : "Y",
	"⁄" : "U",
	"◊" : "I",
	"—" : "O",
	"”" : "P",
	"⨚" : "A",
	"∴" : "S",
	"∷" : "D",
	"≐" : "F",
	"≕" : "G",
	"⊜" : "H",
	"⊠" : "J",
	"⊪" : "K",
	"⊤" : "L",
	"⋣" : "Z",
	"⋮" : "X",
	"⋲" : "C",
	"⨀" : "V",
	"⨡" : "B",
	"⟓" : "N",
	"⧉" : "M",
	"⦺" : ".",
	"⧮" : ",",
	"⟡" : ";",
	"⫷" : ":",
	"⫡" : "?",
	"⫍" : "!",
	"⪤" : "&",
	"⨊" : "'"
}

types = [
	"ZXCVBNM–7",
	"WXCVBN,–9",
	"'XGVWNI-2",
	"90X,INW-"
]



def translateTO():
	global translation
	global code
	global listy
	global translate
	global lstt
	global KEY
	KEY = False
	IN = input("What would you like to translate to this encryption?\n")
	if " (KEY)" in IN:
		KEY = True
		IN = IN.replace(" (KEY)","")
	translate = list(IN)
	listy = []
	translation = []

	ttype = random.choice(types)

	lstt = []

	for i in range(len(translate)):
		lstt.append(i)
	print(str(lstt))

	typespot = random.choice(lstt)
	if KEY == True:
		while len(listy) != len(translate):
			bob = translate[0]
			translate.remove(bob)
			test = code[bob]
			translation.append(test)

		lest = []

		UKey = input("What is your user key?\n")
		for i in range(len(translation)):
			lest.append(i)
		print(str(lest))

		keyspot = random.choice(lest)
		ttype = ""

		translation.insert(int(keyspot), UKey)
	elif ttype == "ZXCVBNM–7":
		while len(listy) != len(translate):
			
			bob = translate[0]
			translate.remove(bob)
			test = code[bob]
			translation.append(test)
	elif ttype == "WXCVBN,–9":
		while len(listy) != len(translate):
			
			bob = translate[0]
			translate.remove(bob)
			test = code[bob]
			translation.append(test)
			translation.append(" - ")
	


		

		

		

		#translation[bob] = code[translate[bob]]

	typespot = random.choice(lstt)

	if KEY != True:
		translation.insert(int(typespot), ttype)
	else:
		translation.insert(int(typespot), "++⊪…˜")

	ftranslation = str(translation)
	ftranslation = ftranslation.replace("['","")
	ftranslation = ftranslation.replace("', '","")
	ftranslation = ftranslation.replace("', ","")
	ftranslation = ftranslation.replace(", '","")
	ftranslation = ftranslation.replace('"',"")
	ftranslation = ftranslation.replace("']","")

	print(ftranslation)


def translateFROM():
	global translation
	global code
	global listy
	global translate
	KEY = False
	IN = input("What would you like to translate from this encryption?\n")
	if "++⊪…˜" in IN:
		KEY = True
		IN = IN.replace("++⊪…˜","")
	translate = list(IN)
	listy = []
	translation = []
	if KEY == True:
		try:
			while len(listy) != len(translate):
				bob = translate[0]
				
				translate.remove(bob)
				
				test = codeREV[bob]
				
				translation.append(test)
				

				ftranslation = str(translation)
		except KeyError:

	else:
		while len(listy) != len(translate):
			bob = translate[0]
			
			translate.remove(bob)
			
			test = codeREV[bob]
			
			translation.append(test)
			

			ftranslation = str(translation)
			ftranslation = ftranslation.replace("['","")
			ftranslation = ftranslation.replace("', '","")
			ftranslation = ftranslation.replace("', ","")
			ftranslation = ftranslation.replace(", '","")
			ftranslation = ftranslation.replace('"',"")
			ftranslation = ftranslation.replace("']","")

		print(ftranslation)

translateTO()
translateFROM()
