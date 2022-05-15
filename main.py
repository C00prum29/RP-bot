import discord                          
from discord.ext import commands
import random
from settings import config
from tools.db_tools import  stat_read, cause_damage, money_transaction, health_condition_read   #Самописные функции для работы с бд
from tools.discord_tools import form_heath_condition_emmed, form_roll_result_emmed

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()    #сделать красивый вывод / готово?
async def dice(ctx, stat='' ,character='' ,mod=0):
    dice_value = random.randint(0,20) +  (stat_read(stat, character)-10)//2 + mod
    embed = form_roll_result_emmed(dice_value)
    await ctx.reply(embed = embed)

@bot.command()    #доделывать много, тк надо вводить дб на оружее, так что да пока прост оне трогай
async def atk(ctx, type='', character='', target=''):
    await ctx.reply('WIP')

@bot.command() #сделать красивый вывод
async def transfer(ctx, character='', amount=0, target=''):
    embed = discord.Embed(color = 0xFFFFFF, title = 'Перевод денег:')
    embed.add_field(name = 'Подтверждено', value=f'{character} перевела цели {target} {amount} aхн')
    await ctx.reply(embed = embed)

'''
Если сделаешь, то удаляй костыли и ставь это:
    embed = form_money_transfer_emmed(result)
    result = money_transaction(character, amount, target)
'''

@bot.command() #сделать красивый вывод
async def health(ctx, character=''):
    health = health_condition_read(character)
    embed = form_heath_condition_emmed(health)
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