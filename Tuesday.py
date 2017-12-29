import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from googletrans import Translator


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Question: ")
        uinput = r.listen(source) #Adds user input
        try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
            uinput = r.recognize_google(uinput)
#    uinput = input("Question: ")
            print(uinput)
            if uinput == "exit":
                exit()
        
            elif uinput.startswith("WIC"):
                #WIKIPEDIA
                uinput = uinput.replace("WIC", "")
                wikipedia.set_lang("en")  #Language!
        #        uinput = uinput.split(" ")
        #        uinput = " ".join(uinput[2:])
                try:
                    reply = wikipedia.summary(uinput, sentences=1)

                    print(reply)

                    tts = gTTS(text=reply, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

                    tts.save("tuesday-input.mp3")

                    playsound('tuesday-input.mp3')

                except wikipedia.exceptions.DisambiguationError as e:
                    tts = gTTS(text="Please narrow down your search.", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                    tts.save("tuesday-input.mp3")
                    playsound('tuesday-input.mp3')
                    print(e)

                except wikipedia.exceptions.HTTPTimeoutError as e:
                    tts = gTTS(text="Oh no! It looks like I have lost connection to the wikipedia server! Please try again later.", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                    tts.save("tuesday-input.mp3")
                    playsound('tuesday-input.mp3')

        #        except wikipedia.exceptions.PageError as e:
        #            tts = gTTS(text="I can't seem to that page ID! Could you try another search?", lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
        #            tts.save("tuesday-input.mp3")
        #            playsound('tuesday-input.mp3')

                except wikipedia.exceptions.WikipediaException as e:
                    tts = gTTS(text=e, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).
                    tts.save("tuesday-input.mp3")
                    playsound('tuesday-input.mp3')

            elif uinput.startswith("wolf"): 
            #WOLFRAM ALPHA
                uinput = uinput.replace("wolf", "")
                app_id = "G58JY9-WQ963T9EQV"  #to get the info
                client = wolframalpha.Client(app_id)  #connecting to info
                result = client.query(uinput)  #collecting result
                answer = next(result.results).text  #processing answer
                print(answer)

                tts = gTTS(text=answer, lang='en',) ###### _Parameters:_ * `text` - String - Text to be spoken. * `lang` - String - [ISO 639-1 language code](#lang_list) (supported by the Google _Text to Speech_ API) to speak in. * `slow` - Boolean - Speak slowly. Default `False` (Note: only two speeds are provided by the API).

                tts.save("tuesday-input.mp3")

                playsound('tuesday-input.mp3')

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

            elif uinput.startswith("translate"):
                if uinput == "translate":
                    tts = gTTS(text="Please enter what is to be translated and if it is to go to another language, state the two letter version after the bleep. BLEEP", lang=en)
        else:
            translator = Translator()
            languagee = uinput.replace("translate ", "")
            language2 = languagee.split(" ")
            gtlanguages = ["af", "ach", "ak", "am", "ar", "az", "be", "bem", "bg", "bh", "bn", "br", "bs", "ca", "chr", "ckb", "co", "crs", "cs", "cy", "da", "de", "ee", "el", "en", "eo", "es", "es-419", "et", "eu", "fa", "fi", "fo", "fr", "fy", "ga", "gaa", "gd", "gl", "gn", "gu", "ha", "haw", "hi", "hr", "ht", "hu", "hy", "ia", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kg", "kk", "km", "kn", "ko", "kri", "ku", "ky", "la", "lg", "ln", "lo", "loz", "lt", "lua", "lv", "mfe", "mg", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "ne", "nl", "nn", "no", "nso", "ny", "nyn", "oc", "om", "or", "pa", "pcm", "pl", "ps", "pt-BR", "pt-PT", "qu", "rm", "rn", "ro", "ru", "rw", "sd", "sh", "si", "sk", "sl", "sn", "so", "sq", "sr", "sr-ME", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "tt", "tum", "tw", "ug", "uk", "ur", "uz", "vi", "wo", "xh", "xx-bork", "xx-elmer", "xx-hacker", "xx-klingon", "xx-pirate", "yi", "yo", "zh-CN", "zh-TW", "zu"]
            if language2[0] in gtlanguages:
                lang = language2[0]
                languagee = languagee.replace(lang, "")
                tts = gTTS(text=translator.translate(languagee, dest=lang), lang=lang)
            else:
                await client.send_message(message.channel, translator.translate(languagee, dest='en'))

    
    
        
