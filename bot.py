from dependencies.dotenv.main import dotenv_values
from dependencies import discord

config = dotenv_values(".env")

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hubstaff'):
      command = message.content
      command.split()
      #TODO switch over commands and carry them out

client.run(config['BOT_TOKEN'])
