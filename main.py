import discord
from tokenHandling import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(get_token())