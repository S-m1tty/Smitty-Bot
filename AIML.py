import discord
import os
import random
import pkg_resources
from discord.ext import commands
import asyncio
import aiml

from init import prefix
from init import botId


STARTUP_FILE = "std-startup.xml"

class AIML:
    def __init__(self, client):
        self.client = client

        # Load AIML kernel
        self.aiml_kernel = aiml.Kernel()
        initial_dir = os.getcwd()
        os.chdir(pkg_resources.resource_filename(__name__, '/aiml/alice/'))  # Change directories to load AIML files properly
        startup_filename = pkg_resources.resource_filename(__name__, STARTUP_FILE)
        self.aiml_kernel.learn(startup_filename)
        self.aiml_kernel.respond("LOAD AIML")
        os.chdir(initial_dir)

    async def on_message(self, message):
        if (message.channel.name == "smitty-bot") and (message.author.id != botId):

            if message.content.startswith(prefix):
                # Pass on to rest of the client commands
                await self.client.process_commands(message)

            elif self.aiml_kernel.respond(message.content) != "":
                aiml_response = self.aiml_kernel.respond(message.content)
                await self.client.send_typing(message.channel)
                await asyncio.sleep(random.randint(1,2))
                await self.client.send_message(message.channel, aiml_response)
            
            else:
                await self.client.send_message(message.channel, "Invalid message")

def setup(client):
    client.add_cog(AIML(client))