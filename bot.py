from dependencies import discord

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

client.run('ODY2OTgxODY2NDQ2NjUxMzky.YPadyA.K1ypIBz7dpmiCQjOFML3STv8zzM')
