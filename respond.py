import discord
import random
from init import prefix
from init import botId
from init import ownerId

class Speak():
	def __init__(self, client):
		self.client = client

	async def on_message(self, message):
		if message.server == None and message.author.id == ownerId:
			if not message.content.startswith(prefix):

				channel = message.content[-18:]
				channelToSend = self.client.get_channel(channel)
				messageToSend = message.content[:-18]

				await self.client.send_message(channelToSend, messageToSend)

		elif message.server != None and message.content.startswith("<@" + botId + ">"):
			if message.author.id == ownerId:
				possibleResponses = [
				"Ye yeet ",
				"Yes? ",
				"What's up? ",
				":b: ",
				]
			else:
				possibleResponses = [
				"Fuck off ",
				"I don't talk to bums ",
				"Piss off loser ",
				"Stop being a bum, then we can talk ",
				"I don't talk to losers ",
				]
			await self.client.send_message(message.channel, random.choice(possibleResponses) + message.author.mention)

def setup(client):
	client.add_cog(Speak(client))
