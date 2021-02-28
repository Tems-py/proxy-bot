import os 
import discord
import requests
from discord.ext import commands
   
client = commands.Bot(command_prefix="-", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Proxy bot by Tems'))
    print("Bot ready")

        
        
@client.command()
async def proxy(ctx, arg1 = None):
    if arg1 == None:
        em = discord.Embed(Title="Usage", description="-proxy [http / socks4 / socks5]")
        await ctx.send(embed=em)
        return
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get(f'https://api.proxyscrape.com/?request=displayproxies&proxytype={arg1}&timeout=1500&ssl=yes')
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
    
    
    
#This code were made by Tems
client.run('TOKEN')
