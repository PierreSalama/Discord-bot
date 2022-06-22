from http import client
import discord
import random


TOKEN = "OTczNzA2NTExNTg5MjAzOTc4.GzuT3D.Dtz3w8B5RcGzClfxbrRNjSo_eqdEnpsEAuxDZI"

client = discord.Client()

list_name = {
    "𓅓   Erectile Reptile#7328": "mina",
    "BOBLAMA#4430": "pierre",
    "M2#1956": "marcus",
    "Ravagerr#7194": "alex",
    "big chad#5456": "nathan"
}

list_of_names = {
    "mina": "𓅓   Erectile Reptile#7328",
    "pierre": "BOBLAMA#4430",
    "marcus": "M2#1956",
    "alex": "Ravagerr#7194",
    "nathan": "big chad#5456"
}

name_number = {
}

@client.event
async def on_ready():
    print(client.user)

async def _cowgif(self, ctx):
    await ctx.send("")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return


    if message.channel.name == "test":
        if user_message.lower() == "!check bal":
            for i in name_number:
                await message.channel.send(str(i) + ": " + str(name_number[i]) + "\n")

        if "chooch" in user_message.lower() and message.author in name_number:
            odds = 2
            ran = random.randint(1,odds)
            if ran == odds:
                name_number[message.author] = name_number[message.author] + 1
                await message.channel.send("you hit the chooch and did an epic vape god trick")
        elif "chooch" in user_message.lower() and message.author not in name_number:
            name_number[message.author] = 0
            name_number[message.author] = name_number[message.author] + 1
        if name_number[message.author] == 5:
            await message.channel.send("u win")
            



client.run(TOKEN)