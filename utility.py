import discord
from urllib.request import urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
import datetime
import wikipedia #adds wikipedia's api
import wolframalpha #adds wolframalpha's api
import random
import os
import yaml #operates with the insults file.
from googletrans import Translator #google translate
import random
from string import punctuation
from weather import Weather
import re
from PyLyrics import *
from PyDictionary import PyDictionary
from selenium import webdriver
import smtplib
import sys
import datetime
import profanity.profanity
import json


async def week():
	global currweek
	while True:
		if datetime.datetime.today().weekday() == 0:
			if currweek == 1:
				currweek = 2
			else:
				currweek = 1
			await asyncio.sleep(60 * 60 * 24 * 6)
		else:
			await asyncio.sleep(60 * 60 * 23)

def getday():
	today = datetime.datetime.today().weekday()
	if currweek == 1:
		if today > 4:
			return 6
		return today + 1
	if today > 4:
		return 1
	return  today + 6

schedules = {}
currweek = 0

def debug(content):
    if debug:
        print("Debug Message: " + content)

async def define(client, message, personal, dictionary):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author
    debug("Start of Define")
    uinput = uinput.replace("`define ", "")
    if uinput.lower() == "sam" and message.server.id in personal:
        await client.send_message(channel, "{'Noun': ['the supernatural being conceived as the perfect and omnipotent and omniscient originator and ruler of the universe; the object of worship in monotheistic religions', 'any supernatural being worshipped as controlling some part of the world or some aspect of life or who is the personification of a force', 'a man of such superior qualities that he seems like a deity to other people', 'a material effigy that is worshipped']}")
        debug("Defined sam")
    elif uinput.lower() == "tuesday":
        await client.send_message(channel, "{'Bot': ['a simply amazing bot that can do a whole lot of things', 'probably the best bot in the history of the world', --- \nHey, wait a minute, this is talking about *me*!")
        debug("Defined tuesday")
    elif uinput.lower() == "greatness" and message.server.id in personal:
        await client.send_message(channel, "{'Noun': ['something that the great god sam achieved', 'the property possessed by something or someone of outstanding importance or eminence', 'unusual largeness in size or extent or number']}")
        debug("Defined greatness")
    elif uinput.lower() == "griffin" and message.server.id in personal:
        await client.send_message(channel, "Don't talk to me about him. He's too annoying.")
        debug("Defined griffin")
    else:
        definition = dictionary.meaning(uinput)
        await client.send_message(channel, definition)
        debug("Defined " + uinput.lower())

async def trending(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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

        await client.send_message(channel, "The top trending hashtags on Twitter currently are: \n" + twitter1.text + "\n" + twitter2.text + "\n" + twitter3.text + "\n" + twitter4.text + "\n" + twitter5.text + "\n" + twitter6.text + "\n" + twitter7.text + "\n" + twitter8.text + "\n" + twitter9.text + "\n" + twitter10.text)
        browser.quit()
    else:
        await client.send_message(channel, "This might take a second.")
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
            await client.send_message(channel, "The top " + uinput + " trending hastags on Twitter currently are: \n" + str(topped))
        else:
            await client.send_message(channel, "The maximum top trending hashtags go up to 20.")

async def forecast(client, message, weather):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    if uinput.lower() == "`forecast":
        await client.send_message(channel, "Please enter a city or a zipcode.")
        # wait for message
        place = await client.wait_for_message(timeout=60, channel=channel, author=author)
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
            await client.send_message(channel, return_str)
        elif place.isnumeric():
            lookup = weather.lookup(place)
            forecasts = lookup.forecast()
            return_str = ""
            for forecast in forecasts:
                return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
            await client.send_message(channel, return_str)
        else:
            await client.send_message(channel, "Please enter a proper zipcode or city.")
    else:
        uinput = uinput.replace("`forecast ", "")
        if uinput.isalpha():
            location = weather.lookup_by_location(uinput)
            forecasts = location.forecast()
            return_str = ""
            for forecast in forecasts:
                return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
            await client.send_message(channel, return_str)
        elif uinput.isnumeric():
            lookup = weather.lookup(uinput)
            forecasts = lookup.forecast()
            return_str = ""
            for forecast in forecasts:
                return_str += forecast.date() + " -- " + forecast.text() + " -- " + forecast.high() + " - " + forecast.low() + "\n"
            await client.send_message(channel, return_str)
        else:
            await client.send_message(channel, "Please enter a proper zipcode or city.")

async def weather(client, message, weather):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    if uinput.lower() == "`weather":
        await client.send_message(channel, "Please enter a city or a zipcode.")
        # wait for message
        place = await client.wait_for_message(timeout=60, channel=channel, author=author)
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
                await client.send_message(channel, condition.text())
                await client.send_message(channel, condition.temp())
            except (KeyError, AttributeError):
                await client.send_message(channel, "Please enter at proper city.")
        elif place.isnumeric():
            lookup = weather.lookup(place)
            try:
                condition = lookup.condition()
                await client.send_message(channel, condition.text())
                await client.send_message(channel, condition.temp())
            except (KeyError, AttributeError):
                await client.send_message(channel, "Please enter a proper zipcode.")
        else:
            await client.send_message(channel, "Please enter a proper zipcode or city.")
    else:
        uinput = uinput.replace("`weather ", "")
        if uinput.isalpha():
            location = weather.lookup_by_location(uinput)
            try:
                condition = location.condition()
                await client.send_message(channel, condition.text())
            except (KeyError, AttributeError):
                await client.send_message(channel, "Please enter a proper city.")
        elif uinput.isnumeric():
            lookup = weather.lookup(uinput)
            try:
                condition = lookup.condition()
                await client.send_message(channel, condition.text())
            except (KeyError, AttributeError):
                await client.send_message(channel, "Please enter a proper zipcode.")
        else:
            await client.send_message(channel, "Please enter a proper zipcode or city.")

async def ezpoll(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
    await client.send_message(channel, epollttl)
    for i in range(epollaltnum):
        await client.send_message(channel, epollrktn2[i+1] + " - "+ epollalt[i])
    epollcat = await client.send_message(channel, "Hey @everyone, take the poll!")
    for i in range(epollaltnum):
        await client.add_reaction(epollcat, epollrktn[i+1])

async def poll(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    pollalts = False
    await client.send_message(channel, "What do you want your poll to be on? At any point in this process, 'cancel' will stop the whole thing.")
    pollttlwait = await client.wait_for_message(timeout=60, channel=channel, author=author)
    if pollttlwait is None:
        await client.send_message(message.channel, "Operation timed out.")
        return
    elif pollttlwait.content.lower() == "cancel":
        await client.send_message(message.channel, "Operation canceled.")
        return

    pollttl = pollttlwait.content

    await client.send_message(channel, "Please enter the choices for the poll, then once you are finished type 'done'.")
    pollalt = []
    while pollalts == False:
        pollaltwait = await client.wait_for_message(timeout=240, channel=channel, author=author)
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
        await client.send_message(channel, "You have too many choices. Please split up the poll.")
        return
    elif pollaltnum < 1:
        await client.send_message(channel, "You have two few choices.")
        return

    await client.send_message(channel, "The poll is now finshed.")
    pollrktn = {1 : "\U00000031\U000020E3", 2 : "\U00000032\U000020E3", 3 : "\U00000033\U000020E3", 4 : "\U00000034\U000020E3", 5 : "\U00000035\U000020E3", 6 : "\U00000036\U000020E3", 7 : "\U00000037\U000020E3", 8 : "\U00000038\U000020E3", 9 : "\U00000039\U000020E3", 10 : "\U0001F51F"}
    pollrktn2 = {1 : ":one:", 2 : ":two:", 3 : ":three:", 4 : ":four:", 5 : ":five:", 6 : ":six:", 7 : ":seven:", 8 : ":eight:", 9 : ":nine:", 10 : ":keycap_ten:"}
    print(pollalt)
    await client.send_message(channel, pollttl)
    for i in range(pollaltnum):
        await client.send_message(channel, pollrktn2[i+1] + " - "+ pollalt[i])
    pollcat = await client.send_message(channel, "Hey @everyone, take the poll!")
    for i in range(pollaltnum):
        await client.add_reaction(pollcat, pollrktn[i+1])

async def bug(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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


async def suggest(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
        await client.send_message(channel, "Do you wish to add a description of this command? (y/n)")

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
            await client.send_message(channel, "What would you like to have as the description?")
            sgtdesctrue = await client.wait_for_message(timeout=90, channel=channel, author=author)
            if sgtdesctrue is None:
                await client.send_message(channel, "Operation Timed out.")
            elif sgtdesctrue.content == "cancel":
                await client.send_message(channel, "Operation cancelled.")
                return

            suggestdesc = sgtdesctrue.content

            await client.send_message(message.channel, "Description confirmed. The suggestion has been sent to the developer.")
            print("\n\nSuggestion: \n---------------")
            print(suggesthead)
            print(suggestdesc)
            suggestdescloop = False

        else:
            await client.send_message(channel, "Invalid Command. Please try again:")

async def translate(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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

async def sms(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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

async def say(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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

async def help(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
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
- wa -> This does math for you! Hurray. It can do algebra, calculus, and even statistics!
- trending -> This allows you to get the top trending hashtags off of twitter. (any number after it up to 20 or nothing is 10.)
- translate (dest) -> This allows you to translate any language into the destination language(dest), you need to specify the ISO 639-1 code form of the language first though.""")
    await client.send_message(message.author, """
Also, anything with  double backticks will pull a wikipedia article.
There are also a lot of hidden commands, have fun trying to find them!""")

async def wa(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    app_id = "G58JY9-WQ963T9EQV"  #to get the info
    cclient = wolframalpha.Client(app_id)  #connecting to info
    uinput = uinput.replace("`wa ", "") #getting rid of ~
    result = cclient.query(uinput)  #collecting result
    answer = next(result.results).text  #processing answer
    await client.send_message(message.channel, answer)  #sending answer

async def wp(client, message, personal):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    wikipedia.set_lang("en")  #Language!
    uinput = uinput.replace("`` ", "")#getting rid of ``
    if uinput.lower() == "tidepod" or uinput.lower() == "tide pod" and message.server.id in personal:
        await client.send_message(channel, "Mmmmmmmm... Tasty.... Right here's your info.")
    try:
        answer = wikipedia.summary(uinput, chars=1900)#shortening the code below
        await client.send_message(message.channel, answer)#sending answer
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e: #:)
        await client.send_message(message.channel, e,)

async def synonym(client, message):
    uinput = message.content
    channel = message.channel
    author = message.author
    bot = client.user
    botID = bot.id
    authorID = message.author.id
    uinput = uinput.replace("`synonym ", "")
    synonym = dictionary.synonym(uinput)
    if synonym == None:
        await client.send_message(channel, "You need to put something after the message.")
        return
    elif len(synonym) > 1999:
        await client.send_message(channel, "Message is too long, send `bug report.")
        return
    elif len(synonym) == 0:
        await client.send_message(channel, "Big error.")
        return
    if synonym == "['synonymy', 'synonymic']":
        print("im there")
        await client.send_message(channel, "You need to put something after the message.")
        return
    await client.send_message(channel, synonym)


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
        query = quote(song)
        debug(query)
        url = "https://www.youtube.com/results?search_query=" + query
        debug(url)
        response = urlopen(url)
        debug("1")
        html = response.read()
        debug(str(html))
        soup = BeautifulSoup(html)
        debug("2")
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            debug("3")
            debug(str(three))
            if three == 3:
                break
                debug("broken")
            else:
                song = 'https://www.youtube.com' + vid['href']
                print(song)
                debug("found")
                three = 3
                debug(str(three))
        player = await join.create_ytdl_player(song)
        player.start()
        print("Playing " + player.title + " for " + str(player.duration))

async def rschedule(client, message):
    schedules[message.author.name + "#" + message.author.discriminator] = {}
    await client.send_message(message.channel, "Hello! What is your A block")
    scheduleA = await client.wait_for_message(timeout=40, channel=message.channel, author=message.author)
    if scheduleA is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator]["A"] = scheduleA.content

    await client.send_message(message.channel, "What is your B block")
    scheduleB = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleB is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator] ["B"] = scheduleB.content

    await client.send_message(message.channel, "What is your C block")
    scheduleC = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleC is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator]["C"] = scheduleC.content

    await client.send_message(message.channel, "What is your D block")
    scheduleD = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleD is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator]["D"] = scheduleD.content

    await client.send_message(message.channel, "What is your E block")
    scheduleE = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleE is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator]["E"] = scheduleE.content

    await client.send_message(message.channel, "What is your F block")
    scheduleF = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleF is None:
        await client.send_message("Sorry, you timed out")
        return

    schedules[message.author.name + "#" + message.author.discriminator]["F"] = scheduleF.content

    await client.send_message(message.channel, "What is your G block")
    scheduleG = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    if scheduleG is None:
        await client.send_message("Sorry, you timed out")

    schedules[message.author.name + "#" + message.author.discriminator]["G"] = scheduleG.content

# Later I can add activities registries for days
    # await client.send_message(message.channel, "What is your first activity? (Day") # Fix Days
    # scheduleA1 = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    # if scheduleA1 is None:
    #     await client.send_message("Sorry, you timed out")
    #
    # schedules[message.author.name + "#" + message.author.discriminator] [A1] = scheduleA1.content
    #
    # await client.send_message(message.channel, "What is your second activity? (Day") # Fix Days
    # scheduleA2 = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    # if scheduleA2 is None:
    #     await client.send_message("Sorry, you timed out")
    #
    # schedules[message.author.name + "#" + message.author.discriminator] [A2] = scheduleA2.content
    #
    # await client.send_message(message.channel, "What is your third activity? (Day") # Fix Days
    # scheduleA3 = await client.wait_for_message(timeout=40, author=message.author, channel=message.channel)
    # if scheduleA3 is None:
    #     await client.send_message("Sorry, you timed out")


    await client.send_message(message.channel, "Thank you. Your schedule is now ready to view")

async def vschedule(client, message):
    global currweek
    day = getday()
    if currweek == 1:
        await client.send_message(message.channel, "It is week 1 and day " + str(day) + " and your schedule is:")
        await client.send_message(message.channel, "--------------")
        if day == 1:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
        if day == 2:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 3:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"])
        if day == 4:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 5:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
        #else:
        #	await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
    if currweek == 2:
        await client.send_message(message.channel, "It is week 2 and day " + str(day))
        await client.send_message(message.channel, "--------------")
        if day == 6:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 7:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"])
        if day == 8:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 9:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
        if day == 10:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
    await client.send_message(message.channel, "--------------")

async def wschedule(client, message):
    global currweek
    await client.send_message(message.channel, currweek)

async def cschedule(client, message):
    global currweek
    await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator])

async def nschedule(client, message):
    global currweek
    day = getday()
    await client.send_message(message.channel, "Tomorrow is day " + str(day) + " and your schedule is:")
    await client.send_message(message.channel, "--------------")
    if currweek == 1:
        if day == 1:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 2:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"])
        if day == 3:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 4:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
        if day == 5:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
    if currweek == 2:
        if day == 6:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"])
        if day == 7:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 8:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
        if day == 9:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["E"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["F"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["G"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["Activities"])
        if day == 10:
            await client.send_message(message.channel, schedules[message.author.name + "#" + message.author.discriminator]["A"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["B"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["C"] + " " + schedules[message.author.name + "#" + message.author.discriminator]["D"])
    await client.send_message(message.channel, "--------------")

async def changeW(client, message):
    global currweek
    if message.author.server_permissions.administrator or message.author.id == "356474528655867905" or message.author.id == "356164886658678794":
        if currweek == 1:
            currweek = 2
        elif currweek == 2:
            currweek = 1
        print(currweek)
        await client.delete_message(message)
