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


async def debug(content):
    if debug:
        print("Debug Message: " + content)

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
        await client.send_message(channel, "Error, Load File Not Found")

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
    global swearchecke
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
        await client.send_message(channel, "Error, Load File Not Found")

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
            presettings[message.server.id].remove("sw0")
        else:
            swearcheck = False
            presettings[message.server.id].remove("sw1")
        if swearcheck == True:
            presettings[message.server.id].append("sw1")
        else:
            presettings[message.server.id].append("sw0")
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
        channel = discord.utils.find(lambda c: c.name == "join-log", member.server.channels)
        await client.send_message(channel, "<@!" + str(member.id) + "> has left " + member.server.name + ".")
        return
    except:
        channel = discord.utils.find(lambda ch: ch.name == "general", member.server.channels)
        try:
            msg = await client.send_message(channel, "There is no join log for me to send a leave message. Add a thumbs up for me to create one.")
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
