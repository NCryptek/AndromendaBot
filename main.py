import os
import discord
import requests
import json
from funkcje import *


client = discord.Client()
def get_inspire():
  response = requests.get("https://zenquotes.io/api/random") 
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)
  
@client.event
async def on_ready():
    print('we have logged {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith(bot_hi):
      await message.channel.send('Hello!')
    if message.content.startswith(bot_inspire):
      quote = get_inspire()
      await message.channel.send(quote)
    if message.content.startswith(bot_help):
      quote=get_help()
      await message.channel.send(quote)
    if message.content.startswith(bot_artillery):
      quote="https://youtu.be/GW6GSa14xXI"
      await message.channel.send(quote)
    if message.content.startswith(bot_shame):
      quote=message.content
      quote=quote[11:]
      await message.channel.send(quote)


client.run(os.environ['TOKEN'])
