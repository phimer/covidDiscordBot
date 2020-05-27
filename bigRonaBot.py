import discord
from discord.ext import commands
from termcolor import colored
from rona_token import discord_token

from dbReader import read


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    activ = discord.Activity(
        name="!", type=discord.ActivityType.listening)
    # await client.change_presence(activity=discord.Music(name="texthere"))
    await client.change_presence(activity=activ)
    print(colored('BigRona Bot running', 'red'))


# @client.command(aliases=['de', 'Deutschland'])
# async def deutschland(ctx):
#     st = read('Gesamt')
#     await ctx.send(f'Deutschland {st}')


@client.command(aliases=['Fälle', 'cases'])
async def fälle(ctx, *, land):
    await ctx.send(f'{read(land)}')


client.run(discord_token)
