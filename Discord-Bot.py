
#This is if you want to have Tuesday on a Discord server as a bot. It works very nicely.

import discord #adds discord
import asyncio, aiohttp #allows the async
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
from selenium import webdriver
import smtplib
import sys
import datetime

personal = [] # Hello, you don't need to hae
dictionary = PyDictionary()
client = discord.Client() #for easier things later on
weather = Weather()

canCollects = {"177831674367836160": "0"}
authorcollection = {"Lionclaw49" : "No-thang"}
swears = ["shit","fuck","cunt","ass","bastard","whore","slut"]


while True:
    try:
        #here begins the start of the functions for the
        global begin_db
        global responce_db
        global bugedition
        global jsonData


        def saver():
            ToJson = json.dumps(authorcollection)

            print(ToJson)

            xname = "tusedayCollection"
            file = open(xname + ".txt","w")
            file.write(ToJson)
            file.close()
        def openr():
            global jsonData
            try:
                xname = "tusedayCollection"
                file = open(xname + ".txt", "r")
                jsonData = file.read()
                print(jsonData)
                file.close()
                print("Load Comlpete")
            except FileNotFoundError:
                print("Error, Load File Not Found")
            print(jsonData)
            authorcollection = json.loads(jsonData)

            print(authorcollection)

        OWcollection = ["Doomfist",
                    "Genji",
                    "McCree",
                    "Soldier: 76",
                    "Pharah",
                    "Reaper",
                    "Sombra",
                    "Tracer",
                    "Bastion",
                    "Hanzo",
                    "Junkrat",
                    "Mei",
                    "Torbjörn",
                    "Widowmaker",
                    "D.va",
                    "Orisa",
                    "Reinhardt",
                    "Roadhog",
                    "Winston",
                    "Zarya",
                    "Ana",
                    "Brigitte",
                    "Lúcio",
                    "Mercy",
                    "Moira",
                    "Symmetra",
                    "Zenyatta"]

        OWcollectionpics = {
                    "Doomfist" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/1/15/Doomfist_Artwork.png/252px-Doomfist_Artwork.png?version=c0b05e57e84040ed5edac1e2f8231c4b",
                    "Genji" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/d/d8/Genji-portrait.png/322px-Genji-portrait.png?version=284e7c2c19f78860c219f62dfc178ab1",
                    "McCree" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/d/d2/Mccree-portrait.png/264px-Mccree-portrait.png?version=000a91f377fd2d6a99ad43ed6f4bc63c",
                    "Soldier: 76" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/e/e0/Soldier76-portrait.png/224px-Soldier76-portrait.png?version=a9373c62fec018039c8e4031f7d57dd8",
                    "Pharah" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/2/26/Pharah-portrait.png/268px-Pharah-portrait.png?version=8791c3743b70a94a188df66fcb89bed2",
                    "Reaper" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/7/74/Reaper-portrait.png/272px-Reaper-portrait.png?version=950d03add54777aeedf41392feb6897b",
                    "Sombra" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/c/c5/Sombra-portrait.png/350px-Sombra-portrait.png?version=9520108b39e3bc3f148449827adaf4c5",
                    "Tracer" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/8/81/Tracer-portrait.png/169px-Tracer-portrait.png?version=8c013cebc86c83ed5a42cbb42e7dd512",
                    "Bastion" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/d/d0/Bastion-portrait.png/332px-Bastion-portrait.png?version=e277ee1033929a8ebf223ab617fb8ced",
                    "Hanzo" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/a/a0/Hanzo-portrait.png/290px-Hanzo-portrait.png?version=a721183b82a0b6a3deb3869c8f4179cc",
                    "Junkrat" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/9/99/Junkrat-Portrait.png/286px-Junkrat-Portrait.png?version=564a39d74f85937e6386515e9e81c470",
                    "Mei" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/d/d0/Mei-portrait.png/196px-Mei-portrait.png?version=6e3d92ef60f5357e67d345368b96e534",
                    "Torbjörn" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/c/c5/Torbjorn-portrait.png/350px-Torbjorn-portrait.png?version=6d899a3e6b6fcdaf0d41334c617fc5bb",
                    "Widowmaker" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/4/4c/Widowmaker-portrait.png/222px-Widowmaker-portrait.png?version=c04d2227553d9203efc3fe51433c5f50",
                    "D.va" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/b/b0/DVa-portrait.png/336px-DVa-portrait.png?version=d4c75428d60b74d3141a996683b06a1c",
                    "Orisa" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/6/66/Orisa-portrait.png/350px-Orisa-portrait.png?version=9385d1245d351a89a921b7629eee1216",
                    "Reinhardt" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/0/07/Reinhardt-portrait.png/350px-Reinhardt-portrait.png?version=be7c2ee9b5ff4cf209e6b8b585185ff0",
                    "Roadhog" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/c/ce/Roadhog-Portrait.png/345px-Roadhog-Portrait.png?version=7c797712fd43d96486c5fbe83462a0f7",
                    "Winston" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/b/b8/Winston-portrait.png/350px-Winston-portrait.png?version=82b209d14d68e43d127a5272173fc8ab",
                    "Zarya" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/6/6d/Zarya-portrait.png/350px-Zarya-portrait.png?version=2f467a16472e4814171fa8a024e775bb",
                    "Ana" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/7/76/Ana.png/143px-Ana.png?version=4d855694641b3d2daaf1b0b9dbf69b25",
                    "Brigitte" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/8/8a/Brigitte_Concept.png/255px-Brigitte_Concept.png?version=46c36e2c1e9ba16db5697729a25b676c",
                    "Lúcio" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/8/8c/Lucio-portrait.png/189px-Lucio-portrait.png?version=75b7891ed0619de3fbdd236f30c264fc",
                    "Mercy" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/d/d2/Mercy-portrait.png/350px-Mercy-portrait.png?version=e5fdf5c2b3ad98b648c585bb631e5dc4",
                    "Moira" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/b/b5/Moira.png/162px-Moira.png?version=8062e3f0899bdb803d1dd80d01c30201",
                    "Symmetra" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/1/18/Symmetra-portrait.png/161px-Symmetra-portrait.png?version=1a2d00ede76d3a7ee3e4c75bcc92cf19",
                    "Zenyatta" : "https://d1u5p3l4wpay3k.cloudfront.net/overwatch_gamepedia/thumb/9/92/Zenyatta-portrait.png/269px-Zenyatta-portrait.png?version=e8de871b947eab2c59029ae0472947be"
        }

        RLcollection = ["Backfire",
                    "Breakout",
                    "Gizmo",
                    "Hotshot",
                    "Merc",
                    "Octane",
                    "Paladin",
                    "Road Hog",
                    "Venom",
                    "X-Devil",
                    "Animus GP",
                    "Breakout Type-S",
                    "Centio V17",
                    "Dominus GT",
                    "Endo",
                    "Imperator DT5",
                    "Jäger 619 RS",
                    "Mantis",
                    "Octane ZSR",
                    "Road Hog XL",
                    "Takumi RX-T",
                    "X-Devil Mk2",]

        RLcollectionpics = {
            "Backfire" : "https://vignette.wikia.nocookie.net/rocketleague/images/c/cf/Backfire_body_icon.png/revision/latest?cb=20170527083720",
            "Breakout" : "https://vignette.wikia.nocookie.net/rocketleague/images/6/6b/Breakout_body_icon.png/revision/latest/scale-to-width-down/222?cb=20170527084936",
            "Gizmo" : "https://vignette.wikia.nocookie.net/rocketleague/images/8/88/Gizmo_body_icon.png/revision/latest?cb=20170526231903",
            "Hotshot" : "https://vignette.wikia.nocookie.net/rocketleague/images/3/3f/Hotshot_body_icon_v1.png/revision/latest?cb=20170528120334",
            "Merc" : "https://vignette.wikia.nocookie.net/rocketleague/images/3/3f/Merc_body_icon.png/revision/latest?cb=20170528134205",
            "Octane" : "https://vignette.wikia.nocookie.net/rocketleague/images/f/f1/Octane_body_icon.png/revision/latest?cb=20170526223331",
            "Paladin" : "https://vignette.wikia.nocookie.net/rocketleague/images/a/a3/Paladin_body_icon.png/revision/latest?cb=20170528155813",
            "Road Hog" : "https://vignette.wikia.nocookie.net/rocketleague/images/9/90/Road_Hog_body_icon_v1.png/revision/latest?cb=20170528093317",
            "Venom" : "https://vignette.wikia.nocookie.net/rocketleague/images/9/9e/Venom_body_icon.png/revision/latest?cb=20170528163048",
            "X-Devil" : "https://vignette.wikia.nocookie.net/rocketleague/images/2/20/X-Devil_body_icon_v1.png/revision/latest?cb=20170528093830",
            "Animus GP" : "https://vignette.wikia.nocookie.net/rocketleague/images/a/a5/Animus_GP_body_icon.png/revision/latest?cb=20170705230526",
            "Breakout Type-S" : "https://vignette.wikia.nocookie.net/rocketleague/images/0/04/Breakout_Type-S_body_icon.png/revision/latest?cb=20170522201553",
            "Centio V17" : "https://vignette.wikia.nocookie.net/rocketleague/images/5/59/Centio_V17_body_icon.png/revision/latest?cb=20170705230548",
            "Dominus GT" : "https://vignette.wikia.nocookie.net/rocketleague/images/9/98/Dominus_GT_body_icon.png/revision/latest?cb=20170523201643",
            "Endo" : "https://vignette.wikia.nocookie.net/rocketleague/images/5/59/Endo_body_icon.png/revision/latest?cb=20170625212547",
            "Imperator DT5" : "https://vignette.wikia.nocookie.net/rocketleague/images/e/e5/Imperator_DT5_body_icon.png/revision/latest?cb=20171204230559",
            "Jäger 619 RS" : "https://vignette.wikia.nocookie.net/rocketleague/images/b/bd/Jäger_619_RS_body_icon.png/revision/latest/scale-to-width-down/480?cb=20170928222159",
            "Mantis" : "https://vignette.wikia.nocookie.net/rocketleague/images/0/0f/Mantis_body_icon.png/revision/latest?cb=20170625211802",
            "Octane ZSR" : "https://vignette.wikia.nocookie.net/rocketleague/images/2/2d/Octane_ZSR_body_icon.png/revision/latest?cb=20170527001324",
            "Road Hog XL" : "https://vignette.wikia.nocookie.net/rocketleague/images/c/c2/Road_Hog_XL_body_icon.png/revision/latest?cb=20170523152051",
            "Takumi RX-T" : "https://vignette.wikia.nocookie.net/rocketleague/images/c/cb/Takumi_RX-T_body_icon.png/revision/latest?cb=20170524181147",
            "X-Devil Mk2" : "https://vignette.wikia.nocookie.net/rocketleague/images/d/db/X-Devil_Mk2_body_icon.png/revision/latest?cb=20170523153541",
        }




        begin_db = ['hi', 'hey', 'hello', 'heyo', 'sup', 'whats up']
        responce_db = {'hows life': ['good'], 'okay': ['nice', 'where are you from', 'whats your favorite color'], 'nothing much': ['okay'], 'im good what about you': ['im good thanks'], 'hey': ['how are you', 'hey', 'hello', 'hows it going', 'sup', 'how is the weather', 'where are you from', 'hi', 'whats going on'], 'hi': ['how are you', 'hi', 'hello', 'hey', 'hows it going', 'whats going on', 'where are you from'], 'hello': ['how are you', 'hi', 'hey', 'sup', 'hows it going', 'whats going on'], 'im fine thanks': ['where are you from', 'whats your favorite color', 'youre welcome'], 'heyo': ['sup', 'hows it going', 'hey', 'hello', 'hi'], 'hows it going': ['im good how are you', 'good and you', 'its going pretty well what about you', 'pretty good you', 'im okay how are you', 'im fine how are you', 'im good how are you', 'its going okay you', 'good and you', 'good', 'pretty well', 'well'], 'its going pretty well what about you': ['im fine thanks'], 'me neither': ['cool'], 'im doing fine thanks for asking': ['whats your favorite color'], 'im fine you': ['im okay'], 'im good how are you': ['im doing fine thanks for asking', 'im doing okay thanks for asking', 'im fine thanks', 'im fine', 'im fine you'], 'im good you': ['good'], 'im okay how about you': ['im fine thanks for asking', 'good'], 'im okay you': ['im doing fine thanks', 'im doing okay', 'good'], 'maryland as well': ['awesome'], 'good day fine sir': ['whats going on'], 'yes': ['whats going on', 'cool', 'that seems nice'], 'its going okay you': ['im okay'], 'im from virginia where are you from': ['virginia as well'], 'how is the weather': ['its cold', 'sunny', 'grey'], 'im doing okay': ['how old are you'], 'whats going on': ['nothing much'], 'im good thanks for asking': ['no problem', 'what is your favorite food', 'when is your birthday'], 'great': ['good'], 'where are you from': ['im from maryland', 'im from maryland what about you', 'im from maryland where are you from', 'america'], 'good and you': ['im okay', 'im fine', 'good'], 'im fine': ['what is your favorite color', 'hows the weather', 'whats your name'], 'how are you': ['good', 'okay', 'great', 'im okay how are you', 'im fine you', 'im okay you', 'im fine how are you', 'im good what about you', 'im good how are you', 'im good thanks', 'good and you', 'im fine', 'im good you', 'im okay you', 'good how are you', 'good'], 'im fine how are you': ['im good thanks for asking', 'im okay thanks', 'im fine', 'im okay', 'good'], 'im okay how are you': ['good'], 'hows the weather': ['its nice thanks', 'its okay'], 'im doing okay thanks for asking': ['no problem'], 'good day': ['hi', 'good day fine sir', 'good day'], 'sup': ['hey', 'howdy', 'how are you', 'whats going on'], 'good how are you': ['good'], 'whats your favorite color': ['grey whats yours'], 'not much': ['me neither', 'me neither'], 'good': ['good', 'yes', 'hows life', 'whats going on']}

        DEBUGGING = False
        VOICEINPUT = False
        VOICEOUTPUT = False

        BOTNAME = "Tuesday"

        async def send(channel, reply):
                await client.send_message(channel, reply)

        async def wait(time, channel, author):
            await client.wait_for_message(timeout=time, channel=channel, author=author)






        debug = False

        async def debug(message):
            if debug == True:
                print("Debug Message: " + message)
            else:
                return

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

        def openm(lst):
            ret = []
            for i in lst:
                ret.append(open(i, 'r'))
            return ret

        def closem(lst):
            for i in lst:
                i.close()

        def rempunc(s):

            return ''.join(c for c in s if c not in punctuation).lower()

        async def SpeachRec(message):
            while 1:
                uinput = message.content
                print("User: " + uinput)
                return uinput # This is just there so you can check to make sure that your speech was caught correctly.

        async def sinput(message):
            if VOICEINPUT:
                return SpeachRec(message)
            else:
                return rempunc(message)

        async def TextToSpeach(output,message):
            await send(messsage.channel, output)

        async def sout(reply,message):
            if VOICEOUTPUT:
                await TextToSpeach(reply, message)
            await send(message.channel, BOTNAME + ": " + reply)

        def debugging(dbstr):
            if DEBUGGING:
                print("DEBUGGING:")
                print(dbstr)

        async def main(message):

            # Variable used to exit the loop
            exitval = False

            while exitval != True:

                if random.choice([True, False]):

                    res = random.choice(begin_db)
                    wm = True

                else:
                    if message.author.id == client.user.id:
                        return


                    elif message.author.id == 380833273112297474 or message.author.id == 365544801954955277 or message.author.id == 208946659361554432 or message.author.id == 235088799074484224 or message.author.id == 330488924449275916:
                        return


                    channelit = await client.wait_for_message(timeout=30, channel=message.channel)
                    if channelit is None:
                        await client.send_message(message.channel, "Operation timed out.")
                        return
                    elif channelit.content == "exit":
                        await client.send_message(message.channel, "Chatbot session exited.")
                        wm = False
                        exitval = True
                    elif channelit.content == "settings":
                        settings(message)
                    else:
                        messagge = channelit.content


                    inp = await sinput(message)


                    try:
                        res = random.choice(responce_db[inp])
                        debugging("Found responce")
                        wm = True

                    except:
                        await send(message.channel, "No responce data found, a new session will begin to gather more data...")
                        debugging("No responce found")
                        print("")
                        begin_db.append(inp)
                        wm = False

                while wm:

                    await sout(res,message)

                    inp = await sinput(message)
                    if inp == 'exit':
                        wm = False
                        exitval = True

                    if wm:

                        try:
                            responce_db[res].append(inp)
                            debugging("Added new responce '" + str.inp + "'' under old key '" + str.res + "'")

                        except:
                            responce_db[res] = [inp]
                            debugging("Added new responce '" + str.inp + "'' under new key '" + str.res + "'")

                        try:
                            res = random.choice(responce_db[inp])
                            debugging("Found responce")

                        except:
                            await send(message.channel, "No responce data found, a new session will begin to gather more data...")
                            debugging("No responce found")

                            wm = False

        async def settings(message):
            while True:
                await client.send_message(message.channel, "Which command do you wish to use?")
                channelit = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                if channelit is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                elif channelit.content == "exit":
                    await client.send_message(message.channel, "Settings exited.")
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
                            print("Load Comlpete")
                        except FileNotFoundError:
                            print("Error, Load File Not Found")

                    elif inp == 'stitch':
                        nfiles = []
                        x = True
                        while 1:
                            inp = input("File Name: ")
                            if inp == '':
                                break
                            else:
                                nfiles.append(inp + '.txt')

                        opened_files = openm(nfiles)

                        fin_b_db = begin_db
                        fin_r_db = responce_db

                        for file in opened_files:
                            for line in file.readlines():
                                exec(line)
                            fin_b_db += begin_db
                            fin_r_db.update(responce_db)

                        begin_db = fin_b_db
                        responce_db = fin_r_db

                        print('Stitching Sucsessfull')


                    elif inp == "continue":
                        if message.author.id != client.user.id:
                            await main(message)
                    else:
                        await client.send_message(message.channel, "Error, Invalid Command")
                        await client.send_message(message.channel, "Avalible Commands are: 'continue'")


        banned = []
        bannedloop = True
        allbanned = False
        debugloop = False
        collectioned = False
        testors = []
        while bannedloop:
            try:
                bannedin = input("Would you like to ban any members from this code? Please provide their ID code. Type 'done' if you are finished.")

                if bannedin.lower() == "done":
                    bannedloop = False
                    break
                elif bannedin.lower() == "all":
                    allbanned = True
                    bannedloop = False
                    break
                elif bannedin.lower() == "debug":
                    debug = True
                    debugloop = True
                    while debugloop:
                        debugIN = input("Would you like to add any bot testors to help debug?? Please provide their ID code. Type 'done' if you are finished.")

                        if debugIN.lower() == "done":
                            debugloop = False
                            break
                        elif debugIN.lower() == "me":
                            testors.append("177831674367836160")
                        else:
                            testors.append(debugIN)

                    bannedloop = False
                    break
                else:
                    banned.append(bannedin)
            except KeyboardInterrupt:
                exit()
                break


        startloop = True
        while startloop:
            try:
                start = input("Would you like to start the program? (y/n)")
                if start.lower() == "y":
                    print("Starting...")
                    startloop = False
                    break
                elif start.lower() == "n":
                    print("Okay. Exiting...")
                    exit()
                else:
                    print("Invalid command.")
            except KeyboardInterrupt:
                exit()
                break


        @client.event
        async def on_ready():
            print("-------")
            print("Logged in as " + client.user.name + ": ")#Bot Name
            print(client.user.id)#Bot User ID
            print("-------")
            global tstzne
            global tstzne_authr
            global secretmode
            await client.change_presence(game=discord.Game(name='Say `help'))
            tstzne = False
            tstzne_authr = []
            secretmode = False
            global bugconfirm
            global bugedition
            print("Information:\nBanned members: " + str(banned))
            print("-------")
            if debug == True:
                print("Debuggers: " + str(testors))
            else:
                return
            print("-------")
            await debug("Bot is now online.")




        @client.event
        async def on_message(message):
            global tstzne
            global tstzne_authr
            global secretmode
            global begin_db
            global responce_db
            global swears

            uinput = message.content #variable in actual tuesday (below was copied)
            channel = message.channel
            author = message.author
            bot = client.user
            botID = bot.id
            authorID = author.id


            try:
                if authorID in banned or allbanned == True:
                    return

                if authorID not in testors and debug == True:
                    return

                elif uinput.startswith(".`") or uinput.startswith(".~") or uinput.startswith(".``"):
                    await client.send_message(message.channel, "Remember, when trying to use my commands, delete the '.'!")

                elif uinput.startswith("```"):
                    return

                elif authorID == botID:
                    return

                elif message.author.bot:
                    return

                for item in swears:
                    print(item)
                    print(str(swears))
                    if item in uinput.lower():
                        await client.delete_message(message)
                        await send(channel, "<@!" + authorID + "> Please don't swear.")
                        return



                #elif authorID == "356474528655867905":
                #   return

                if authorID == "155103255993647104":
                    robotgif = random.choice(["https://www.technologyreview.com/i/images/robot.fallx392.gif", "http://4.bp.blogspot.com/-_rwfpbwpHTs/Vf_5UX_Kw4I/AAAAAAAAUDs/qLHX51tld34/s1600/robot-breaking-through-door.gif", "https://i.imgur.com/9SKc6D9.gif", ])
                    await send(author, robotgif)

                elif uinput.lower().startswith("hey tuesday") or uinput.startswith("`chat"):
                    while 1:
                        if message.author.id == client.user.id:
                            return
                        else:
                            await main(message)
            #      await send(channel, "This command has been put on hold for the time being. Please check back later.")

            # Now here is where one can add the new commands.
         # fine HEY GRIFFIN ARE YOU HERE
                elif "overwatch" in uinput.lower() and "not" in uinput.lower() and "sport" in uinput.lower() and message.server.id in personal:# GRIFFIN ARE YOU HERE
                    await send(channel, "Yes, it is!")

                elif "esport" in uinput.lower() and "not" in uinput.lower() and "sport" in uinput.lower() and message.server.id in personal:
                    await send(channel, "Yes, they are!")

                elif "overwatch" in uinput.lower() and "bad" in uinput.lower() and message.server.id in personal:
                    await send(channel, "No! It's very good!")

                elif "esport" in uinput.lower() and "bad" in uinput.lower() and message.server.id in personal:
                    await send(channel, "No! They're very good!")

                elif uinput.lower() == "`announce" and message.server.id in personal:
                    server = smtplib.SMTP('smtp.gmail.com' , 587)

                    server.ehlo()
                    server.starttls()

                    server.login("tuesdayybot@gmail.com", "TuesdayBottttt")

                    await send(channel, "What do you wish to announce?")
                    msg = await client.wait_for_message(timeout=50, author=author, channel=channel)
                    if msg is None:
                        return
                    elif msg == "cancel":
                        return
                    announcement = msg.content
                    print(announcement)
                    u = unicode(announcement, "utf-8")

                    for i in phonenumbers:
                        print(i)
                        server.sendmail("tuesdayybot@gmail.com", str(i), str(u))
                        print("Sent: " + u)


                elif uinput.lower() == "`collect":
                    global needReset
                    global jsonData
                    global collectioned
                    global collected
                    global resetOW
                    global resetRL
                    global canCollects
                    needReset = False
                    jsonData = ""
                    resetOW = []
                    resetRL = []
                    try:
                        xname = "2SDAYcanCollect"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    """canCollects = json.loads(jsonData)
                    print(str(canCollects))
                    try:
                        originalT = canCollects[authorID]
                        print("no error")
                    except KeyError:
                        originalT = 0
                        print("error")

                    print(originalT)
                    actTime = datetime.datetime.now()
                    print(actTime)
                    diff = datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
                    print(diff)
                    if diff > 0:
                        timeleft = diff / 60
                        await send(channel, "You can't collect any more cards yet. You have " + str(timeleft) + " left.")
                        return"""

                    try:
                        xname = "tusedayCollection"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    authorcollection = json.loads(jsonData)

                    game = random.choice(["ow", "rl"])



                    if game == "ow":
                        collected = random.choice(OWcollection)
                    else:
                        collected = random.choice(RLcollection)

                    for item in OWcollection:
                        try:
                            if item + " x5" in authorcollection[authorID]:
                                resetOW.append("*")
                        except KeyError:
                            pass
                    for item in RLcollection:
                        try:
                            if item + " x5" in authorcollection[authorID]:
                                resetRL.append("*")
                        except KeyError:
                            pass
                    if len(resetOW) == len(OWcollection) and len(resetRL) == len(RLcollection):
                        needReset == True

                        #collectioned = True
                    #  + " x5"
                       # await send(channel, "You are out of things to collect. Reset with ``resetinv`.")
                        #needReset = True
                        #collectioned = True
                    if game == "ow":
                        collectedpic = OWcollectionpics[collected]
                    else:
                        collectedpic = RLcollectionpics[collected]
                    if needReset != True:
                        if game == "rl":
                            await send(channel, "You got a **" + collected + "**! \n" + str(collectedpic))
                        else:
                            await send(channel, "You got a **" + collected + "** card! \n" + str(collectedpic))
                    else:
                        await send(channel, "You need to fuse your cards (`fuse), or reset your inventory (`resetinv).")

                    try:
                        authorcollection[authorID].append(collected)
                        """if collected in authorcollection[authorID]:
                            authorcollection[authorID].remove(collected)
                            authorcollection[authorID].append(collected + " x2")
                        elif collected + " x2" in authorcollection[authorID]:
                            authorcollection[authorID].remove(collected + " x2")
                            authorcollection[authorID].append(collected + " x3")
                        elif collected + " x3" in authorcollection[authorID]:
                            authorcollection[authorID].remove(collected + " x3")
                            authorcollection[authorID].append(collected + " x4")
                        elif collected + " x4" in authorcollection[authorID]:
                            authorcollection[authorID].remove(collected + " x4")
                            authorcollection[authorID].append(collected + " x5")
                        elif collected + " x5" in authorcollection[authorID]:
                            await send(channel, "Error. Something went dreadfully wrong.")
                        else:
                            authorcollection[authorID].append(collected)"""

                    except KeyError:
                        authorcollection[authorID] = [collected]


                    ToJson = json.dumps(authorcollection)

                    xname = "tusedayCollection"
                    file = open(xname + ".txt","w")
                    file.write(ToJson)
                    file.close()


                    collectioned = False
                    """canCollects[authorID] = datetime.datetime.now()

                    ToJson = json.dumps(canCollects)

                    xname = "2SDAYcanCollect"
                    file = open(xname + ".txt","w")
                    file.write(ToJson)
                    file.close()"""


            #










                elif uinput.lower() == "`inv" or uinput.lower() == "`inventory":
                    global jsonData

                    try:
                        xname = "tusedayCollection"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    authorcollection = json.loads(jsonData)

                    try:
                        authorINV = authorcollection[authorID]
                        authorINV = str(authorINV)
                        authorINV = authorINV.replace("[","")
                        authorINV = authorINV.replace("]","")
                        await send(channel, authorINV)
                    except KeyError:
                        await send(channel, "You don't have an inventory.")

                elif uinput.lower() == "`resetinv":
                    global jsonData

                    try:
                        xname = "tusedayCollection"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    authorcollection = json.loads(jsonData)
                    try:
                        del authorcollection[authorID]
                        await send(channel, "Inventory reset.")
                    except KeyError:
                        await send(channel, "You never had an inventory.")
                    ToJson = json.dumps(authorcollection)

                    xname = "tusedayCollection"
                    file = open(xname + ".txt","w")
                    file.write(ToJson)
                    file.close()


                elif uinput.lower().startswith("`fuse"):
                    global fuserl
                    global fuseow
                    global jsonData
                    global fuseAble
                    global fusey
                    fuserl = False
                    fuseow = False
                    fusey = []
                    fuseAble = False

                    try:
                        xname = "tusedayCollection"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    authorcollection = json.loads(jsonData)

                    if uinput.lower() == "`fuse":
                        await send(channel, "What pack do you wish to fuse? (two letter form)")
                        fusing = await client.wait_for_message(timeout=40, author=author, channel=channel)
                        if fusing is None:
                            await send(channel, "Operation timed out.")
                        elif fusing.content.lower() == "cancel":
                            await send(channel, "Operation canceled.")
                        elif fusing.content.lower() == "rl":
                            fuserl = True
                        elif fusing.content.lower() == "ow":
                            fuseow = True
                        else:
                            await send(channel, "That is not a proper pack.")

                        fusey = []
                        if fuserl == True:
                            try:
                                for item in authorcollection[authorID]:
                                    if item in RLcollection:
                                        fusey.append("*")
                            except KeyError:
                                await send("You can't fuse that pack yet.")
                            if len(fusey) == len(RLcollection):
                                fuseAble = True


                            if fuseAble == True:
                                print("Good.")
                                await send(channel, "You gained a __**Rocket League Pack**__!")
                                authorcollection[authorID].append("**Rocket League Pack**")
                                for item in authorcollection[authorID]:
                                    if item in RLcollection:
                                        authorcollection[authorID].remove(item)
                                        print(item)
                                        print(str(authorcollection[authorID]))


                            else:
                                await send(channel, "You can't fuse that pack yet.")

                        elif fuseow == True:
                            try:
                                for item in authorcollection[authorID]:
                                    if item in OWcollection:
                                        fusey.append("*")
                            except KeyError:
                                await send("You can't fuse that pack yet.")
                            if len(fusey) == len(OWcollection):
                                fuseAble = True


                            if fuseAble == True:
                                print("able")


                            else:
                                await send(channel, "You can't fuse that pack yet.")




                        ToJson = json.dumps(authorcollection)

                        xname = "tusedayCollection"
                        file = open(xname + ".txt","w")
                        file.write(ToJson)
                        file.close()


                elif uinput.lower() == "``fillinv":
                    try:
                        xname = "tusedayCollection"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    authorcollection = json.loads(jsonData)

                    await send(channel,"Filling...")
                    for item in OWcollection:
                        authorcollection[authorID].append(item)
                    for item in RLcollection:
                        authorcollection[authorID].append(item)


                    ToJson = json.dumps(authorcollection)

                    xname = "tusedayCollection"
                    file = open(xname + ".txt","w")
                    file.write(ToJson)
                    file.close()

                if uinput.lower() == "`shop":
                    print("gotten")
                    global shopinfo
                    try:
                        print("working")
                        xname = "tusedayShop"
                        file = open(xname + ".txt", "r")
                        jsonData = file.read()
                        print("recieved")
                        file.close()
                    except FileNotFoundError:
                        print("Error, Load File Not Found")

                    shopinfo = jsonData
                    if shopinfo == {}:
                        anyshop = False
                    else:
                        anyshop = True

                    if anyshop == True:
                        print("There's a shop!" + str(shopinfo))
                    else:
                        print("There's no shop!")

                    ToJson = json.dumps(shopinfo)

                    xname = "tuesdayShop"
                    file = open(xname + ".txt","w")
                    file.write(ToJson)
                    file.close()








                if uinput.lower() == "`department" or uinput.lower() == "`discord":
                    await send(channel, "**Join the Department!**\nhttps://discord.gg/TjWzXZN.")

                elif uinput.lower() == "`github":
                    await send(channel, "Here's my source code: \nhttps://github.com/Lionclaw49/Project_Tuesday.")















                elif uinput.lower() == "`sam" and message.server.id in personal:
                    await send(channel, "The best human in the entire world. Basically a god.")

                elif uinput.lower() == "`griffin" and message.server.id in personal:
                    await send(channel, "Don't talk to me about him. He's too annoying.")



                elif uinput.lower().startswith("`define"):
                    uinput = uinput.replace("`define ", "")
                    if uinput.lower() == "sam" and message.server.id in personal:
                        await send(channel, "{'Noun': ['the supernatural being conceived as the perfect and omnipotent and omniscient originator and ruler of the universe; the object of worship in monotheistic religions', 'any supernatural being worshipped as controlling some part of the world or some aspect of life or who is the personification of a force', 'a man of such superior qualities that he seems like a deity to other people', 'a material effigy that is worshipped']}")
                    elif uinput.lower() == "tuesday":
                        await send(channel, "{'Bot': ['a simply amazing bot that can do a whole lot of things', 'probably the best bot in the history of the world', --- \nHey, wait a minute, this is talking about *me*!")
                    elif uinput.lower() == "greatness" and message.server.id in personal:
                        await send(channel, "{'Noun': ['something that the great god sam achieved', 'the property possessed by something or someone of outstanding importance or eminence', 'unusual largeness in size or extent or number']}")
                    elif uinput.lower() == "griffin" and message.server.id in personal:
                        await send(channel, "Don't talk to me about him. He's too annoying.")
                    else:
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

                elif uinput.lower() == "`dancehotdog":
                    await send(channel, "https://media.giphy.com/media/l1K9Dcy7ww0CW3JHq/source.gif")

                elif uinput.lower() == "`hotdogman":
                    await send(channel, '''⢀⠠⡣⡑⡜⣜⢮⣳⡣⣯⡳⣝⣞⡼⡔⡄⠨⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⡢⡆⡇⡇⢎⢮⡳⣝⣞⢮⣗⢽⣣⡗⡽⡽⣕⡇⡜⢔⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⢕⢵⢹⣪⢪⢊⠎⡞⡼⣕⡗⣽⢪⡟⡼⡽⣽⢪⡗⣽⢸⠘⡜⡕⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡅⡣⢣⢣⢇⢇⢅⢣⢹⢪⠧⡯⣳⢹⣪⣻⢼⣳⡹⣪⠳⣕⠱⡘⢜⢜⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢌⠢⢣⠱⢀⠃⡜⡸⡱⡝⣼⣳⢽⣺⢪⣗⢧⣟⢼⣣⢳⠨⢐⠅⢇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠐⠨⠐⡐⡜⡜⣜⢕⣗⢽⢽⡺⣽⡪⣗⣗⢽⣪⢪⠈⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⢣⢫⢪⡎⡆⡣⢪⢸⢸⢸⢱⡙⠩⡻⣼⡣⣟⢾⢼⢑⠑⡇⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⠰⡱⢱⠱⠩⢃⢣⢫⢪⠢⡱⡱⡹⡜⡦⡴⣜⢷⣝⢧⢯⣳⢢⡪⡪⢢⢳⡀⠀⠀⠀⠀⠀⢀⢠⣪⢫⢝⢧⢳⣢⡀⠀
            ⠀⠀⠀⠀⠀⠀⢄⡃⡂⠢⡈⠪⢈⠔⡕⡎⡎⡌⡎⡎⢯⢽⣝⠧⢟⢮⢯⣳⠳⡝⡎⡎⠬⡪⡎⡄⠀⠀⢀⢀⠆⡇⢷⢱⠁⡃⠃⢇⠃⠀
            ⠀⠀⠀⠀⠀⠘⢔⠨⢂⢑⢠⢵⣻⣎⢪⢝⢖⠌⡎⡎⣗⢽⣺⣢⢡⣈⣈⡠⡼⣜⢕⠅⢝⢜⡕⣷⣰⢰⢱⢑⢈⠀⡁⠐⠀⠂⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠍⢜⠘⡌⠢⣝⣗⣗⣟⡆⡝⣺⠨⡪⡪⣎⡗⡷⣝⣗⣗⢧⣟⢼⣣⢳⠁⡇⣗⢕⢷⡕⢕⠨⡂⠅⠃⠂⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠘⠠⡑⠠⣝⡞⡾⣼⣳⣇⢣⢳⡑⢜⢜⡜⡽⣽⢺⣺⣪⡗⣽⢣⢗⡕⢱⢸⢸⢪⣟⡎⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢔⡜⣞⡼⡺⣝⣞⣞⡗⡌⢮⢪⠸⡸⣜⢽⡺⡣⡣⣳⡫⣗⢯⡳⡱⠡⡪⡣⡻⣮⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⢜⡞⡼⣝⡞⣼⣳⡫⡂⢏⢎⠪⡪⡎⡗⡕⡇⣽⢺⢮⣳⣽⡟⡎⠜⡜⡌⣟⣮⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢣⢳⢝⡞⡼⣝⣞⡮⣗⠡⡫⡪⡊⢮⢝⢜⢜⢜⢷⢽⢽⣺⣟⢽⡘⠌⣞⠸⡵⣳⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢽⢸⡣⣏⡟⣼⣪⢿⢜⠄⡇⡗⡸⣨⢳⢕⢕⢭⢳⢽⢝⣞⣗⡗⡕⢡⢇⢝⢽⣺⡊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⢧⡫⣞⢼⣹⢺⢮⢯⣓⠌⢎⢎⠜⡜⣮⢻⣔⢕⢕⢽⣣⢗⡗⣯⡊⡜⡜⣜⢽⣺⡊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠘⢼⢜⢮⢳⡳⡽⡽⣧⣓⠨⢣⢣⠣⡣⡗⣽⢺⡪⡪⡺⣜⣗⢽⡗⡆⡪⡪⡪⣗⣗⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⡎⣗⡝⡧⣏⡯⣟⣞⢖⢑⢕⢕⢱⢩⡝⣷⢹⢜⢜⡼⣕⣗⣿⣛⢆⢪⠪⡮⣗⣗⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠠⡹⡜⣎⡟⣼⢺⢷⣝⣇⠢⡣⡣⡱⡱⡝⡎⡮⡪⣞⢮⣳⣿⢳⡣⡣⢸⠪⡮⣗⣗⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢇⢯⢧⢯⣳⣫⣟⡞⣖⠡⡣⡣⡪⡪⣇⢇⢧⢻⢼⡝⣾⣻⡳⣝⠔⢕⢕⢽⣺⣺⡪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢣⢻⢼⡕⣗⣗⣯⢿⣜⠘⡜⡎⡜⡜⣦⢃⢏⢽⢪⣟⢼⢧⣟⢼⠨⢕⢕⢽⣺⡺⣎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢕⢕⡗⡽⣺⢺⡮⡿⣜⡘⢼⢸⢸⢸⡪⣗⡕⡕⢽⢜⣗⢽⣳⣝⠌⡇⡇⣟⢮⣟⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠘⡕⣝⢽⢺⢽⢯⣟⣎⠆⡝⣜⢸⢸⡪⣗⡗⡇⡧⣹⢪⡗⣷⣳⠡⡣⡣⡫⡿⣼⣓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠈⢕⢧⡫⣏⢯⣟⡾⣜⢌⢎⢎⢜⢜⢮⣳⢫⡣⡣⡣⣟⣾⣿⢕⢅⢣⢣⢫⡟⣾⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢣⢣⢻⢼⢽⣪⣟⡖⡄⡫⡪⢢⢳⡱⡱⢱⠱⣵⢹⢧⡳⣕⢗⠄⢣⠣⢧⢯⣳⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢝⡜⡮⣳⢳⣣⡓⢌⢜⢢⢡⢣⡣⡫⢧⡻⣜⢽⡚⡞⡮⡪⠨⡘⢌⢗⢧⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⣝⢜⢧⣓⠂⢕⣂⠢⡱⢱⢸⢱⢣⡫⣪⢳⢹⢪⢪⡞⣖⠨⠊⠇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠸⡸⡮⣟⡮⣗⠈⠌⠘⠸⠘⠜⠘⠸⡸⡪⣗⢽⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢮⢯⡗⣯⡳⠀⠀⠀⠀⠀⠀⠀⠀⡇⡗⡷⣝⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⣗⢧⡟⣮⡊⠀⠀⠀⠀⠀⠀⠀⠠⡸⢸⢸⢸⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡰⡱⡱⡱⡣⡫⡪⡂⠀⠀⠀⠀⠀⠀⠀⡐⡜⢌⢎⢎⢎⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⢣⢯⡞⣼⣸⣸⢪⡪⡆⠀⠀⠀⠀⠀⠀⠨⡪⣎⢮⢮⢮⣳⣳⢳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠯⢳⢕⠗⡏⠚⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠌⠳⠹⠸⠪⠓''')





                elif uinput.lower() == "`meme" and message.server.id in personal:
                    memecheck = []
                    while len(memecheck) < 3:
                        print(memecheck)
                        await send(channel, "dank meme")
                        print(author)
                        meme = await client.wait_for_message(timeout=30, author="Ethan 2.0#8892", channel=channel)
                        if meme is None:
                            memecheck.append(".")
                            print("added")






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

                    if song.lower() == "mouton noir" and message.server.id in personal:
                        await send(channel, """Baa baa mouton noir
As-tu de la laine?
Oui monsieur, oui monsieur,
Trois poches pleines
Une pour mon maître,
et une pour madame
Une pour les enfants
Qui jouent au ratatam.""")
                        return

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



                #elif uinput.lower().startswith("`edit") and authorID == "177831674367836160":
                 #   await client.delete_message(message)
                  #
                   # async for message in client.logs_from(channel, limit=1):
                    #   print(message.content)
#
 #             uinput.replace("`edit ", "")
#
 #             print(uinput)
#
 #             await client.edit_message(message, new_content=uinput)















                elif uinput.lower().startswith("`trending"):
                    if uinput.lower() == "`trending":
                        url1 = 'http://www.tweeplers.com/hashtags/?cc=WORLD'
                        browser = webdriver.Chrome() # setting the browswer type

                        browser.get('http://www.tweeplers.com/hashtags/?cc=WORLD') # accessing the webpage

                        twitter1 = browser.find_element_by_id("item_u_1") # finding the id of the element1
                        twitter2 = browser.find_element_by_id("item_u_2") # finding the id of the element2
                        twitter3 = browser.find_element_by_id("item_u_3") # finding the id of the element3
                        twitter4 = browser.find_element_by_id("item_u_4") # finding the id of the element4
                        twitter5 = browser.find_element_by_id("item_u_5") # finding the id of the element5
                        twitter6 = browser.find_element_by_id("item_u_6") # finding the id of the element6
                        twitter7 = browser.find_element_by_id("item_u_7") # finding the id of the element7
                        twitter8 = browser.find_element_by_id("item_u_8") # finding the id of the element8
                        twitter9 = browser.find_element_by_id("item_u_9") # finding the id of the element9
                        twitter10 = browser.find_element_by_id("item_u_10") # finding the id of the element10

                        await send(channel, "The top trending hashtags on Twitter currently are: \n" + twitter1.text + "\n" + twitter2.text + "\n" + twitter3.text + "\n" + twitter4.text + "\n" + twitter5.text + "\n" + twitter6.text + "\n" + twitter7.text + "\n" + twitter8.text + "\n" + twitter9.text + "\n" + twitter10.text)

                        browser.quit()
                    else:
                        await send(channel, "This might take a second.")
                        uinput = uinput.replace("`trending ","")
                        forr = []
                        top = []
                        idk = []
                        if int(uinput) < 20:
                            while len(forr) < int(uinput):
                                forr.append("*")
                                url1 = 'http://www.tweeplers.com/hashtags/?cc=WORLD'
                                browser = webdriver.Chrome() # setting the browswer type
                                browser.get('http://www.tweeplers.com/hashtags/?cc=WORLD')
                                twitterr = browser.find_element_by_id("item_u_" + str(len(forr)))
                                 # accessing the webpage
                                top.append(twitterr.text)
                                print(top)
                                browser.quit()
                                topped = str(top).replace("['", "")
                                topped = topped.replace("']", "")
                                if len(top) > 1:
                                    topped = topped.replace("'", "")

                            await send(channel, "The top " + uinput + " trending hastags on Twitter currently are: \n" + str(topped))
                        else:
                            await send(channel, "The maximum top trending hashtags go up to 20.")









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
                                await send(channel, condition.temp())
                            except (KeyError, AttributeError):
                                await send(channel, "Please enter at proper city.")
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

                elif uinput.lower() == "`ezpoll":
                    epollalts = False
                    epollttl = input("What do you want your poll to be on? At any point in this process, 'cancel' will stop the whole thing.\n")
                    if epollttl.lower() == "cancel":
                        print("Operation canceled.")
                        return


                    epollalt = []
                    while epollalts == False:
                        epollaltin = input("Please enter the choices for the poll, then once you are finished type 'done'.")
                        if epollaltin.lower() == "cancel":
                            print("Operation canceled.")
                            return
                        elif epollaltin.lower() != "done":
                            epollalt.append(epollaltin)
                        else:
                            epollalts = True
                    epollaltnum = len(epollalt)
                    if epollaltnum > 10:
                        print("You have too many choices. Please split up the poll.")
                        return
                    elif epollaltnum < 1:
                        print("You have two few choices.")
                        return

                    print("The poll is now finshed.")
                    epollrktn = {1 : "\U00000031\U000020E3", 2 : "\U00000032\U000020E3", 3 : "\U00000033\U000020E3", 4 : "\U00000034\U000020E3", 5 : "\U00000035\U000020E3", 6 : "\U00000036\U000020E3", 7 : "\U00000037\U000020E3", 8 : "\U00000038\U000020E3", 9 : "\U00000039\U000020E3", 10 : "\U0001F51F"}
                    epollrktn2 = {1 : ":one:", 2 : ":two:", 3 : ":three:", 4 : ":four:", 5 : ":five:", 6 : ":six:", 7 : ":seven:", 8 : ":eight:", 9 : ":nine:", 10 : ":keycap_ten:"}
                    await send(channel, epollttl)
                    for i in range(epollaltnum):
                        await send(channel, epollrktn2[i+1] + " - "+ epollalt[i])
                    epollcat = await client.send_message(channel, "Hey @everyone, take the poll!")
                    for i in range(epollaltnum):
                        await client.add_reaction(epollcat, epollrktn[i+1])

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
                        await client.send_message(message.channel, "Please confirm the your bug report: \nTitle: " + bugttl + "\nCommand: " + bugcmd + "\nDescription: " + bugdsc)
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


                elif uinput == "`suggest":
                    suggestdesc = ""
                    suggestdescloop = True
                    await client.send_message(message.channel, "What would you call the suggestion that you are submitting? Type 'cancel' if you wish to escape this operation.")

                    # the title of the suggestion
                    sgtttlwait = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                    if sgtttlwait is None:
                        await client.send_message(message.channel, "Operation timed out.")
                        return
                    elif sgtttlwait.content == "cancel":
                        await client.send_message(message.channel, "Operation canceled.")
                        return

                    suggesthead = sgtttlwait.content


                    while suggestdescloop == True:
                        await send(channel, "Do you wish to add a description of this command? (y/n)")

                        sgtdescwait = await client.wait_for_message(timeout=30, channel=channel, author=author)
                        if sgtdescwait is None:
                            await client.send_message(message.channel, "Operation timed out.")
                            return

                        elif sgtdescwait.content == "n" or sgtdescwait.content == "no":
                            await client.send_message(message.channel, "The suggestion has been sent to the developer.")
                            print("\n\nSuggestion: \n---------------")
                            print(suggesthead)
                            suggestdescloop = False

                        elif sgtdescwait.content == "y" or sgtdescwait.content == "yes":
                            await send(channel, "What would you like to have as the description?")
                            sgtdesctrue = await client.wait_for_message(timeout=90, channel=channel, author=author)
                            if sgtdesctrue is None:
                                await send(channel, "Operation Timed out.")
                            elif sgtdesctrue.content == "cancel":
                                await send(channel, "Operation cancelled.")
                                return

                            suggestdesc = sgtdesctrue.content

                            await client.send_message(message.channel, "Description confirmed. The suggestion has been sent to the developer.")
                            print("\n\nSuggestion: \n---------------")
                            print(suggesthead)
                            print(suggestdesc)
                            suggestdescloop = False

                        else:
                            await send(channel, "Invalid Command. Please try again:")

#               await send(channel, "Thank you. The suggestion has been sent to the developer.")
#               if suggestdesc != "":
#                  print("You have a suggestion from:" + author)
#                  print(suggesthead)
#                  print(suggestdesc)
#               else:
#                  print("You have a suggestion from:" + author)
#                  print(suggesthead)
#                  print("There is no description of this command.")"""


                #elif message.author.id == "177831674367836160" and tstzne == True and tstzne_authr == message.author:
                #   await client.add_reaction(message, "🦊")

                elif uinput == "`secret-on" and message.author.id == "177831674367836160":
                    await client.delete_message(message)
                    secretmode = True

                elif uinput == "`secret-off" and message.author.id == "177831674367836160":
                    await client.delete_message(message)
                    secretmode = False

                elif secretmode == True:
                    print(message.author)
                    print(message.author.id)

                #elif uinput.lower().startswith("`github"):
                #   await client.send_message(message.channel, "Here's the github for my code: https://github.com/Lionclaw49/Project_Tuesday")

                elif uinput.startswith("`testing") and tstzne == True and message.author in tstzne_authr:
                    await client.send_message(message.channel, "It has worked.")

                elif uinput.lower().startswith("`translate"):
                    if uinput == "`translate":
                        await client.send_message(message.channel, "Please enter what is to be translated and if it is to go to another language, state the two letter version after the bleep.")
                    else:
                        translator = Translator()
                        languagee = uinput.replace("`translate ", "")
                        language2 = languagee.split(" ")
                        gtlanguages = ["af", "ach", "ak", "am", "ar", "az", "be", "bem", "bg", "bh", "bn", "br", "bs", "ca", "chr", "ckb", "co", "crs", "cs", "cy", "da", "de", "ee", "el", "en", "eo", "es", "es-419", "et", "eu", "fa", "fi", "fo", "fr", "fy", "ga", "gaa", "gd", "gl", "gn", "gu", "ha", "he", "haw", "hi", "hr", "ht", "hu", "hy", "ia", "id", "ig", "is", "it", "iw", "ja", "jw", "ka", "kg", "kk", "km", "kn", "ko", "kri", "ku", "ky", "la", "lg", "ln", "lo", "loz", "lt", "lua", "lv", "mfe", "mg", "mi", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "ne", "nl", "nn", "no", "nso", "ny", "nyn", "oc", "om", "or", "pa", "pcm", "pl", "ps", "pt-BR", "pt-PT", "qu", "rm", "rn", "ro", "ru", "rw", "sd", "sh", "si", "sk", "sl", "sn", "so", "sq", "sr", "sr-ME", "st", "su", "sv", "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "tt", "tum", "tw", "ug", "uk", "ur", "uz", "vi", "wo", "xh", "xx-bork", "xx-elmer", "xx-hacker", "xx-klingon", "xx-pirate", "yi", "yo", "zh-CN", "zh-TW", "zu"]
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
                                break
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
                    if uinput.lower() == "`sinsult tuesday" or uinput.lower().startswith("`sinsult " + "<@!415190531459776513>"):
                        config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
                        pref = 'Thee'
                        # algorithm simply makes a random choice from three different columns and concatenates them.
                        col1 = random.choice(config['column1'])
                        col2 = random.choice(config['column2'])
                        col3 = random.choice(config['column3'])
                        # print generated insult for the 'user'
                        await client.send_message(message.channel, "I'm not going to insult myself, " + pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '!')

                    else:

                        if uinput.lower() == "`sinsult": #code for general
                            config = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))
                            pref = 'Thee'
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

                elif uinput == "`Tuesday" or uinput == "``Tuesday":
                    await client.send_message(message.channel, "That's me!") #This is just a fun reference to an AI... If only...

                elif uinput.lower() == "worship kevvy" or uinput.lower() == "worship tevin" and message.server.id in personal:
                    await client.send_message(message.channel, "HAIL!") #WORSHIP TEVIN AND KEVVY

                elif uinput.lower() == "`clean":
                    delete_messages = []
                    async for m in client.logs_from(channel, limit=10):
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
                    await send(channel, ":white_check_mark:")

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
                    await client.send_message(message.author, """
Hi! I'm Tuesday, a personal assistant created by <@!177831674367836160>, I'm being updated all the time, so I'll try and keep this up to date. Here's my list of commands, you can use all of them with the backtick (`, It's the top left of most keyboards) before them:""")
                    await client.send_message(message.author, """
 - say -> This allows you to tell me what to say. You can also add tts by adding tts after the 'say'.
 - clean -> This clears my last 10 messages.
 - sinsult -> This sends a shakespearean insult.
 - bug -> This allows you to report a bug to the developer.
 - chat -> This allows you to chat with Tuesday. (currently disabled)
 - lyrics -> If you the song name, and the song artist, I can post the entire lyrics verse by verse.
 - suggest -> This command allows you to send the developer suggestions. And please do it for anything!
 - poll -> This allows you to create a poll with Tuesday.
 - forecast -> This sends a forcast for the week of the specified location.
 - roll -> This rolls a 6 sided die.
 - coinflip -> This flips a coin.
 - weather -> This gives you the weather in a specified location.
 - define -> This allows you to define something.
 - synonym -> This gives you a synonym of a word.
 - antonym -> This givs you an antonym of a word.
 - github -> This allows you to view the source code.
 - discord -> This allows you to join my help server!
 - collect -> This allows you to collect any car from Rocket League and any a card for any character in Overwatch.
 - inventory -> This allws you to see your inventory for the collect command.
 - fuse -> This allows you to fuse your cards into a certain type of pack.
 - trending -> This allows you to get the top trending hashtags off of twitter. (any number after it up to 20 or nothing is 10.)
 - translate (dest) -> This allows you to translate any language into the destination language(dest), you need to specify the ISO 639-1 code form of the language first though.""")
                    await client.send_message(message.author, """
Also, anything with  double backticks will pull a wikipedia article, while anything with a tilda (~) will pull wolframalpha (Math).
There are also a lot of hidden commands, have fun trying to find them!""")

                elif uinput.lower().startswith("`mime") and 1 == 2:
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
                #      uinput = uinput.split(" ")
                #      uinput = " ".join(uinput[2:])
                        uinput = uinput.replace("``", "")#getting rid of ``
                        if uinput.lower() == "tidepod" or uinput.lower() == "tide pod" and message.server.id in personal:
                            await send(channel, "Mmmmmmmm... Tasty.... Right here's your info.")
                        try:
                            answer = wikipedia.summary(uinput, chars=1900)#shortening the code below
                            await client.send_message(message.channel, answer)#sending answer
                        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e: #:)
                            await client.send_message(message.channel, e,)
                        #except wikipedia.exceptions.PageError as r:
                        #   print("Error caught!")
                        #   await client.send_message(message.channel, r)
            except KeyboardInterrupt:
                print("Exiting the program.\n")
            except TimeoutError:
                print("Timed out. Now trying again.\n")

            preMessage = message.content
        #
        #
        #
        try:
            client.run("Tuesday's Token")
        finally:
            client.close()
    except TimeoutError:
        print("Timed out. Now trying again.")


    except OSError:
        print("The network connection has been lost. Now trying to reconnect.")

    except KeyboardInterrupt:
        print("Exiting....")
      #I have my bot token there, so you would have to replace it with yours. The instructions for that are below..
      #On the Discord Developers website, you have to create an bot id for it. Then you get the token, paste it above. Then add it to your server!
      #Have fun!
