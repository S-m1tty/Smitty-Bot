from discord.ext import commands
from discord import Game
import discord
import random
import asyncio

prefix = ("$", "<")
token = "NDk4NTQ4NjE0MDc1OTA4MDk4.DpvVwA.GEH7lcxeqH6KqrumwDvhFKwcnvM"

client = commands.Bot(command_prefix = prefix)
client.remove_command('help')
extensions = ['command', 'respond']

authServerList = [] # Authorized server ID's


@client.command()
async def load(extension):
    for extension in extensions:
        try:
            client.load_extension(extension)
            print("{} loaded [{}]".format(extension))
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))

@client.command()
async def unload(extension):
    for extension in extensions:
        try:
            client.unload_extension(extension)
            print("{} unloaded [{}]".format(extension))
        except Exception as error:
            print("{} cannot be unloaded. [{}]".format(extension, error))

@client.event
async def on_ready():
    serverList = client.servers
    await client.change_presence(game = Game(name = "| $help | $git |"))
    print("\nLogged in as " + client.user.name)
    for server in serverList:
        if not server.id in authServerList:
            await client.leave_server(client.get_server(server.id))
            print("\nLeft Server :: " + server.name)


async def listServers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("-------------------","\nCurrent servers:")
        for server in client.servers:
            print(server.name)
        print("-------------------")
        await asyncio.sleep(60)

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))


    client.loop.create_task(listServers())
    client.run(token)