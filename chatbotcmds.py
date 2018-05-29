import discord

async def debug(content):
    if debug:
        print("Debug Message: " + content)

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
