#This is if you want to have Tuesday on a Discord server as a bot. It works very nicely.

import discord #adds discord
import asyncio #allows the async
import wikipedia #adds wikipedia's api
import wolframalpha #adds wolframalpha's api

client = discord.Client() #for easier things later on

@client.event
async def on_ready():
    print("-------")
    print("Logged in as")
    print(client.user.name)#Bot Name
    print(client.user.id)#Bot Token
    print("-------")

@client.event
async def on_message(message):
    if message.content.startswith("`"):
        uinput = message.content #variable in actual tuesday (below was copied)
        if uinput.startswith("`What's") or uinput.startswith("`whats") or uinput.startswith("`Whats") or uinput.startswith("`what's"): 
        #WOLFRAM ALPHA
            app_id = "G58JY9-WQ963T9EQV"  #to get the info
            cclient = wolframalpha.Client(app_id)  #connecting to info
            uinput = uinput.replace("`", "") #getting rid of `
            result = cclient.query(uinput)  #collecting result
            answer = next(result.results).text  #processing answer
            await client.send_message(message.channel, answer)  #sending answer

        elif uinput.startswith("`"):
            #WIKIPEDIA
            wikipedia.set_lang("en")  #Language!
#           uinput = uinput.split(" ")
#           uinput = " ".join(uinput[2:])
            uinput = uinput.replace("`", "")#getting rid of `
            answer = wikipedia.summary(uinput, chars=1900)#shortening the code below
            await client.send_message(message.channel, answer)#sending answer
    
  client.run("Your Token Here")
  
  #On the Discord Developers website, you have to create an bot id for it. Then you get the token, paste it above. Then add it to your server!
  #Have fun!
                     
