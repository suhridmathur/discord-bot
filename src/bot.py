import os
import random

import discord

from utilities import constants, google_search

TOKEN = os.getenv("BOT_TOKEN")


class Client(discord.Client):
    async def on_message(self, message):
        # If message is from bot itself, return #
        if self.user == message.author:
            return

        message_content = message.content

        # Send Hello message on greeting from user #
        if message_content.lower() in constants.USER_GREETING_MESSAGES:
            await message.channel.send(
                f"{random.choice(constants.BOT_GREETING_MESSAGES)} {message.author.display_name}"
            )

        # Search on Google if Message StartsWith "!google" #
        elif message_content.startswith("!google"):
            search_term = " ".join(
                message_content.split()[1:]
            )  # `!google leo messi` -> `leo messi`#
            if not search_term:
                await message.channel.send(
                    random.choice(constants.NO_TERM_ENTERED_MESSAGES)
                )
                return

            search_service = google_search.GoogleSearch()
            results = search_service.get_top_five_links(search_term)

            embeded_response = discord.Embed(
                title=f"{constants.EMBEDDED_RESULTS_TITLE} '{search_term}'",
            )
            for result in results:
                embeded_response.add_field(
                    name=result["title"], value=result["url"], inline=False
                )
            await message.channel.send(embed=embeded_response)


client = Client()
client.run(TOKEN)
