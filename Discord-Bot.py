
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
from weather import Weather
from urllib.request import urlopen
import re
from PyLyrics import *
from PyDictionary import PyDictionary


dictionary = PyDictionary()
client = discord.Client() #for easier things later on
weather = Weather()


#here begins the start of the functions for the 
global begin_db
global responce_db
global bugedition

begin_db = ['hi', 'hey', 'hello', 'heyo', 'sup', 'whats up']
responce_db = {'hows life': ['good'], 'okay': ['nice', 'where are you from', 'whats your favorite color'], 'nothing much': ['okay'], 'im good what about you': ['im good thanks'], 'hey': ['how are you', 'hey', 'hello', 'hows it going', 'sup', 'how is the weather', 'where are you from', 'hi', 'whats going on'], 'hi': ['how are you', 'hi', 'hello', 'hey', 'hows it going', 'whats going on', 'where are you from'], 'hello': ['how are you', 'hi', 'hey', 'sup', 'hows it going', 'whats going on'], 'im fine thanks': ['where are you from', 'whats your favorite color', 'youre welcome'], 'heyo': ['sup', 'hows it going', 'hey', 'hello', 'hi'], 'hows it going': ['im good how are you', 'good and you', 'its going pretty well what about you', 'pretty good you', 'im okay how are you', 'im fine how are you', 'im good how are you', 'its going okay you', 'good and you', 'good', 'pretty well', 'well'], 'its going pretty well what about you': ['im fine thanks'], 'me neither': ['cool'], 'im doing fine thanks for asking': ['whats your favorite color'], 'im fine you': ['im okay'], 'im good how are you': ['im doing fine thanks for asking', 'im doing okay thanks for asking', 'im fine thanks', 'im fine', 'im fine you'], 'im good you': ['good'], 'im okay how about you': ['im fine thanks for asking', 'good'], 'im okay you': ['im doing fine thanks', 'im doing okay', 'good'], 'maryland as well': ['awesome'], 'good day fine sir': ['whats going on'], 'yes': ['whats going on', 'cool', 'that seems nice'], 'its going okay you': ['im okay'], 'im from virginia where are you from': ['virginia as well'], 'how is the weather': ['its cold', 'sunny', 'grey'], 'im doing okay': ['how old are you'], 'whats going on': ['nothing much'], 'im good thanks for asking': ['no problem', 'what is your favorite food', 'when is your birthday'], 'great': ['good'], 'where are you from': ['im from maryland', 'im from maryland what about you', 'im from maryland where are you from', 'america'], 'good and you': ['im okay', 'im fine', 'good'], 'im fine': ['what is your favorite color', 'hows the weather', 'whats your name'], 'how are you': ['good', 'okay', 'great', 'im okay how are you', 'im fine you', 'im okay you', 'im fine how are you', 'im good what about you', 'im good how are you', 'im good thanks', 'good and you', 'im fine', 'im good you', 'im okay you', 'good how are you', 'good'], 'im fine how are you': ['im good thanks for asking', 'im okay thanks', 'im fine', 'im okay', 'good'], 'im okay how are you': ['good'], 'hows the weather': ['its nice thanks', 'its okay'], 'im doing okay thanks for asking': ['no problem'], 'good day': ['hi', 'good day fine sir', 'good day'], 'sup': ['hey', 'howdy', 'how are you', 'whats going on'], 'good how are you': ['good'], 'whats your favorite color': ['grey whats yours'], 'not much': ['me neither', 'me neither'], 'good': ['good', 'yes', 'hows life', 'whats going on']}

DEBUGGING = False
VOICEINPUT = False
VOICEOUTPUT = False

BOTNAME = "Tuesday"

async def send(channel, reply):
    return await client.send_message(channel, reply)

async def wait(time, channel, author):
    return await client.wait_for_message(timeout=time, channel=channel, author=author)










class htmlp:

    def __init__(self, hstr):

        try:
            self.hstr = hstr.decode("utf-8")
        except UnicodeDecodeError as e:
            self.hstr = str(hstr)
            print(e)

    def __str__(self):
        return str(self.hstr)

    # Method that returns a list of all strings between a begin string and end string
    # doesntbeginwith is an optional parameter that excludes certain  lists that begin with a certian substring
    # eg. all strings between "foo" and "bar" that dont begin with the substring "n"

    def between(self, substring1, substring2, must_not_match=re.compile(r"\A(\n|\r)")):
        """docstring goez heer"""
        retval = []
        s = self.hstr.split(substring1)
        for i in s:
            try:
                if must_not_match.search(i[0]) is None:
                    retval.append(i[0:i.index(substring2)])
            except: # What error are you trying to catch here?
                pass
        if len(retval) == 1:
            return retval[0]
        return retval

def rempunc(s):

    return ''.join(c for c in s if c not in punctuation).lower()

async def SpeachRec(message):
    while 1: # This is the prompt. I probably should make this tts... (CAN BE CHANGED)
        uinput = message.content
        await client.send_message(message.channel, "User: " + uinput)
        return uinput # This is just there so you can check to make sure that your speech was caught correctly.

async def sinput(message):
    if VOICEINPUT:
        return SpeachRec(message)
    else:
        return rempunc(message)

async def TextToSpeach(output, message):
    await client.send_message(message.channel, output)

async def sout(reply, message):
    if VOICEOUTPUT:
        await TextToSpeach(reply, message)
    await client.send_message(message.channel, BOTNAME + ": " + reply)

async def debugging(dbstr, message):
    if DEBUGGING:
        await client.send_message(message.channel, "DEBUGGING:")
        await client.send_message(message.channel, dbstr)

async def main(message):

    # Variable used to exit the loop
    exitloop = False

    while exitloop != True:

        if random.choice([True, False]):
    
            res = random.choice(begin_db)
            wm = True
    
        else: 
            if message.author.id == client.user.id:
                return
            elif message.author.id == 380833273112297474 or message.author.id == 365544801954955277 or message.author.id == 208946659361554432 or message.author.id == 235088799074484224 or message.author.id == 330488924449275916:
                return
            else:
                channelit = await client.wait_for_message(timeout=30, channel=message.channel)
                if channelit is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                elif channelit.content == "exit":
                    await client.send_message(message.channel, "Chatbot session exited.")
                else:
                    messagge = channelit.content
                    inp = await sinput(messagge)
        
                    if inp == 'exit':

                        await debugging("exit message seen", messagge)
                        wm = False
                        exitloop = True
            
                    else:
            
                        try:
                            res = random.choice(responce_db[inp])
                            await debugging("Found responce", message)
                            wm = True
            
                        except:
                            await client.send_message(message.channel, "No response data found, a new session will begin to gather more data...")
                            await debugging("No responce found", message)
                            begin_db.append(inp)
                            wm = False
        
        while wm:
    
            await sout(res, message)
    
            if message.author.id == client.user.id:
                return
            else:
                channelit = await client.wait_for_message(timeout=30, channel=message.channel)
                if channelit is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                elif channelit.content == "exit":
                    await client.send_message(message.channel, "Chatbot session exited...")
                    wm = False
                    exitloop = True
                else:
                    messagge = channelit.content
                    inp = await sinput(messagge)
                    if inp == 'exit':
                        wm = False
                        exitloop = True
            
                    if wm:
                        
                        if inp == "No response data found, a new session will begin to gather more data...":
                            return
                        else:
                            try:
                                responce_db[res].append(inp)
                                await debugging("Added new responce '" + inp + "'' under old key '" + res + "'", message)
                    
                            except:
                                responce_db[res] = [inp]
                                await debugging("Added new responce '" + inp + "'' under new key '" + res + "'", message)
                    
                            try:
                                res = random.choice(responce_db[inp])
                                await debugging("Found responce", message)
                    
                            except:
                                await client.send_message(message.channel, "No responce data found, a new session will begin to gather more data...")
                                await debugging("No responce found", message)
                
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
    global bugconfirm
    global bugedition
    

@client.event     
async def on_message(message):
    global tstzne
    global tstzne_authr
    global secretmode
    global begin_db
    global responce_db

    uinput = message.content #variable in actual tuesday (below was copied)
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = author.id

    if uinput.startswith(".`") or uinput.startswith(".~") or uinput.startswith(".``"):
        await client.send_message(message.channel, "Remember, when trying to use my commands, delete the '.'!")

    elif uinput.startswith("```"):
        return

    elif uinput.lower().startswith("hey tuesday") or uinput.startswith("`chat"):
        while 1:
            
            if message.author.id == client.user.id:
                return
            else:
                await client.send_message(message.channel, "Which command do you wish to use?")
                channelit = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                if channelit is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                elif channelit.content == "exit":
                    await client.send_message(message.channel, "Chatbot session exited.")
                    break
                else:
                    inp = channelit.content

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
                    if inp == "run":
                        if message.author.id != client.user.id:
                            await main(message)
                    else:
                        await client.send_message(message.channel, "Error, Invalid Command")
                        await client.send_message(message.channel, "Avalible Commands are: 'run'")

# Now here is where one can add the new commands.









    elif uinput.lower().startswith("`define"):
        uinput = uinput.replace("`define ", "")
        definition = dictionary.meaning(uinput)
        await send(channel, definition)

    elif uinput.lower().startswith("`synonym"):
        uinput = uinput.replace("`synonym ", "")
        synonym = dictionary.synonym(uinput)
        await send(channel, synonym)

    elif uinput.lower().startswith("`antonym"):
        uinput = uinput.replace("`antonym ", "")
        antonym = dictionary.antonym(uinput)
        await send(channel, antonym)







    elif uinput.lower() == "`lyrics":

        await send(channel, "Please enter a song name.")
        # wait for message
        song = await wait(60, channel, author)
        if song is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif song.content.lower() == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return

        song = song.content

        await send(channel, "Please enter a musical artist name.")
        # wait for message
        artist = await wait(60, channel, author)
        if artist is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif artist.content.lower() == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return
        
        artist = artist.content

        
        lyricss = PyLyrics.getLyrics(artist, song)
        lyricss = lyricss.split("\n\n")
        for i in lyricss:
            await client.send_message(channel, i)
            














    



    elif uinput.lower() == "`trending":
        url1 = 'http://www.tweeplers.com/hashtags/?cc=WORLD'
        html1 = htmlp(urlopen(url1).read())
        begstr1 = '<div class="col-xs-8 wordwrap" id="item_u_1" name="'
        endstr1 = '" style="font-size:1.5em"><a href='
        doesntbegw1 = "<"
        lst1 = html1.between(begstr1, endstr1, must_not_match=doesntbegw1)

        begstr2 = '<div class="col-xs-8 wordwrap" id="item_u_2" name="'
        my_reg = re.compile(r'<div class="col-xs-8 wordwrap" id="item_u_(\d)" name="(\w+)')
        lst2 = my_reg.find_all(html1)

        begstr3 = '<div class="col-xs-8 wordwrap" id="item_u_3" name="'
        lst3 = html1.between(begstr3, endstr1, must_not_match=doesntbegw1)

        begstr4 = '<div class="col-xs-8 wordwrap" id="item_u_4" name="'
        lst4 = html1.between(begstr4, endstr1, must_not_match=doesntbegw1)

        begstr5 = '<div class="col-xs-8 wordwrap" id="item_u_5" name="'
        lst5 = html1.between(begstr5, endstr1, must_not_match=doesntbegw1)

        begstr6 = '<div class="col-xs-8 wordwrap" id="item_u_6" name="'
        lst6 = html1.between(begstr6, endstr1, must_not_match=doesntbegw1)

        begstr7 = '<div class="col-xs-8 wordwrap" id="item_u_7" name="'
        lst7 = html1.between(begstr7, endstr1, must_not_match=doesntbegw1)

        begstr8 = '<div class="col-xs-8 wordwrap" id="item_u_8" name="'
        lst8 = html1.between(begstr8, endstr1, must_not_match=doesntbegw1)

        begstr9 = '<div class="col-xs-8 wordwrap" id="item_u_9" name="'
        lst9 = html1.between(begstr9, endstr1, must_not_match=doesntbegw1)

        begstr10 = '<div class="col-xs-8 wordwrap" id="item_u_10" name="'
        lst10 = html1.between(begstr10, endstr1, must_not_match=doesntbegw1)


        print("#" + str(lst1))
        print("#" + str(lst2))
        print("#" + str(lst3))
        print("#" + str(lst4))
        print("#" + str(lst5))
        print("#" + str(lst6))
        print("#" + str(lst7))
        print("#" + str(lst8))
        print("#" + str(lst9))
        print("#" + str(lst10))








    elif uinput.lower() == "`coinflip":
        coin = random.choice(["heads", "tails"])
        await send(channel, coin)

    elif uinput.lower() == "`roll":
        die = random.choice(["1", "2", "3", "4", "5", "6"])
        await send(channel, die)


    elif uinput.lower().startswith("`forecast"):
        if uinput.lower() == "`forecast":
            await send(channel, "Please enter a city or a zipcode.")
            # wait for message
            place = await wait(60, channel, author)
            if place is None:
                await client.send_message(message.channel, "Operation timed out.")
                return
            elif place.content.lower() == "cancel":
                await client.send_message(message.channel, "Operation canceled.")
                return

            place = place.content

            if place.isalpha():
                location = weather.lookup_by_location(place)
                forecasts = location.forecast()
                return_str = ""
                for forecast in forecasts:
                    return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
                await send(channel, return_str)
            elif place.isnumeric():
                lookup = weather.lookup(place)
                forecasts = lookup.forecast()
                return_str = ""
                for forecast in forecasts:
                    return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
                await send(channel, return_str)
            else:
                await send(channel, "Please enter a proper zipcode or city.")
        else:
            uinput = uinput.replace("`forecast ", "")
            if uinput.isalpha():
                location = weather.lookup_by_location(uinput)
                forecasts = location.forecast()
                return_str = ""
                for forecast in forecasts:
                    return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
                await send(channel, return_str)
            elif uinput.isnumeric():
                lookup = weather.lookup(uinput)
                forecasts = lookup.forecast()
                return_str = ""
                for forecast in forecasts:
                    return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
                await send(channel, return_str)
            else:
                await send(channel, "Please enter a proper zipcode or city.")


    elif uinput.lower().startswith("`weather"):
        if uinput.lower() == "`weather":
            await send(channel, "Please enter a city or a zipcode.")
            # wait for message
            place = await wait(60, channel, author)
            if place is None:
                await client.send_message(message.channel, "Operation timed out.")
                return
            elif place.content.lower() == "cancel":
                await client.send_message(message.channel, "Operation canceled.")
                return

            place = place.content

            if place.isalpha():
                location = weather.lookup_by_location(place)
                try:
                    condition = location.condition()
                    await send(channel, condition.text())
                except (KeyError, AttributeError):
                    await send(channel, "Please enter at proper zipcode.")
            elif place.isnumeric():
                lookup = weather.lookup(place)
                try:
                    condition = lookup.condition()
                    await send(channel, condition.text())
                    await send(channel, condition.temp())
                except (KeyError, AttributeError):
                    await send(channel, "Please enter a proper zipcode.")
            else:
                await send(channel, "Please enter a proper zipcode or city.")
        else:
            uinput = uinput.replace("`weather ", "")
            if uinput.isalpha():
                location = weather.lookup_by_location(uinput)
                try:
                    condition = location.condition()
                    await send(channel, condition.text())
                except (KeyError, AttributeError):
                    await send(channel, "Please enter a proper city.")
            elif uinput.isnumeric():
                lookup = weather.lookup(uinput)
                try:
                    condition = lookup.condition()
                    await send(channel, condition.text())
                except (KeyError, AttributeError):
                    await send(channel, "Please enter a proper zipcode.")
            else:
                await send(channel, "Please enter a proper zipcode or city.")
                
    elif uinput.lower() == "`poll":
        
        pollalts = False
        await send(channel, "What do you want your poll to be on? At any point in this process, 'cancel' will stop the whole thing.")
        pollttlwait = await wait(60, channel, author)
        if pollttlwait is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif pollttlwait.content.lower() == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return

        pollttl = pollttlwait.content

        await send(channel, "Please enter the choices for the poll, then once you are finished type 'done'.")
        pollalt = []
        while pollalts == False:    
            pollaltwait = await wait(240, channel, author)
            if pollaltwait is None:
                await client.send_message(message.channel, "Operation timed out.")
                return
            elif pollaltwait.content.lower() == "cancel":
                await client.send_message(message.channel, "Operation canceled.")
                return
            elif pollaltwait.content.lower() != "done":
                pollalt.append(pollaltwait.content)
                print(pollalt)
            else:
                pollalts = True
        print(pollalt)
        pollaltnum = len(pollalt)
        if pollaltnum > 10:
            await send(channel, "You have too many choices. Please split up the poll.")
            return
        elif pollaltnum < 1:
            await send(channel, "You have two few choices.")
            return

        await send(channel, "The poll is now finshed.")
        pollrktn = {1 : "\U00000031\U000020E3", 2 : "\U00000032\U000020E3", 3 : "\U00000033\U000020E3", 4 : "\U00000034\U000020E3", 5 : "\U00000035\U000020E3", 6 : "\U00000036\U000020E3", 7 : "\U00000037\U000020E3", 8 : "\U00000038\U000020E3", 9 : "\U00000039\U000020E3", 10 : "\U0001F51F"}
        pollrktn2 = {1 : ":one:", 2 : ":two:", 3 : ":three:", 4 : ":four:", 5 : ":five:", 6 : ":six:", 7 : ":seven:", 8 : ":eight:", 9 : ":nine:", 10 : ":keycap_ten:"}
        print(pollalt)
        await send(channel, pollttl)
        for i in range(pollaltnum):
            await send(channel, pollrktn2[i+1] + " - "+ pollalt[i])
        pollcat = await client.send_message(channel, "Hey @everyone, take the poll!") 
        for i in range(pollaltnum):
            await client.add_reaction(pollcat, pollrktn[i+1])

    elif uinput.lower().startswith("`bug"):
        bugconfirm = False
        bugedition = False
        await client.send_message(message.channel, "What would you call the bug that you wish to report? Type 'cancel' if you wish to escape this operation.")
        
        # the title of the bug
        bugttlwait = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
        if bugttlwait is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif bugttlwait.content == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return

        bugttl = bugttlwait.content

        # the operation in which the bug appeared
        await client.send_message(message.channel, "What command did you use in which the bug then appeared? Type 'cancel' if you wish to escape this operation.")
        bugcmdwait = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
        if bugcmdwait is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif bugcmdwait.content == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return

        bugcmd = bugcmdwait.content

        # description of the bug
        await client.send_message(message.channel, "Please clearly describe the bug in question. Type 'cancel' if you wish to escape this operation.")
        bugdscwait = await client.wait_for_message(timeout=180, channel=message.channel, author=message.author)
        if bugdscwait is None:
            await client.send_message(message.channel, "Operation timed out.")
            return
        elif bugdscwait.content == "cancel":
            await client.send_message(message.channel, "Operation canceled.")
            return

        bugdsc = bugdscwait.content


        while bugconfirm == False:
            await client.send_message(message.channel, "Please confirm the your bug report: ")
            await client.send_message(message.channel, "Title: " + bugttl)
            await client.send_message(message.channel, "Command: " + bugcmd)
            await client.send_message(message.channel, "Description: " + bugdsc)
            bugconfirmation = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
            if bugconfirmation is None:
                await client.send_message(message.channel, "Operation timed out.")
                return
            elif bugconfirmation.content == "deny":
                await client.send_message(message.channel, "Operation denied.")
                return
            elif bugconfirmation.content == "confirm":
                await client.send_message(message.channel, "Operation confirmed. The bug has been sent to the developer.")
                print("Bug Report:")
                print(bugttl)
                print("Command Which Caused Bug: " + bugcmd)
                print(bugdsc)
                bugconfirm = True
            elif bugconfirmation.content == "edit":
                while bugedition == False:
                    await client.send_message(message.channel, "What part of the bug report do you wish to edit?")
                    bugedit = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                    if bugedit is None:
                        await client.send_message(message.channel, "Operation timed out.")
                        return
                    elif bugedit.content.lower() == "title":
                        await client.send_message(message.channel, "You wish to edit the title. The current title is: " + bugttl + " What do you wish to change it to?")
                        bugttlwait = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                        if bugttlwait is None:
                            await client.send_message(message.channel, "Operation timed out.")
                            return
                        elif bugttlwait.content == "cancel":
                            await client.send_message(message.channel, "Operation canceled.")
                            return
                        else:
                            bugttl = bugttlwait.content
            

                    elif bugedit.content.lower() == "command":
                        await client.send_message(message.channel, "You wish to edit the command. The current command is: " + bugcmd + " What do you wish to change it to?")
                        bugcmdwait = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                        if bugcmdwait is None:
                            await client.send_message(message.channel, "Operation timed out.")
                            return
                        elif bugcmdwait.content == "cancel":
                            await client.send_message(message.channel, "Operation canceled.")
                            return
                        else:
                            bugcmd = bugcmdwait.content
                                



                    elif bugedit.content.lower() == "description":
                        await client.send_message(message.channel, "You wish to edit the description. The current description is: " + bugdsc + " What do you wish to change it to?")
                        bugdscwait = await client.wait_for_message(timeout=180, channel=message.channel, author=message.author)
                        if bugdscwait is None:
                            await client.send_message(message.channel, "Operation timed out.")
                            return
                        elif bugdscwait.content == "cancel":
                            await client.send_message(message.channel, "Operation canceled.")
                            return
                        else:
                            bugdsc = bugdscwait.content
                            
                    else:
                        await client.send_message(message.channel, "That is not a valid part of the bug report. The valid parts are 'title', 'command', and 'description'.")

                    await client.send_message(message.channel, "Do you wish to edit anymore?")
                    bugeditagn = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                    if bugeditagn is None:
                        await client.send_message(message.channel, "Operation timed out.")
                        return
                    elif bugeditagn.content.lower() == "no":
                        bugedition = True
                    elif bugeditagn.content.lower() == "yes":
                        return
                    else:
                        await client.send_message(message.channel, "Invalid command. Valid commands are 'yes' and 'no'.")
            else:
                await client.send_message(message.channel, "That is not a valid command. The valid commands are 'confirm', 'deny', and 'edit'.")


    #elif message.author.id == "177831674367836160" and tstzne == True and tstzne_authr == message.author:
    #    await client.add_reaction(message, "🦊")

    elif uinput == "`secret-on" and message.author.id == "177831674367836160":
        await client.delete_message(message)
        secretmode = True
            
    elif uinput == "`secret-off" and message.author.id == "177831674367836160":
        await client.delete_message(message)
        secretmode = False

    elif secretmode == True:
        print(message.author)
        print(message.author.id)

    elif uinput.lower().startswith("`github"):
        await client.send_message(message.channel, "Here's the github for my code: https://github.com/Lionclaw49/Project_Tuesday")

    elif uinput.startswith("`testing") and tstzne == True and tstzne_authr == message.author:
        await client.send_message(message.channel, "It has worked.")

    elif uinput.lower().startswith("`translate"):
        if uinput == "`translate":
            await client.send_message(message.channel, "Please enter what is to be translated and if it is to go to another language, state the two letter version after the bleep.")
        else:
            translator = Translator()
            languagee = uinput.replace("`translate ", "")
            language2 = languagee.split(" ")
            gtlanguages = ["af", "ach", "ak", "am", "ar", "az", "be", "bem", "bg", "bh", "bn", "br", "bs", "ca", "chr", "ckb", "co", "crs", "cs", "cy", "da", "de", "ee", "el", "en", "eo", "es", "es-419", "et", "eu", "fa", "fi", "fo", "fr", "fy", "ga", "gaa", "gd", "gl", "gn", "gu", "ha", "haw", "hi", "hr", "ht", "hu", "hy", "ia", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kg", "kk", "km", "kn", "ko", "kri", "ku", "ky", "la", "lg", "ln", "lo", "loz", "lt", "lua", "lv", "mfe", "mg", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "ne", "nl", "nn", "no", "nso", "ny", "nyn", "oc", "om", "or", "pa", "pcm", "pl", "ps", "pt-BR", "pt-PT", "qu", "rm", "rn", "ro", "ru", "rw", "sd", "sh", "si", "sk", "sl", "sn", "so", "sq", "sr", "sr-ME", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "tt", "tum", "tw", "ug", "uk", "ur", "uz", "vi", "wo", "xh", "xx-bork", "xx-elmer", "xx-hacker", "xx-klingon", "xx-pirate", "yi", "yo", "zh-CN", "zh-TW", "zu"]
            if language2[0] in gtlanguages:
                lang = language2[0]
                languagee = languagee.replace(lang, "")
                await client.send_message(message.channel, translator.translate(languagee, dest=lang))
            else:
                await client.send_message(message.channel, translator.translate(languagee, dest='en'))


    elif uinput == "`speakmyspeech":
        await client.delete_message(message)
        print("I will speak anything you say:")
        while True:
            uiinput = input("")
            if uiinput != "":
                if uiinput == "`stopmyspeech":
                    print("Stopping.")
                    return
                else:
                    await client.send_message(message.channel, uiinput)

    elif uinput.lower() == "`enter-test":
        await client.delete_message(message)
        tstzne = True
        tstzne_authr = message.author

    elif uinput.lower() == "`exit-test" and tstzne_authr == message.author and tstzne == True:
        await client.delete_message(message)
        tstzne = False
        tstzne_authr = None
    
    elif uinput.lower().startswith("`sinsult"):
        if uinput.lower() == "`sinsult tuesday" or uinput.lower().startswith("`sinsult " + "<@!386700961051049985>"):
            config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
            pref = 'Thou'
            # algorithm simply makes a random choice from three different columns and concatenates them. 
            col1 = random.choice(config['column1'])
            col2 = random.choice(config['column2'])
            col3 = random.choice(config['column3'])
            # print generated insult for the 'user' 
            await client.send_message(message.channel, "I'm not going to insult myself, " + pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '!')

        else:

            if uinput.lower() == "`sinsult": #code for general
                config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
                pref = 'Thou'
                # algorithm simply makes a random choice from three different columns and concatenates them. 
                col1 = random.choice(config['column1'])
                col2 = random.choice(config['column2'])
                col3 = random.choice(config['column3'])
                # print generated insult for the 'user' 
                await client.send_message(message.channel, pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '!' )

            elif uinput.lower() != "`sinsult ": #and message.mentions.users.size == 1: #code for directions
                uinput = uinput.replace("`sinsult ", "")
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

    elif uinput.lower() == "`clean":
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

    elif uinput.lower().startswith("`say"):
        try:
            if uinput.lower().startswith("`say tts"):
                uinput = uinput.replace("`say", "")
                uinput = uinput.replace("`SAY", "")
                uinput = uinput.replace("`Say", "")
                uinput = uinput.replace("`sAy", "")
                uinput = uinput.replace("`saY", "")
                uinput = uinput.replace("`SAy", "")
                uinput = uinput.replace("`sAY", "")
                uinput = uinput.replace("`SaY", "")
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
                uinput = uinput.replace("`say", "")
                uinput = uinput.replace("`SAY", "")
                uinput = uinput.replace("`Say", "")
                uinput = uinput.replace("`sAy", "")
                uinput = uinput.replace("`saY", "")
                uinput = uinput.replace("`SAy", "")
                uinput = uinput.replace("`sAY", "")
                uinput = uinput.replace("`SaY", "")
                await client.send_message(message.channel, uinput)
        except discord.errors.HTTPException:
            await client.send_message(message.channel, "Did you add something after the command? If so, please feel free to contact the developer.")

    elif uinput.lower() == "`help":
        await client.send_message(message.channel, "I've sent you a private message with all the commands!")
        await client.send_message(message.author, "Hi! I'm Tuesday, a personal assistant created by @Lionclaw49, I'm being updated all the time, so I'll try and keep this up to date. Here's my list of commands, you can use all of them without the dots before them:\n - .`say -> This allows you to tell me what to say. You can also add tts by adding tts after the 'say'.\n - .`clean -> This clears my last 10 messages.\n - .`sinsult -> This sends a shakespearean insult.\n- .`bug -> This allows you to report a bug to the developer.\n - .`chat -> This allows you to chat with Tuesday.\n - .`translate (dest) -> This allows you to translate any language into the destination language(dest), you need to specify the ISO 639-1 code form of the language first though.\nAlso, anything with the prefix, ``, will pull a wikipedia article, while anything with the prefix, ~, will pull wolframalpha (Math).\nThere are also some hidden commands, have fun trying to find them!")

    elif uinput.lower().startswith("`mime"):
        if message.server.id == "367076093523656704":
            uinput = uinput.replace("`mime ", "")
            await send(discord.utils.find(lambda ch: ch.id == "399269109029797899", message.server.channels), author.mention + " said: \"" + uinput + "\" in " + channel.mention + ".")
            await client.delete_message(message)
            await client.send_message(message.channel, uinput)
        else:
            uinput = uinput.replace("`mime ", "")
            await client.delete_message(message)
            await client.send_message(message.channel, uinput)


    else:
        if uinput.startswith("~"): 
        #WOLFRAM ALPHA
            app_id = "G58JY9-WQ963T9EQV"  #to get the info
            cclient = wolframalpha.Client(app_id)  #connecting to info
            uinput = uinput.replace("~", "") #getting rid of ~
            result = cclient.query(uinput)  #collecting result
            answer = next(result.results).text  #processing answer
            await client.send_message(message.channel, answer)  #sending answer

        elif uinput.startswith("``"):
            #WIKIPEDIA
            wikipedia.set_lang("en")  #Language!
    #       uinput = uinput.split(" ")
    #       uinput = " ".join(uinput[2:])
            uinput = uinput.replace("``", "")#getting rid of ``
            try:
                answer = wikipedia.summary(uinput, chars=1900)#shortening the code below
                await client.send_message(message.channel, answer)#sending answer
            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e: #:)
                await client.send_message(message.channel, e,)
            #except wikipedia.exceptions.PageError as r:
            #    print("Error caught!")
            #    await client.send_message(message.channel, r)

#
#
#

client.run("Mzg2NzAwOTYxMDUxMDQ5OTg1.DQbmfA.GICszcU-1t_Xk6Dc7TE2pdnfC6w")
  
  #I have my bot token there, so you would have to replace it with yours. The instructions for that are below..
  #On the Discord Developers website, you have to create an bot id for it. Then you get the token, paste it above. Then add it to your server!
  #Have fun!
               
