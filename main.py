import os 
import discord
import requests
from discord.ext import commands
   
client = commands.Bot(command_prefix="-", help_command=None)

@client.event
async def on_ready():
    print("Bot ready")

        
        
@client.command()
async def proxy(ctx):
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    await ctx.send(file=discord.File('./proxies.txt'))
    
    
    
    
client.run('TOKEN')