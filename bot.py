from asyncio.windows_events import NULL
from dependencies.dotenv.main import dotenv_values
from dependencies import discord

config = dotenv_values(".env")

try:
    BOT_TOKEN = config['BOT_TOKEN']
except:
    raise KeyError("BOT_TOKEN not set in environment variables")


def report(command):
    try:
        # TODO implement report command
        return 'Report Command Successfully Called'
    except:
        return False


def commandNotRecognised(command):
  return 'Command Not Recognised'


def commandSwitch(command):
    return {
        'report': report,
    }.get(command[1], commandNotRecognised)    # Command Not Recognised is default


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    return

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hubstaff'):
        message_text = message.content
        command = message_text.split()
        command_function = commandSwitch(command)
        try:
          await message.channel.send(command_function(command))
        except:
          await message.channel.send('Unknown error attempting to run command function for command: '+message_text)
          raise Exception('Unknown error attempting to run command function')
    return

client.run(config['BOT_TOKEN'])
