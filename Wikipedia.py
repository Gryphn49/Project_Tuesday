import wikipedia

while True:
	uinput = raw_input("Question: ")

	wikipedia.set_lang("en")

	print wikipedia.summary(uinput,sentences=2)

