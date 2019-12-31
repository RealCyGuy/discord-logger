import discord
from discord.ext import commands
from time import ctime
from the_variables import token

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    iasf = ctime() #idk why its iasf
    print('Message from [{0.author}] in [#{0.channel}] on [{1}]: {0.content}'.format(message, iasf))
    with open('log.txt','a') as f:
        f.write('Message from [{0.author}] in [#{0.channel}] on [{1}]: {0.content}\n'.format(message, iasf))

client.run(token)
