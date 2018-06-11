import discord
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

async def debug(content):
    if debug == True:
        print("Debug Message: " + content + "  ---  " + str(datetime.datetime.now()))

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

async def music(client, message):
    three = 0
    print("recieved")
    author = message.author
    voice_channel = author.voice_channel
    join = await client.join_voice_channel(voice_channel)
    song = message.content.replace("`play ","")
    print(song)
    if song.startswith("https://"):
        player = await join.create_ytdl_player(song)
        player.start()
        print("Playing " + player.title + " for " + str(player.duration))
    else:
        if " " in song:
            blah = list(song.split(" "))
            song = ""
            for item in blah:
                song += "+" + item
                await debug(song)
            song = song.replace("+","",1)
            await debug(song)
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + song)
        await debug("http://www.youtube.com/results?" + song)
        search_results = re.findall(r'href="/watch?v=', html_content.read().decode())
        await debug(search_results[0])
        song = "http://www.youtube.com/watch?v=" + search_results[0]
        await debug(song)
        player = await join.create_ytdl_player(song)
        player.start()
        await client.send_message(message.channel, "Playing " + player.title + " for " + str(player.duration))
