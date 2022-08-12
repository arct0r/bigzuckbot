import discord 
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startwith('hey, test!'):
        await message.channel.send('Testeron dei testeroni!')

client.run(os.getenv('MTAwNzM4ODQ4MTU3NzgyMDE3MA.GLH35o.AIaa6nkW9gWqybXhZJaXovk6gp__uCLzGJQg20'))
    