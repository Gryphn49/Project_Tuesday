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
        await client.send_message(channel, "You can't collect any more cards yet. You have " + str(timeleft) + " left.")
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

    lyricss = PyLyrics.getLyrics(artist, song)
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
