from dis import disco
from http import client
import discord
import random
from btc import *




TOKEN = "token goes here"

client = discord.Client()

@client.event
async def on_ready():
    print(client.user)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == "crypto-boys":
        if user_message.lower() == "!btc":
            await message.channel.send(f'current price of btc is: {int(get_price())}')
            return

    if message.channel.name == 'the-jungle':
        if user_message.lower() == 'hello':
            await message.channel.send(f'hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'see u later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is ur random number: {random.randrange(100)}'
            await message.channel.send(response)
            return
    
    if user_message.lower() == "!anywhere":
        await message.channel.send("this can be used anywhere")
        return

client.run(TOKEN)
