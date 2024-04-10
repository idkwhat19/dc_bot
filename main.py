import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.messages = True 
my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix='!', intents=intents)

user1_id = 866889840863346688
user2_id = 649959541798338582
response_message = " Don’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe cope harder + ho mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + repelled + get a life + ok + and? + cringe + touch grass + donowalled + not based + your a (insert stereotype) + not funny didn’t laugh + you “re” + grammar issues + go outside + get good + reported + ad hominem + GG! + ask deez + ez clap + straight cash + ratio agian + final ratio + problematic"

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
     # Check if the message authors are the specific users
     if message.author.id == user1_id or message.author.id == user2_id:
         # Send a response
         await message.channel.send(response_message)

     # Pass the message to the command processor
     await bot.process_commands(message)

# Replace 'YOUR_TOKEN' with your bot's token
bot.run(my_secret)
