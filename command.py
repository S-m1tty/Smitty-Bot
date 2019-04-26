import discord
from discord.ext import commands
from discord.utils import get
import random

class Commands():
	def __init__(self, client):
		self.client = client

	@commands.command(pass_context = True)
	async def info(self, ctx):
		embed = discord.Embed(name = "info", color = 0x307af2)
		embed.set_author(name = "{}'s info".format(ctx.message.server.name))
		embed.add_field(name = "Name", value = ctx.message.server.name)
		embed.add_field(name = "ID", value = ctx.message.server.id, inline = True)
		embed.add_field(name = "Owner", value = ctx.message.server.owner)
		embed.add_field(name = "Region", value = ctx.message.server.region, inline = True)
		embed.add_field(name = "Roles", value = len(ctx.message.server.roles))
		embed.add_field(name = "Members", value = len(ctx.message.server.members), inline = True)
		embed.set_thumbnail(url = ctx.message.server.icon_url)
		await self.client.say(embed = embed)

	@commands.command(pass_context = True)
	async def flashback(self, ctx):
		embed = discord.Embed(name = "info", color = 0x307af2)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/498542050346795008/526479709949788182/Capture.JPG')
		await self.client.say(embed = embed)

	@commands.command(pass_context = True)
	async def otis(self, ctx):
		embed1 = discord.Embed(name = "info", color = 0x307af2)
		embed1.set_image(url = "https://i.ytimg.com/vi/LX3HCQBlZpo/hqdefault.jpg")

		embed2 = discord.Embed(name = "info", color = 0x307af2)
		embed2.set_author(name = "Bully_Hunter99's Rainbow Six Siege Stats")
		embed2.add_field(name = "Kill/Death", value = "**Kills**: -9 **Deaths**:<OverflowError: integer too large>\n**K/D**: 0.00")
		embed2.add_field(name = "Win/Loss", value = "**Won**: 121\n**Lost**: 631\n**Win%**: 16.09%", inline = True)
		embed2.add_field(name = "Stats", value = "**Headshots**: 118\n**Penetration Kills**: 24\n**Melee Kills**: 2\n**Revives**: 0.5")
		embed2.add_field(name = "Shots", value = "**Fired**: 6438654\n**Hit**: 3518\n**Accuracy**: 0.00%", inline = True)
		embed2.add_field(name = "Extras", value = "**Suicides**: 643\n**Barricades**: 466\n**Reinforcements**: 1672\n**Gadgets Destroyed**: -234", inline = True)

		possibleResponses = random.choice([
			self.client.say("Is it time to sexualize the minors? <@273540808051785729>"),
			self.client.say("<@273540808051785729> Knock knock, it's the pedo police", embed = embed1),
			self.client.say("<@273540808051785729>'s R6 Siege Stats", embed = embed2),
			self.client.say("<@273540808051785729> *child predator noises*")
		])
		await possibleResponses

	@commands.command(pass_context = True)
	async def smitty(self, ctx):
		possibleResponses = [
			"Yup, I'm ",
			"Bow down to ",
			"Help, they're attacking me ",
			"yeet ",
			"Me? ",
			"They're summoning you ",
			"God = ",
			"My creator is ",
			"All hail "
		]
		await self.client.say(random.choice(possibleResponses) + "<@257247797311569920>")

	@commands.command(pass_context = True)
	async def bailey(self, ctx):
		possibleResponses = [
			"Don't abort our kid next time ",
			"Wanna go smash again? ",
			"<3 <3 ",
			"Hey cutie ;) ",
			":heart: ",
			"UwU ",
			":eggplant::sweat_drops: ",
			":peach::eyes: ",
			"*insert cute doggo picture here* "
		]
		await self.client.say(random.choice(possibleResponses) + "<@190254753215807488>")	

	@commands.command(pass_context = True)
	async def lauren(self, ctx):
		possibleResponses = [
			"Want to go out sometime? ",
			"Smash? ",
			"Wanna come over? ;) ",
			"I love you. ",
			":heart: ",
			"Prom? ",
			":point_right::ok_hand: ",
			":kissing_closed_eyes: ",
			":kissing_heart: "
		]
		await self.client.say(random.choice(possibleResponses) + "<@297895701252407297>")

	@commands.command(pass_context = True)
	async def colin(self, ctx):
		possibleResponses = [
			"*white knight noises* ",
			"Colin has small pp ",
			"F ",
			"Got an extra lung? Give it to ",
			"Guess who's house flooded --> ",
			":b:olin ",
			"Uhhhh "
		]
		await self.client.say(random.choice(possibleResponses) + "<@207369269758001152>")

	@commands.command(name = "8ball", pass_context = True)
	async def eight_ball(self, ctx):
		possibleResponses = [
	    	"That'll be a no, chief ",
	    	"It aint looking good ",
	    	"Too hard to tell ",
	    	"That's a fat yes, chief ",
	    	"100% ",
	    	"0% ",
	    	"69.420% ",
	    	"Perhaps ",
	    	"no "
		]
		await self.client.say(random.choice(possibleResponses) + ctx.message.author.mention)

	@commands.command(pass_context = True)
	async def kms(self, ctx):
		possibleResponses = [
	    	" No, you are great and I love you. Things are going to get better. Trust me.",
	    	" I know things aren't good rn but just you wait, happiness is right around the corner. Just, for me, hold out until then. Please.",
	    	" I'm afraid I can't do that. I care too much about you to let you go like this.",
	    	" I understand how you feel. I know how much it hurts. I know the feeling of never-ending pain and sadness. I know it doesn't seem like it now but happiness is coming. You are cared for by so many. It'll get better soon. I promise."
		]
		await self.client.say(ctx.message.author.mention + random.choice(possibleResponses))

	@commands.command(pass_context = True)
	async def gn(self, ctx):
		await self.client.say("Goodnight " + ctx.message.author.mention)

	@commands.command(pass_context = True)
	async def uwu(self, ctx):
		await self.client.say(ctx.message.author.mention + " UwU")

	@commands.command(pass_context = True)
	async def nword(self, ctx):
		await self.client.say(ctx.message.author.mention + " nice try :sunglasses:")

	@commands.command(pass_context = True)
	async def perhaps(self, ctx):
		embed = discord.Embed(name = "info", color = 0x307af2)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/423263838951964673/500858908307619881/image0.jpg')
		await self.client.say(embed = embed)

	@commands.command(pass_context = True)
	async def egirl(self, ctx):
		embed = discord.Embed(name = "info", color = 0x307af2)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/282388422692306945/502941812546207754/image0.jpg')
		await self.client.say(embed = embed)

	@commands.command(name = "deletethis", pass_context = True)
	async def delete(self, ctx):
		possibleResponses = [
		"https://vignette.wikia.nocookie.net/meleehell/images/3/36/Delete_this_gundam.jpg/revision/latest?cb=20160630092920",
		"https://www.rpnation.com/proxy.php?image=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FC3tNGGeWIAAFB5u.jpg&hash=2f9900ffcb1a1d6c30314712f3c05f29",
		"https://www.shitpostbot.com/img/sourceimages/delete-this-engineer-58fd84f15ef98.jpeg",
		"https://pics.me.me/delet-this-3385839.png",
		"https://www.meme-arsenal.com/memes/db0975046a0133771d8bcddba7e690a9.jpg",
		"https://i.pinimg.com/originals/29/01/e3/2901e3bbf94144aab9fc5249790bf8a3.jpg",
		"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVE555lZTjy7OnnSd1qJ7HmpZpCye762AukDFOpmYYxSu7PUw_",
		"https://i.kym-cdn.com/photos/images/facebook/001/100/078/7c3.jpg",
		"https://cdn.discordapp.com/attachments/423263838951964673/501067291694465040/image0.png",
		"https://cdn.discordapp.com/attachments/423263838951964673/567024084698005514/image0.jpg"
		]
		embed = discord.Embed(name = "info", color = 0x307af2)
		embed.set_image(url = random.choice(possibleResponses))
		await self.client.say(embed = embed)		

	@commands.command(name = "@498548614075908098>", pass_context = True)
	async def tagged(self, ctx):
		if ctx.message.author.id == "257247797311569920":
			possibleResponses = [
			"Ye yeet ",
			"Yes? ",
			"What's up? ",
			":b: ",
			]
		else:
			possibleResponses = [
			"Fuck off ",
			"I don't talk to blacks ",
			"Piss off cunt ",
			"Stop being a faggot, then we can talk ",
			"I don't talk to gays ",
			]
		await self.client.say(random.choice(possibleResponses) + ctx.message.author.mention)

	@commands.command()
	async def stfu(self):
		embed = discord.Embed(name = "info", color = 0x307af2)
		possibleResponses = [
		"https://i.kym-cdn.com/entries/icons/mobile/000/026/375/stfu-liberal-mao.jpg",
		"https://pbs.twimg.com/media/DUZmF-tVoAArabV.jpg",
		"https://i.kym-cdn.com/photos/images/facebook/001/379/483/6de.jpg",
		"https://i.kym-cdn.com/photos/images/original/001/379/484/18e.jpg",
		"https://i.imgur.com/OQXforY.jpg",
		"https://pbs.twimg.com/media/DbmzOX2VwAAJswG.jpg",
		"https://i.imgur.com/0kbxcvk.jpg"
		]
		embed.set_image(url = random.choice(possibleResponses))
		await self.client.say(embed = embed)

	@commands.command(name = "git")
	async def github(self):
		await self.client.say("https://github.com/S-m1tty/Smitty-Bot")

	@commands.command(pass_context = True)
	async def help(self, ctx):
		embed = discord.Embed(name = "help", description = "Prefix: $\nhttps://github.com/S-m1tty/Smitty-Bot", color = 0x307af2)
		embed.set_author(name = "Smitty Bot Help Page info")
		embed.add_field(name = "People", value = "`otis`: Spits straight facts\n`lauren`: Makes Lauren super horny\n`bailey`: Says a nice thing to Bailey\n`smitty`: Hails Smitty\n`colin`: Says some stuff to Colin", inline = True)
		embed.add_field(name = "Reactions", value = "`perhaps`: Perhaps\n`deletethis`: Delete this post\n`egirl`: Shut up e-girl\n`stfu`: Shut the fuck up, liberal")
		embed.add_field(name = "Misc", value = "`nword`: Answers with the n word\n`8ball`: Answers with a probability\n`uwu`: Answers with UwU\n`gn`: Goodnight", inline = True)
		embed.add_field(name = "Helpful", value = "`git`: Pastes Github repo link\n`info`: Gives server information\n`kms`: When you're feeling down")
		await self.client.say(embed = embed)

def setup(client):
	client.add_cog(Commands(client))