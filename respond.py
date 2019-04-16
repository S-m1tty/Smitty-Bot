import discord

class Speak():
	def __init__(self, client):
		self.client = client

	async def on_message(self, message):
		if message.server is None and message.author.id == "Your ID here":

			channel = (message.content).split()[-1]
			messageToSend = str((message.content).split()[:-1]).replace(',', ' ').replace("'",'').replace('[', '').replace(']','')
			channelToSend = self.client.get_channel(channel)

			if not message.content.startswith("$"):
				await self.client.send_message(channelToSend, messageToSend)

def setup(client):
	client.add_cog(Speak(client))