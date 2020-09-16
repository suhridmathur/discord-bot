import os

import discord

TOKEN = os.getenv("BOT_TOKEN")

class Client(discord.Client):
    pass

client = Client()
client.run(TOKEN)