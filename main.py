import discord                          
from discord.ext import commands
import random
from settings import config
from database.db_tools import  stat_read, cause_damage, money_transaction, health_condition_read   #Самописные функции для работы с бд

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()    #сделать красивый вывод
async def dice(ctx, stat='' ,character='' ,mod=0):
    await ctx.reply(random.randint(0,20) +  (stat_read(stat, character)-10)//2 + mod)

@bot.command()    #доделывать много, тк надо вводить дб на оружее, так что да пока прост оне трогай
async def atk(ctx, type='', character='', target=''):
    await ctx.reply('WIP')

@bot.command() #сделать красивый вывод
async def transfer(ctx, character='', amount=0, target=''):
    money_transaction(character, amount, target)
    await ctx.reply('Money transfered')

@bot.command() #сделать красивый вывод
async def health(ctx, character='', amount=0, target=''):
    health = health_condition_read('Маргарита')

    embed = discord.Embed(color = 0xFFFFFF, title = f'Анализ состояния {health[0]}')
    embed.add_field(name="Name", value="you can make as much as fields you like to")

    await ctx.reply(embed = embed)

@bot.command()   #Если удалишь - трахну <3
async def pat(ctx):
    await ctx.reply('UwU')

@bot.command()   #Тестовая функция для нанесения урона, потом удалю
async def bite(ctx, character='', target='', part='body'):
    damage = random.randint(0,2) +   (stat_read('justice', character)-10)//2
    cause_damage(target, part, damage)
    await ctx.reply('WIP')

bot.run(config['token'])