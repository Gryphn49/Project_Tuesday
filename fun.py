import discord
import json
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
from urllib.request import quote
import re
from PyLyrics import *
from PyDictionary import PyDictionary
from selenium import webdriver
import smtplib
import sys
import datetime
import profanity.profanity
import urllib
from bs4 import BeautifulSoup

debug = False
debug = False #debug function
begin_db = ['hi', 'hey', 'hello', 'heyo', 'sup', 'whats up'] #beginning expressions (chat command)
personal = ["439204820243447818"] #for my personal servers
dictionary = PyDictionary() #define command
client = discord.Client() #EVERYTHING
weather = Weather() #weather command
banned = [] #banning people
bannedloop = True #banning loop
allbanned = False #to ban everyone
debugloop = False #debugging loop
collectioned = False #collection loop
testors = [] #debug testers loop
canCollects = {"177831674367836160": "0"} #collect command
authorcollection = {"Lionclaw49" : "No-thang"} #collect command

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
    "Zenyatta"
]
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
RLcollection = [
    "Backfire",
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
    "X-Devil Mk2"
]
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
    "X-Devil Mk2" : "https://vignette.wikia.nocookie.net/rocketleague/images/d/db/X-Devil_Mk2_body_icon.png/revision/latest?cb=20170523153541"
}

async def error(alert):
    msg = "Tuesday had an error: " + alert + " - " + datetime.datetime.now()

    xname = "2sdayALERTS"
    file = open(xname + ".txt", "r")
    jsonData = file.read()
    k = json.loads(jsonData)
    file.close()

    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login(k[0], k[1])
    server.sendmail(k[0], k[2], msg)

async def debug(content):
    if debug:
        print("Debug Message: " + content + str(datetime.datetime.now()))

async def sinsult(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
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

async def collect(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
        jsonDataa = file.read()
        file.close()
    except FileNotFoundError:
        await client.send_message(message.channel, "Error, The file wasn't found. This should never happen. Send the bot devs a message for a quick fix.")
        xname = "2SDAYcanCollect"
        file = open(xname + ".txt", "w")
        file.write("{" + "}")
        file.close()
        xname = "2SDAYcanCollect"
        file = open(xname + ".txt", "r")
        jsonDataa = file.read()
        file.close()


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
        await client.send_message(channel, "You can't collect any more cards yet. You have " + str(timeleft) + " left.")
        return"""


    try:
        xname = "tusedayCollection"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        await client.send_message(message.channel, "Error, The file wasn't found. This should never happen. Send the bot devs a message for a quick fix.")
        xname = "tusedayCollection"
        file = open(xname + ".txt", "w")
        file.write("{" + "}")
        file.close()
        xname = "tusedayCollection"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()

    authorcollection = json.loads(jsonData)
    print(str(authorcollection))
    game = random.choice(["ow", "rl"])
    print(game)


    if game == "ow":
        collected = random.choice(OWcollection)
    else:
        collected = random.choice(RLcollection)

    print(collected)

    # for item in OWcollection:
    #     try:
    #         if item + " x5" in authorcollection[authorID]:
    #             resetOW.append("*")
    #     except KeyError:
    #         pass
    # for item in RLcollection:
    #     try:
    #         if item + " x5" in authorcollection[authorID]:
    #             resetRL.append("*")
    #     except KeyError:
    #         pass
    # if len(resetOW) == len(OWcollection) and len(resetRL) == len(RLcollection):
    #     needReset == True
    if game == "ow":
        collectedpic = OWcollectionpics[collected]
    else:
        collectedpic = RLcollectionpics[collected]
    if needReset != True:
        if game == "rl":
            await client.send_message(channel, "You got a **" + collected + "**! \n" + str(collectedpic))
        else:
            await client.send_message(channel, "You got a **" + collected + "** card! \n" + str(collectedpic))
    else:
        await client.send_message(channel, "You need to fuse your cards (`fuse), or reset your inventory (`resetinv).")
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
            await client.send_message(channel, "Error. Something went dreadfully wrong.")
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

async def inventory(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
        await client.send_message(channel, authorINV)
    except KeyError:
        await client.send_message(channel, "You don't have an inventory.")

async def resetinv(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
        await client.send_message(channel, "Inventory reset.")
    except KeyError:
        await client.send_message(channel, "You never had an inventory.")

    ToJson = json.dumps(authorcollection)
    xname = "tusedayCollection"
    file = open(xname + ".txt","w")
    file.write(ToJson)
    file.close()

async def fuse(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
        await client.send_message(channel, "What pack do you wish to fuse? (two letter form)")
        fusing = await client.wait_for_message(timeout=40, author=author, channel=channel)
        if fusing is None:
            await client.send_message(channel, "Operation timed out.")
        elif fusing.content.lower() == "cancel":
            await client.send_message(channel, "Operation canceled.")
        elif fusing.content.lower() == "rl":
            fuserl = True
        elif fusing.content.lower() == "ow":
            fuseow = True
        else:
            await client.send_message(channel, "That is not a proper pack.")

        fusey = []
        if fuserl == True:
            try:
                for item in authorcollection[authorID]:
                    if item in RLcollection:
                        fusey.append("*")
            except KeyError:
                await client.send_message("You can't fuse that pack yet.")
            if len(fusey) == len(RLcollection):
                fuseAble = True


            if fuseAble == True:
                print("Good.")
                await client.send_message(channel, "You gained a __**Rocket League Pack**__!")
                authorcollection[authorID].append("**Rocket League Pack**")
                for item in authorcollection[authorID]:
                    if item in RLcollection:
                        authorcollection[authorID].remove(item)
                        print(item)
                        print(str(authorcollection[authorID]))


            else:
                await client.send_message(channel, "You can't fuse that pack yet.")

        elif fuseow == True:
            try:
                for item in authorcollection[authorID]:
                    if item in OWcollection:
                        fusey.append("*")
            except KeyError:
                await client.send_message("You can't fuse that pack yet.")
            if len(fusey) == len(OWcollection):
                fuseAble = True


            if fuseAble == True:
                print("able")


            else:
                await client.send_message(channel, "You can't fuse that pack yet.")




        ToJson = json.dumps(authorcollection)

        xname = "tusedayCollection"
        file = open(xname + ".txt","w")
        file.write(ToJson)
        file.close()

async def fillinv(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    try:
        xname = "tusedayCollection"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        print("Error, Load File Not Found")

    authorcollection = json.loads(jsonData)

    await client.send_message(channel,"Filling...")
    for item in OWcollection:
        authorcollection[authorID].append(item)
    for item in RLcollection:
        authorcollection[authorID].append(item)


    ToJson = json.dumps(authorcollection)

    xname = "tusedayCollection"
    file = open(xname + ".txt","w")
    file.write(ToJson)
    file.close()

async def shop(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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

async def meme(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    memecheck = []
    while len(memecheck) < 3:
        print(memecheck)
        await client.send_message(channel, "dank meme")
        print(author)
        meme = await client.wait_for_message(timeout=30, author="Ethan 2.0#8892", channel=channel)
        if meme is None:
            memecheck.append(".")
            print("added")

async def lyrics(client, message, personal):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    await client.send_message(channel, "Please enter a song name.")
    # wait for message
    song = await client.wait_for_message(timeout=60, channel=channel, author=author)
    if song is None:
        await client.send_message(message.channel, "Operation timed out.")
        return
    elif song.content.lower() == "cancel":
        await client.send_message(message.channel, "Operation canceled.")
        return
    song = song.content

    if song.lower() == "mouton noir" and message.server.id in personal:
        await client.send_message(channel, """Baa baa mouton noir
                            As-tu de la laine?
                            Oui monsieur, oui monsieur,
                            Trois poches pleines
                            Une pour mon maître,
                            et une pour madame
                            Une pour les enfants
                            Qui jouent au ratatam."""
        )
        return

    await client.send_message(channel, "Please enter a musical artist name.")
    # wait for message
    artist = await client.wait_for_message(timeout=60, channel=channel, author=author)
    if artist is None:
        await client.send_message(message.channel, "Operation timed out.")
        return
    elif artist.content.lower() == "cancel":
        await client.send_message(message.channel, "Operation canceled.")
        return
    artist = artist.content
    try:
        lyricss = PyLyrics.getLyrics(artist, song)
    except ValueError:
        await client.send_message(message.channel, "That song isn't in the database.")
    lyricss = lyricss.split("\n\n")
    for i in lyricss:
        await client.send_message(channel, i)

async def mime(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    if authorID == "356474528655867905":
        return
    if message.server.id == "367076093523656704":
        uinput = uinput.replace("`mime ", "")
        await client.send_message(discord.utils.find(lambda ch: ch.id == "399269109029797899", message.server.channels), author.mention + " said: \"" + uinput + "\" in " + channel.mention + ".")
        await client.delete_message(message)
        await client.send_message(message.channel, uinput)
    else:
        uinput = uinput.replace("`mime ", "")
        await client.delete_message(message)
        await client.send_message(message.channel, uinput)
        print("Tuesday mimed '" + uinput + "' for " + str(author))
