if message.content.lower().startswith("purge"):
            channel = None
            user = None
            all_users = False
            while True:
                await client.send_message(message.channel, "Please mention the channel, or type cancel.")
                channel_in = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                if channel_in is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                if channel_in.content == "cancel":
                    await client.send_message(message.channel, "Operation canceled.")
                    return
                channel = discord.utils.find(lambda c: c.mention in channel_in.content, list(client.servers)[0].channels)
                if channel is not None:
                    break
                await client.send_message(message.channel, "That channel doesn't exist.")
            while True:
                await client.send_message(message.channel, "Please mention the user, or type all or cancel.")
                user_in = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
                if user_in is None:
                    await client.send_message(message.channel, "Operation timed out.")
                    return
                if user_in.content == "cancel":
                    await client.send_message(message.channel, "Operation canceled.")
                    return
                if user_in.content == "all":
                    all_users = True
                    break
                user = discord.utils.find(lambda u: u.mention in user_in.content, channel.server.members)
                
                if user is not None:
                    break
                await client.send_message(message.channel, "That user does not exist.")
            await client.send_message(message.channel, "I will delete all messages {}in {}. Please type \"yes\" to confirm. Anything else will cancel.".format("from {} ".format(user.mention) if not all_users else "", channel.mention))
            confirm = await client.wait_for_message(timeout=30, channel=message.channel, author=message.author)
            if confirm is None:
                await client.send_message(message.channel, "Operation timed out.")
                return
            if confirm.content != "yes":
                await client.send_message(message.channel, "Operation canceled.")
                return
            print(channel, user if user is not None else "all", "ready")
            delete_message = await client.send_message(message.channel, "Deleting…")
            delete_messages = []
            async for m in client.logs_from(channel, limit=2**32):
                if (m.author == user if not all_users else True) and (not m.pinned if not message.content.lower().startswith("purge!") else True):
                    delete_messages.append(m)
            print(delete_messages)
            # delete_messages = await filter