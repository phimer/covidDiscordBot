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


# @client.command(brief='!cases Gesamt -> gibt Infos zu Deutschland aus (Stand heute)\n!cases Hessen -> gibt Infos zu Bundesland (Stand heute)\n!cases Hessen 28.5.2020 -> gibt Infos zu bestimmten Tag', description='This is the full description')
# async def foo(ctx):
#     await ctx.send('bar')


@client.command(aliases=['hilf'])
async def hilfe(ctx):
    await ctx.send('!cases Deutschland -> gibt Infos zu Deutschland aus (Stand heute)\n!cases Hessen -> gibt Infos zu Bundesland (Stand heute)\n!cases Hessen 2020-05-28 -> gibt Infos zu bestimmten Tag')


# @client.command(aliases=['de', 'Deutschland'])
# async def deutschland(ctx):
#     st = read('Gesamt')
#     await ctx.send(f'Deutschland {st}')


@client.command(aliases=['Fälle', 'cases', 'fälle', 'corona'])
async def c(ctx, *, land):
    # Hessen 2020-08-12
    sp = land.split()
    print(sp)
    if (len(sp) > 1):
        land = sp[0]
        print(land)
        date = sp[1]
        print(date)
        await ctx.send(returnToBot(land, date))
    else:
        await ctx.send(returnToBot(land))


client.run(discord_token)
