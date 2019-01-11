
#This is if you want to have Tuesday on a Discord server as a bot. It works very nicely.

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


# commands
from moderation import *
from chatbotcmds import *
from fun import *
from utility import *
from music import *

# Variables for commands
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

# Large variables
HOTDOGMAN = '''⢀⠠⡣⡑⡜⣜⢮⣳⡣⣯⡳⣝⣞⡼⡔⡄⠨⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠯⢳⢕⠗⡏⠚⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠌⠳⠹⠸⠪⠓'''
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
debug = False
# functions
send = client.send_message
wait = client.wait_for_message

async def debug(content):
    if debug == True:
        print("Debug Message: " + content)

async def error(alert):
    msg = "\nTuesday had an error: " + str(sys.exc_info()) + " - " + str(alert)
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
    server.quit()


while True:
    try:
        #here begins the start of the functions for the
        global responce_db
        global bugedition
        global jsonData



        @client.event
        async def on_ready():
            print("-------")
            print("Logged in as " + client.user.name + ": ")#Bot Name
            print(client.user.id)#Bot User ID
            print("-------")
            await client.change_presence(game=discord.Game(name='Say `help'))
            await debug("Bot is now online.")

        @client.event
        async def on_error(event, *args, **kwargs):
            await error(args[0])

        @client.event
        async def on_member_join(member):
            await join(member, client)

        @client.event
        async def on_member_remove(member):

            await leave(member, client)


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

            try:
                if authorID in banned or allbanned == True:
                    return

                if authorID not in testors and debug == True:
                    return

                elif message.content.lower() == "`alertme":
                    await client.send_message(message.channel, "IT WORKS")
                    await error("alert")

                elif uinput.startswith(".`") or uinput.startswith(".~") or uinput.startswith(".``"):
                    await client.send_message(message.channel, "Remember, when trying to use my commands, delete the '.'!")

                elif uinput.startswith("```"):
                    return

                elif authorID == botID:
                    return

                elif message.author.bot:
                    return

                if profanity.profanity.contains_profanity(uinput.lower()):
                    await swearchecker(client, message)

                if authorID == "155103255993647104":
                    robotgif = random.choice(["https://www.technologyreview.com/i/images/robot.fallx392.gif", "http://4.bp.blogspot.com/-_rwfpbwpHTs/Vf_5UX_Kw4I/AAAAAAAAUDs/qLHX51tld34/s1600/robot-breaking-through-door.gif", "https://i.imgur.com/9SKc6D9.gif", ])
                    await send(author, robotgif)

                elif uinput.lower().startswith("hey tuesday") or uinput.startswith("`chat"):
                    if message.author.id == client.user.id:
                        return
                    else:
                        await main(client, message)

                elif "overwatch" in uinput.lower() and "not" in uinput.lower() and "sport" in uinput.lower() and message.server.id in personal:# GRIFFIN ARE YOU HERE
                    await send(channel, "Yes, it is!")

                elif "esport" in uinput.lower() and "not" in uinput.lower() and "sport" in uinput.lower() and message.server.id in personal:
                    await send(channel, "Yes, they are!")

                elif "overwatch" in uinput.lower() and "bad" in uinput.lower() and message.server.id in personal:
                    await send(channel, "No! It's very good!")

                elif "esport" in uinput.lower() and "bad" in uinput.lower() and message.server.id in personal:
                    await send(channel, "No! They're very good!")

                elif uinput.lower() == "`announce" and message.server.id in personal:
                    await announce(client, message)

                elif uinput.lower() == "`collect":
                    await collect(client, message)

                elif uinput.lower() == "`inv" or uinput.lower() == "`inventory":
                    await inventory(client, message)

                elif uinput.lower() == "`resetinv":
                    await resetinv(client, message)

                elif uinput.lower().startswith("`fuse"):
                    await fuse(client, message)

                elif uinput.lower() == "``fillinv":
                    await fillinv(client, message)

                elif uinput.lower() == "`shop":
                    await shop(client, message)

                elif uinput.lower() == "`settings":
                    await settings(client, message)

                elif uinput.lower() == "`department" or uinput.lower() == "`discord":
                    await send(channel, "**Join the Department!**\nhttps://discord.gg/TjWzXZN.")

                elif uinput.lower() == "`github":
                    await send(channel, "Here's my source code: \nhttps://github.com/Lionclaw49/Project_Tuesday.")

                elif uinput.lower() == "`sam" and message.server.id in personal:
                    await send(channel, "The best human in the entire world. Basically a god.")

                elif uinput.lower() == "`gia" and message.server.id in personal:
                    await send(channel, "Don't talk to me about her. She's too annoying.")

                elif uinput.lower().startswith("`define"):
                    await define(client, message, personal, dictionary)

                elif uinput.lower().startswith("`prune"):
                    await prune(client, message)

                elif uinput.lower().startswith("`toggle"):
                    await toggle(client, message)

                elif uinput.lower().startswith("`synonym"):
                    await synonym(client, message)

                elif uinput.lower().startswith("`antonym"):
                    uinput = uinput.replace("`antonym ", "")
                    antonym = dictionary.antonym(uinput)
                    await send(channel, antonym)

                elif uinput.lower() == "`dancehotdog":
                    await send(channel, "https://media.giphy.com/media/l1K9Dcy7ww0CW3JHq/source.gif")

                elif uinput.lower() == "`hotdogman":
                    await send(channel, HOTDOGMAN)

                elif uinput.lower() == "`meme" and message.server.id in personal:
                    await meme(client, message)

                elif uinput.lower() == "`lyrics":
                    await lyrics(client, message, personal)

                elif uinput.lower().startswith("`trending"):
                    await trending(client, message)

                elif uinput.lower() == "`coinflip":
                    coin = random.choice(["heads", "tails"])
                    await send(channel, coin)

                elif uinput.lower() == "`roll":
                    die = random.choice(["1", "2", "3", "4", "5", "6"])
                    await send(channel, die)

                elif uinput.lower().startswith("`forecast"):
                    await forecast(client, message, weather)

                elif uinput.lower().startswith("`weather"):
                    await weather(client, message, weather)

                elif uinput.lower() == "`ezpoll":
                    await ezpoll(client, message)

                elif uinput.lower() == "`poll":
                    await poll(client, message)

                elif uinput.lower().startswith("`bug"):
                    await bug(client, message)

                elif uinput == "`suggest":
                    await suggest(client, message)

                elif uinput.startswith("`testing") and tstzne == True and message.author in tstzne_authr:
                    await client.send_message(message.channel, "It has worked.")

                elif uinput.lower().startswith("`translate"):
                    await translate(client, message)

                elif uinput == "`speakmyspeech":
                    await sms(client, message)

                elif uinput.lower() == "`enter-test":
                    await client.delete_message(client, message)
                    tstzne = True
                    tstzne_authr = message.author

                elif uinput.lower() == "`exit-test" and message.author in tstzne_authr and tstzne == True:
                    await client.delete_message(client, message)
                    tstzne = False
                    tstzne_authr = None

                elif uinput.lower().startswith("`sinsult"):
                    await sinsult(client, message)

                elif uinput == "`Tuesday" or uinput == "``Tuesday":
                    await client.send_message(message.channel, "That's me!") #This is just a fun reference to an AI... If only...

                elif uinput.lower() == "worship kevvy" or uinput.lower() == "worship tevin" and message.server.id in personal:
                    await client.send_message(message.channel, "HAIL!") #WORSHIP TEVIN AND KEVVY

                elif uinput.lower() == "`clean" or uinput.lower() == "`clear":
                    await clean(client, message)

                elif uinput.lower().startswith("`say"):
                    await say(client, message)

                elif uinput.lower() == "`help":
                    await help(client, message)

                elif uinput.lower().startswith("`mime"):
                    await mime(client, message)

                elif uinput.lower().startswith("`play"):
                    await music(client, message)

                elif uinput.lower().startswith("`register") and message.server.id in personal:
                    await rschedule(client, message)

                elif uinput.lower().startswith("`schedule"):
                    await vschedule(client, message)

                elif uinput.lower().startswith("`week") and message.server.id in personal:
                    await wschedule(client, message)

                elif uinput.lower().startswith("`complete") and message.server.id in personal:
                    await cschedule(client, message)

                elif uinput.lower().startswith("`nextday") and message.server.id in personal:
                    await nschedule(client, message)

                elif uinput.lower().startswith("`cal") and message.server.id in personal:
                    await changeW(client, message)

                elif "laurel" in uinput.lower() and "yanny" in uinput.lower():
                    lanny = random.choice(["Laurel", "Yanny"])
                    await client.send_message(message.channel, "It's " + str(lanny) + "!")

                elif message.content.startswith("`update") and message.author.id == "177831674367836160":
                    await update(client, message)

                elif message.content == "pls work":
                    await client.send_message("ayyo it worko")

                elif message.content == "deleto el deleto" and message.author.id == "177831674367836160":
                    await deleto(client, message)

                else:
                    if uinput.startswith("`wa"):
                        #WOLFRAM ALPHA
                        await wa(client, message)

                    elif uinput.startswith("``"):
                        #WIKIPEDIA
                        await wp(client, message, personal)



            except KeyboardInterrupt:
                print("Exiting the program.\n")
                exit()
            except TimeoutError:
                print("Timed out. Now trying again.\n")
            except discord.errors.Forbidden:
                return
        try:
            client.run("NDE1MTkwNTMxNDU5Nzc2NTEz.Da7DdA.rSSccNnSFcCWKEZ-pfINE5YeA48")
        finally:
            client.close()
    except TimeoutError:
        print("Timed out. Now trying again.")


    except OSError:
        print("The network connection has been lost. Now trying to reconnect.")

    except KeyboardInterrupt:
        print("Exiting....")
        exit()

    except discord.errors.Forbidden:
        print("An action was forbidden.")
