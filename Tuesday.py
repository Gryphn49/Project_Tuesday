import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pyowm

owm = pyowm.OWM('45441db00c108adaf665726143718637')

def Tuesday():
        while True:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    try:
                        print("What is your question?")
                    except KeyboardInterrupt:
                        exit()
                        print("Exiting...")
                    uinput = r.listen(source) #Adds user input
                #uinput = input("Question: ")
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
            #    try:
             #       uinput = r.recognize_google(uinput)

              #  except speech_recognition.UnknownValueError:
               #     tts = gTTS(text="I'm sorry, I don't know what you said.", lang='en')
                #    tts.save("tuesday-output.mp3")
                 #   playsound('tuesday-output.mp3')
    #
     #           except sr.RequestError as e:
      #              tts = gTTS(text="I need to be connected to the internet to understand what you say.", lang='en')
     #               tts.save("tuesday-output.mp3")
      #              playsound('tuesday-output.mp3')
    #
     #           except KeyboardInterrupt:
      #              print("Exiting...")

                
                digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                wolfA = False
                print(uinput)
                for number in digits[0:10]:
                    if number in uinput:
                        something = False
                        wolfA = True

                if wolfA == True:
                    try:
                        app_id = "G58JY9-WQ963T9EQV"  #to get the info
                        client = wolframalpha.Client(app_id)  #connecting to info
                        result = client.query(uinput)  #collecting result
                        answer = next(result.results).text  #processing answer
                        print(answer)

                        tts = gTTS(text=answer, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

                        tts.save("tuesday-output.mp3")

                        playsound('tuesday-output.mp3')

                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                        
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))

                elif uinput == "exit":
                    exit()

                elif "temperature" in uinput.lower():
                    uinput = uinput.split(" ")
                    placenum = len(uinput)
                    placenum = placenum-1
                    place = uinput[placenum]
                    observation = owm.weather_at_place(uinput[len(uinput)-1])
                    w = observation.get_weather()
                    print(w)
                    print(w.get_temperature("farenhe"))
                        

                elif uinput == "jfhfh":
                    return

                else:
                    #WIKIPEDIA
                    wikipedia.set_lang("en")  #Language!
            #        uinput = uinput.split(" ")
            #        uinput = " ".join(uinput[2:])
                    try:
                        reply = wikipedia.summary(uinput, sentences=1)

                        print(reply)

                        tts = gTTS(text=reply, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

                        tts.save("tuesday-output.mp3")

                        playsound('tuesday-output.mp3')

                    except wikipedia.exceptions.DisambiguationError as e:
                        e = e.split("\n")
                        tts = gTTS(text="Please narrow down your search."+e[0], lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                        tts.save("tuesday-output.mp3")
                        playsound('tuesday-output.mp3')
                        print(e)

                    except wikipedia.exceptions.HTTPTimeoutError as e:
                        tts = gTTS(text="Oh no! It looks like I have lost connection to the wikipedia server! Please try again later.", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                        tts.save("tuesday-output.mp3")
                        playsound('tuesday-output.mp3')

            #        except wikipedia.exceptions.PageError as e:
            #            tts = gTTS(text="I can't seem to that page ID! Could you try another search?", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
            #            tts.save("tuesday-output.mp3")
            #            playsound('tuesday-output.mp3')

                    except wikipedia.exceptions.WikipediaException as e:
                        tts = gTTS(text=e, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                        tts.save("tuesday-output.mp3")
                        playsound('tuesday-output.mp3')

            except KeyboardInterrupt:
                tts = gTTS(text="Exiting...", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                tts.save("tuesday-exit.mp3")
                playsound('tuesday-exit.mp3')

Tuesday()


    
    
        
