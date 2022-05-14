import discord                          
from discord.ext import commands
import random
from settings import config
from database.db_tools import  stat_read, cause_damage     #Самописные функции для работы с бд

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def dice(ctx, stat='' ,character='' ,mod=0):
    await ctx.reply(random.randint(0,20) +  (stat_read(stat, character)-10)//2 + mod)

@bot.command()
async def bite(ctx, character='', target='', part='body'):
    damage = random.randint(0,2) +   (stat_read('justice', character)-10)//2
    cause_damage(target, part, damage)
    await ctx.reply('Ну сейчас уже точно')

@bot.command()
async def pat(ctx):
    await ctx.reply('UwU')

bot.run(config['token'])