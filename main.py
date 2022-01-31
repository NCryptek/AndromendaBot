import os
import discord
import requests
import json

client = discord.Client()

def get_inspire():

  
@client.event
async def on_ready():
    print('we have logged {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$StrategOS'):
      await message.channel.send('Hello!')

client.run(os.environ['TOKEN'])
