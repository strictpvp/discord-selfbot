import time
import os
import random

try:
    import discord
    import pystyle
    from dotenv import load_dotenv
except ModuleNotFoundError:
    os.system('pip install discord.py-self')
    os.system('pip install pystyle')
    os.system('pip install python-dotenv')
    os.system('python main.py')

import discord
from pystyle import Write, Colors, System
from dotenv import load_dotenv
    
def is_me(m):
    return m.author == client.user

class MyClient(discord.Client):
    async def on_ready(self):
        System.Clear()
        # https://patorjk.com/software/taag/
        Write.Print("""
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
\t\t  ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓
\t\t▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
\t\t░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
\t\t  ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
\t\t▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
\t\t▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
\t\t░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░    
\t\t░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░      
\t\t░     ░  ░    ░  ░        ░          ░ ░           
\t\t                                     ░
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        """, Colors.red_to_blue, interval=0.001)
        Write.Print(f'\t\tLogged on as {self.user}\n', Colors.red_to_blue, interval=0.001)
        Write.Print('Welcome!\n', Colors.red_to_blue)

    async def on_message(self, message):
        if message.author != self.user:
            return

        if message.content == '-ping':
            await message.channel.send('pong!')
        
        if message.content.startswith('-count'):
            arg = message.content.split(' ')
            count = await message.channel.send(arg[1])
            Write.Print(f'[Bot] Count message sent: {arg[1]}seconds\n', Colors.red_to_blue, interval=0.01)
            for i in range(0, int(arg[1])):
                time.sleep(1)
                await count.edit(content=str((i - int(arg[1]) + 1) * -1))
                
        if message.content.startswith('-rp') or message.content.startswith('-randomping'):
            message.delete()
            arg = message.content.split(' ')
            members = await message.guild.fetch_members(message.channel, cache=False, force_scraping=False, delay=0)
            string = ''
            for i in range(0, int(arg[1])):
                string = string + '<@' + str(members[random.randint(0, len(members) - 1)].id) + '> '
                
            await message.channel.send(string)
            Write.Print(f"[Bot] Random Ping Sent: {string}\n", Colors.red_to_blue, interval=0.01)
        
        if message.content.startswith("-del"):
            arg = message.content.split(' ')
            
            if arg[1].isdigit():
                deleted = await message.channel.purge(limit=int(arg[1]) + 1, check=is_me)
                await message.channel.send(f'Deleted {int(len(deleted)) - 1} messages')
                Write.Print(f'[Bot] Deleted {int(len(deleted)) - 1} messages\n', Colors.red_to_blue, interval=0.01)
            else:
                await message.channel.send("NaN")
                
        if message.content.startswith("-spam"):
            arg = message.content.split(' ')
            string = arg[2]
            for i in range(3, len(arg)):
                string = string + " " + arg[i]
            
            if arg[1].isdigit():
                message.channel.purge(limit=1)
                Write.Print(f'[Bot] spam {int(arg[1])} message: {string}\n', Colors.red_to_blue, interval=0.01)
                for i in range(int(arg[1])):
                    await message.channel.send(string)
            else:
                await message.channel.send("NaN")
                
        if message.content.startswith("-server"):
            arg = message.content.split(' ')
            sid = 0
            if len(arg) == 1:
                sid = message.guild.id
            elif arg[1].isdigit():
                sid = int(arg[1])
            else:
                await message.channel.send("NaN")
            
            guild = self.get_guild(sid)
            await message.channel.send(
                "Name: " + guild.name
                + "\nID: " + str(guild.id)
                + "\nOwner: <@" + str(guild.owner_id) + ">"
                + "\nUser: " + str(guild.member_count)
                + "\nVerification Level: " + str(guild.verification_level)
                + "\nIcon: " + str(guild.icon)
                + "\nBanner: " + str(guild.banner)
            )
            Write.Print(f'[Bot] Server Info Sent: {guild.name}({sid}) msg: {message.guild.name}({message.guild.id})\n', Colors.red_to_blue, interval=0.01)
            

client = MyClient()
load_dotenv()
client.run(os.getenv('TOKEN'))
