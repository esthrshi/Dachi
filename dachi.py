import discord
import secret

client = discord.Client()

# on_ready discord.py function: what to do on startup
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# on_message discord.py function: what to do when messaged
@client.event
async def on_message(message):
    if message.author == client.user:   # if msg is from ourselves, do nothing
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(secret.TOKEN)

# update test
