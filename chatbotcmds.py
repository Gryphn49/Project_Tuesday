import discord #adds discord
# you don't need this line import asyncio, aiohttp #allows the async
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
import json
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
    if debug:
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


def rempunc(s):
    return ''.join(c for c in s if c not in punctuation).lower()

async def sinput(inn):
    return rempunc(inn)

async def sout(out, client, message):
    await client.send_message(message.channel, out)

async def main(client, message):
    try:
        xname = "masterbot"
        file = open(xname + ".txt", "r")
        jsonData = file.read()
        file.close()
    except FileNotFoundError:
        print("Error, Load File Not Found")

    responce_db = json.loads(jsonData)
# Variable used to exit the loop
    exitval = False

    if message.content.lower() != "`chat":

        res = random.choice(begin_db)
        wm = True

    else:
        if message.author.id == client.user.id:
            return

        if message.author.bot:
            return

        while exitval != True:
            print("1")
            channelit = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
            if channelit is None:
                await client.send_message(message.channel, "Chatbot timed out.")
                return
            elif channelit.content == "exit":
                await client.send_message(message.channel, "Chatbot session exited.")
                wm = False
                exitval = True
            else:
                messagge = channelit.content

            print("2")
            print(messagge)
            inp = await sinput(messagge)


            try:
                resp = random.choice(responce_db[inp])
                debug("Found responce")
                wm = True
                print("3")

            except:
                await client.send_message(message.channel, "No responce data found, a new session will begin to gather more data...")
                debug("No responce found")
                begin_db.append(inp)
                wm = False
                print("3.1")

            while wm:
                print("4")
                await sout(resp,client,message)
                print("5")
                channelit = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                if channelit is None:
                    await client.send_message(message.channel, "Chatbot timed out.")
                    return
                elif channelit.content == "exit":
                    await client.send_message(message.channel, "Chatbot session exited.")
                    wm = False
                    exitval = True
                else:
                    messagge = channelit.content
                print("6")
                print(messagge)
                inp = await sinput(messagge)

                if wm:

                    try:
                        responce_db[resp].append(inp)
                        debug("Added new responce '" + str(inp) + "'' under old key '" + str(resp) + "'")

                    except:
                        responce_db[resp] = [inp]
                        debug("Added new responce '" + str(inp) + "'' under new key '" + str(resp) + "'")

                    try:
                        resp = random.choice(responce_db[inp])
                        debug("Found responce")

                    except:
                        await client.send_message(message.channel, "No responce data found, a new session will begin to gather more data...")
                        debug("No responce found")

                        wm = False
