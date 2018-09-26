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

@client.command(name='czy',
				description="odpowiada",
				brief="odpowiada na pytania zamkniete",
				pass_context=True)
async def eight_ball(context):
	possible_responses = [
		'Tak',
		'Nie',
		'Może',
		':thinking:',
	]
	await client.say(random.choice(possible_responses))

@client.event
async def on_ready():
	await client.change_presence(game=Game(name='prefix [.]'))
	print("logged in as" + client.user.name)

@client.command(name='clear',
				description="czyszczenie",
				brief="wprowadź daną liczbę by wyczyśić tyle komentarzy ",
				pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)


@client.command(name='info',
				description="informacje",
				brief="informacje na temat ról (nie nie z tego serwera krzysiek)",
				pass_context=True)
async def info():
	embed = discord.Embed (
		title= 'Informacje o rolach ',
		description= 'Role dla community ',
		color = discord.Color.blue()
	)

	embed.set_footer(text='W razie problemow prosimy o kontakt z administracja')
	embed.set_author(name='Makro',
	icon_url='https://cdn.discordapp.com/attachments/485045416757428244/487981250108194816/zmxn.png')
	embed.add_field(name="member", value="Rola dla osob ktore osiagnely lvl 5", inline=False)
	embed.add_field(name="Active member", value="Rola dla aktywnych osob (+10lvl)", inline=False)
	embed.add_field(name="verifed member", value="rola przyznawana przez administracje dla zaufanych osob", inline=False)

	await client.say(embed=embed)

@client.command(name='regulamin',
				description="regulamin",
				brief="aktualny regulamin serwera (nie też nie tego serwera)",
				pass_context=True)
async def regulamin():
	embed = discord.Embed (
		title= 'REGULAMIN',
		description= 'Serwer jest publicznym serwerem z tego powodu prosimy zachowac kulture osobista',
		color = discord.Color.blue()
	)

	embed.set_footer(text='W razie problemow prosimy o kontakt z administracja')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/485045416757428244/487981245826072577/XD.png')
	embed.set_author(name='Makro',
	icon_url='https://cdn.discordapp.com/attachments/485045416757428244/487981250108194816/zmxn.png')
	embed.add_field(name="zakaz obrazania", value="Prosimy nie obrazac innych uzytkownikow", inline=False)
	embed.add_field(name="zakaz kontentu NSFW", value="Prosimy nie udostepniac tresci pornograficznych itp, itd", inline=False)
	embed.add_field(name="zakaz reklamy", value="Prosimy nie reklamowac sie na serwerze", inline=False)

	await client.say(embed=embed)








client.run(TOKEN)
