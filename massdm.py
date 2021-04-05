#Modules
import discord
import asyncio
import colorama
from colorama import *
from discord.ext import commands

token = "enter-token-here"
message = input("enter message here:")

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents, self_bot=True)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is on!")
    for _ in range(10000):
        for guild in client.guilds:
            await dm(guild)
            asyncio.sleep(3600)

async def dm(guild):
    for user in list(guild.members):
        try:
            await asyncio.sleep(25) 
            await user.send(message)
            print(f'Sent "{message}" To {user}')

        except:
            print(f"could not send {message} To {user}")

try: 
  client.run(token)
  print("login sucessfull")
except: 
  print(f"{Fore.RED} Token is invalid, please try again.")
