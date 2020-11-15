# This is the discord Bot - allows users to request rki data through discord chat commands

import discord
from discord.ext import commands
from termcolor import colored
from rona_token import discord_token

from dbReader import returnToBot


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    activ = discord.Activity(
        name="!hilfe", type=discord.ActivityType.listening)
    # await client.change_presence(activity=discord.Music(name="texthere"))
    await client.change_presence(activity=activ)
    print(colored('BigRona Bot running', 'red'))


@client.command(aliases=['hilf'])
async def hilfe(ctx):
    await ctx.send('!c Deutschland -> gibt Infos zu Deutschland aus (Stand heute)\n!c Hessen -> gibt Infos zu Bundesland (Stand heute)\n!c Hessen 2020-05-28 -> gibt Infos zu bestimmten Tag')


@client.command(aliases=['Fälle', 'cases', 'fälle', 'corona'])
async def c(ctx, *, land):
    # Hessen 2020-08-12
    sp = land.split()
    if (len(sp) > 1):
        land = sp[0]
        print(land)
        date = sp[1]
        print(date)
        await ctx.send(returnToBot(land, date))
    else:
        print(land)
        await ctx.send(returnToBot(land))


client.run(discord_token)
