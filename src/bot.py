import os
import random

import discord

from utilities import constants

TOKEN = os.getenv("BOT_TOKEN")


class Client(discord.Client):
    async def on_message(self, message):
        # If message is from bot itself, return #
        if self.user == message.author:
            return

        # Send Hello message on greeting from user #
        message_content = message.content
        if message_content.lower() in constants.GREETING_MESSAGE_LIST:
            await message.channel.send(
                f"{random.choice(constants.BOT_GREETING_MESSAGES)} {message.author.display_name}"
            )


client = Client()
client.run(TOKEN)
