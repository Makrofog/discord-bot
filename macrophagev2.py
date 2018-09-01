import random
import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

BOT_PREFIX= "."
TOKEN = "NDUwNDM3NDc0OTUxNjI2NzUz.Dmqusw.TI9ft6al2xLlhk5aBVA7ETEqQ60"

client = Bot (command_prefix=BOT_PREFIX) 

@client.command(name='8ball',
				description="madry bot",
				brief="odpowiada na pytania zamkniete",
				pass_context=True)
async def eight_ball(context):
	possible_responses = [
		'Tak',
		'Nie',
		'Może',
		':thinking:',
	]
	await client.say(random.choice(possible_responses)+ "," + context.message.author.mention)
	
@client.event
async def on_ready():
	await client.change_presence(game=Game(name='prefix [.]'))
	print("logged in as" + client.user.name)
	
@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [] 
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)

@client.command()
async def embed():
	embed = discord.Embed (
		title= 'title',
		description='description',
		colour= discord.Colour.blue()
	)

	embed.set_footer(text='lul')
	embed.set_image(url='https://cdn.discordapp.com/attachments/485045416757428244/485103687635828737/nerfglogopodstawowe.png')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/485045416757428244/485103687635828737/nerfglogopodstawowe.png')
	embed.set_author(name='Makro', 
	icon_url='https://cdn.discordapp.com/attachments/485045416757428244/485103687635828737/nerfglogopodstawowe.png')

	await client.say(embed=embed)


client.run(TOKEN)
