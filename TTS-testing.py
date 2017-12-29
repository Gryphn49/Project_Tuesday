# Tuesday - Testing out the text to speech from gtts

from gtts import gTTS
from playsound import playsound

uinput = input("Test: ")

if uinput != "":

	tts = gTTS(text=uinput, lang='en', slow=True) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

	tts.save("hello.mp3")

	playsound('hello.mp3')

else:
	print("Empty.")



