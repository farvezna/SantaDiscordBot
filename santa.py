import os

import discord
from dotenv import load_dotenv

from discord.ext import commands
from pprint import pprint

load_dotenv() #load in environment vars
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
BOT_CHANNEL = int(os.getenv('BOT_CHANNEL'))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)

@bot.event
async def on_ready():
    print('{} has connected to Discord!'.format(bot.user.name))
    print(str(GUILD))
    print(bot.guilds)
    guild = discord.utils.get(bot.guilds, id=GUILD)
    print(guild.channels)
    #print(f'Members: {guild.members}, size: {len(guild.members)}')
    #print(f'GUILD:{guild.name};id:{guild.id}')
    #channel = bot.get_channel(BOT_CHANNEL)
    #print("\n\n\n\n")
    #print(discord.utils.get(guild.members, name="Samin", discriminator="5548"))

@bot.command(name='deliver', help='!deliver user#1234 MM/DD')
async def send_delivery_status(ctx, *args):
    guild = discord.utils.get(bot.guilds,id=GUILD)
    channel = bot.get_channel(BOT_CHANNEL)
    name = args[0].split("#")[0]
    discriminator = args[0].split("#")[1]
    date = args[1]
    print(args)
    member = discord.utils.get(guild.members, name=name, discriminator=discriminator)
    myid = '<@{}>'.format(member.id)
    await channel.send(myid + ": Expected Delivery on " + date)
bot.run(TOKEN)
