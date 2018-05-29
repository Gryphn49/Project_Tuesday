import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pyowm
from appJar import gui

VOICEOUTPUT = True
begin_db = ["hi", "hey"]
responce_db = {
                "hi": ["how are you", "hi"],
                "hey": ["how are you", "hey"],
                 "how are you": ["good", "okay", "great",],
                 "khjhaskjdhjkhenkajjhuy3jh42bjknuc": ["Sorry, i didnt catch that, could you say it again?"]
                 }


owm = pyowm.OWM('45441db00c108adaf665726143718637')

app=gui("Tuesday", "400x250")

def sinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Hello!")
        except KeyboardInterrupt:
            exit()
            print("Exiting...")
        uinput = r.listen(source)

def tts(response):
    tts = gTTS(text=response, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

    tts.save("tuesday-output.mp3")

    playsound('tuesday-output.mp3')

def sout(reply):
    if VOICEOUTPUT:
        tts(reply)
    print(BOTNAME + ": " + reply)

def main(inn):



    # Variable used to exit the loop
    exitloop = False

    inp = inn
    if not wm:

        try:
            res = random.choice(responce_db[inp])
            debugging("Found responce")
            wm = True
            sout(res)

        except:
            tts("No responce data found, a new session will begin to gather more data...")
            debugging("No responce found")
            print("")
            begin_db.append(inp)
            wm = False

    else:
        inp = uinput
        print("USER: " + inp)
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
                tts("No responce data found, a new session will begin to gather more data...")
                debugging("No responce found")
                print("")

                wm = False


def Tuesday():
    while True:
        try:
            sinput()
            #Adds user input
            #uinput = input("Question: ")
            #    try:
            #       uinput = r.recognize_google(uinput)
            #
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
            #
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

            elif "temperature" in uinput.lower() or "weather" in uinput.lower():
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

            elif uinput.lower().startswith("what is") or uinput.lower().startswith("what are") or uinput.lower().startswith("who is") or uinput.lower().startswith("who was") or uinput.lower().startswith("what was") or uinput.lower().startswith("what did"):
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
            else:
                main()



        except KeyboardInterrupt:
            tts = gTTS(text="Exiting...", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
            tts.save("tuesday-exit.mp3")
            playsound('tuesday-exit.mp3')

def TuesdayTXT(uinput):
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    wolfA = False
    print(uinput)
    for number in digits[0:10]:
        if number in uinput:
            something = False
            wolfA = True
    #
    if wolfA == True:
        try:
            app_id = "G58JY9-WQ963T9EQV"  #to get the info
            client = wolframalpha.Client(app_id)  #connecting to info
            result = client.query(uinput)  #collecting result
            answer = next(result.results).text  #processing answer

            app.addLabel(answer)

        except sr.UnknownValueError:
            app.addLabel("Google Speech Recognition could not understand audio.")

        except sr.RequestError as e:
            app.addLabel("Could not request results from Google Speech Recognition service; {0}".format(e))

    elif uinput == "exit":
        exit()

    elif "temperature" in uinput.lower() or "weather" in uinput.lower():
        uinput = uinput.split(" ")
        placenum = len(uinput)
        placenum = placenum-1
        place = uinput[placenum]
        observation = owm.weather_at_place(uinput[len(uinput)-1])
        w = observation.get_weather()
        app.addLabel(w)
        app.addLabel(w.get_temperature("farenhe"))


    elif uinput == "jfhfh":
        return

    elif uinput.lower().startswith("what is") or uinput.lower().startswith("what are") or uinput.lower().startswith("who is") or uinput.lower().startswith("who was") or uinput.lower().startswith("what was") or uinput.lower().startswith("what did"):
        #WIKIPEDIA
        wikipedia.set_lang("en")  #Language!
#        uinput = uinput.split(" ")
#        uinput = " ".join(uinput[2:])
        try:
            reply = wikipedia.summary(uinput, sentences=3)
            app.addLabel(reply)

        except wikipedia.exceptions.DisambiguationError as e:
            e = e.split("\n")
            app.addLabel("Please narrow down your search."+e[0])
            print(e) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

        except wikipedia.exceptions.HTTPTimeoutError as e:
            app.addLabel("Oh no! It looks like I have lost connection to the wikipedia server! Please try again later.") ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

#        except wikipedia.exceptions.PageError as e:
#            tts = gTTS(text="I can't seem to that page ID! Could you try another search?", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
#            tts.save("tuesday-output.mp3")
#            playsound('tuesday-output.mp3')

        except wikipedia.exceptions.WikipediaException as e:
            app.addLabel(e)
    else:
        main(uinput)

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Input:")
        print("Input:", usr)
        TuesdayTXT(usr)

app.addLabelEntry("Input:")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.go()
