
#This is if you want to have Tuesday on a Discord server as a bot. It works very nicely.

import discord #adds discord 
import asyncio #allows the async 
import wikipedia #adds wikipedia's api 
import wolframalpha #adds wolframalpha's api 
import random  
import os 
import yaml #operates with the insults file. 
from googletrans import Translator #google translate
import random
from string import punctuation

client = discord.Client() #for easier things later on
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

async def rempunc(s):

    return ''.join(c for c in s if c not in punctuation).lower()

async def SpeachRec():
    while 1:
        await client.send_message(message.channel, "...") # This is the prompt. I probably should make this tts... (CAN BE CHANGED)
        uinput = input("")
        await client.send_message(message.channel, "User: " + uinput)
        return uinput # This is just there so you can check to make sure that your speech was caught correctly.

async def sinput():
    if VOICEINPUT:
        return SpeachRec()
    else:
        return rempunc(input("User: "))

async def TextToSpeach(output):
    await client.send_message(message.channel, output)

async def sout(reply):
    if VOICEOUTPUT:
        TextToSpeach(reply)
    await client.send_message(message.channel, BOTNAME + ": " + reply)

async def debugging(dbstr):
    if DEBUGGING:
        await client.send_message(message.channel, "DEBUGGING:")
        await client.send_message(message.channel, dbstr)

async def main():

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
                    await client.send_message(message.channel, "No responce data found, a new session will begin to gather more data...")
                    debugging("No responce found")
                    await client.send_message(message.channel, "")
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
                    await client.send_message(message.channel, "No responce data found, a new session will begin to gather more data...")
                    debugging("No responce found")
                    await client.send_message(message.channel, "")
    
                    wm = False

@client.event
async def on_ready():
    print("-------")
    print("Logged in as")
    print(client.user.name)#Bot Name
    print(client.user.id)#Bot User ID
    print("-------")
    global tstzne
    global tstzne_authr
    global secretmode
    await client.change_presence(game=discord.Game(name='Actively Online'))
    tstzne = False
    tstzne_authr = None
    secretmode = False

@client.event
async def on_message(message):
    global tstzne
    global tstzne_authr
    global secretmode
    global begin_db
    global responce_db

    uinput = message.content #variable in actual tuesday (below was copied)

    if uinput.startswith(".`") or uinput.startswith(".~") or uinput.startswith(".`~"):
        await client.send_message(message.channel, "Remember, when trying to use my commands, delete the '.'!")

    elif uinput.startswith("```"):
        return

    elif uinput.lower().startswith("hey tuesday") or uinput.startswith("`~chat"):
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
                await main()
            else:
                print("Error, Invalid Command")
                print("Avalible Commands are: 'save', 'load', 'run'")

    #elif message.author.id == "177831674367836160" and tstzne == True and tstzne_authr == message.author:
    #    await client.add_reaction(message, "🦊")

    elif uinput == "`~secret-on" and message.author.id == "177831674367836160":
        await client.delete_message(message)
        secretmode = True
            
    elif uinput == "`~secret-off" and message.author.id == "177831674367836160":
        await client.delete_message(message)
        secretmode = False

    elif secretmode == True:
        print(message.author)
        print(message.author.id)

    elif uinput.startswith("`~testing") and tstzne == True and tstzne_authr == message.author:
        await client.send_message(message.channel, "It has worked.")

    elif uinput.lower().startswith("`~translate"):
        if uinput == "`~translate":
            await client.send_message(message.channel, "Please enter what is to be translated and if it is to go to another language, state the two letter version after the bleep.")
        else:
            translator = Translator()
            languagee = uinput.replace("`~translate ", "")
            language2 = languagee.split(" ")
            gtlanguages = ["af", "ach", "ak", "am", "ar", "az", "be", "bem", "bg", "bh", "bn", "br", "bs", "ca", "chr", "ckb", "co", "crs", "cs", "cy", "da", "de", "ee", "el", "en", "eo", "es", "es-419", "et", "eu", "fa", "fi", "fo", "fr", "fy", "ga", "gaa", "gd", "gl", "gn", "gu", "ha", "haw", "hi", "hr", "ht", "hu", "hy", "ia", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kg", "kk", "km", "kn", "ko", "kri", "ku", "ky", "la", "lg", "ln", "lo", "loz", "lt", "lua", "lv", "mfe", "mg", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "ne", "nl", "nn", "no", "nso", "ny", "nyn", "oc", "om", "or", "pa", "pcm", "pl", "ps", "pt-BR", "pt-PT", "qu", "rm", "rn", "ro", "ru", "rw", "sd", "sh", "si", "sk", "sl", "sn", "so", "sq", "sr", "sr-ME", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "tt", "tum", "tw", "ug", "uk", "ur", "uz", "vi", "wo", "xh", "xx-bork", "xx-elmer", "xx-hacker", "xx-klingon", "xx-pirate", "yi", "yo", "zh-CN", "zh-TW", "zu"]
            if language2[0] in gtlanguages:
                lang = language2[0]
                languagee = languagee.replace(lang, "")
                await client.send_message(message.channel, translator.translate(languagee, dest=lang))
            else:
                await client.send_message(message.channel, translator.translate(languagee, dest='en'))


    elif uinput == "`~speakmyspeech":
        await client.delete_message(message)
        print("I will speak anything you say:")
        while True:
            uiinput = input("")
            if uiinput != "":
                if uiinput == "`~stopmyspeech":
                    print("Stopping.")
                    return
                else:
                    await client.send_message(message.channel, uiinput)

    elif uinput.lower() == "`~enter-test":
        await client.delete_message(message)
        tstzne = True
        tstzne_authr = message.author

    elif uinput.lower() == "`~exit-test" and tstzne_authr == message.author and tstzne == True:
        await client.delete_message(message)
        tstzne = False
        tstzne_authr = None
    
    elif uinput.lower().startswith("`~sinsult"):
        if uinput.lower() == "`~sinsult tuesday" or uinput.lower().startswith("`~sinsult " + "<@!386700961051049985>"):
            config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
            pref = 'Thou'
            # algorithm simply makes a random choice from three different columns and concatenates them. 
            col1 = random.choice(config['column1'])
            col2 = random.choice(config['column2'])
            col3 = random.choice(config['column3'])
            # print generated insult for the 'user' 
            await client.send_message(message.channel, "I'm not going to insult myself, " + pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '!')

        else:

            if uinput.lower() == "`~sinsult": #code for general
                config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
                pref = 'Thou'
                # algorithm simply makes a random choice from three different columns and concatenates them. 
                col1 = random.choice(config['column1'])
                col2 = random.choice(config['column2'])
                col3 = random.choice(config['column3'])
                # print generated insult for the 'user' 
                await client.send_message(message.channel, pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '!' )

            elif uinput.lower() != "`~sinsult ": #and message.mentions.users.size == 1: #code for directions
                uinput = uinput.replace("`~sinsult ", "")
                config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
                pref = 'Thou'
                # algorithm simply makes a random choice from three different columns and concatenates them. 
                col1 = random.choice(config['column1'])
                col2 = random.choice(config['column2'])
                col3 = random.choice(config['column3'])
                # print generated insult for the 'user' 
                await client.send_message(message.channel, pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + ' ' + uinput + '!')

            else:
                await client.send_message(message.channel, "Something went really wrong...")

    elif uinput == "`Tuesday" or uinput == "~Tuesday":
        await client.send_message(message.channel, "That's me!") #This is just a fun reference to an AI... If only...

    elif uinput.lower() == "worship kevvy" or uinput.lower() == "worship tevin":
        await client.send_message(message.channel, "HAIL!") #WORSHIP TEVIN AND KEVVY

    elif uinput.lower() == "`~clean":
        delete_messages = []
        async for m in client.logs_from(message.channel, limit=10):
            if m.author == client.user:
                delete_messages.append(m)
        while delete_messages:
            try:
                await client.delete_messages(delete_messages)
                delete_messages = []
            except discord.ClientException:
                try:
                    await client.delete_messages(delete_messages[:100])
                    del delete_messages[:100]
                except discord.ClientException:
                    await client.delete_message(delete_messages[0])
        await client.send_message(message.channel, ":white_check_mark:")

    elif uinput.lower().startswith("`~say"):
        try:
            if uinput.lower().startswith("`~say tts"):
                uinput = uinput.replace("`~say", "")
                uinput = uinput.replace("`~SAY", "")
                uinput = uinput.replace("`~Say", "")
                uinput = uinput.replace("`~sAy", "")
                uinput = uinput.replace("`~saY", "")
                uinput = uinput.replace("`~SAy", "")
                uinput = uinput.replace("`~sAY", "")
                uinput = uinput.replace("`~SaY", "")
                uinput = uinput.replace("tts", "")
                uinput = uinput.replace("TTS", "")
                uinput = uinput.replace("Tts", "")
                uinput = uinput.replace("tTs", "")
                uinput = uinput.replace("ttS", "")
                uinput = uinput.replace("TTs", "")
                uinput = uinput.replace("tTS", "")
                uinput = uinput.replace("TtS", "")
                await client.send_message(message.channel, uinput, tts=True)
            
            else:
                uinput = uinput.replace("`~say", "")
                uinput = uinput.replace("`~SAY", "")
                uinput = uinput.replace("`~Say", "")
                uinput = uinput.replace("`~sAy", "")
                uinput = uinput.replace("`~saY", "")
                uinput = uinput.replace("`~SAy", "")
                uinput = uinput.replace("`~sAY", "")
                uinput = uinput.replace("`~SaY", "")
                await client.send_message(message.channel, uinput)
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Did you add something after the command? If so, please feel free to contact the developer.")

    elif uinput.lower() == "`~help":
        await client.send_message(message.channel, "I've sent you a private message with all the commands!")
        await client.send_message(message.author, "Hi! I'm Tuesday, a personal assistant created by @Lionclaw49, I'm being updated all the time, so I'll try and keep this up to date. Here's my list of commands, you can use all of them without the dots before them:\n")
        await client.send_message(message.author, " - .`~say -> This allows you to tell me what to say. You can also add tts by adding tts after the 'say'.\n")
        await client.send_message(message.author, " - .`~clean -> This clears my last 10 messages.\n")
        await client.send_message(message.author, " - .`~sinsult -> This sends a shakespearean insult.\n")
        await client.send_message(message.author, " - .`~translate (dest) -> This allows you to translate any language into the destination language(dest), you need to specify the ISO 639-1 code form of the language first though.")
        await client.send_message(message.author, "Also, anything with the prefix, `, will pull a wikipedia article, while anything with the prefix, ~, will pull wolframalpha (Math).\n")
        await client.send_message(message.author, "There are also some hidden commands, have fun trying to find them!")

    elif uinput.lower().startswith("`~mime") and tstzne == True and tstzne_authr == message.author:
        uinput = uinput.replace("`~mime", "")
        await client.delete_message(message)
        await client.send_message(message.channel, uinput)

    else:
        if uinput.startswith("~"): 
        #WOLFRAM ALPHA
            app_id = "G58JY9-WQ963T9EQV"  #to get the info
            cclient = wolframalpha.Client(app_id)  #connecting to info
            uinput = uinput.replace("~", "") #getting rid of `
            result = cclient.query(uinput)  #collecting result
            answer = next(result.results).text  #processing answer
            await client.send_message(message.channel, answer)  #sending answer

        elif uinput.startswith("`"):
            #WIKIPEDIA
            wikipedia.set_lang("en")  #Language!
    #       uinput = uinput.split(" ")
    #       uinput = " ".join(uinput[2:])
            uinput = uinput.replace("`", "")#getting rid of `
            try:
                answer = wikipedia.summary(uinput, chars=1900)#shortening the code below
                await client.send_message(message.channel, answer)#sending answer
            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e: #:) huh.
                print("Error caught!")
                await client.send_message(message.channel, e,)
            #except wikipedia.exceptions.PageError as r:
            #    print("Error caught!")
            #    await client.send_message(message.channel, r)

# So, did you catch the error? Try this: WAIT TESTING
#
#
    
client.run("Mzg2NzAwOTYxMDUxMDQ5OTg1.DQbmfA.GICszcU-1t_Xk6Dc7TE2pdnfC6w")
  
  #I have my bot token there, so you would have to replace it with yours. The instructions for that are below..
  #On the Discord Developers website, you have to create an bot id for it. Then you get the token, paste it above. Then add it to your server!
  #Have fun!
               
