import discord

class Speak():
	def __init__(self, client):
		self.client = client

	async def on_message(self, message):
		if message.server is None and message.author.id == "Your ID here":
			if not message.content.startswith("$"):

				channel = message.content[-18:]
				channelToSend = self.client.get_channel(channel)
				messageToSend = message.content[:-18]

				await self.client.send_message(channelToSend, messageToSend)

def setup(client):
	client.add_cog(Speak(client))