#MeFunny Bot

import discord
import aiohttp #For making HTTP requests

intents = discord.Intents.all() #predefined list of all available intents
client = discord.Client(intents=intents) 

@client.event #Event called the the bot is ready to interact with users
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event #Event that extracts infromation about the user and channel
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username}: {user_message} ({channel})') #basic information printed in the command line
    print('------')

    if message.author == client.user:
        return #Do nothing if message was sent by the bot itself

    if user_message.lower() == '!givejoke':
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}) as resp: #HTTP GET request to 'icanhazdadjoke' API for a random joke,
                data = await resp.json() #
                joke = data['joke'] #Stores the joke itself from the json file
                jokeid = data["id"] #Stores the specific joke ID from the json file
                print(f'joke id: {jokeid}') 
                bot_joke = await message.channel.send(f"{message.author.mention} {joke}")
                await bot_joke.add_reaction("😂") #Creates reactions which the users can use to vote wheather the joke was funny or not
                await bot_joke.add_reaction("🤢")
TOKEN = 'MTA1OTk5MDI2ODQyMzcwNDcwNw.GXH-UM.YkXvZeJnqxxZHQCaWRsTS22bkIkBsTz5HDiVvo'
client.run(TOKEN)

