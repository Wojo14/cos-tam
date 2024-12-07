import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def papier(ctx):
    await ctx.send(f'papier rozkłada sie 6 miesięcy')     
    
@bot.command()
async def plastik(ctx):
    await ctx.send(f'plastik rozkłada się od 100 do 1000 lat')
    
@bot.command()
async def szklo(ctx):
    await ctx.send(f'szkło rozkłada się od Kilku miesięcy do nawet kilku tysięcy lat')

@bot.command()
async def k(ctx):
    await ctx.send(f'komendy:  !papier(mówi ile rozkłada się papier)  !plastik(mówi ile rozkłada sie plastik)   !szklo(mówi ile rozkłada się szkło)    !gplastik(mówi gdzie dajemy plastik)     !gpapier(mówi gdzie dajemy papier)     !mem(pookazuje losowy mem)')

@bot.command()
async def gplastik(ctx):
    await ctx.send(f'plastik dajemy do recyklingu')

@bot.command()
async def gpapier(ctx):
    await ctx.send(f'papier dajemy do śmieci')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
