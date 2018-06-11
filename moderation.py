# This is for the moderation subsection of Tuesday.

# imports
import discord #adds discord
import os
import sys
import json
import wikipedia #adds wikipedia's api
import wolframalpha #adds wolframalpha's api
import random
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


async def debug(content):
    if debug == True:
        print("Debug Message: " + content + str(datetime.datetime.now()))

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


async def prune(client, message):
    authorus = ""
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    authorID = message.author.id
    if uinput.lower() == "`prune":
        await client.send_message(channel, "You need to add a number and an author.")
    elif uinput.lower() != "`prune":
        uinput = uinput.replace("`prune ","")
        if uinput.isnumeric():
            await client.send_message(channel, "You need to add an author or say 'all'.")
        elif uinput.isalpha():
            await client.send_message(channel, "You need to add a number.")
        else:
            await client.delete_message(message)
            uinput = list(uinput.split(" "))
            print(str(uinput))
            if uinput[0].lower() == "all":
                authorus = ""
            elif uinput[0].startswith("<@!") and uinput[1].endswith(">"):
                authorus = uinput[0].replace("<@!","")
                authorus = authorus.replace(">","")
            else:
                await client.send_message(channel, "Invalid Subject.")
            if int(uinput[1]) < int("1"):
                await client.send_message(channel, "Invalid Number")
            delete_messages = []
            async for m in client.logs_from(channel, limit=int(uinput[1])):
                if authorus == "":
                    delete_messages.append(m)
                elif m.author.id == authorus:
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
            await client.send_message(channel, uinput[0] +  " messages have been deleted.")

async def clean(client, message): #soon to be added with purge/prune
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    authorID = message.author.id
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
    await client.send_message(message.channel, ":white_check_mark:")

async def swearchecker(client, message):
    try:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt","w")
        file.write("{" + "}")
        jsonData = "{message.server.id : 'jl1','sc1'}"
        file.close()

    presettings = json.loads(jsonData)
    try:
        if "sc0" in presettings[message.server.id]:
            return
        elif "sc1" in presettings[message.server.id]:
            pass
        else:
            presettings[message.server.id] = []
            presettings[message.server.id].append("jl1")
            presettings[message.server.id].append("sc1")
    except KeyError:
        presettings[message.server.id] = []
        presettings[message.server.id].append("jl1")
        presettings[message.server.id].append("sc1")
    authorID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@!" + authorID + "> Please don't swear.")
    return

async def settings(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    authorID = message.author.id
    swc = ""
    jnl = ""

    try:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt","w")
        file.write("{" + "}")
        file.close()

    presettings = json.loads(jsonData)

    try:
        if "jl1" in presettings[message.server.id]:
            jnl = "On"
        elif "jl0" in presettings[message.server.id]:
            jnl = "Off"
    except KeyError:
        presettings[message.server.id] = []
        presettings[message.server.id].append("jl1")
        presettings[message.server.id].append("sc1")
        jnl = "On"

    if "sc1" in presettings[message.server.id]:
        swc = "On"
    elif "sc0" in presettings[message.server.id]:
        swc = "Off"


    contentz = "Join Log == " + jnl + "\nSwear Checker == " + swc + "."
    em = discord.Embed(title='Settings', description=contentz, colour=0xDEADBF)

    em.set_author(name='Tuesday', icon_url=client.user.default_avatar_url)

    await client.send_message(message.channel, embed=em)

async def toggle(client, message):
    global swearchecker
    global joinlog
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    authorID = message.author.id

    uinput = uinput.replace("`toggle ","")

    try:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        xname = "2sdaySETTINGS"
        file = open(xname + ".txt","w")
        file.write("{" + "}")
        file.close()

    presettings = json.loads(jsonData)

    try:
        if "jl1" in presettings[message.server.id]:
            joinlog = True
        elif "jl0" in presettings[message.server.id]:
            joinlog = False
        else:
            presettings[message.server.id] = []
            presettings[message.server.id].append("jl1")
            presettings[message.server.id].append("sc1")
            joinlog = True
    except KeyError:
        presettings[message.server.id] = []
        presettings[message.server.id].append("jl1")
        presettings[message.server.id].append("sc1")
        joinlog = True

    if "sc1" in presettings[message.server.id]:
        swearcheck = True
    elif "sc0" in presettings[message.server.id]:
        swearcheck = False


    if uinput.lower() == "joinlog":
        await client.send_message(channel, "Toggled Join Log.")
        if joinlog == False:
            joinlog = True
            presettings[message.server.id].remove("jl0")
        else:
            joinlog = False
            presettings[message.server.id].remove("jl1")
        if joinlog == True:
            presettings[message.server.id].append("jl1")
        else:
            presettings[message.server.id].append("jl0")
    elif uinput.lower() == "swearchecker" or uinput.lower() == "swear checker":
        await client.send_message(channel, "Toggled Swear Checker.")
        if swearcheck == False:
            swearcheck = True
            presettings[message.server.id].remove("sc0")
        else:
            swearcheck = False
            presettings[message.server.id].remove("sc1")
        if swearcheck == True:
            presettings[message.server.id].append("sc1")
        else:
            presettings[message.server.id].append("sc0")
    else:
        await client.send_message(channel, "That is not a togglable setting.")



    ToJson = json.dumps(presettings)

    xname = "2sdaySETTINGS"
    file = open(xname + ".txt","w")
    file.write(ToJson)
    file.close()

async def join(member, client):
    try:
        channel = discord.utils.find(lambda c: c.name == "join-log", member.server.channels)
        await client.send_message(channel, "Welcome <@!" + str(member.id) + "> to " + member.server.name + ".")
        return
    except:
        channel = discord.utils.find(lambda ch: ch.name == "general", member.server.channels)
        try:
            msg = await client.send_message(channel, "There is no join log for me to send a join message. Add a thumbs up for me to create one.")
            await client.add_reaction(msg, "👍")
            await client.add_reaction(msg, "👎")
            responce = client.wait_for_reaction(["👍", "👎"],message=msg,timeout=30)
            if responce.reaction.emoji == "👍":
                await client.create_channel(member.server, 'join-log', type=discord.ChannelType.text)
                channel = discord.utils.find(lambda c: c.name == "join-log", member.server.channels)
                await client.send_message(channel, "Welcome <@!" + str(member.id) + "> to " + member.server.name + ".")
                return
            elif responce.reaction.emoji == "👎":
                return
            else:
                return
        except:
            return

async def leave(member, client):
    try:
        await debug("Someone has left.")
        channel = discord.utils.find(lambda c: c.name == "join-log", member.server.channels)
        await debug("Found joinlog.")
        await client.send_message(channel, "<@!" + str(member.id) + "> has left " + member.server.name + ".")
        await debug("Sent leave message.")
        return
    except:
        await debug("No joinlog.")
        channel = discord.utils.find(lambda ch: ch.name == "general", member.server.channels)
        await debug("Looking for general")
        try:
            await debug("Found general.")
            msg = await client.send_message(channel, "There is no join log for me to send a leave message. Add a thumbs up for me to create one.")
            await debug("Sent message.")
            await client.add_reaction(msg, "👍")
            await client.add_reaction(msg, "👎")
            await debug("Added reactions.")
            responce = client.wait_for_reaction(["👍", "👎"],message=msg,timeout=60)
            if responce.reaction.emoji == "👍":
                await debug("Reaction: Positive.")
                await client.create_channel(member.server, 'join-log', type=discord.ChannelType.text)
                await debug("Created joinlog.")
                channel = discord.utils.find(lambda c: c.name == "join-log", member.server.channels)
                await debug("Found joinlog.")
                await client.send_message(channel, "<@!" + str(member.id) + "> has left " + member.server.name + ".")
                await debug("Sent leave message.")
                return
            elif responce.reaction.emoji == "👎":
                await debug("Reaction: Negative.")
                return
            else:
                await debug("Something went wrong.")
                return
        except:
            await debug("No general channel.")
            return
