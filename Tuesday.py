import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


while True:
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Question: ")
#        uinput = r.listen(source) #Adds user input
#        print(uinput)  

    uinput = input("Question: ")
    
    if uinput == "exit":
        exit()
        
    elif uinput.startswith("(WP)"):
        #WIKIPEDIA
        uinput = uinput.replace("(WP)", "")
        wikipedia.set_lang("en")  #Language!
#        uinput = uinput.split(" ")
#        uinput = " ".join(uinput[2:])
        reply = wikipedia.summary(uinput)

        tts = gTTS(text=reply, lang='en', slow=True) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

        tts.save("tuesday-input.mp3")

        playsound('tuesday-input.mp3')

    elif uinput.startswith("(WA)"): 
    #WOLFRAM ALPHA
        uinput = uinput.replace("(WA)", "")
        app_id = "G58JY9-WQ963T9EQV"  #to get the info
        client = wolframalpha.Client(app_id)  #connecting to info
        result = client.query(uinput)  #collecting result
        answer = next(result.results).text  #processing answer
        print(answer)

        tts = gTTS(text=answer, lang='en', slow=True) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

        tts.save("tuesday-input.mp3")

        playsound('tuesday-input.mp3')
    
    
        
