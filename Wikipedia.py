import wikipedia

while True:
	input = raw_input("Question: ")

	wikipedia.set_lang("en")

	print wikipedia.summary(input,sentences=2)

